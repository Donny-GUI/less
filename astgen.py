
import ast
import luaparser.ast as last
from luaparser.ast import to_lua_source

last_dict:ast.Dict = None
last_class_def: ast.ClassDef = None

RANGE = ast.Name(id='range', ctx=ast.Load())
LEN = ast.Name(id='len', ctx=ast.Load())
ELLIPSIS = ast.Constant(value="...")
NONE = ast.Constant(value=None)
TRUE = ast.Constant(value=True)
FALSE = ast.Constant(value=False)


""" ----------------------------------------------------------------------- """
""" Expressions                                                             """
""" ----------------------------------------------------------------------- """

LUA_EXPRESSION_TYPES_OR_VALUES = [last.Nil, last.TrueExpr, last.FalseExpr, last.Number, last.Varargs, last.String, last.Field, last.Table, last.AnonymousFunction, last.Dots]

LUA_OPERAND_MAP = {
    "AddOp":ast.Add(),
    "SubOp":ast.Sub(),
    "MultOp":ast.Mult(),
    "FloatDivOp":ast.Div(),
    "FloorDivOp":ast.FloorDiv(),
    "ModOp":ast.Mod(),
    "ExpoOp":ast.Pow(),
    "BAndOp":ast.BitAnd(),
    "BOrOp":ast.BitOr(),
    "BXorOp":ast.BitXor(),
    "BShiftROp":ast.RShift(),
    "BShiftLOp":ast.LShift(),
    "LessThanOp":ast.Lt(),
    "GreaterThanOp":ast.Gt(),
    "LessOrEqThanOp":ast.LtE(),
    "GreaterOrEqThanOp":ast.GtE(),
    "EqToOp":ast.Eq(),
    "NotEqToOp":ast.NotEq(),
    "LOrOp": ast.Or(),
    "LAndOp": ast.And(),
    "REqOp": ast.Eq(),
    "RGtOp": ast.Gt(),
    "Concat": ast.Add(),
    "RNotEqOp":ast.NotEq(),
    "RLtOp": ast.Lt(),
    "RLtEqOp": ast.LtE(),
    "RGtEqOp": ast.GtE(),
}


def index_to_attribute(index_str: last.Index) -> ast.Attribute:
    """
    Converts a string representing nested attribute access into an AST attribute node.

    Args:
        index_str (str): String representing nested attribute access, e.g., "thing.attr.attr2".

    Returns:
        ast.Attribute: AST node representing the nested attribute access.
    """
    print("attribute: ", to_lua_source(index_str))
    return ast.Constant(value=to_lua_source(index_str))
    
def var_reference(name:str):
    return ast.Name(name, ast.Load())

def var_malloc(name:str):
    return ast.Name(name, ast.Store())

def handle_unary_minus(expression:last.UMinusOp):
    return ast.UnaryOp(op=ast.USub(), operand=handle_expression(expression.operand))

def handle_unary_binary_not(expression:last.UBNotOp):
    return ast.UnaryOp(op=ast.Invert(),
                       operand=handle_expression(expression.operand))

def handle_unary_logical_not(expression: last.ULNotOp):
    return ast.UnaryOp(op=ast.Not(),
                       operand=handle_expression(expression.operand))

def handle_length_operator(expression:last.ULengthOP):
    return ast.Expr(value=ast.Name(id='len', ctx=ast.Load()), 
                    args=[handle_expression(expression.operand)], keywords=[])
    


LUA_UNARY_OPERAND_MAP = {
    "UMinusOp":handle_unary_minus,
    "UBNotOp":handle_unary_binary_not,
    "ULNotOp":handle_unary_logical_not,
    "ULengthOP":handle_length_operator,
}

def handle_unary_op(expression:last.UnaryOp):
    return LUA_UNARY_OPERAND_MAP[expression._name](expression)

def handle_binary_op(binop:last.BinaryOp):
    try:
        o = LUA_OPERAND_MAP[binop._name]
    except:
        o = LUA_OPERAND_MAP[binop._name]
    return ast.BinOp(left=handle_expression(binop.left), 
                       op=o, 
                       right=handle_expression(binop.right))

def handle_arithmetic_op(op:last.AriOp):
    return ast.BinOp(left=handle_expression(op.left), 
                       op=LUA_OPERAND_MAP[op._name], 
                       right=handle_expression(op.right))

