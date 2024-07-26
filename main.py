import os
from transpile.astmaker import LessASTConverter
from transpile.astwriter import LessASTWriter
from transpile.sourcewriter import SourceWriter
import re



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

def delete_converted():
    for root, dirs, files in os.walk(f".\\converted\\"):
        for file in files:
            os.remove(os.path.join(root, file))

def extract_method_arguments(method_string):
    # Regex to capture method arguments
    pattern = r'def\s+\w+\s*\(\s*([^)]+)\s*\):'
    match = re.search(pattern, method_string)
    if match:
        return match.group(1)
    return None

def fix_supers(string:str):
    superfind = r"\:[A-Z][a-z]+\.[a-z]+\(.*\)"
    argfind = extract_method_arguments(string)
    string = re.sub(superfind, f":\n        super().__init__({argfind})", string)
    return string

def fix_bases_init(string, class_ast):
    names = [base.name.id for base in class_ast.bases]
    for name in names:
        pat = name + r"\.[a-z]\(.*\)"
        argfind = extract_method_arguments(string)
        string = re.sub(pat, f"\n        super().__init__({argfind})", string)
    return string
     
def transpile_lua(file):
    global patmat

    convert = LessASTConverter(patmat)
    writer = LessASTWriter()
    source = SourceWriter()

    mod = convert.to_module(file)
    pyfile = os.path.basename(file)
    pyfile = pyfile.split(".")[0] + ".py"

    for node in mod.body:
        string = writer.visit(node)
        source.add(node, string)
    with open(f".\\converted\\{pyfile}", "w") as f:
        source.dump(f)
    
    patmat.save()


if __name__ == '__main__':
    from transpile.patternmatch import LuaAstMatch
    from luaparser import ast as last

    patmat = LuaAstMatch()
    

    delete_converted()
    for file in LUAFILES:
        transpile_lua(file)