import ast
from transpile.exprgen import starred_to_string, try_star_to_string
from transpile.maps import get_op_string


"""============================================================================"""
"""       [Transpiler]   Source Generator                                      """
"""============================================================================"""


def python_module_to_nodes(mod:ast.Module):
    return mod.body

def binop_to_string(op):
    """
    Convert a binary operator AST node to its string representation.
    
    Args:
        op (ast.operator): The binary operator AST node to convert.
    
    Returns:
        str: The string representation of the binary operator.
    """
    if isinstance(op, ast.Add):
        return "+"
    elif isinstance(op, ast.Sub):
        return "-"
    elif isinstance(op, ast.Mult):
        return "*"
    elif isinstance(op, ast.Div):
        return "/"
    elif isinstance(op, ast.Mod):
        return "%"
    elif isinstance(op, ast.Pow):
        return "**"
    elif isinstance(op, ast.LShift):
        return "<<"
    elif isinstance(op, ast.RShift):
        return ">>"
    elif isinstance(op, ast.BitOr):
        return "|"
    elif isinstance(op, ast.BitXor):
        return "^"
    elif isinstance(op, ast.BitAnd):
        return "&"
    elif isinstance(op, ast.FloorDiv):
        return "//"
    else:
        return get_op_string(op)

def attr_string(node: ast.Attribute):
    return f"{node.value.id}.{node.attr}"

def if_or_expression(left, right):
    return f"{left} if {left} else {right}"

def value_to_string(node):
    if node == None:
        return ""
    if isinstance(node, ast.arguments):
        return ", ".join([value_to_string(x) for x in node.args])
    if isinstance(node, ast.arg):
        return node.arg
    if isinstance(node, ast.Constant):
        if node.kind == 'attribute':
            return node.value.strip("'")
        
        return repr(node.value)
    elif isinstance(node, ast.Name):
        if isinstance(node.id, ast.Name):
            return node.id.id
        return node.id
    elif isinstance(node, ast.BinOp):
        left = value_to_string(node.left)
        right = value_to_string(node.right)
        op = binop_to_string(node.op)
        if op == "or":
            if right == "{}" or right == "[]":
                return if_or_expression(left, right)
        return f"{left} {op} {right}"
    elif isinstance(node, ast.Call):
        return make_call(node)
    elif isinstance(node, ast.Subscript):
        value = value_to_string(node.value)
        slice = value_to_string(node.slice)
        return f"{value}[{slice}]"
    elif isinstance(node, ast.Tuple):
        elts = [value_to_string(elt) for elt in node.elts]
        return f"({', '.join(elts)})"
    elif isinstance(node, ast.List):
        if len(node.elts) <= 1:
            return value_to_string(node.elts[0])
        elts = [value_to_string(elt) for elt in node.elts]
        try:
            return f"[{', '.join(elts)}]"
        except:
            return "[]"
    elif isinstance(node, ast.Dict):
        keys = [value_to_string(key) for key in node.keys]
        values = [value_to_string(value) for value in node.values]
        items = [f"{k}: {v}" for k, v in zip(keys, values)]
        return f"{{{', '.join(items)}}}"
    elif isinstance(node, ast.FunctionDef):
        return f"lambda x: {node.name}"
    elif isinstance(node, ast.Index):
        return "index what"
    try:
        return node.id
    except:
        try:
            return node.value
        except:
            return node

def make_call(node:ast.Call):
    ass = make_arg_list(node.args)
    name = "?????????"
    if isinstance(node.func, ast.Name):
        name = node.func.id
    elif isinstance(node.func, ast.Constant):
        name = node.func.value
    return f"{name}({ass})"

def handle_or_and_expression(left, op, right):
    string = f"{left} {op} {right}"
    parts = string.split(" ")
    for p in parts:
        if p == "or":
            return f"{left} if {left} else {right}"
        elif p == "and":
            return f"{left} if {left} else {right}"
    
