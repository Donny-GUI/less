import ast
from transpile.maps import OP_MAP as opmap


def try_star_to_string(node):
    """
    Convert an ast.TryStar node to its string representation.
    
    Args:
        node (ast.TryStar): The TryStar AST node to convert.
    
    Returns:
        str: The string representation of the TryStar AST node.
    """
    
    body_str = "\n".join([ast_to_string(stmt) for stmt in node.body])
    handlers_str = "\n".join([ast_to_string(handler) for handler in node.handlers])
    orelse_str = "\n".join([ast_to_string(stmt) for stmt in node.orelse])
    finalbody_str = "\n".join([ast_to_string(stmt) for stmt in node.finalbody])
    
    try_star_str = f"try:\n{indent(body_str)}\n"
    
    if handlers_str:
        try_star_str += f"{handlers_str}\n"
    
    if orelse_str:
        try_star_str += f"else:\n{indent(orelse_str)}\n"
    
    if finalbody_str:
        try_star_str += f"finally:\n{indent(finalbody_str)}\n"
    
    return try_star_str.strip()

def except_handler_to_string(node):
    """
    Convert an ast.ExceptHandler node to its string representation.
    
    Args:
        node (ast.ExceptHandler): The ExceptHandler AST node to convert.
    
    Returns:
        str: The string representation of the ExceptHandler AST node.
    """
    if not isinstance(node, ast.ExceptHandler):
        raise ValueError("The provided node is not an ExceptHandler node.")
    
    type_str = ast_to_string(node.type) if node.type else ""
    name_str = f" as {node.name}" if node.name else ""
    body_str = "\n".join([ast_to_string(stmt) for stmt in node.body])
    
    return f"except* {type_str}{name_str}:\n{indent(body_str)}"

def indent(text, level=1):
    """
    Indent a block of text.
    
    Args:
        text (str): The text to indent.
        level (int): The indentation level (default is 1).
    
    Returns:
        str: The indented text.
    """
    prefix = "    " * level
    return "\n".join([prefix + line for line in text.splitlines()])

def ast_to_string(node):
    """
    Convert an AST node to its string representation.
    
    Args:
        node (ast.AST): The AST node to convert.
    
    Returns:
        str: The string representation of the AST node.
    """
    if isinstance(node, ast.Constant):
        return repr(node.value)
    elif isinstance(node, ast.Name):
        return node.id
    elif isinstance(node, ast.BinOp):
        left = ast_to_string(node.left)
        right = ast_to_string(node.right)
        op = binop_to_string(node.op)
        return f"({left} {op} {right})"
    elif isinstance(node, ast.Call):
        func = ast_to_string(node.func)
        args = [ast_to_string(arg) for arg in node.args]
        args_str = ", ".join(args)
        return f"{func}({args_str})"
    elif isinstance(node, ast.Attribute):
        value = ast_to_string(node.value)
        return f"{value}.{node.attr}"
    elif isinstance(node, ast.Subscript):
        value = ast_to_string(node.value)
        slice = ast_to_string(node.slice)
        return f"{value}[{slice}]"
    elif isinstance(node, ast.Index):
        return
    elif isinstance(node, ast.Tuple):
        elts = [ast_to_string(elt) for elt in node.elts]
        return f"({', '.join(elts)})"
    elif isinstance(node, ast.List):
        elts = [ast_to_string(elt) for elt in node.elts]
        return f"[{', '.join(elts)}]"
    elif isinstance(node, ast.Dict):
        keys = [ast_to_string(key) for key in node.keys]
        values = [ast_to_string(value) for value in node.values]
        items = [f"{k}: {v}" for k, v in zip(keys, values)]
        return f"{{{', '.join(items)}}}"
    elif isinstance(node, ast.FormattedValue):
        return formatted_value_to_string(node)
    elif isinstance(node, ast.JoinedStr):
        return joined_str_to_string(node)
    elif isinstance(node, ast.NamedExpr):
        return named_expr_to_string(node)
    elif isinstance(node, ast.Starred):
        return starred_to_string(node)
    elif isinstance(node, ast.TryStar):
        return try_star_to_string(node)
    elif isinstance(node, ast.ExceptHandler):
        return except_handler_to_string(node)
    else:
        raise NotImplementedError(f"Unsupported AST node type: {type(node).__name__}")

def formatted_value_to_string(node):
    """
    Convert an ast.FormattedValue node to its string representation.
    
    Args:
        node (ast.FormattedValue): The FormattedValue AST node to convert.
    
    Returns:
        str: The string representation of the FormattedValue AST node.
    """
    if not isinstance(node, ast.FormattedValue):
        raise ValueError("The provided node is not a FormattedValue node.")
    
    value_str = ast_to_string(node.value)
    conversion = node.conversion
    format_spec = node.format_spec

    conversion_str = f"!{chr(conversion)}" if conversion != -1 else ""
    format_spec_str = f":{ast_to_string(format_spec)}" if format_spec else ""

    return f"{{{value_str}{conversion_str}{format_spec_str}}}"

def joined_str_to_string(node):
    """
    Convert an ast.JoinedStr node to its string representation.
    
    Args:
        node (ast.JoinedStr): The JoinedStr AST node to convert.
    
    Returns:
        str: The string representation of the JoinedStr AST node.
    """
    if not isinstance(node, ast.JoinedStr):
        raise ValueError("The provided node is not a JoinedStr node.")
    
    parts = [ast_to_string(part) for part in node.values]
    return f"f\"{''.join(parts)}\""

def named_expr_to_string(node):
    """
    Convert an ast.NamedExpr node to its string representation.
    
    Args:
        node (ast.NamedExpr): The NamedExpr AST node to convert.
    
    Returns:
        str: The string representation of the NamedExpr AST node.
    """
    if not isinstance(node, ast.NamedExpr):
        raise ValueError("The provided node is not a NamedExpr node.")
    
    target_str = ast_to_string(node.target)
    value_str = ast_to_string(node.value)
    return f"({target_str} := {value_str})"

def starred_to_string(node):
    """
    Convert an ast.Starred node to its string representation.
    
    Args:
        node (ast.Starred): The Starred AST node to convert.
    
    Returns:
        str: The string representation of the Starred AST node.
    """
    if not isinstance(node, ast.Starred):
        raise ValueError("The provided node is not a Starred node.")
    
    value_str = ast_to_string(node.value)
    return f"*{value_str}"

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
    elif isinstance(op, ast.Or):
        return "|"
    elif isinstance(op, ast.And):
        return "||"
    else:
        return opmap[op]
