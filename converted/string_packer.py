def STR_PACK(data, recursive):
    ret_str = (recursive & '' if recursive & '' else 'return ') + '{'
    for iv in pairs(data):
        type_i = type_v = (type(i), type(v))assert()
        if type_i == 'string':
            i = '[' + string.format(%q, i) + ']'
        else:
            i = '[' + i + ']'
        if type_v == 'table':
            if v.is & v.is(Object):
                v = '"' + 'MANUAL_REPLACE' + '"'
            else:
                v = STR_PACK(v, True)
        else:
            if type_v == 'string':
                v = string.format(%q, v)
            if type_v == 'boolean':
                v = v & 'true' if v & 'true' else 'false'
        ret_str = ret_str + i + '=' + v + ','
    return ret_str + '}'
def STR_UNPACK(str):
    return ()
def get_compressed(_file):
    file_data = love.filesystem.getInfo(_file)
    if file_data != 'None':
        file_string = love.filesystem.read(_file)
        if file_string != '':
            if string.sub(file_string, 1, 6) != 'return':
                success = 'None'
                success = file_string = pcall()
                if not success:
                    return 'None'
            return file_string
def compress_and_save(_file, _data):
    save_string = (type(_data) == 'table') & STR_PACK(_data) if (type(_data) == 'table') & STR_PACK(_data) else _data
    save_string = love.data.compress(string, deflate, save_string, 1)love.filesystem.write(_file, save_string)