def make_expression(node:ast.Expr):
    if isinstance(node, ast.Name):
        if isinstance(node.id, ast.Name):
            return make_expression(node.id)
        return node.id
    
    if node == None:
        return ""
    elif isinstance(node, ast.Call):
        return make_call(node)
    elif isinstance(node, ast.UnaryOp):
        return f"{get_op_string(node.op)}{value_to_string(node.operand)}"
    elif isinstance(node, ast.BoolOp):
        exprs = ", ".join([make_expression(x) for x in node.values])
        return f"{get_op_string(node.op)} {exprs}"
    elif isinstance(node, ast.BinOp):
        left = value_to_string(node.left)
        right = value_to_string(node.right)
        op = binop_to_string(node.op)
        if op in "or":
            return handle_or_and_expression(left, op, right)
        return f"{left} {op} {right}"
    elif isinstance(node, ast.Lambda):
        return f"lambda {", ".join([arg.arg for arg in node.args.args])}: {value_to_string(node.body)}"
    elif isinstance(node, ast.IfExp):
        pass
    elif isinstance(node, ast.Dict):
        return value_to_string(node)
    elif isinstance(node, ast.Set):
        return value_to_string(node)
    elif isinstance(node, ast.ListComp):
        return
    elif isinstance(node, ast.SetComp):
        return
    elif isinstance(node, ast.DictComp):
        return
    elif isinstance(node, ast.GeneratorExp):
        return
    elif isinstance(node, ast.Await):
        return f"await {make_expression(node.value)}"
    elif isinstance(node, ast.Yield):
        return f"yield {make_expression(node.value)}"
    elif isinstance(node, ast.YieldFrom):
        return f"yield from {make_expression(node.value)}"
    elif isinstance(node, ast.Compare):
        return f"{make_expression(node.left)} {"".join([get_op_string(x) for x in node.ops])} {make_expression(node.value)}"
    elif isinstance(node, ast.IfExp):
        t = make_expression(node.test)
        e = ""
        if node.orelse != None:
            e = "else " + make_expression(node.orelse)
        return f"if {t} {make_expression(node.body)} {e}"
    return value_to_string(node)

def make_list(iterable):
    if len(iterable.elts) == 1:
        return value_to_string(iterable.elts[0])
    return "[" + ", ".join([make_expression(x) for x in iterable.elts]) + "]"

def make_tuple(iterable):
    return "(" + ", ".join([make_expression(x) for x in iterable.elts]) + ")"

def make_set(iterable):
    return "{" + ", ".join([make_expression(x) for x in iterable.elts]) + "}"

def make_iterable(iterable):
    if isinstance(iterable, ast.Name):
        return iterable.id
    if isinstance(iterable, ast.List):
        return make_list(iterable)
    if isinstance(iterable, ast.Tuple):
        return make_tuple(iterable)
    if isinstance(iterable, ast.Set):
        return make_set(iterable)

def make_target(target: ast.Name|ast.Attribute|ast.Subscript):
    if isinstance(target, ast.Name):
        return target.id
    elif isinstance(target, ast.Attribute):
        return f"{make_expression(target.value)}.{target.attr}"
    elif isinstance(target, ast.Subscript):
        return f"{make_expression(target.value)}[{make_expression(target.slice)}]"

def make_targets(targets: list[ast.expr]) -> str:
    if isinstance(targets, ast.Name):
        return targets.id
    targets = [x if not isinstance(x, ast.Name) else x.id for x in targets]
    return ", ".join([make_expression(x) for x in targets])
    
def make_arg_list(args: ast.arguments) -> str:
    return ", ".join([arg.arg for arg in args.args])

def make_bases(bases):
    return ", ".join([make_expression(x) for x in bases])

def make_indent(count):
    if count == 0:
        return ""
    return "    "*count

"""------------------------------------------------------------------------------------------"""
""" Main Class                                                                               """
"""------------------------------------------------------------------------------------------"""

