import os
from transpile.astmaker import LessASTConverter
from transpile.astwriter import LessASTWriter
from transpile.sourcewriter import SourceWriter
from transpile.patternmatch import LuaAstMatch
from transpile.transtimer import Timer


def collect_lua(directory:str=f"C:\\Users\\{os.getlogin()}\\Desktop"):
    files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".lua"):
                files.append(os.path.join(root, file))
    return files

LUAFILES = collect_lua()  

def delete_converted():
    for root, dirs, files in os.walk(f".\\converted\\"):
        for file in files:
            os.remove(os.path.join(root, file))


def transpile_lua(file):
    global patmat
    print(f"[Transpiling]: {file}")

    convert = LessASTConverter(patmat)
    writer = LessASTWriter()
    source = SourceWriter()
    source.make_directory("converted")

    mod = convert.to_module(file)
    pyfile = os.path.basename(file)
    pyfile = pyfile.split(".")[0] + ".py"

    for node in mod.body:
        string = writer.visit(node)
        source.add(node, string)
    with open(f".\\converted\\{pyfile}", "w") as f:
        source.dump(f)



if __name__ == '__main__':
    

    patmat = LuaAstMatch()
    
    delete_converted()
    for file in LUAFILES:
        transpile_lua(file)

    patmat.save()