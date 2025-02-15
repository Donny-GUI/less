"""
converts lua.luaparser.astnodes[nodes] into python.ast[nodes] 
"""
import ast
import luaparser.ast as last
import os
from pathlib import Path
from transpile.macros import Is
from transpile.nodes import Range, Super, MethodCall, MethodDef, ClassBase
from transpile.patternmatch import LuaAstMatch



"""----------------------------------------------------------------------------"""
"""       Lua Node convertor                                                   """
"""----------------------------------------------------------------------------"""



from dataclasses import dataclass

@dataclass
class FindableMethod:
    key: str
    function:ast.FunctionDef


class LessASTConverter:
    
    def __init__(self, patmat: LuaAstMatch = None):
        self._classes = []
        self._to_find: list[FindableMethod] = []
        self._classes_map: dict[str, ast.ClassDef] = {}
        self._patmat:LuaAstMatch = patmat

    def to_module(self, object: str|last.Chunk|Path|ast.AST):
        """takes a python object and returns an ast.Module

        Args:
            object (_type_): _description_

        Raises:
            Exception: _description_
        """
        if isinstance(object, str):
            string = object
            if os.path.exists(string):
                with open(string, "r", errors="ignore") as f:
                    string = f.read()
            o = last.parse(string)

        elif isinstance(object, last.Chunk):
            o = object

        elif isinstance(object, list):
            is_body = True
            for item in object:
                if not isinstance(item, last.Node):
                    is_body = False
            if not is_body:
                raise Exception("not a listable object to convert")
            o = last.Chunk(body=last.Block(body=[object]))

        elif isinstance(object, last.Block):
            o = last.Chunk(body=object)

        # assign the methods to the classes they should be in
        if isinstance(o.body, last.Block):
            total_nodes = [self.convert(x) for x in o.body.body]
        elif isinstance(o, last.Chunk):
            total_nodes = [self.convert(x) for x in o.body]

        for cl in self._to_find:
            if cl.function.name == "init":
                cl.function.name = "__init__"
            try:
                self._classes_map[cl.key].body.append(cl.function)
                total_nodes = [x for x in total_nodes if x!=cl.function]
            except:
                pass
        
        retv = []

        # cleanse the last.Node types
        for node in total_nodes:
            if isinstance(node, last.Node):
                node = self.convert(node)
            elif isinstance(node, ast.AST):
                for child in ast.iter_child_nodes(node):
                    if isinstance(child, last.Node):
                        child = self.convert(child)
            retv.append(node)
                
        m = ast.Module(body=retv, type_ignores=[])
        
        return m
    
    def _super_from_callattr(self, node:ast.Call):
        callfunc = ast.Attribute(value=ast.Call(func=ast.Name(id='super', 
                                                              ctx=ast.Load()), 
                                                args=[], 
                                                keywords=[]), 
                                 attr='__init__', 
                                 ctx=ast.Load())
        return ast.Call(func=callfunc, args=node.args, keywords=[])
    
    def _check_for_super(self, node:FindableMethod):
        clss = self._classes_map[node.key]
        for arg in node.function.args.args:
            if arg.arg == "self":
                for n in node.function.body:
                    if isinstance(n, ast.Call):
                        if isinstance(n.func, ast.Attribute):
                            if n.func.attr == "init":
                                for base in clss.bases:
                                    if base.name.id == n.func.value.id:
                                        n = self._super_from_callattr(n)

    def _multi_value(self, values:list[any]):
        lv = len(values)
        if lv == 0:
            return ast.Constant(value=None, kind="i")
        elif lv == 1:
            return self.convert(values[0])
        return ast.Tuple(elts=[self.convert(x) for x in values])


    def finalize(self):
        for cl in self._to_find:
            if cl.function.name == "init":
                cl.function.name = "__init__"
            try:
                self._classes_map[cl.key].body.append(cl.function)
                total_nodes = [x for x in total_nodes if x!=cl.function]
            except:
                pass
        
        retv = []

        # cleanse the last.Node types
        for node in total_nodes:
            if isinstance(node, last.Node):
                node = self.convert(node)
            elif isinstance(node, ast.AST):
                for child in ast.iter_child_nodes(node):
                    if isinstance(child, last.Node):
                        child = self.convert(child)
            retv.append(node)
                
        m = ast.Module(body=retv, type_ignores=[])
        
        return m
    
    def convert(self, node):
        if self._patmat != None:
            self._patmat.add_node(node)
            
        n = self._fetchMethod(node)(node)
        if isinstance(n, list):
            for x in n:
                ast.fix_missing_locations(x)
        elif isinstance(n, ast.AST):
            ast.fix_missing_locations(n)

        return n
    
    def _table_is_list(self, node:last.Table) -> bool:
        for field in node.fields:
            if field.key == None:
                return True
            return False

    def _fetchMethod(self, node):
        
        method = 'convert_' + node.__class__.__name__
        try:
            convertor = getattr(self, method)
        except AttributeError as ae:
            if isinstance(node, last.ULNotOp):
                return self.convert_ULNotOp

            exit()
        
        return convertor

    def make_LITERAL(self, node: ast.AST):
        if isinstance(node, ast.Constant):
            if node.kind == "s":
                return node.value
            if node.kind == "i":
                return node.value
            elif node.kind == "idx":
                return node.value
            elif node.kind == "OrLoOp":
                return self.convert_OrLoOp(node.kind).value
        elif isinstance(node, ast.Name):
            return node.id
        elif isinstance(node, ast.Attribute):
            return f"{self.make_LITERAL(node.value)}.{self.make_LITERAL(node.attr)}"
        
    def convert_str(self, node: str):
        return node

    def convert_float(self, node: float):
        return node
    
    def convert_int(self, node:int):
        return node

    def convert_list(self, node: list):
        n = [self.convert(x) for x in node]
        
        return n

    def convert_type(self, node):
        return "None"

    def convert_String(self, node:last.String) -> ast.Constant:
        n = ast.Constant(f"{node.s}", kind="s")
        
        return n

    def convert_NoneType(self, node: None):
        return ast.Constant(None, kind=None)
    
    def convert_Number(self, node:last.Number):
        n = ast.Constant(node.n, kind='i')
        
        return n

    def convert_Chunk(self, node: last.Chunk) -> ast.Module:
        body = self.convert(node.body)
        return ast.Module(body=body)

    def convert_Block(self, node: last.Block) -> list:
        n = [self.convert(x) for x in node.body]
        return n

    def convert_ClassBases(self, node:last.Assign):
        return [self.convert_ClassBase(val) for val in node.values]

    def convert_ClassBase(self, node:last.Invoke|last.Index|last.Name):
        string = last.to_lua_source(node)
        if ":" in string:
            name = string.split(":")[0]
            if name == "Object":
                name = name.lower()
            return ClassBase(name)
        return ClassBase(string)
        
    def convert_ClassDef(self, node: last.Assign):
        
        bases = self.convert_ClassBases(node)
        #base = self.convert(node.values)
        #if len(base) > 0:
        #    base = base[0]
        names = [node for node in node.targets if isinstance(node, last.Name)]
        _class = ast.ClassDef(name=names[0].id, bases=bases, keywords=[], body=[], decorator_list=[], type_params=[])
        self._classes.append(_class)
        self._classes_map[names[0].id] = _class
        
        return self._classes[-1]

    def convert_Assign(self, node:last.Assign=None) -> ast.Assign:

        if Is.ClassDef(node) == True:
            return self.convert_ClassDef(node)
                    
        # Get left hand expressions as python asts
        targets = [self.convert(x) for x in node.targets]
        for target in targets:
            # if it is a variable name, give context of storing
            if isinstance(target, ast.Name):
                target.ctx = ast.Store()
        values = self._multi_value(node.values)
        n = ast.Assign(targets=targets, value=values, type_comment=None)
        
        return n
        
    def convert_While(self, node:last.While=None):
        body = self.convert(node.body)
        test = self.convert(node.test)
        n = ast.While(test=test, body=body, orelse=None)
        
        return n
        
    def convert_Do(self, node:last.Do=None) -> list[ast.AST]|None:
        items = []
        for n in node.body:
            items.append(self.convert(n))
        
        return items
        
    def convert_If(self, node:last.If=None):
        test = self.convert(node.test)
        body = self.convert(node.body)
        orelse = []
        if node.orelse:
            orelse = self.convert(node.orelse)
            if isinstance(orelse, list) == False:
                orelse = [orelse]
        
        n = ast.If(test=test, body=body, orelse=orelse)
        
        return n

    def convert_ElseIf(self, node:last.ElseIf=None):
        test = self.convert(node.test)
        body = self.convert(node.body)
        orelse = []
        if node.orelse:
            orelse = self.convert(node.orelse)
            if isinstance(orelse, list) == False:
                orelse = [orelse]
        
        n = ast.If(test=test, body=body, orelse=orelse)
        
        return n

    def convert_Label(self, node:last.Label=None):
        n = ast.Constant(f"\n# {node}\n", kind="label")
        
        return n

    def convert_Goto(self, node:last.Goto=None):
        n = ast.Constant(f"\n# {node}\n", kind="goto")
        
        return n

    def convert_Break(self, node:last.Break=None):
        n = ast.Break()
        return n

    def convert_Return(self, node:last.Return=None):
        if isinstance(node.values, bool):
            kind = node.values
            value = True if node.values == True else False
            v = ast.Constant(value, kind=kind)
        else:
            n = self.convert(node.values)
            v = n if len(n) > 1 else n
        n = ast.Return(value=v)
        
        return n

    def convert_Fornum(self, node:last.Fornum=None):
        target = self.convert(node.target)
        start = self.convert(node.start)
        stop = self.convert(node.stop)
        step = self.convert(node.step)
        body = self.convert(node.body)
        orelse = []
        n = ast.For(target=target, iter=ast.Call(func=ast.Name(id="range"), args=[start, stop, step], keywords=[]), body=body, orelse=orelse)
        
        return n

    def convert_Forin(self, node:last.Forin=None):
        targets = self.convert(node.targets)
        iter = self.convert(node.iter)
        if isinstance(node.iter, last.Invoke):
            if node.iter.func.id == "pairs":
                iter = ast.Call(func=ast.Attribute(value=self.convert(node.iter.args[0]), attr="items", ctx=ast.Load()), args=[], keywords=[])
                targets = [ast.Name(value=x, kind='i') for x in node.targets[0].id]

        body = self.convert(node.body)
        orelse = []
        n = ast.For(target=targets, iter=iter,body=body, orelse=[])
        
        return n

    def convert_Args(self, node: list[last.Name|last.Index]):
        """ converts arguments `list[Expression]` to 
        ast.arguments.
        Args:
            node(list[last.Name|last.Expression]) : list of lua expressions
        Returns:
            ast.arguments object
        """
        items = []
        for x in node:
            py = self.convert(x)
            if isinstance(py, ast.Name):
                if x.id == "/":
                    break
                items.append(ast.arg(py.id))
            elif isinstance(py, ast.Constant):
                items.append(ast.arg(py.value))
            
            else:
                break
        args = items
        return ast.arguments(posonlyargs=args, args=args, vararg=None, kw_defaults=[], kwarg=None, defaults=[], kwonlyargs=[])

    def convert_funcArg(self, node: last.Name|last.Index):
        if isinstance(node, last.Name):
            return self.convert_Name(node)
        elif isinstance(node, last.Index):
            return self.convert_Index(node)

    def convert_Require(self, node:last.Call) -> ast.ImportFrom:
        try:
            if isinstance(node.func.args[0], last.String):
                # makes sure that the Call parent has a String as an arg
                parts = node.func.args[0].s.split(node.func.args[0].delimiter)
                length = len(parts)
                if length == 1:
                    return ast.Import(names=[parts[0]])
                elif length == 2:
                    return ast.ImportFrom(module=parts[0], names=[parts[1:]])
                elif length >= 3:
                    return ast.ImportFrom(module=".".join(parts[:-1]), names=[parts[-1]])
        except:
            pass
    def convert_Call(self, node: last.Call=None):
        if Is.Require(node):
            return self.convert_Require(node)

        func = self.convert_funcArg(node.func)
        args = self.convert_Args(node.args)
        keywords = []
        n = ast.Call(func=func, args=args, keywords=keywords)
        return n

    def convert_Invoke(self, node:last.Invoke=None) -> ast.Call:

        # Ensure the node is of type Invoke
        if not isinstance(node, last.Invoke):
            raise TypeError("Expected luaparser.astnodes.Invoke")
        # Convert the object part
        obj_python_ast = self.convert(node.source)  # This is the 'object' part of 'object:method'
        for subnode in ast.walk(obj_python_ast):
            if isinstance(subnode, ast.Name):
                subnode.id = subnode.id.replace(":", ".")
        
        # Convert the method name part
        method_name = self.convert(node.func)  # This is the 'method' part of 'object:method'
        if isinstance(method_name, ast.Name):
            method_name = method_name.id
        elif isinstance(method_name, ast.Call):
            if isinstance(method_name.func, ast.Name):
                method_name = method_name.func.id
            else:
                method_name = method_name.func
        
        
        # Create an ast.Attribute for the 'object.method' part
        method_attr = ast.Attribute(
            value=obj_python_ast,  # The object part as Python AST
            attr=method_name,   # The method name as a string
            ctx=ast.Load()         # Context is load because we're accessing an attribute
        )

        # Convert the arguments part
        args = node.args  # This should be a list of argument nodes
        args_python_ast = self.convert_Args(args)

        # Create an ast.Call for the method invocation
        call_node = ast.Call(
            func=method_attr,
            args=args_python_ast,
            keywords=[]  # Lua doesn't have keyword arguments
        )

        return call_node

    def convert_Function(self, node:last.Function=None):
        name = self.convert(node.name)
        args = self.convert_Args(node.args)
        body = self.convert(node.body)
        n = ast.FunctionDef(name=name, args=args, body=body)
        
        return n

    def convert_LocalFunction(self, node:last.LocalFunction=None):
        
        name = self.convert(node.name)
        args = self.convert_Args(node.args)
        body = self.convert(node.body)
        n = ast.FunctionDef(name=name, args=args, body=body)
        
        return n
    
    def convert_Super(self, node:last.Invoke):
        callfunc = ast.Attribute(value=ast.Call(func=ast.Name(id='super', 
                                                              ctx=ast.Load()), 
                                                args=[], 
                                                keywords=[]), 
                                 attr='__init__', 
                                 ctx=ast.Load())
        return ast.Call(func=callfunc, args=self.convert_Args(node.args), keywords=[])
        
    def convert_InitializerBody(self, method:last.Method):
        retv = []
        b = method.body
        if isinstance(b, last.Block):
            b = method.body.body
        for node in b:
            if isinstance(node, last.Invoke):
                if node.func.id == "init":
                    retv.append(self.convert_Super(node))
                    continue
            retv.append(self.convert(node))
        
        return retv

    def convert_Method(self, node:last.Method=last.Method):
        key = None
        src = self.convert(node.source)
        if isinstance(src, ast.Name):
            key = src.id

        name = self.convert(node.name)
        # make arguments ast here
        args: ast.arguments = self.convert_Args(node.args)
        # manually add the self arg
        try:
            args.args.insert(0, ast.arg(arg="self"))
        except AttributeError as ae:
            args.insert(0, ast.arg(arg="self"))
        body = self.convert(node.body)
        if isinstance(name, ast.Name):
            name = name.id
        if name == "init":
            name == "__init__"
            body = self.convert_InitializerBody(node)
        n = ast.FunctionDef(name=name, args=args, body=body, type_params=[], decorator_list=[])
        self._to_find.append(FindableMethod(key=key, function=n))
        return n

    def convert_Nil(self, node: last.Nil=None):
        n = ast.Constant(value="None", kind="None")
        return n

    def convert_TrueExpr(self, node:last.TrueExpr=None):
        n = ast.Constant(value=True, kind="True")
        return n

    def convert_FalseExpr(self, node:last.FalseExpr=None):
        n = ast.Constant(value=False, kind="False")
        return n

    def convert_List(self, node:last.Table):
        l = ast.List(elts=[])
        for k, v in node.fields:
            l.elts.append(self.convert(v))
        return l

    def convert_Dict(self, node: last.Table):
        d = ast.Dict(keys=[], values=[])
        for field in node.fields:
            k, v = self.convert_Field(field)
            if isinstance(k, ast.Name):
                k = ast.Constant(value=k.id, kind="s")

            d.keys.append(k)
            d.values.append(v)
        return d

    def convert_Table(self, node:last.Table=None):
        if Is.List(node) == True:
            n = self.convert_List(node)
        else:
            n = self.convert_Dict(node)
        
        return n

    def convert_Field(self, node:last.Field=None) -> tuple[ast.AST]:
        n = (self.convert(node.key), self.convert(node.value))
        
        return n

    def convert_Dots(self, node:last.Dots=None):
        n = ast.Constant(..., kind="Ellipsis")
        return n

    def convert_AnonymousFunction(self, node:last.AnonymousFunction=None):
        
        args = self.convert(node.args)
        body = self.convert(node.body)
        n = ast.Lambda(args, body)
        
        return n

    def convert_UnaryOp(self, node: last.UnaryOp) -> ast.UnaryOp:
        operand = self.convert(node.operand)
        if isinstance(node, last.UMinusOp):
            n = ast.UnaryOp(operand=operand, op=ast.USub())
        if isinstance(node, last.UBNotOp):
            n = ast.UnaryOp(operand=operand, op=ast.Not())
        if isinstance(node, last.ULNotOp):
            n = ast.Call(func=ast.Name(value="not"), args=[operand], keywords=[])
        if isinstance(node, last.ULengthOP):
            n = ast.Call(func=ast.Name("len"), args=[operand], keywords=[])
        
        return n

    def convert_LoOp(self, node: last.LoOp) -> ast.IfExp:
        left = self.convert(node.left)
        if isinstance(left, ast.Name):
            left.ctx = ast.Store()
        right = self.convert(node.right)
        if isinstance(right, ast.Name):
            right.ctx = ast.Load()
        if isinstance(node, last.OrLoOp):
            n = ast.Constant(value=f"{right} if {right} else {left}")
        elif isinstance(node, last.OrLoOp):
            n = ast.Constant(value=f"{left} if {left} else {right}")
        
        return n

    def convert_AriOp(self, node: last.AriOp) -> ast.Compare:
        left = self.convert(node.left)
        if isinstance(left, ast.Name):
            left.ctx = ast.Store()
        right = self.convert(node.right)
        if isinstance(right, ast.Name):
            right.ctx = ast.Load()
        if isinstance(node, last.AddOp):
            n = ast.BinOp(left, ast.Add(), right)
        elif isinstance(node, last.SubOp):
            n = ast.BinOp(left, ast.Sub(), right)
        elif isinstance(node, last.MultOp):
            n = ast.BinOp(left, ast.Mult(), right)
        elif isinstance(node, last.FloatDivOp):
            n = ast.BinOp(left, ast.Div(), right)
        elif isinstance(node, last.FloorDivOp):
            n = ast.BinOp(left, ast.FloorDiv(), right)
        elif isinstance(node, last.ModOp):
            n = ast.BinOp(left, ast.Mod(), right)
        elif isinstance(node, last.ExpoOp):
            n = ast.BinOp(left, ast.Pow(), right)
        
        return n

    def convert_BitOp(self, node: last.BitOp) -> ast.Compare|ast.Constant| ast.Tuple:
        left = self.convert(node.left)
        if isinstance(left, ast.Name):
            left.ctx = ast.Store()
        right = self.convert(node.right)
        if isinstance(right, ast.Name):
            right.ctx = ast.Load()
        if isinstance(node, last.BAndOp):
            n = ast.BinOp(left=left, op=ast.BitAnd(), right=right)
        elif isinstance(node, last.BOrOp):
            n =  ast.BinOp(left=left, op=ast.BitOr(), right=right)
        elif isinstance(node, last.BXorOp):
            n = ast.BinOp(left, ast.BitXor(), right) 
        elif isinstance(node, last.BShiftLOp):
            n = ast.BinOp(left, ast.LShift(), right)
        elif isinstance(node, last.BShiftROp):
            n = ast.BinOp(left, ast.RShift(), right)
        
        return n

    def convert_RelOp(self, node: last.RelOp) -> ast.Compare:
        left = self.convert(node.left)
        if isinstance(left, ast.Name):
            left.ctx = ast.Store()
        right = self.convert(node.right)
        if isinstance(right, ast.Name):
            right.ctx = ast.Load()
        if isinstance(node, last.EqToOp):
            n = ast.BinOp(left=left, op=ast.Eq(), right=right)
        elif isinstance(node, last.NotEqToOp):
            n = ast.BinOp(left=left, op=ast.NotEq(), right=right)
        elif isinstance(node, last.LessThanOp):
            n = ast.BinOp(left=left, op=ast.Lt(), right=right)
        elif isinstance(node, last.LessOrEqThanOp):
            n = ast.BinOp(left=left, op=ast.LtE(), right=right)
        elif isinstance(node, last.GreaterThanOp):
            n = ast.BinOp(left=left, op=ast.Gt(), right=right)
        elif isinstance(node, last.GreaterOrEqThanOp):
            n = ast.BinOp(left=left, op=ast.GtE(), right=right)
        
        return n

    def convert_BinaryOp(self, node:last.BinaryOp=None):
        if isinstance(node, last.RelOp):
            n = self.convert_RelOp(node)
        elif isinstance(node, last.AriOp):
            n = self.convert_AriOp(node)
        elif isinstance(node, last.BitOp):
            n = self.convert_BitOp(node)
        elif isinstance(node, last.LoOp):
            n = self.convert_LoOp(node)
        
        return n
        
    def convert_OP(self, node: last.Op):
        if isinstance(node, last.RelOp):
            n = self.convert_RelOp(node)
        elif isinstance(node, last.AriOp):
            n = self.convert_AriOp(node)
        elif isinstance(node, last.BitOp):
            n = self.convert_BitOp(node)
        elif isinstance(node, last.LoOp):
            n = self.convert_LoOp(node)
        
        return n

    def convert_UnaryOp(self, node:last.UnaryOp=None):
        n = self.convert_OP(node)
        
        return n

    def convert_Name(self, node:last.Name=None):
        if node.id == "true":
            return ast.Constant(value=True)
        elif node.id == "false":
            return ast.Constant(value=False)
        
        n = ast.Name(id=node.id)
        
        return n

    def convert_valueName(self, node):
        n = self.convert_funcArg(node)
        if isinstance(n, last.Name):
            return n.id
        elif isinstance(n, last.Index):
            nn = self.convert_Index(n)
            return nn
        elif isinstance(n, last.String):
            return n.id
        
    def convert_Index(self, node:last.Index=None):
        if node.notation == last.IndexNotation.DOT:
            value = self.convert(node.value)
            idx = self.convert(node.idx)
            n = ast.Attribute(value=value, attr=idx)
        elif node.notation == last.IndexNotation.SQUARE:
            _value = last.to_lua_source(node.value)
            _idx = last.to_lua_source(node.idx)
            n = ast.Constant(value=f"{_idx}[{_value}]", kind="i")
        
        return n

    def convert_Varargs(self, node:last.Varargs=None):
        n = ast.Constant(value="*args", kind="*args")
        
        return n

    def convert_Repeat(self, node:last.Repeat=None):
        body = self.convert(node.body)
        t = ast.If(test=self.convert(node.test), body=ast.Break(), orelse=[])
        body.append(t)
        n = ast.While(test=ast.Constant(value=True), body=body)
        
        return n

    def convert_SemiColon(self, node:last.SemiColon=None):
        n = ast.Constant(";")
        return n
    
    def convert_ULNotOp(self, node: last.ULNotOp):
        operand = self.convert(node.operand)
        n = ast.UnaryOp(operand=operand, op=ast.Not())
        return n
    
    def convert_OrLoOp(self, node: last.OrLoOp):
        """ name = Expression1 or Expression2
        name = expression1 if expression1 else expression2
        Args:
            node (last.OrLoOp): _description_

        Returns:
            _type_: _description_
        """
        return ast.IfExp(test=self.convert(node.left),body=self.convert(node.left), orelse=self.convert(node.right))
        
    def convert_LocalAssign(self, node: last.LocalAssign):
        
        return self.convert_Assign(node)

    def convert_EqToOp(self, node: last.EqToOp):
        left = self.convert(node.left)
        right = self.convert(node.right)
        return ast.Compare(left=left, ops=[ast.Eq(), ast.Eq()], comparators=[right])

    def convert_UMinusOp(self, node: last.UMinusOp):
        operand = self.convert(node.operand)
        return ast.UnaryOp(op=ast.USub(), operand=operand)

    def convert_MultOp(self, node:last.MultOp):
        left = self.convert(node.left)
        right = self.convert(node.right)
        return ast.BinOp(left, ast.Mult(), right)

    def convert_bool(self, node):
        return node
    
    def convert_AndLoOp(self, node: last.AndLoOp):
        return ast.BinOp(left=self.convert(node.left), op=ast.BitAnd(), right=self.convert(node.right))

    def convert_AddOp(self, node:last.AddOp):
        return ast.BinOp(left=self.convert(node.left), right=self.convert(node.right), op=ast.Add())
    
    def convert_FloatDivOp(self, node:last.FloatDivOp):
        
        return ast.BinOp(left=self.convert(node.left), right=self.convert(node.right), op=ast.Div())

    def convert_SubOp(self, node:last.SubOp):
        return ast.BinOp(left=self.convert(node.left), right=self.convert(node.right), op=ast.Sub())
    
    def convert_LessThanOp(self, node: last.LessThanOp):
        
        return ast.BinOp(left=self.convert(node.left), right=self.convert(node.right), op=ast.Lt())
    
    def convert_Concat(self, node:last.Concat):
        return ast.BinOp(left=self.convert(node.left), op=ast.Add(), right=self.convert(node.right))

    def convert_LessOrEqThanOp(self, node:last.LessOrEqThanOp):
        
        return ast.Compare(
            left=self.convert(node.left),
            ops=[ast.LtE()],
            comparators=[self.convert(node.right)])
    
    def convert_ULengthOP(self, node: last.ULengthOP):
        return ast.Call(func=ast.Name(id="len"), args=[self.convert(node.operand)], keywords=[])

    def convert_NotEqToOp(self, node:last.LessOrEqThanOp):
        return ast.Compare(
            left=self.convert(node.left),
            ops=[ast.NotEq()],
            comparators=[self.convert(node.right)])
    
    def convert_GreaterThanOp(self, node:last.GreaterThanOp):
        
        return ast.Compare(
            left=self.convert(node.left),
            ops=[ast.Gt()],
            comparators=[self.convert(node.right)])
    
    def convert_GreaterOrEqThanOp(self, node:last.GreaterOrEqThanOp):
        
        return ast.Compare(
            left=self.convert(node.left),
            ops=[ast.GtE()],
            comparators=[self.convert(node.right)])

    def convert_ModOp(self, node:last.ModOp):
        return ast.Compare(
            left=self.convert(node.left),
            ops=[ast.Mod()],
            comparators=[self.convert(node.right)])

    def convert_ExpoOp(self, node:last.ExpoOp):
        return ast.Compare(
            left=self.convert(node.left),
            ops=[ast.Pow()],
            comparators=[self.convert(node.right)])