class SourceGenerator:
    def __init__(self, nodes: list[ast.AST]) -> None:
        self.nodes = nodes
        self._nlen = len(self.nodes) -1 
        self._nindex = -1
        self.source = []
        self.indentation = ""
        self.indent = 0

        self._meths = [
            self.source_FunctionDef,
            self.source_AsyncFunctionDef,
            self.source_ClassDef,
            self.source_Return,
            self.source_Delete,
            self.source_Assign,
            self.source_AugAssign,
            self.source_AnnAssign,
            self.source_For,
            self.source_AsyncFor,
            self.source_While,
            self.source_If,
            self.source_With,
            self.source_AsyncWith,
            self.source_Raise,
            self.source_Try,
            self.source_TryStar,
            self.source_Assert,
            self.source_Import,
            self.source_ImportFrom,
            self.source_Global,
            self.source_Nonlocal,
            self.source_Expr,
            self.source_Pass,
            self.source_Break,
            self.source_Continue,
            self.source_Match,
            self.source_TypeAlias,
            self.source_BoolOp,
            self.source_BinOp,
            self.source_UnaryOp,
            self.source_Lambda,
            self.source_IfExp,
            self.source_Dict,
            self.source_Set,
            self.source_ListComp,
            self.source_SetComp,
            self.source_DictComp,
            self.source_GeneratorExp,
            self.source_Await,
            self.source_Yield,
            self.source_YieldFrom,
            self.source_Compare,
            self.source_Call,
            self.source_FormattedValue,
            self.source_JoinedStr,
            self.source_Constant,
            self.source_NamedExpr,
            self.source_Attribute,
            self.source_Subscript,
            self.source_Starred,
            self.source_Name,
            self.source_List,
            self.source_Tuple]
        self._types = [
            ast.FunctionDef,
            ast.AsyncFunctionDef,
            ast.ClassDef,
            ast.Return,
            ast.Delete,
            ast.Assign,
            ast.AugAssign,
            ast.AnnAssign,
            ast.For,
            ast.AsyncFor,
            ast.While,
            ast.If,
            ast.With,
            ast.AsyncWith,
            ast.Raise,
            ast.Try,
            ast.TryStar,
            ast.Assert,
            ast.Import,
            ast.ImportFrom,
            ast.Global,
            ast.Nonlocal,
            ast.Expr,
            ast.Pass,
            ast.Break,
            ast.Continue,
            ast.Match,
            ast.TypeAlias,
            ast.BoolOp,
            ast.BinOp,
            ast.UnaryOp,
            ast.Lambda,
            ast.IfExp,
            ast.Dict,
            ast.Set,
            ast.ListComp,
            ast.SetComp,
            ast.DictComp,
            ast.GeneratorExp,
            ast.Await,
            ast.Yield,
            ast.YieldFrom,
            ast.Compare,
            ast.Call,
            ast.FormattedValue,
            ast.JoinedStr,
            ast.Constant,
            ast.NamedExpr,
            ast.Attribute,
            ast.Subscript,
            ast.Starred,
            ast.Name,
            ast.List,
            ast.Tuple
        ]
    
    def _add(self, line: str):
        self.source.append(self.indentation+line)

    def _function(self, node: ast.AST):
        for idx, t in enumerate(self._types):
            if isinstance(node, t):
                return self._meths[idx]
        return None
    
    def _nextnode(self):
        if self._nindex == self._nlen:
            self.node = None
            return
        self._nindex+=1
        self.node = self.nodes[self._nindex]

    def _next_node_type(self, type:ast.AST):
        while True:
            self._nextnode()
            if isinstance(self.node, type):
                break
    
    def _incr(self):
        """ Increment the indentation, make the spacing for it"""
        self.indent+=1
        self.indentation = "".join(["    "*self.indent])

    def _decr(self):
        """ Decrement the indent and make the spacing for it"""
        self.indent-=1
        if self.indent == 0:
            self.indentation = ""
        else:
            self.indentation = "".join(["    "*self.indent])
                
    def writelines(self):
        self._nindex = -1
        self.source = []
        self.indentation = ""
        self.indent = 0

        while True:
            self._nextnode()
            if self.node == None:
                break
            f = self._function(self.node)
            if f != None:
                f(self.node)

        return self.source

    def source_FunctionDef(self, statement: ast.FunctionDef, method=False) -> None:
        al = ""
        if method == True:
            al = "self, " + make_arg_list(statement.args)
            self._incr()
        elif method == False:
            al = make_arg_list(statement.args)
        self._add(f"def {statement.name}({al}):")
        self._incr()
        for st in statement.body:
            self.source_statement(st)
        self._decr()
        if method == True:
            self._decr()
        

    def source_AsyncFunctionDef(self, statement: ast.AsyncFunctionDef, method=False) -> None:
        al = ""
        if method == True:
            al = "self, " + make_arg_list(statement.args)
            self._incr()
        elif method == False:
            al = make_arg_list(statement.args)
        self._add(f"async def {statement.name}({al}):")
        self._incr()
        for st in statement.body:
            self.source_statement(st)
        self._decr()
        if method == True:
            self._decr()
        
    def source_ClassDef(self, statement: ast.ClassDef) -> None:
        self._add(f"class {statement.name}({make_bases(statement.bases)}):")
        self._incr()
        for node in statement.body:
            if isinstance(node, ast.FunctionDef):
                self.source_FunctionDef(node, True)
            else:
                self.source_statement(node)
        self._decr()
        
    def source_Return(self, statement: ast.Return) -> None:
        self._add(f"return {make_expression(statement.value)}")
        
    def source_Delete(self, statement: ast.Delete) -> None:
        self._add(f"del {make_targets(statement.targets)}")
        
    def source_Assign(self, statement: ast.Assign) -> None:
        self._add(f"{make_targets(statement.targets)} = {make_expression(statement.value)}")

    def source_AugAssign(self, statement: ast.AugAssign) -> None:
        self._add(f"{make_target(statement.target)}{get_op_string(statement.op)}{make_expression(statement.value)}")
        
    def source_AnnAssign(self, statement: ast.AnnAssign) -> None:
        t= value_to_string(statement.target)
        ann = make_expression(statement.annotation)
        value = make_expression(statement.value)
        self._add(f"{t}:{ann} = {value}")
    
    def source_For(self, statement: ast.For) -> None:
        
        if isinstance(statement.target, ast.Tuple|ast.List):
            _target = ",".join([make_expression(x) for x in statement.target.elts])
        else:
            _target = make_target(statement.target)
        self._add(f"for {_target} in {make_iterable(statement.iter)}:")
        self._incr()
        for st in statement.body:
            self.source_statement(st)
        self._decr()
   
    def source_AsyncFor(self, statement: ast.AsyncFor) -> None:
        if isinstance(statement.target, ast.Tuple|ast.List):
            _target = ",".join([make_expression(x) for x in statement.target.elts])
        else:
            _target = make_target(statement.target)
        self._add(f"async for {_target} in {make_iterable(statement.iter)}:")
        self._incr()
        for st in statement.body:
            self.source_statement(st)
        self._decr()
        
    def source_While(self, statement: ast.While) -> None:
        self._add(f"while {make_expression(statement.test)}:")
        self._incr()
        for st in statement.body:
            self.source_statement(st)
        self._decr()
        if statement.orelse != []:
            self._add("else:")
            self._incr()
            for n in statement.orelse:
                self.source_statement(n)
            self._decr()

    def source_If(self, statement: ast.If, elseif=False) -> None:
        if statement.test == False:
            if statement.body == []:
                return
            i = "else:"
            self._add(i)
            self._incr()
            for item in statement.body:
                self.source_statement(item)
            self._decr()
            return
        
        i = "if" if elseif == False else "elif"
        te = make_expression(statement.test)
        self._add(f"{i} {make_expression(statement.test)}:")
        self._incr()
        for n in statement.body:
            self.source_statement(n)
        self._decr()
        if statement.orelse != []:
            for st in statement.orelse:
                if isinstance(st, ast.If):
                    self.source_If(statement=st, elseif=True)
                    continue
                self.source_statement(st)


    def _make_with_items(self, items:list[ast.withitem]):
        its = []
        for item in items:
            cont = make_expression(item.context_expr)
            if item.optional_vars != None:
                cont+=f" as {make_expression(item.optional_vars)}"
            its.append(cont)
        return ", ".join(its)

    def source_With(self, statement: ast.With) -> None:
        self._add(f"with {self._make_with_items(statement.items)}:")
        self._incr()
        for n in statement.body:
            self.source_statement(n)
        self._decr()
        
    def source_AsyncWith(self, statement: ast.AsyncWith) -> None:
        self._add(f"async with {self._make_with_items(statement.items)}:")
        self._incr()
        for n in statement.body:
            self.source_statement(n)
        self._decr()
        
    def source_Raise(self, statement: ast.Raise) -> None:
        c = "" if statement.cause == None else make_expression(statement.cause)
        ex = "" if statement.exc == None else make_expression(statement.exc)
        self._add(f"raise {c}{ex}")
        
    def source_Try(self, statement: ast.Try) -> None:
        self._add(f"try:")
        self._incr()
        for st in statement.body:
            self.source_statement(st)
        self._decr()
        for h in statement.handlers:
            cont = "except"
            if h.type != None:
                cont += " " + make_expression(h.type)
            if h.name != None:
                cont+=f" as {h.name}"
            cont+=":"
            self._add(cont)
            self._incr()
            for b in h.body:
                self.source_statement(b)
            self._decr()
        if statement.finalbody != []:
            self._add("finally:")
            self._incr()
            for f in statement.finalbody:
                self.source_statement(f)
            self._decr()

    def source_TryStar(self, statement: ast.TryStar) -> None:
        self._add(try_star_to_string(statement))
        
    def source_Assert(self, statement: ast.Assert) -> None:
        self._add(f"assert {make_expression(statement.test)}")
        
    def source_Import(self, statement: ast.Import) -> None:
        x = []
        for name in statement.names:
            s = name.name
            if name.asname != None:
                s+=f" as {name.asname}"
            x.append(s)
        self._add(f"{",".join(x)}")
        
    def source_ImportFrom(self, statement: ast.ImportFrom) -> None:
        m = statement.module if statement.module != None else "*"
        x = []
        for name in statement.names:
            s = name.name
            if name.asname != None:
                s+=f" as {name.asname}"
            x.append(s)
        self._add(f"from {m} import {", ".join(x)}")

    def source_Global(self, statement: ast.Global) -> None:
        pass
    def source_Nonlocal(self, statement: ast.Nonlocal) -> None:
        pass
        
    def source_Expr(self, statement: ast.Expr) -> None:
        self._add(make_expression(statement))
        
    def source_Pass(self, statement: ast.Pass) -> None:
        self._add("pass")
        
    def source_Break(self, statement: ast.Break) -> None:
        self._add("break")
        
    def source_Continue(self, statement: ast.Continue) -> None:
        self._add("continue")
    
    def _make_pattern(self, pattern: ast.pattern):
        if isinstance(pattern, ast.MatchValue):
            return make_expression(pattern.value)
        elif isinstance(pattern, ast.MatchSingleton):
            return str(pattern.value)
        elif isinstance(pattern, ast.MatchSequence):
            return ", ".join([self._make_pattern(x) for x in pattern.patterns])
        elif isinstance(pattern, ast.MatchStar):
            return "*" + pattern.name
        elif isinstance(pattern, ast.MatchMapping):
            return 
        elif isinstance(pattern, ast.MatchClass):
            pass
        elif isinstance(pattern, ast.MatchAs):
            pass
        elif isinstance(pattern, ast.MatchOr):
            pass
        
    def _source_case(self, match_case: ast.match_case):
        self._add(f"case {self._make_pattern(match_case.pattern)}:")
        self._incr()
        for x in match_case.body:
            self.source_statement(x)
        self._decr()

    def source_Match(self, statement: ast.Match) -> None:
        self._add(f"match {make_expression(statement.subject)}:")
        self._incr()
        for ca in statement.cases:
            self._add() 
        self.source.append()
        
    def source_TypeAlias(self, statement: ast.TypeAlias) -> None:
        pass

    def source_statement(self, statement:ast.stmt) -> None:
        if isinstance(statement, ast.FunctionDef):
            self.source_FunctionDef(statement)
            return
        elif isinstance(statement, ast.AsyncFunctionDef):
            self.source_AsyncFunctionDef(statement)
            return
        elif isinstance(statement, ast.ClassDef):
            self.source_ClassDef(statement)
            return
        elif isinstance(statement, ast.Return):
            self.source_Return(statement)
            return
        elif isinstance(statement, ast.Delete):
            self.source_Delete(statement)
            return
        elif isinstance(statement, ast.Assign):
            self.source_Assign(statement)
            return
        elif isinstance(statement, ast.AugAssign):
            self.source_AugAssign(statement)
            return
        elif isinstance(statement, ast.AnnAssign):
            self.source_AnnAssign(statement)
            return
        elif isinstance(statement, ast.For):
            self.source_For(statement)
            return
        elif isinstance(statement, ast.AsyncFor):
            self.source_AsyncFor(statement)
            return
        elif isinstance(statement, ast.While):
            self.source_While(statement)
            return
        elif isinstance(statement, ast.If):
            self.source_If(statement)
            return
        elif isinstance(statement, ast.With):
            self.source_With(statement)
            return
        elif isinstance(statement, ast.AsyncWith):
            self.source_AsyncWith(statement)
            return
        elif isinstance(statement, ast.Raise):
            self.source_Raise(statement)
            return
        elif isinstance(statement, ast.Try):
            self.source_Try(statement)
            return
        elif isinstance(statement, ast.TryStar):
            self.source_TryStar(statement)
            return
        elif isinstance(statement, ast.Assert):
            self.source_Assert(statement)
            return
        elif isinstance(statement, ast.Import):
            self.source_Import(statement)
            return
        elif isinstance(statement, ast.ImportFrom):
            self.source_ImportFrom(statement)
            return
        elif isinstance(statement, ast.Global):
            self.source_Global(statement)
            return
        elif isinstance(statement, ast.Nonlocal):
            self.source_Nonlocal(statement)
            return
        elif isinstance(statement, ast.Expr):
            self.source_Expr(statement)
            return
        print(statement)

    def source_BoolOp(self, expr: ast.BoolOp) -> None:
        exprs = ", ".join([make_expression(x) for x in expr.values])
        self._add(f"{get_op_string(expr.op)} {exprs}")
        
    def source_BinOp(self, expr: ast.BinOp) -> None:
        self._add(f"{make_expression(expr.left)} {get_op_string(expr.op)} {make_expression(expr.right)}")

    def source_UnaryOp(self, expr: ast.UnaryOp) -> None:
        self._add(f"{get_op_string(expr.op)}{make_expression(expr.operand)}")

    def source_Lambda(self, expr: ast.Lambda) -> None:
        _args = ", ".join([arg.arg for arg in expr.args.args])
        b = value_to_string(expr.body)
        self._add(f"lambda {_args}: {b}")

    def source_IfExp(self, expr: ast.IfExp) -> None:
        t = make_expression(expr.test)
        e = ""
        if expr.orelse != None:
            e = "else " + make_expression(expr.orelse)
        self._add(f"if {t} {make_expression(expr.body)}")
        
    def source_Dict(self, expr: ast.expr) -> None:
        self._add(value_to_string(expr))

    def source_Set(self, expr: ast.expr) -> None:
        self._add(value_to_string(expr))

    def source_ListComp(self, expr: ast.expr) -> None:
        pass

    def source_SetComp(self, expr: ast.expr) -> None:
        pass

    def source_DictComp(self, expr: ast.expr) -> None:
        pass

    def source_GeneratorExp(self, expr: ast.expr) -> None:
        pass

    def source_Await(self, expr: ast.expr) -> None:
        self._add(make_expression(expr))

    def source_Yield(self, expr: ast.expr) -> None:
        self._add(make_expression(expr))

    def source_YieldFrom(self, expr: ast.expr) -> None:
        self._add(make_expression(expr))

    def source_Compare(self, expr: ast.expr) -> None:
        self._add(make_expression(expr))

    def source_Call(self, expr: ast.expr) -> None:
        self._add(value_to_string(expr))

    def source_FormattedValue(self, expr: ast.FormattedValue) -> None:
        value_str = value_to_string(expr.value)
        conversion = expr.conversion
        format_spec = expr.format_spec
        conversion_str = f"!{chr(conversion)}" if conversion != -1 else ""
        format_spec_str = f":{value_to_string(format_spec)}" if format_spec else ""
        self._add(f"{{{value_str}{conversion_str}{format_spec_str}}}")

    def source_JoinedStr(self, expr: ast.JoinedStr) -> None:
        parts = [make_expression(part) for part in expr.values]
        self._add(f"f\"{''.join(parts)}\"")

    def source_Constant(self, expr: ast.expr) -> None:
        self._add(value_to_string(expr))

    def source_NamedExpr(self, expr: ast.NamedExpr) -> None:
        target_str = make_expression(expr.target)
        value_str = make_expression(expr.value)
        self._add(f"{target_str} := {value_str}")
        
    def source_Attribute(self, expr: ast.expr) -> None:
        self._add(value_to_string(expr))

    def source_Subscript(self, expr: ast.expr) -> None:
        self._add(value_to_string(expr))

    def source_Starred(self, expr: ast.expr) -> None:
        self._add(starred_to_string(expr))

    def source_Name(self, expr: ast.Name) -> None:
        self._add(f"{expr.id}")

    def source_List(self, expr: ast.expr) -> None:
        self._add(value_to_string(expr))

    def source_Tuple(self, expr: ast.expr) -> None:
        self._add(value_to_string(expr))
        
        