def handle_Nil(expression: last.Nil):
	return ast.Constant(value=None)

def handle_TrueExpr(expression: last.TrueExpr) -> ast.Constant:
	return ast.Constant(value=True)

def handle_FalseExpr(expression: last.FalseExpr) -> ast.Constant:
	return ast.Constant(value=False)

def handle_Number(expression: last.Number) -> ast.Constant:
	return ast.Constant(value=int(expression.n), kind="i")

def handle_Varargs(expression: last.Varargs):
	pass

def handle_String(expression: last.String) -> ast.Constant:
	return ast.Constant(value=str(expression.s), kind="s")

def handle_Field(expression: last.Field):
    global last_dict
    last_dict.keys.append(handle_expression(expression.key))
    last_dict.values.append(handle_expression(expression.value))

def handle_Table(expression: last.Table):
    global last_dict
    d = ast.Dict(keys=[], values=[])
    last_dict = d
    for field in expression.fields:
        d.keys.append(handle_expression(field.key))
        d.values.append(handle_expression(field.value))
    return d

def handle_AnonymousFunction(expression: last.AnonymousFunction):
	# Extract the arguments
    arg_names = []
    for x in expression.args:
        if isinstance(x, last.Name):
            if isinstance(x.id, last.Name):
                arg_names.append(x.id.id)
            else:
                arg_names.append(x.id)
        elif isinstance(x, str):
            arg_names.append(x)
    
    python_args = ast.arguments(
        args=[ast.arg(arg=arg_name, annotation=None) for arg_name in arg_names],
        vararg=None,
        kwonlyargs=[],
        kw_defaults=[],
        kwarg=None,
        defaults=[]
    )
    
    # Extract the body
    python_body = []
    for statement in expression.body.body:
        python_body.append(pyast(statement))
        
    # Create a Python function definition
    python_function = ast.FunctionDef(
        name="<lambda>",
        returns=None,
        type_params=[],
        args=python_args,
        body=python_body,
        decorator_list=[]
    )

    return python_function

def handle_attribute(expression:last.Index):
    return index_to_attribute(expression)

def handle_subscript(expression: last.Index):
    return ast.Subscript(value=handle_expression(expression.idx), 
                        slice=handle_expression(expression=expression.value))

def handle_index(expression: last.Index):
    if expression.notation == last.IndexNotation.DOT:
        return ast.Constant(value=to_lua_source(expression), kind="attribute")
    elif expression.notation == last.IndexNotation.SQUARE:
        return handle_subscript(expression)

def handle_lefthand_expression(expression: last.Lhs):
    if isinstance(expression, last.Name):
        return ast.Name(id=expression.id, ctx=ast.Load())
    elif isinstance(expression, last.Index):
        return handle_index(expression)
    
def handle_relational_op(expression: last.RelOp):
    return ast.BinOp(left=handle_expression(expression.left), 
                     op=LUA_OPERAND_MAP[expression._name], 
                     right=handle_expression(expression.right))

def handle_Dots(expression:last.Dots):
    return ELLIPSIS

LUA_EXPRESSION_FUNCTIONS = [handle_Nil, handle_TrueExpr, handle_FalseExpr, handle_Number, handle_Varargs, handle_String, handle_Field, handle_Table, handle_AnonymousFunction, handle_Dots]

def handle_eq_to(expression:last.EqToOp):
    return ast.BinOp(left=handle_expression(expression.left), op="==", right=handle_expression(expression.right))

def handle_expression(expression: last.Expression):
    if isinstance(expression, last.Name):
        return ast.Name(expression.id)
    elif isinstance(expression, last.EqToOp):
        return handle_eq_to(expression)
    elif isinstance(expression, last.Index):
        return handle_index(expression)
    elif isinstance(expression, last.ULNotOp):
        return handle_unary_logical_not(expression)
    elif isinstance(expression, last.AndLoOp):
        return ast.BinOp(left=handle_expression(expression.left), op="and", right=handle_expression(expression.left))
    if isinstance(expression, last.TrueExpr):
        return TRUE
    if isinstance(expression, last.FalseExpr):
        return FALSE
    if isinstance(expression, last.Name):
        if isinstance(expression.id, last.Name):
            return ast.Name(expression.id.id)
        return ast.Name(id=expression.id)
    if isinstance(expression, last.Index):
        return handle_index(expression)
    elif isinstance(expression, last.ULNotOp):
        return handle_unary_logical_not(expression)
    if isinstance(expression, last.BinaryOp):
        return handle_binary_op(expression)
    elif isinstance(expression, last.AriOp):
        return handle_arithmetic_op(expression)
    elif isinstance(expression, last.RelOp):
        return handle_relational_op(expression)
    elif isinstance(expression, last.Lhs):
        return handle_lefthand_expression(expression)
    elif isinstance(expression, last.ULNotOp):
        return handle_unary_logical_not(expression)
    elif isinstance(expression, last.Index):
        return handle_index(expression)
    elif isinstance(expression, last.EqToOp):
        return handle_eq_to(expression)
    for index, c in enumerate(LUA_EXPRESSION_TYPES_OR_VALUES):
        if isinstance(expression, c):
            return LUA_EXPRESSION_FUNCTIONS[index](expression)
    
    return None


