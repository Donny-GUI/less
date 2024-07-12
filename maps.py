import ast


def key(object):
    return str(type(object))[8:-2].strip("'")

def get_op_string(op:ast.AST):
    try:
        return OP_MAP[key(op)]
    except:
        return op

OP_MAP = {
    'ast.Add': "+",
    'ast.Sub': "-",
    'ast.Mult': "*",
    'ast.Div': "/",
    'ast.FloorDiv': "//",
    'ast.Mod': "%",
    'ast.Pow': "**",
    'ast.LShift': "<<",
    'ast.RShift': ">>",
    'ast.BitOr': "|",
    'ast.BitXor': "^",
    'ast.BitAnd': "&",
    'ast.MatMult': "@",
    'ast.And': "and",
    'ast.Or': "or",
    'ast.Invert': "~",
    'ast.Not': "not",
    'ast.UAdd': "+",
    'ast.USub': "-",
    'ast.Eq': "==",
    'ast.NotEq': "!=",
    'ast.Lt': "<",
    'ast.LtE': "<=",
    'ast.Gt': ">",
    'ast.GtE': ">=",
    'ast.Is': "is",
    'ast.IsNot': "is not",
    'ast.In': "in",
    'ast.NotIn': "not in",
}

