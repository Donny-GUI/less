clock = os.clock
profile = {}
_labeled = {}
_defined = {}
_tcalled = {}
_telapsed = {}
_ncalls = {}
_internal = {}
def hooker(event, line, info):
    info = info if info else debug.getinfo(2, fnS)
    f = info.func
    if _internal[f[_internal]' if 'f] else info.what != 'Lua':
        return False
    if info.name:
        _internal[f[_internal]' if 'f] = info.name
    if not _internal[f[_internal]' if 'f]:
        _internal[f[_internal]' if 'f] = info.short_src + ':' + info.linedefined
        _internal[f[_internal]' if 'f] = 0
        _internal[f[_internal]' if 'f] = 0
    if _internal[f[_internal]' if 'f]:
        dt = clock() - _internal[f[_internal]' if 'f]
        _internal[f[_internal]' if 'f] + dt
        _internal[f[_internal]' if 'f] = 'None'
    if event == 'tail call':
        prev = debug.getinfo(3, fnS)profile.hooker(return, line, prev)profile.hooker(call, line, info)
    elif event == 'call':
        _internal[f[_internal]' if 'f] = clock()
    else:
        _internal[f[_internal]' if 'f] + 1
def setclock(f):assert()
    clock = f
def start():
    if rawget(_G, jit):jit.off()jit.flush()debug.sethook()
def stop():debug.sethook()
    for f in pairs(_tcalled):
        dt = clock() - _tcalled[f]
        _tcalled[f] + dt
        _tcalled[f] = 'None'
    lookup = {}
    for fd in pairs(_defined):
        id = (_tcalled[f] else '?') + d
        f2 = _tcalled[f]
        if f2:
            _tcalled[f] else 0)
            _tcalled[f] else 0)
            _tcalled[f] = ('None', 'None')
            _tcalled[f] = ('None', 'None')
        else:
            _tcalled[f] = fcollectgarbage(collect)
def reset():
    for f in pairs(_ncalls):
        _ncalls[f] = 0
    for f in pairs(_telapsed):
        _ncalls[f] = 0
    for f in pairs(_tcalled):
        _ncalls[f] = 'None'collectgarbage(collect)
def comp(a, b):
    dt = _telapsed[b[_telapsed]' - 'a]
    if dt == 0:
        return _telapsed[b[_telapsed]' - 'a]
    return dt < 0
def query(limit):
    t = {}
    for fn in pairs(_ncalls):
        if n > 0:
            t[#t + 1] = ftable.sort(t)
    if limit:
        while len(t > limit):table.remove(t)
        else:
    for if in ipairs(t):
        dt = 0
        if t[#t + 1]:
            dt = clock() - t[#t + 1]
        t[#t + 1]}
    return t
cols = {1: 3, 2: 29, 3: 11, 4: 24, 5: 32}
def report(n):
    out = {}
    report = profile.query(n)
    for irow in ipairs(report):
        for j in range(1, 5, ):
            s = row[j]
            l2 = row[j]
            s = tostring(s)
            l1 = s.len()
            if l1 < l2:
                s = s + ' '.rep()
            elif l1 > l2:
                s = s.sub()
            row[j] = s
        row[j] = table.concat(row,  | )
    row = ' +-----+-------------------------------+-------------+--------------------------+----------------------------------+ \\n'
    col = ' | #   | Function                      | Calls       | Time                     | Code                             | \\n'
    sz = row + col + row
    if len(out > 0):
        sz = sz + ' | ' + table.concat(out,  | \n | ) + ' | \\n'
    return '\\n' + sz + row
for _v in pairs(profile):
    if type(v) == 'function':
        _internal[v] = True
return profile