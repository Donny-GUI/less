

_global_types = {}


def typehint(node):
    k = str(type(node))[8:-2].split(".")[-1]
    if k in ["list", "tuple", "set"]:
        k+="["
        parts = []
        for item in node:
            parts.append(typehint(item))
        k+=",".join(parts)
        k+="]"
    elif k == "dict":
        k+="["
        key_parts = []
        value_parts = []
        for k, v in node.items():
            key_parts.append(typehint(k))
            value_parts.append(typehint(v))
        key_parts = list(set(key_parts))
        value_parts = list(set(value_parts))
        k+="|".join(key_parts)
        k+=", "
        K+="|".join(value_parts)
        k+="]"
    return k


# BASES
class Typed:
    def __init__(self, value: any ) -> None:
        self.value = value
        self.type = typehint(value)

class NamedValue(Typed):
    def __init__(self, value, name) -> None:
        super.__init__(value)
        self.name = name

class IndexedValue(Typed):
    def __init__(self, value: any, index:int) -> None:
        super().__init__(value)
        self.index = index

# OBJECTS
class Parent(Typed):
    """ A parent is the original object in question with attributes of either Attribute or ParentAttribute, or IterableAttribute

    Args:
        Typed (_type_): _description_
    """
    def __init__(self, value:any) -> None:
        super().__init__(value)
        self.attributes: list[Attribute|ParentAttribute] = []
        for name, value in self.value.__dict__.items():
            if name.startswith("__"):
                pass
            if isinstance(value, str|int|bytes|bytearray|float|complex):
                self.attributes.append(Attribute(self.type, name, value))
            elif isinstance(value, list|set|tuple):
                self.attributes.append(IterableAttribute(self.type, name, value))
            else:
                self.attributes.append(ParentAttribute(value, name))

class Attribute(NamedValue):
    def __init__(self, parent:any, name: str, value:any) -> None:
        super().__init__(value, name)
        self.parent = parent
        self.parent_type = typehint(parent)

class IterableAttribute(Attribute):
    def __init__(self, parent: any, name: str, value: any) -> None:
        super().__init__(parent, name, value)
        self.items: list[IndexedValue] = []
        for idx, v in enumerate(self.value):
            self.items.append(IndexedValue(v, idx))

    
    def __str__(self):
        return f"{self.parent_type}.{self.name}: {self.type} = {self.value}"

class ParentAttribute(NamedValue, Parent):
    def __init__(self, value, name) -> None:
        super(NamedValue).__init__(value, name)
        super(Parent).__init__(value)


AttributeType = Attribute|ParentAttribute|IterableAttribute