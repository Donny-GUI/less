import os
import ast

def show(filename:str):
    with open(filename, "r") as f:
        content = f.read()
    tree = ast.parse(content)
    print(ast.dump(tree))
    print("==============================================")
    print(content)


show(".\\examples\\super.py")