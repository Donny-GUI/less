
import re
import ast
import os


def index_fix(string):
    matching = r"\'.+\[.+\]\'"
    pattern = r"\'(.+)\[(.+)\]\'"
    patsearch = re.search(pattern, string)
    if patsearch:
        digit = patsearch.group(1)
        object = patsearch.group(2)
        string = re.sub(matching, f"{object}[{digit}]", string)
    return string


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
     


class SourceWriter:
    def __init__(self) -> None:
        self.source = []
        self.nodes = []
    
    def make_directory(self, dir):
        os.makedirs(dir, exist_ok=True)

    def add(self, node, source):
            
        self.nodes.append(node)
        source = fix_supers(source)
        source = index_fix(source)
        if isinstance(node, ast.ClassDef):
            source = fix_bases_init(source, node)
        self.source.append(source)

        with open("temp.py", "a") as f:
            f.write(source+"\n")
    
    def clear(self):
        self.source.clear()
        self.nodes.clear()
    
    def dump(self, fp=None):
        l = "\n".join(self.source)
        if fp:
            fp.write(l)
        return l
        
    