def make_expression(expression:ast.AST):
    return expression

""" ----------------------------------------------------------------------- """
""" Statements                                                              """
""" ----------------------------------------------------------------------- """

def make_statement(statement: ast.AST):
    return statement

def handle_statement(statement: last.Statement):
    if isinstance(statement, last.Chunk):
        return handle_chunk(statement)
    elif isinstance(statement, last.Block):
        return handle_block(statement)
    elif isinstance(statement, last.Do):
        return handle_do(statement)
    elif isinstance(statement, last.While):
        return handle_while(statement)
    elif isinstance(statement, last.Repeat):
        return handle_repeat(statement)
    elif isinstance(statement, last.If):
        return handle_if(statement)
    elif isinstance(statement, last.ElseIf):
        return handle_elseif(statement)
    elif isinstance(statement, last.Forin):
        return handle_forin(statement)
    elif isinstance(statement, last.Fornum):
        return handle_fornum(statement)
    elif isinstance(statement, last.Assign):
        return handle_assign(statement)
    elif isinstance(statement, last.LocalAssign):
        return handle_local_assign(statement)
    elif isinstance(statement, last.Label):
        return handle_label(statement)
    elif isinstance(statement, last.Goto):
        return handle_goto(statement)
    elif isinstance(statement, last.Return):
        return handle_return(statement)
    elif isinstance(statement, last.Break):
        return ast.Break()
    #elif isinstance(statement, last.Invoke):
    #    return handle_invoke(statement)
    elif isinstance(statement, last.Function):
        return handle_function(statement)
    elif isinstance(statement, last.LocalFunction):
        return handle_localfunction(statement)
    elif isinstance(statement, last.Method):
        return handle_method(statement)
    
    if isinstance(statement, last.Call):
        return handle_call_statement(statement)
    
    return handle_expression(statement)

def handle_function(statement: last.Function):
    arg_names = [arg.id for arg in statement.args]
    python_args = ast.arguments(
        args=[ast.arg(arg=arg_name, annotation=None) for arg_name in arg_names],
        vararg=None,
        kwonlyargs=[],
        posonlyargs=[],
        kw_defaults=[],
        kwarg=None,
        defaults=[]
    )
    name = statement.name
    if isinstance(statement.name, last.Index):
        name = handle_lefthand_expression(statement.name)
    elif isinstance(statement.name, last.Name):
        name = statement.name.id
    py = ast.FunctionDef(name=str(statement.name.id),
                         args=python_args,
                         body=[], decorator_list=[])
    for node in statement.body.body:
        py.body.append(handle_statement(node))
    return py

def handle_class_def(node: last.Assign):
    global last_class_def
    it: last.Invoke = node.values[0]
    for item in node.values:
        if isinstance(item, last.Invoke):
            it = item
            break
    nn: last.Name = node.targets[0]
    for t in node.targets:
        if isinstance(t, last.Name):
            nn = t
            break
    
    c = ast.ClassDef(name=str(nn.id),
                     bases=[ast.Name(it.source.id, ctx=ast.Store())],
                     keywords=[], body=[], decorator_list=[],type_params=[]
                     )
    last_class_def = c
    return c

def handle_assign(statement: last.Assign) -> ast.Assign:
    for lnode in last.walk(statement):
        if isinstance(lnode, last.Invoke):
            inode = lnode
            if inode.func.id.startswith("extend"):
                return handle_class_def(statement)

    return ast.Assign(targets=[handle_expression(x) for x in statement.targets], value=ast.List(elts=[handle_expression(x) for x in statement.values]))

