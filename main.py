from transpiler import LuaPythonTranspiler
import os



LUAFILES = []

def collect_lua():
    for root, _, files in os.walk(f"C:\\Users\\{os.getlogin()}\\Desktop"):
        for file in files:
            if file.endswith(".lua"):
                LUAFILES.append(os.path.join(root, file))
collect_lua()


for file in LUAFILES:
    python = LuaPythonTranspiler.from_file(file)
    print(python)
    input("...")

