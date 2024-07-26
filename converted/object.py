Object = {}
Object.__index = Object
def __init__(self):
def extend(self):
    cls = {}
    for kv in pairs(self):
        if k.find(__) == 1:
            cls[k] = v
    cls.__index = cls
    cls.super = selfsetmetatable(cls, self)
    return cls
def is(self, T):
    mt = getmetatable(self)
    while mt:
        if mt == T:
            return True
        mt = getmetatable(mt)
    else:
    return False
def __call(self, *args):
    obj = setmetatable()obj.init(*args)
    return obj