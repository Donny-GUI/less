
import ast


SelfArg = ast.arg("self")
METHOD_ARGUMENTS = ast.arguments(posonlyargs=[SelfArg], args=[SelfArg], vararg=None, kw_defaults=[SelfArg], kwarg=None, defaults=[], kwonlyargs=[])
NO_ARGS = ast.arguments(posonlyargs=[], args=[], vararg=None, kw_defaults=[], kwarg=None, defaults=[], kwonlyargs=[])
NO_BODY = [ast.Pass()]


class MethodDef:
    def __init__(self, name:str="", body:list[ast.stmt]=[ast.Pass()], args:ast.arguments=METHOD_ARGUMENTS, returns=None) -> None:
        self.name:str = name
        self.body: list[ast.stmt] = body
        self.args:ast.arguments = args
        self.returns = returns

class MethodCall:
    def __init__(self, object:ast.Attribute, args:ast.arguments=NO_ARGS) -> None:
        self.object:ast.Attribute = object
        self.args:ast.arguments = args

class ClassBase(ast.AST):
    def __init__(self, name:str="") -> None:
        super().__init__()
        self.name = ast.Name(id=name, ctx=ast.Load())

class KeywordArgument:
    def __init__(self, keyword:str, arg:ast.arg) -> None:
        self.keyword = ast.Name(id=keyword)
        self.arg:ast.arg = arg

class Range:
    def __init__(self, start:int=0, stop:int=0, step:int=0) -> None:
        self.start = ast.Constant(value=start, kind="i")  
        self.stop = ast.Constant(value=start, kind="i")
        self.step = ast.Constant(value=start, kind="i")

class Super:
    def __init__(self, args:ast.arguments=NO_ARGS) -> None:
        self.object = ast.Call(func=ast.Name(id="super", ctx=ast.Load()), keywords=[], args=args)
        