def handle_local_assign(statement: last.LocalAssign):
    return handle_assign(statement)

def handle_goto(statement: last.Goto):
    pass

def handle_label(statement: last.Label):
    pass 

def handle_return(statement: last.Return):
    try:
        if len(statement.values) > 1:
            retv = ast.Tuple([handle_expression(x) for x in statement.values])
        else:
            retv = handle_expression(statement.values)
    except:
        return handle_expression(statement.values)
    return ast.Return(value=retv)

def handle_chunk(chunk:last.Chunk):
    retv = []
    for node in chunk.body.body:
        n = handle_statement(node)
        if n != None:
            retv.append(n)
    return retv

def handle_block(statement: last.Block):
    retv = []
    for x in statement.body:
        retv.append(pyast(x))
    return retv

def handle_call_statement(statement: last.Call):
    return ast.Call(func=handle_expression(statement.func), args=[pyast(x) for x in statement.args])

def handle_localfunction(statement: last.LocalFunction):
    return handle_function(statement=statement)

def handle_method(statement: last.Method):
    n :last.Name = statement.name
    xname = n.id
    if n.id in ["init", "initialize", "__init", "__initialize"]:
        xname = "__init__"
    arg_names = []
    for x in statement.args:
        if isinstance(x, last.Name):
            if isinstance(x.id, last.Name):
                arg_names.append(x.id.id)
            else:
                arg_names.append(x.id)
        elif isinstance(x, str):
            arg_names.append(x)
    
    args=[ast.arg(arg=arg_name, annotation=None, type_comment=None) for arg_name in arg_names]
    python_args = ast.arguments(
        args=args,
        vararg=None,
        kwonlyargs=[],
        posonlyargs=args,
        kw_defaults=[],
        kwarg=None,
        defaults=[])
    d = ast.FunctionDef(name=xname, 
                        body=handle_block(statement.body), 
                        args=python_args, 
                        decorator_list=[], 
                        returns=None, 
                        type_params=[])
    global last_class_def
    last_class_def.body.append(d)
    return None

def handle_while(statement:last.While):
    return ast.While(test=handle_expression(statement.test),
                     body=handle_block(statement.body),
                     orelse=[])

def handle_repeat(statement:last.Repeat):
    pass

def handle_orelse(orelse: last.ElseIf|list):
    orx = []
    if isinstance(orelse, list):
        orx = [handle_statement(x) for x in orelse]
    elif isinstance(orelse, last.ElseIf):
        orx = handle_elseif(orelse)
    return orx

def handle_if(statement: last.If):
    t = statement.test 
    if statement.test != False:
        t = handle_expression(statement.test)
    oe = []
    if isinstance(statement.orelse, last.Block):
        oe = handle_block(statement.orelse)
    elif isinstance(statement.orelse, list):
        oe = [handle_statement(x) for x in statement.orelse]
    return ast.If(test=t, body=handle_block(statement.body), orelse=oe)

def handle_elseif(statement:last.ElseIf):
    return ast.If(False, handle_block(statement.body), handle_block(statement.orelse) if statement.orelse != None else []) 

def handle_multi_value(multiv:list[last.Node], container=list):
    length = len(multiv)
    if length == 0:
        return ast.Constant(value=None)
    elif length == 1:
        return pyast(multiv[0])
    return container([pyast(x) for x in multiv])

def handle_forin(statement: last.Forin):
    target = handle_multi_value(statement.targets, container=tuple)
    retv = ast.For(target=target, 
                   body=handle_block(statement.body), 
                   iter=handle_expression(statement.iter),
                   orelse=[])
    
def handle_fornum(statement:last.Fornum):
    target = ast.Name(id=statement.target.id)
    st = handle_expression(statement.start)
    end = handle_expression(statement.stop)
    step = handle_expression(statement.step)
    range_call = ast.Call(
        func=RANGE,
        args=[st, end, step])
    return ast.For(target=target, 
                   iter=range_call, 
                   body=handle_block(statement.body), 
                   orelse=[])

def handle_do(statement: last.Do):
    pass 

def pyast(lua_ast:last.Node):
    if isinstance(lua_ast, last.Statement):
        return handle_statement(lua_ast)
    return handle_expression(lua_ast)

