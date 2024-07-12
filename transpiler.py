from srcgen import SourceGenerator
from astgen import make_python3_module, lua_ast_from_string, pyast,  python3_module


def lua_to_python(lua_filepath:str) -> str:
    """Converts a lua filepath into python source code.

    Args:
        lua_filepath (str): path to a lua file

    Returns:
        str: python source code
    """
    nodes = [x for x in make_python3_module(lua_filepath).body]
    sgen = SourceGenerator(nodes)
    lines = sgen.writelines()
    for line in lines:
        print(line)
    return "\n".join(lines)


class LuaPythonTranspiler:
    """
    A transpiler class for converting Lua code to Python code.

    Methods:
        from_file(filepath: str) -> str:
            Transpiles Lua code from a file to equivalent Python code.

            Args:
                filepath (str): The path to the Lua file.

            Returns:
                str: The equivalent Python code as a string.

        from_string(string: str) -> str:
            Transpiles Lua code from a string to equivalent Python code.

            Args:
                string (str): The Lua code as a string.

            Returns:
                str: The equivalent Python code as a string.
    """
    
    @classmethod
    def from_file(cls, filepath: str) -> str:
        """
        Transpiles Lua code from a file to equivalent Python code.

        Args:
            filepath (str): The path to the Lua file.

        Returns:
            str: The equivalent Python code as a string.
        """
        nodes = [x for x in make_python3_module(filepath).body]
        sgen = SourceGenerator(nodes)
        lines = sgen.writelines()
        return "\n".join(lines)

    @classmethod
    def from_string(cls, string: str) -> str:
        """
        Transpiles Lua code from a string to equivalent Python code.

        Args:
            string (str): The Lua code as a string.

        Returns:
            str: The equivalent Python code as a string.
        """
        tree = lua_ast_from_string(string)
        body = []
        for statement in tree.body.body:
            st = pyast(statement)
            if st is not None:
                body.append(st)
        sgen = SourceGenerator(body)
        lines = sgen.writelines()
        return "\n".join(lines)
    