import os
from transpile.astmaker import LessASTConverter
from transpile.astwriter import LessASTWriter



LUAFILES = []

def collect_lua():
    for root, _, files in os.walk(f"C:\\Users\\{os.getlogin()}\\Desktop"):
        for file in files:
            if file.endswith(".lua"):
                LUAFILES.append(os.path.join(root, file))
collect_lua()

class LuaPythonTranspiler:
    def __init__(self) -> None:
        self.converter = LessASTConverter()

    def convert(self, object):
        mod = self.converter.to_module(object)    

for file in LUAFILES:
    converter = LessASTConverter()
    writer = LessASTWriter()
    mod = converter.to_module(file)
    
    strings = []
    for node in mod.body:
        print(f"[NODE] \033[33m {node}\033[0m")
        strings.append(writer.visit(node))
    with open("tempfile.py", "w") as f:
        f.write("\n".join(strings))    
    input("Check tempfile now....")