def python3_module(lua_chunk:last.Chunk):
    body = []
    for statement in lua_chunk.body.body:
        st = pyast(statement)
        if st != None:
            body.append(st)

    return ast.Module(body=body, type_ignores=[])

def make_python3_module(lua_file:str):
    with open(lua_file, "r", errors="ignore") as f:
        content = f.read()
    ch = last.parse(content)
    py = python3_module(ch)
    return ast.fix_missing_locations(py)

def lua_ast_from_string(string:str):
    return last.parse(string)


def handle_unary_logical_length(node: last.ULengthOP):
    pass

def handle_unary_length(node: last.ULengthOP):
    pass

def handle_logical_and(node: last.AndLoOp):
    pass

def handle_node(node: last.Node):
    pass

def handle_break(node: last.Break):
    return ast.Break()

def go(*args):
    pass

last_func_map = {
    "last.Nil": handle_Nil,
    "last.TrueExpr": handle_TrueExpr,
    "last.FalseExpr": handle_FalseExpr,
    "last.Number": handle_Number,
    "last.Varargs": handle_Varargs,
    "last.String": handle_String,
    "last.Field": handle_Field,
    "last.Table": handle_Table,
    "last.AnonymousFunction": handle_AnonymousFunction,
    "last.Dots": handle_Dots,
    "last.UMinusOp": handle_unary_minus,
    "last.UBNotOp": handle_unary_binary_not,
    "last.ULNotOp": handle_unary_logical_not,
    "last.ULengthOP": handle_unary_length,
    "last.UnaryOp": handle_unary_op,
    "last.BinaryOp": handle_binary_op,
    "last.AriOp": handle_arithmetic_op,
    "last.Nil": handle_Nil,
    "last.TrueExpr": handle_TrueExpr,
    "last.FalseExpr": handle_FalseExpr,
    "last.Number": handle_Number,
    "last.Varargs": handle_Varargs,
    "last.String": handle_String,
    "last.Field": handle_Field,
    "last.Table": handle_Table,
    "last.IndexNotation": go,
    "last.Dots": handle_Dots,
    "last.Expression": handle_expression,
    "last.ULNotOp": handle_unary_logical_not,
    "last.AndLoOp": handle_logical_and,
    "last.TrueExpr": handle_TrueExpr,
    "last.FalseExpr": handle_FalseExpr,
    "last.ULNotOp": handle_unary_logical_not,
    "last.BinaryOp": handle_binary_op,
    "last.AriOp": handle_arithmetic_op,
    "last.RelOp": handle_relational_op,
    "last.Lhs": handle_lefthand_expression,
    "last.ULNotOp": handle_unary_logical_not,
    "last.Index": handle_index,
    "last.EqToOp": handle_eq_to,
    "last.Do": handle_do,
    "last.While": handle_while,
    "last.Repeat": handle_repeat,
    "last.Break": handle_break,
    "last.Function": handle_function,
    "last.Assign": handle_assign,
    "last.Invoke": go,
    "last.LocalAssign": handle_assign,
    "last.Goto": handle_goto,
    "last.Label": handle_label,
    "last.Return": handle_return,
    "last.Chunk": handle_chunk,
    "last.Block": handle_block,
    "last.Call": handle_call_statement,
    "last.LocalFunction": handle_localfunction,
    "last.Method": handle_method,
    "last.While": handle_while,
    "last.Repeat": handle_repeat,
    "last.ElseIf": handle_elseif,
    "last.If": handle_if,
    "last.Block": handle_block,
    "last.ElseIf": handle_elseif,
    "last.Forin": handle_forin,
    "last.Fornum": handle_fornum,
    "last.Do": handle_do,
    "last.Node": handle_node,
    "last.Statement": handle_statement,
    "last.Chunk": handle_chunk,
}

lua_python_statement_map = {
"last.Do":go,
"last.While":ast.While,
"last.Repeat":go,
"last.If":ast.If,
"last.ElseIf":ast.If,
"last.Forin":ast.For,
"last.Fornum":ast.For,
"last.Assign":ast.Assign,
"last.LocalAssign":ast.Assign,
"last.Label":go,
"last.Goto":go,
"last.Return":ast.Return,
"last.Break":ast.Break,
"last.Invoke":ast.ClassDef,
"last.Function":ast.FunctionDef,
"last.LocalFunction":ast.FunctionDef,
"last.Method":ast.FunctionDef,
"last.Call":ast.Call
}
