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
    if 'f[_internal]' if 'f[_internal]' else info.what != 'Lua':
        return False
    if info.name:
        'f[_labeled]' = info.name
    if not 'f[_defined]':
        'f[_defined]' = info.short_src + ':' + info.linedefined
        'f[_ncalls]' = 0
        'f[_telapsed]' = 0
    if 'f[_tcalled]':
        dt = clock() - 'f[_tcalled]'
        'f[_telapsed]' = 'f[_telapsed]' + dt
        'f[_tcalled]' = 'None'
    if event == 'tail call':
        prev = debug.getinfo(3, fnS)profile.hooker(return, line, prev)profile.hooker(call, line, info)
    elif event == 'call':
        'f[_tcalled]' = clock()
    else:
        'f[_ncalls]' = 'f[_ncalls]' + 1
def setclock(f):assert()
    clock = f
def start():
    if rawget(_G, jit):jit.off()jit.flush()debug.sethook()
def stop():debug.sethook()
    for f in pairs(_tcalled):
        dt = clock() - 'f[_tcalled]'
        'f[_telapsed]' = 'f[_telapsed]' + dt
        'f[_tcalled]' = 'None'
    lookup = {}
    for fd in pairs(_defined):
        id = ('f[_labeled]' if 'f[_labeled]' else '?') + d
        f2 = 'id[lookup]'
        if f2:
            'f2[_ncalls]' = 'f2[_ncalls]' + ('f[_ncalls]' if 'f[_ncalls]' else 0)
            'f2[_telapsed]' = 'f2[_telapsed]' + ('f[_telapsed]' if 'f[_telapsed]' else 0)
            'f[_defined]' = 'f[_labeled]' = ('None', 'None')
            'f[_ncalls]' = 'f[_telapsed]' = ('None', 'None')
        else:
            'id[lookup]' = fcollectgarbage(collect)
def reset():
    for f in pairs(_ncalls):
        'f[_ncalls]' = 0
    for f in pairs(_telapsed):
        'f[_telapsed]' = 0
    for f in pairs(_tcalled):
        'f[_tcalled]' = 'None'collectgarbage(collect)
def comp(a, b):
    dt = 'b[_telapsed]' - 'a[_telapsed]'
    if dt == 0:
        return 'b[_ncalls]' < 'a[_ncalls]'
    return dt < 0
def query(limit):
    t = {}
    for fn in pairs(_ncalls):
        if n > 0:
            '#t + 1[t]' = ftable.sort(t)
    if limit:
        while len(t > limit):table.remove(t)
        else:
    for if in ipairs(t):
        dt = 0
        if 'f[_tcalled]':
            dt = clock() - 'f[_tcalled]'
        'i[t]' = {1: i, 2: 'f[_labeled]' if 'f[_labeled]' else '?', 3: 'f[_ncalls]', 4: 'f[_telapsed]' + dt, 5: 'f[_defined]'}
    return t
cols = {1: 3, 2: 29, 3: 11, 4: 24, 5: 32}
def report(n):
    out = {}
    report = profile.query(n)
    for irow in ipairs(report):
        for j in range(1, 5, ):
            s = 'j[row]'
            l2 = 'j[cols]'
            s = tostring(s)
            l1 = s.len()
            if l1 < l2:
                s = s + ' '.rep()
            elif l1 > l2:
                s = s.sub()
            'j[row]' = s
        'i[out]' = table.concat(row,  | )
    row = ' +-----+-------------------------------+-------------+--------------------------+----------------------------------+ \\n'
    col = ' | #   | Function                      | Calls       | Time                     | Code                             | \\n'
    sz = row + col + row
    if len(out > 0):
        sz = sz + ' | ' + table.concat(out,  | \n | ) + ' | \\n'
    return '\\n' + sz + row
for _v in pairs(profile):
    if type(v) == 'function':
        'v[_internal]' = True
return profile