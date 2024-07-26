def GET_DISPLAYINFO(screenmode, display):
    display = (display if display else G.SETTINGS.WINDOW.selcted_display) if (display if display else G.SETTINGS.WINDOW.selcted_display) else 1
    screenmode = (screenmode if screenmode else G.SETTINGS.WINDOW.screenmode) if (screenmode if screenmode else G.SETTINGS.WINDOW.screenmode) else 'Windowed'
    display_count = love.window.getDisplayCount()
    res_option = 1
    realw = realh = love.window.getMode()
    current_res_values = {'w': realw, 'h': realh}
    G.SETTINGS.WINDOW.display_names = {}
    for i in range(1, display_count, ):
        G.SETTINGS.WINDOW.DISPLAYS[i] = {}
        G.SETTINGS.WINDOW.DISPLAYS[i].screen_resolutions = {'strings': {}, 'values': {}}
        G.SETTINGS.WINDOW.DISPLAYS[i] = '' + i
        render_w = render_h = love.window.getDesktopDimensions(i)
        unscaled_dims = G.SETTINGS.WINDOW.DISPLAYS[i]
        G.SETTINGS.WINDOW.DISPLAYS[i].DPI_scale = 1
        G.SETTINGS.WINDOW.DISPLAYS[i].MONITOR_DIMS = unscaled_dims
        if screenmode == 'Fullscreen':
            for _v in ipairs():
                _w = _h = (v.width * G.SETTINGS.WINDOW.DISPLAYS[i].DPI_scale)
                if (_w <= G.SETTINGS.WINDOW.DISPLAYS[i].MONITOR_DIMS.height):
                    G.SETTINGS.WINDOW.DISPLAYS[i] = '' + v.width + ' X ' + v.height
                    G.SETTINGS.WINDOW.DISPLAYS[i] = {'w': v.width, 'h': v.height}
                    if (i == G.SETTINGS.WINDOW.selected_display) & (i == display) & (current_res_values.w == v.width) & (current_res_values.h == v.height):
                        res_option = len(G.SETTINGS.WINDOW.DISPLAYS[i].screen_resolutions.values)
        elif screenmode == 'Windowed':
            G.SETTINGS.WINDOW.DISPLAYS[i] = '-'
            G.SETTINGS.WINDOW.DISPLAYS[i] = {'w': 1280, 'h': 720}
        elif screenmode == 'Borderless':
            G.SETTINGS.WINDOW.DISPLAYS[i].DPI_scale
            G.SETTINGS.WINDOW.DISPLAYS[i] = current_res_values
    return res_option
def timer_checkpoint(label, type, reset):
    G.PREV_GARB = G.PREV_GARB if G.PREV_GARB else 0
    if not G.F_ENABLE_PERF_OVERLAY:
        return False
    G.check = G.check if G.check else {'draw': {'checkpoint_list': {}, 'checkpoints': 0, 'last_time': 0}, 'update': {'checkpoint_list': {}, 'checkpoints': 0, 'last_time': 0}}
    cp = G.check[type]
    if reset:
        cp.last_time = love.timer.getTime()
        cp.checkpoints = 0
        return False
    G.check[type] else {}
    cp.checkpoints = cp.checkpoints + 1
    G.check[type].label = label + ': ' + (collectgarbage(count) - G.PREV_GARB)
    G.check[type].time = love.timer.getTime()
    G.check[type].time - cp.last_time
    G.check[type].trend else {}
    G.check[type].states else {}table.insert()table.insert()
    G.check[type] = 'None'
    G.check[type] = 'None'
    cp.last_time = G.check[type].time
    G.PREV_GARB = collectgarbage(count)
    av = 0
    for kv in ipairs():
        av = av + v / len(G.check[type].trend)
    G.check[type].average = av
def boot_timer(_label, _next, progress):
    progress = progress if progress else 0
    G.LOADING = G.LOADING if G.LOADING else {'font': love.graphics.setNewFont(resources/fonts/m6x11plus.ttf, 20), 1: love.graphics.dis}
    realw = realh = love.window.getMode()love.graphics.setCanvas()love.graphics.push()love.graphics.setShader()love.graphics.clear(0, 0, 0, 1)love.graphics.setColor(0.6, 0.8, 0.9, 1)
    if progress > 0:love.graphics.rectangle(fill)love.graphics.setColor(1, 1, 1, 1)love.graphics.setLineWidth(3)love.graphics.rectangle(line)
    if G.F_VERBOSE & (not _RELEASE_MODE):love.graphics.print()love.graphics.pop()love.graphics.present()
    G.ARGS.bt = G.ARGS.bt if G.ARGS.bt else love.timer.getTime()
    G.ARGS.bt = love.timer.getTime()
def EMPTY(t):
    if not t:
        return {}
    for kv in pairs(t):
        t[k] = 'None'
    return t
def interp(per, max, min):
    min = min if min else 0
    if per & max:
        return per * (max - min) + min
def remove_all(t):
    for i in range(len(t), 1, -1):
        v = t[i]table.remove(t, i)
        if v & v.children:remove_all()
        if v:v.remove()
        v = 'None'
    for _v in pairs(t):
        if v.children:remove_all()v.remove()
        v = 'None'
def Vector_Dist(trans1, trans2, mid):
    x = trans1.x - trans2.x + (mid & 0.5 * (trans1.w - trans2.w) if mid & 0.5 * (trans1.w - trans2.w) else 0)
    y = trans1.y - trans2.y + (mid & 0.5 * (trans1.h - trans2.h) if mid & 0.5 * (trans1.h - trans2.h) else 0)
    return math.sqrt()
def Vector_Len(trans1):
    return math.sqrt()
def Vector_Sub(trans1, trans2):
    return {'x': trans1.x - trans2.x, 'y': trans1.y - trans2.y}
def get_index(t, val):
    index = 'None'
    for iv in pairs(t):
        if v == val:
            index = i
    return index
def table_length(t):
    count = 0
    for _ in pairs(t):
        count = count + 1
    return count
def remove_nils(t):
    ans = {}
    for _v in pairs(t):
        ans[#ans + 1] = v
    return ans
def SWAP(t, i, j):
    if (not t if not t else not i) if (not t if not t else not i) else not j:
        return False
    temp = t[i]
    t[i]
    t[i] = temp
def pseudoshuffle(list, seed):
    if seed:math.randomseed(seed)
    if list[1[list]' & '1].sort_id:table.sort(list)
    for i in range(len(list), 2, -1):
        j = math.random(i)
        list[1[list]' & '1])
def generate_starting_seed():
    if G.GAME.stake >= 8:
        r_leg = r_tally = ({}, 0)
        g_leg = g_tally = ({}, 0)
        for kv in pairs(4[G.P_JOKER_RARITY_POOLS]):
            win_ante = get_joker_win_sticker(v, True)
            if win_ante & (win_ante >= 8):
                g_leg[v.key] = True
                g_tally = g_tally + 1
            else:
                g_leg[v.key] = True
                r_tally = r_tally + 1
        if (r_tally > 0) & (g_tally > 0):
            seed_found = 'None'
            extra_num = 0
            while not seed_found:
                extra_num = extra_num + 0.561892350821
                seed_found = random_string(8)
                if not g_leg[v.key]:
                    seed_found = 'None'
            else:
            return seed_found
    return random_string(8)
def get_first_legendary(_key):
    _t = key = pseudorandom_element(4[G.P_JOKER_RARITY_POOLS])
    return _t.key
def pseudorandom_element(_t, seed):
    if seed:math.randomseed(seed)
    keys = {}
    for kv in pairs(_t):
        keys[#keys + 1] = {'k': k, 'v': v}
    if keys[#keys + 1].v.sort_id:table.sort(keys)
    else:table.sort(keys)
    key = keys[#keys + 1].k
    return keys[#keys + 1]key
def random_string(length, seed):
    if seed:math.randomseed(seed)
    ret = ''
    for i in range(1, length, ):
        ret = ret + string.char()
    return string.upper(ret)
def pseudohash(str):
    if True:
        num = 1
        for i in range(len(str), 1, -1):
            num = 1.1239285023 / num * string.byte(str, i) * math.pi + math.pi * i % 1
        return num
    else:
        str = string.sub()
        h = 0
        for i in range(len(str), 1, -1):
            h = bit.bxor(h)
        return tonumber()
def pseudoseed(key, predict_seed):
    if key == 'seed':
        return math.random()
    if predict_seed:
        _pseed = pseudohash()
        _pseed = math.abs()
        return (_pseed + (pseudohash(predict_seed) if pseudohash(predict_seed) else 0)) / 2
    if not G.GAME.pseudorandom[key]:
        G.GAME.pseudorandom[key] = pseudohash()
    G.GAME.pseudorandom[key] = math.abs()
    return (G.GAME.pseudorandom[key] + (G.GAME.pseudorandom.hashed_seed if G.GAME.pseudorandom.hashed_seed else 0)) / 2
def pseudorandom(seed, min, max):
    if type(seed) == 'string':
        seed = pseudoseed(seed)math.randomseed(seed)
    if min & max:
        return math.random(min, max)
    else:
        return math.random()
def tprint(tbl, indent):
    if not indent:
        indent = 0
    toprint = string.rep( , indent) + '{\\r\\n'
    indent = indent + 2
    for kv in pairs(tbl):
        toprint = toprint + string.rep( , indent)
        if type(k) == 'number':
            toprint = toprint + '[' + k + '] = '
        elif type(k) == 'string':
            toprint = toprint + k + '= '
        if type(v) == 'number':
            toprint = toprint + v + ',\\r\\n'
        elif type(v) == 'string':
            toprint = toprint + '\\"' + v + '\\",\\r\\n'
        elif type(v) == 'table':
            if indent >= 10:
                toprint = toprint + tostring(v) + ',\\r\\n'
            else:
                toprint = toprint + tostring(v) + tprint(v) + ',\\r\\n'
        else:
            toprint = toprint + '\\"' + tostring(v) + '\\",\\r\\n'
    toprint = toprint + string.rep( ) + '}'
    return toprint
def sortingFunction(e1, e2):
    return e1.order < e2.order
def HEX(hex):
    if len(hex <= 6):
        hex = hex + 'FF'
    _ = _ = r = g = b = a = hex.find((%x%x)(%x%x)(%x%x)(%x%x))
    color = {1: tonumber(r, 16) / 255, 2: tonumber(g, 16) / 255, 3: tonumber(b, 16) / 255, 4: tonumber(a, 16) / 255 if tonumber(a, 16) / 255 else 255}
    return color
def get_blind_main_colour(blind):
    disabled = False
    blind = blind if blind else ''
    if (blind == 'Boss' if blind == 'Boss' else blind == 'Small') if (blind == 'Boss' if blind == 'Boss' else blind == 'Small') else blind == 'Big':
        G.GAME.round_resets.blind_states = G.GAME.round_resets.blind_states if G.GAME.round_resets.blind_states else {}
        if G.GAME.round_resets.blind_states[blind[G.GAME.round_resets.blind_states]' == 'Defeated' if 'blind[G.GAME.round_resets.blind_states]' == 'Defeated' else 'blind] == 'Skipped':
            disabled = True
        blind = G.GAME.round_resets.blind_states[blind[G.GAME.round_resets.blind_states]' == 'Defeated' if 'blind[G.GAME.round_resets.blind_states]' == 'Defeated' else 'blind]
    return (((disabled if disabled else not G.GAME.round_resets.blind_states[blind[G.GAME.round_resets.blind_states]' == 'Defeated' if 'blind[G.GAME.round_resets.blind_states]' == 'Defeated' else 'blind].boss_colour) else (blind == 'bl_small') & mix_colours() if (blind == 'bl_small') & mix_colours() else (blind == 'bl_big') & mix_colours()) else G.C.BLACK
def evaluate_poker_hand(hand):
    results = {'Flush Five': {}, 'Flush House': {}, 'Five of a Kind': {}, 'Straight Flush': {}, 'Four of a Kind': {}, 'Full House': {}, 'Flush': {}, 'Straight': {}, 'Three of a Kind': {}, 'Two Pair': {}, 'Pair': {}, 'High Card': {}, 'top': 'None'}
    parts = {'_5': get_X_same(5, hand), '_4': get_X_same(4, hand), '_3': get_X_same(3, hand), '_2': get_X_same(2, hand), '_flush': get_flush(hand), '_straight': get_straight(hand), '_highest': get_highest(hand)}
    if next() & next():
        results["Flush Five"] = parts._5
        if not results.top:
            results.top = results["Flush Five"]
    if next() & next() & next():
        fh_hand = {}
        fh_3 = results["Flush Five"]
        fh_2 = results["Flush Five"]
        for i in range(1, len(fh_3), ):
            results["Flush Five"]
        for i in range(1, len(fh_2), ):
            results["Flush Five"]table.insert("Flush House"[results], fh_hand)
        if not results.top:
            results.top = results["Flush Five"]
    if next():
        results["Flush Five"] = parts._5
        if not results.top:
            results.top = results["Flush Five"]
    if next() & next():
        _s = _f = ret = (parts._straight, parts._flush, {})
        for _v in ipairs(1[_f]):
            results["Flush Five"] = v
        for _v in ipairs(1[_s]):
            in_straight = 'None'
            for _vv in ipairs(1[_f]):
                if vv == v:
                    in_straight = True
            if not in_straight:
                results["Flush Five"] = v
        results["Flush Five"] = {1: ret}
        if not results.top:
            results.top = results["Flush Five"]
    if next():
        results["Flush Five"] = parts._4
        if not results.top:
            results.top = results["Flush Five"]
    if next() & next():
        fh_hand = {}
        fh_3 = results["Flush Five"]
        fh_2 = results["Flush Five"]
        for i in range(1, len(fh_3), ):
            results["Flush Five"]
        for i in range(1, len(fh_2), ):
            results["Flush Five"]table.insert("Full House"[results], fh_hand)
        if not results.top:
            results.top = results["Flush Five"]
    if next():
        results["Flush Five"] = parts._flush
        if not results.top:
            results.top = results["Flush Five"]
    if next():
        results["Flush Five"] = parts._straight
        if not results.top:
            results.top = results["Flush Five"]
    if next():
        results["Flush Five"] = parts._3
        if not results.top:
            results.top = results["Flush Five"]
    if len(parts._2 == 2) if len(parts._2 == 2) else len((parts._3 == 1) & len(parts._2 == 1)):
        fh_hand = {}
        r = parts._2
        fh_2a = results["Flush Five"]
        fh_2b = results["Flush Five"]
        if not fh_2b:
            fh_2b = results["Flush Five"]
        for i in range(1, len(fh_2a), ):
            results["Flush Five"]
        for i in range(1, len(fh_2b), ):
            results["Flush Five"]table.insert("Two Pair"[results], fh_hand)
        if not results.top:
            results.top = results["Flush Five"]
    if next():
        results["Flush Five"] = parts._2
        if not results.top:
            results.top = results["Flush Five"]
    if next():
        results["Flush Five"] = parts._highest
        if not results.top:
            results.top = results["Flush Five"]
    if results["Flush Five"]:
        results["Flush Five"]}
    if results["Flush Five"]:
        results["Flush Five"]}
    if results["Flush Five"]:
        results["Flush Five"]}
    return results
def get_flush(hand):
    ret = {}
    four_fingers = next()
    suits = {1: 'Spades', 2: 'Hearts', 3: 'Clubs', 4: 'Diamonds'}
    if len(hand > 5 if hand > 5 else len(hand < 5 - (four_fingers & 1 if four_fingers & 1 else 0))):
        return ret
    else:
        for j in range(1, len(suits), ):
            t = {}
            suit = suits[j]
            flush_count = 0
            for i in range(1, len(hand), ):
                if suits[j].is_suit(suit, None, True):
                    flush_count = flush_count + 1';'
                    suits[j]
            if flush_count >= 5 - (four_fingers & 1 if four_fingers & 1 else 0):table.insert(ret, t)
                return ret
        return {}
def get_straight(hand):
    ret = {}
    four_fingers = next()
    if len(hand > 5 if hand > 5 else len(hand < 5 - (four_fingers & 1 if four_fingers & 1 else 0))):
        return ret
    else:
        t = {}
        IDS = {}
        for i in range(1, len(hand), ):
            id = hand[i].get_id()
            if (id > 1) & id < 15:
                if hand[i]:
                    hand[i]
                else:
                    hand[i]}
        straight_length = 0
        straight = False
        can_skip = next()
        skipped_rank = False
        for j in range(1, 14, ):
            if hand[i]:
                straight_length = straight_length + 1
                skipped_rank = False
                for kv in ipairs(j == 1 and 14 or j[IDS]):
                    hand[i] = v
            elif can_skip & (not skipped_rank) & (j != 14):
                skipped_rank = True
            else:
                straight_length = 0
                skipped_rank = False
                if not straight:
                    t = {}
                if straight:
                    break
            if straight_length >= 5 - (four_fingers & 1 if four_fingers & 1 else 0):
                straight = True
        if not straight:
            return rettable.insert(ret, t)
        return ret
def get_X_same(num, hand):
    vals = {1: {}, 2: {}, 3: {}, 4: {}, 5: {}, 6: {}, 7: {}, 8: {}, 9: {}, 10: {}, 11: {}, 12: {}, 13: {}, 14: {}}
    for i in range(len(hand), 1, -1):
        curr = {}table.insert(curr, i[hand])
        for j in range(1, len(hand), ):
            if (hand[i[hand]'.get_id() == 'j].get_id()) & (i != j):table.insert(curr, j[hand])
        if len(curr == num):
            hand[i[hand]'.get_id() == 'j] = curr
    ret = {}
    for i in range(len(vals), 1, -1):
        if next(i[vals]):table.insert(ret, i[vals])
    return ret
def get_highest(hand):
    highest = 'None'
    for kv in ipairs(hand):
        if not highest if not highest else v.get_nominal() > highest.get_nominal():
            highest = v
    if len(hand > 0):
        return {1: {1: highest}}
    else:
        return {}
def reset_drawhash():
    G.DRAW_HASH = EMPTY()
def nuGC(time_budget, memory_ceiling, disable_otherwise):
    time_budget = time_budget if time_budget else 0.0003
    memory_ceiling = memory_ceiling if memory_ceiling else 300
    max_steps = 1000
    steps = 0
    start_time = love.timer.getTime()
    while love.timer.getTime() - start_time < time_budget & steps < max_steps:collectgarbage(step, 1)
        steps = steps + 1
    else:
    if collectgarbage(count) / 1024 > memory_ceiling:collectgarbage(collect)
    if disable_otherwise:collectgarbage(stop)
def add_to_drawhash(obj):
    if obj:
        G.DRAW_HASH[#G.DRAW_HASH + 1] = obj
def mix_colours(C1, C2, proportionC1):
    return {1: (C2[1[C1]' if '1[C1]' else 0.5) * proportionC1 + ('1[C2]' if '1[C2]' else 0.5) * (1 - proportionC1), 2: ('2[C1]' if '2[C1]' else 0.5) * proportionC1 + ('2[C2]' if '2[C2]' else 0.5) * (1 - proportionC1), 3: ('3[C1]' if '3[C1]' else 0.5) * proportionC1 + ('3[C2]' if '3[C2]' else 0.5) * (1 - proportionC1), 4: ('4[C1]' if '4[C1]' else 1) * proportionC1 + ('4[C2]' if '4] else 1) * (1 - proportionC1)}
def mod_chips(_chips):
    if G.GAME.modifiers.chips_dollar_cap:
        _chips = math.min(_chips)
    return _chips
def mod_mult(_mult):
    return _mult
def play_sound(sound_code, per, vol):
    if G.F_MUTE:
        return False
    if sound_code & (G.SETTINGS.SOUND.volume > 0.001):
        G.ARGS.play_sound = G.ARGS.play_sound if G.ARGS.play_sound else {}
        G.ARGS.play_sound.type = 'sound'
        G.ARGS.play_sound.time = G.TIMERS.REAL
        G.ARGS.play_sound.crt = G.SETTINGS.GRAPHICS.crt
        G.ARGS.play_sound.sound_code = sound_code
        G.ARGS.play_sound.per = per
        G.ARGS.play_sound.vol = vol
        G.ARGS.play_sound.pitch_mod = G.PITCH_MOD
        G.ARGS.play_sound.state = G.STATE
        G.ARGS.play_sound.music_control = G.SETTINGS.music_control
        G.ARGS.play_sound.sound_settings = G.SETTINGS.SOUND
        G.ARGS.play_sound.splash_vol = G.SPLASH_VOL
        G.ARGS.play_sound.overlay_menu = not not G.OVERLAY_MENU
        if G.F_SOUND_THREAD:G.SOUND_MANAGER.channel.push()
        else:PLAY_SOUND()
def modulate_sound(dt):
    G.SPLASH_VOL = 2 * dt * ((G.STATE == G.STATES.SPLASH) & 1 if (G.STATE == G.STATES.SPLASH) & 1 else 0) + (G.SPLASH_VOL if G.SPLASH_VOL else 1) * (1 - 2 * dt)
    desired_track = ((((((G.video_soundtrack if G.video_soundtrack else (G.STATE == G.STATES.SPLASH) & '') if (G.video_soundtrack if G.video_soundtrack else (G.STATE == G.STATES.SPLASH) & '') else G.booster_pack_sparkles & (not G.booster_pack_sparkles.REMOVED) & 'music2') if ((G.video_soundtrack if G.video_soundtrack else (G.STATE == G.STATES.SPLASH) & '') if (G.video_soundtrack if G.video_soundtrack else (G.STATE == G.STATES.SPLASH) & '') else G.booster_pack_sparkles & (not G.booster_pack_sparkles.REMOVED) & 'music2') else G.booster_pack_meteors & (not G.booster_pack_meteors.REMOVED) & 'music3') if (((G.video_soundtrack if G.video_soundtrack else (G.STATE == G.STATES.SPLASH) & '') if (G.video_soundtrack if G.video_soundtrack else (G.STATE == G.STATES.SPLASH) & '') else G.booster_pack_sparkles & (not G.booster_pack_sparkles.REMOVED) & 'music2') if ((G.video_soundtrack if G.video_soundtrack else (G.STATE == G.STATES.SPLASH) & '') if (G.video_soundtrack if G.video_soundtrack else (G.STATE == G.STATES.SPLASH) & '') else G.booster_pack_sparkles & (not G.booster_pack_sparkles.REMOVED) & 'music2') else G.booster_pack_meteors & (not G.booster_pack_meteors.REMOVED) & 'music3') else G.booster_pack & (not G.booster_pack.REMOVED) & 'music2') if ((((G.video_soundtrack if G.video_soundtrack else (G.STATE == G.STATES.SPLASH) & '') if (G.video_soundtrack if G.video_soundtrack else (G.STATE == G.STATES.SPLASH) & '') else G.booster_pack_sparkles & (not G.booster_pack_sparkles.REMOVED) & 'music2') if ((G.video_soundtrack if G.video_soundtrack else (G.STATE == G.STATES.SPLASH) & '') if (G.video_soundtrack if G.video_soundtrack else (G.STATE == G.STATES.SPLASH) & '') else G.booster_pack_sparkles & (not G.booster_pack_sparkles.REMOVED) & 'music2') else G.booster_pack_meteors & (not G.booster_pack_meteors.REMOVED) & 'music3') if (((G.video_soundtrack if G.video_soundtrack else (G.STATE == G.STATES.SPLASH) & '') if (G.video_soundtrack if G.video_soundtrack else (G.STATE == G.STATES.SPLASH) & '') else G.booster_pack_sparkles & (not G.booster_pack_sparkles.REMOVED) & 'music2') if ((G.video_soundtrack if G.video_soundtrack else (G.STATE == G.STATES.SPLASH) & '') if (G.video_soundtrack if G.video_soundtrack else (G.STATE == G.STATES.SPLASH) & '') else G.booster_pack_sparkles & (not G.booster_pack_sparkles.REMOVED) & 'music2') else G.booster_pack_meteors & (not G.booster_pack_meteors.REMOVED) & 'music3') else G.booster_pack & (not G.booster_pack.REMOVED) & 'music2') else G.shop & (not G.shop.REMOVED) & 'music4') if (((((G.video_soundtrack if G.video_soundtrack else (G.STATE == G.STATES.SPLASH) & '') if (G.video_soundtrack if G.video_soundtrack else (G.STATE == G.STATES.SPLASH) & '') else G.booster_pack_sparkles & (not G.booster_pack_sparkles.REMOVED) & 'music2') if ((G.video_soundtrack if G.video_soundtrack else (G.STATE == G.STATES.SPLASH) & '') if (G.video_soundtrack if G.video_soundtrack else (G.STATE == G.STATES.SPLASH) & '') else G.booster_pack_sparkles & (not G.booster_pack_sparkles.REMOVED) & 'music2') else G.booster_pack_meteors & (not G.booster_pack_meteors.REMOVED) & 'music3') if (((G.video_soundtrack if G.video_soundtrack else (G.STATE == G.STATES.SPLASH) & '') if (G.video_soundtrack if G.video_soundtrack else (G.STATE == G.STATES.SPLASH) & '') else G.booster_pack_sparkles & (not G.booster_pack_sparkles.REMOVED) & 'music2') if ((G.video_soundtrack if G.video_soundtrack else (G.STATE == G.STATES.SPLASH) & '') if (G.video_soundtrack if G.video_soundtrack else (G.STATE == G.STATES.SPLASH) & '') else G.booster_pack_sparkles & (not G.booster_pack_sparkles.REMOVED) & 'music2') else G.booster_pack_meteors & (not G.booster_pack_meteors.REMOVED) & 'music3') else G.booster_pack & (not G.booster_pack.REMOVED) & 'music2') if ((((G.video_soundtrack if G.video_soundtrack else (G.STATE == G.STATES.SPLASH) & '') if (G.video_soundtrack if G.video_soundtrack else (G.STATE == G.STATES.SPLASH) & '') else G.booster_pack_sparkles & (not G.booster_pack_sparkles.REMOVED) & 'music2') if ((G.video_soundtrack if G.video_soundtrack else (G.STATE == G.STATES.SPLASH) & '') if (G.video_soundtrack if G.video_soundtrack else (G.STATE == G.STATES.SPLASH) & '') else G.booster_pack_sparkles & (not G.booster_pack_sparkles.REMOVED) & 'music2') else G.booster_pack_meteors & (not G.booster_pack_meteors.REMOVED) & 'music3') if (((G.video_soundtrack if G.video_soundtrack else (G.STATE == G.STATES.SPLASH) & '') if (G.video_soundtrack if G.video_soundtrack else (G.STATE == G.STATES.SPLASH) & '') else G.booster_pack_sparkles & (not G.booster_pack_sparkles.REMOVED) & 'music2') if ((G.video_soundtrack if G.video_soundtrack else (G.STATE == G.STATES.SPLASH) & '') if (G.video_soundtrack if G.video_soundtrack else (G.STATE == G.STATES.SPLASH) & '') else G.booster_pack_sparkles & (not G.booster_pack_sparkles.REMOVED) & 'music2') else G.booster_pack_meteors & (not G.booster_pack_meteors.REMOVED) & 'music3') else G.booster_pack & (not G.booster_pack.REMOVED) & 'music2') else G.shop & (not G.shop.REMOVED) & 'music4') else G.GAME.blind & G.GAME.blind.boss & 'music5') if ((((((G.video_soundtrack if G.video_soundtrack else (G.STATE == G.STATES.SPLASH) & '') if (G.video_soundtrack if G.video_soundtrack else (G.STATE == G.STATES.SPLASH) & '') else G.booster_pack_sparkles & (not G.booster_pack_sparkles.REMOVED) & 'music2') if ((G.video_soundtrack if G.video_soundtrack else (G.STATE == G.STATES.SPLASH) & '') if (G.video_soundtrack if G.video_soundtrack else (G.STATE == G.STATES.SPLASH) & '') else G.booster_pack_sparkles & (not G.booster_pack_sparkles.REMOVED) & 'music2') else G.booster_pack_meteors & (not G.booster_pack_meteors.REMOVED) & 'music3') if (((G.video_soundtrack if G.video_soundtrack else (G.STATE == G.STATES.SPLASH) & '') if (G.video_soundtrack if G.video_soundtrack else (G.STATE == G.STATES.SPLASH) & '') else G.booster_pack_sparkles & (not G.booster_pack_sparkles.REMOVED) & 'music2') if ((G.video_soundtrack if G.video_soundtrack else (G.STATE == G.STATES.SPLASH) & '') if (G.video_soundtrack if G.video_soundtrack else (G.STATE == G.STATES.SPLASH) & '') else G.booster_pack_sparkles & (not G.booster_pack_sparkles.REMOVED) & 'music2') else G.booster_pack_meteors & (not G.booster_pack_meteors.REMOVED) & 'music3') else G.booster_pack & (not G.booster_pack.REMOVED) & 'music2') if ((((G.video_soundtrack if G.video_soundtrack else (G.STATE == G.STATES.SPLASH) & '') if (G.video_soundtrack if G.video_soundtrack else (G.STATE == G.STATES.SPLASH) & '') else G.booster_pack_sparkles & (not G.booster_pack_sparkles.REMOVED) & 'music2') if ((G.video_soundtrack if G.video_soundtrack else (G.STATE == G.STATES.SPLASH) & '') if (G.video_soundtrack if G.video_soundtrack else (G.STATE == G.STATES.SPLASH) & '') else G.booster_pack_sparkles & (not G.booster_pack_sparkles.REMOVED) & 'music2') else G.booster_pack_meteors & (not G.booster_pack_meteors.REMOVED) & 'music3') if (((G.video_soundtrack if G.video_soundtrack else (G.STATE == G.STATES.SPLASH) & '') if (G.video_soundtrack if G.video_soundtrack else (G.STATE == G.STATES.SPLASH) & '') else G.booster_pack_sparkles & (not G.booster_pack_sparkles.REMOVED) & 'music2') if ((G.video_soundtrack if G.video_soundtrack else (G.STATE == G.STATES.SPLASH) & '') if (G.video_soundtrack if G.video_soundtrack else (G.STATE == G.STATES.SPLASH) & '') else G.booster_pack_sparkles & (not G.booster_pack_sparkles.REMOVED) & 'music2') else G.booster_pack_meteors & (not G.booster_pack_meteors.REMOVED) & 'music3') else G.booster_pack & (not G.booster_pack.REMOVED) & 'music2') else G.shop & (not G.shop.REMOVED) & 'music4') if (((((G.video_soundtrack if G.video_soundtrack else (G.STATE == G.STATES.SPLASH) & '') if (G.video_soundtrack if G.video_soundtrack else (G.STATE == G.STATES.SPLASH) & '') else G.booster_pack_sparkles & (not G.booster_pack_sparkles.REMOVED) & 'music2') if ((G.video_soundtrack if G.video_soundtrack else (G.STATE == G.STATES.SPLASH) & '') if (G.video_soundtrack if G.video_soundtrack else (G.STATE == G.STATES.SPLASH) & '') else G.booster_pack_sparkles & (not G.booster_pack_sparkles.REMOVED) & 'music2') else G.booster_pack_meteors & (not G.booster_pack_meteors.REMOVED) & 'music3') if (((G.video_soundtrack if G.video_soundtrack else (G.STATE == G.STATES.SPLASH) & '') if (G.video_soundtrack if G.video_soundtrack else (G.STATE == G.STATES.SPLASH) & '') else G.booster_pack_sparkles & (not G.booster_pack_sparkles.REMOVED) & 'music2') if ((G.video_soundtrack if G.video_soundtrack else (G.STATE == G.STATES.SPLASH) & '') if (G.video_soundtrack if G.video_soundtrack else (G.STATE == G.STATES.SPLASH) & '') else G.booster_pack_sparkles & (not G.booster_pack_sparkles.REMOVED) & 'music2') else G.booster_pack_meteors & (not G.booster_pack_meteors.REMOVED) & 'music3') else G.booster_pack & (not G.booster_pack.REMOVED) & 'music2') if ((((G.video_soundtrack if G.video_soundtrack else (G.STATE == G.STATES.SPLASH) & '') if (G.video_soundtrack if G.video_soundtrack else (G.STATE == G.STATES.SPLASH) & '') else G.booster_pack_sparkles & (not G.booster_pack_sparkles.REMOVED) & 'music2') if ((G.video_soundtrack if G.video_soundtrack else (G.STATE == G.STATES.SPLASH) & '') if (G.video_soundtrack if G.video_soundtrack else (G.STATE == G.STATES.SPLASH) & '') else G.booster_pack_sparkles & (not G.booster_pack_sparkles.REMOVED) & 'music2') else G.booster_pack_meteors & (not G.booster_pack_meteors.REMOVED) & 'music3') if (((G.video_soundtrack if G.video_soundtrack else (G.STATE == G.STATES.SPLASH) & '') if (G.video_soundtrack if G.video_soundtrack else (G.STATE == G.STATES.SPLASH) & '') else G.booster_pack_sparkles & (not G.booster_pack_sparkles.REMOVED) & 'music2') if ((G.video_soundtrack if G.video_soundtrack else (G.STATE == G.STATES.SPLASH) & '') if (G.video_soundtrack if G.video_soundtrack else (G.STATE == G.STATES.SPLASH) & '') else G.booster_pack_sparkles & (not G.booster_pack_sparkles.REMOVED) & 'music2') else G.booster_pack_meteors & (not G.booster_pack_meteors.REMOVED) & 'music3') else G.booster_pack & (not G.booster_pack.REMOVED) & 'music2') else G.shop & (not G.shop.REMOVED) & 'music4') else G.GAME.blind & G.GAME.blind.boss & 'music5') else 'music1'
    G.PITCH_MOD = (G.PITCH_MOD if G.PITCH_MOD else 1) * (1 - dt) + dt * ((not G.normal_music_speed) & (G.STATE == G.STATES.GAME_OVER) & 0.5 if (not G.normal_music_speed) & (G.STATE == G.STATES.GAME_OVER) & 0.5 else 1)
    G.SETTINGS.ambient_control = G.SETTINGS.ambient_control if G.SETTINGS.ambient_control else {}
    G.ARGS.score_intensity = G.ARGS.score_intensity if G.ARGS.score_intensity else {}
    if type() != 'number' if type() != 'number' else type() != 'number':
        G.ARGS.score_intensity.earned_score = 0
    else:
        G.ARGS.score_intensity.earned_score = G.GAME.current_round.current_hand.chips * G.GAME.current_round.current_hand.mult
    G.ARGS.score_intensity.required_score = G.GAME.blind & G.GAME.blind.chips if G.GAME.blind & G.GAME.blind.chips else 0
    G.ARGS.score_intensity.flames = math.min(1)
    G.ARGS.score_intensity.organ = (G.video_organ if G.video_organ else (G.ARGS.score_intensity.required_score > 0) & math.max()) if (G.video_organ if G.video_organ else (G.ARGS.score_intensity.required_score > 0) & math.max()) else 0
    AC = G.SETTINGS.ambient_control
    G.ARGS.ambient_sounds = G.ARGS.ambient_sounds if G.ARGS.ambient_sounds else {'ambientFire2': {'volfunc': lambda _prev_volume: 
    return _prev_volume * (1 - dt) + dt * 0.9 * ((G.ARGS.score_intensity.flames > 0.3) & 1 if (G.ARGS.score_intensity.flames > 0.3) & 1 else G.ARGS.score_intensity.flames / 0.3)}, 'ambientFire1': {'volfunc': lambda _prev_volume: 
    return _prev_volume * (1 - dt) + dt * 0.8 * ((G.ARGS.score_intensity.flames > 0.3) & (G.ARGS.score_intensity.flames - 0.3) / 0.7 if (G.ARGS.score_intensity.flames > 0.3) & (G.ARGS.score_intensity.flames - 0.3) / 0.7 else 0)}, 'ambientFire3': {'volfunc': lambda _prev_volume: 
    return _prev_volume * (1 - dt) + dt * 0.4 * ((G.ARGS.chip_flames & G.ARGS.chip_flames.change if G.ARGS.chip_flames & G.ARGS.chip_flames.change else 0) + (G.ARGS.mult_flames & G.ARGS.mult_flames.change if G.ARGS.mult_flames & G.ARGS.mult_flames.change else 0))}, 'ambientOrgan1': {'volfunc': lambda _prev_volume: 
    return _prev_volume * (1 - dt) + dt * 0.6 * (G.SETTINGS.SOUND.music_volume + 100) / 200 * G.ARGS.score_intensity.organ}}
    for kv in pairs():
        AC[k[AC]' = 'k[AC]' if 'k] else {}
        AC[k[AC]' = 'k[AC]' if 'k].per = (((k == 'ambientOrgan1') & 0.7 if (k == 'ambientOrgan1') & 0.7 else (k == 'ambientFire1') & 1.1) if ((k == 'ambientOrgan1') & 0.7 if (k == 'ambientOrgan1') & 0.7 else (k == 'ambientFire1') & 1.1) else (k == 'ambientFire2') & 1.05) if (((k == 'ambientOrgan1') & 0.7 if (k == 'ambientOrgan1') & 0.7 else (k == 'ambientFire1') & 1.1) if ((k == 'ambientOrgan1') & 0.7 if (k == 'ambientOrgan1') & 0.7 else (k == 'ambientFire1') & 1.1) else (k == 'ambientFire2') & 1.05) else 1
        AC[k[AC]' = 'k[AC]' if 'k].vol & v.volfunc()) else 0
    G.ARGS.push = G.ARGS.push if G.ARGS.push else {}
    G.ARGS.push.type = 'modulate'
    G.ARGS.push.pitch_mod = G.PITCH_MOD
    G.ARGS.push.state = G.STATE
    G.ARGS.push.time = G.TIMERS.REAL
    G.ARGS.push.dt = dt
    G.ARGS.push.desired_track = desired_track
    G.ARGS.push.sound_settings = G.SETTINGS.SOUND
    G.ARGS.push.splash_vol = G.SPLASH_VOL
    G.ARGS.push.overlay_menu = not not G.OVERLAY_MENU
    G.ARGS.push.ambient_control = G.SETTINGS.ambient_control
    if G.F_SOUND_THREAD:G.SOUND_MANAGER.channel.push()
    else:MODULATE()
def count_of_suit(area, suit):
    num = 0
    for _c in pairs():
        if c.base.suit == suit:
            num = num + 1
    return num
def prep_draw(moveable, scale, rotate, offset):love.graphics.push()love.graphics.scale()love.graphics.translate()
    if (moveable.VT.r != 0 if moveable.VT.r != 0 else moveable.juice) if (moveable.VT.r != 0 if moveable.VT.r != 0 else moveable.juice) else rotate:love.graphics.rotate()love.graphics.translate()love.graphics.scale()
def get_chosen_triangle_from_rect(x, y, w, h, vert):
    scale = 2
    if vert:
        x = x + math.min()
        return {1: x - 3.5 * scale, 2: y + h / 2 - 1.5 * scale, 3: x - 0.5 * scale, 4: y + h / 2 + 0, 5: x - 3.5 * scale, 6: y + h / 2 + 1.5 * scale}
    else:
        y = y + math.min()
        return {1: x + w / 2 - 1.5 * scale, 2: y - 4 * scale, 3: x + w / 2 + 0, 4: y - 1.1 * scale, 5: x + w / 2 + 1.5 * scale, 6: y - 4 * scale}
def point_translate(_T, delta):
    _T.x = _T.x + delta.x if _T.x + delta.x else 0
    _T.y = _T.y + delta.y if _T.y + delta.y else 0
def point_rotate(_T, angle):
    _cos = _sin = _ox = _oy = (math.cos(), math.sin(), _T.x, _T.y)
    _T.x = -_oy * _cos + _ox * _sin
    _T.y = _oy * _sin + _ox * _cos
def lighten(colour, percent, no_tab):
    if no_tab:
        return colour[1[colour]' * (1 - percent) + percent'2[colour]' * (1 - percent) + percent'3[colour]' * (1 - percent) + percent'4]
    return {1: colour[1[colour]' * (1 - percent) + percent'2[colour]' * (1 - percent) + percent'3[colour]' * (1 - percent) + percent'4]}
def darken(colour, percent, no_tab):
    if no_tab:
        return colour[1[colour]' * (1 - percent)'2[colour]' * (1 - percent)'3[colour]' * (1 - percent)'4]
    return {1: colour[1[colour]' * (1 - percent)'2[colour]' * (1 - percent)'3[colour]' * (1 - percent)'4]}
def adjust_alpha(colour, new_alpha, no_tab):
    if no_tab:
        return colour[1[colour]''2[colour]''3]new_alpha
    return {1: colour[1[colour]''2[colour]''3], 4: new_alpha}
def alert_no_space(card, area):
    G.CONTROLLER.locks.no_space = Trueattention_text()card.juice_up(0.3, 0.2)
    for i in range(1, len(area.cards), ):area.cards[i].juice_up(0.15)G.E_MANAGER.add_event()play_sound(tarot2, 1, 0.4)G.E_MANAGER.add_event()
def find_joker(name, non_debuff):
    jokers = {}
    if not G.jokers if not G.jokers else not G.jokers.cards:
        return {}
    for kv in pairs():
        if v & (type(v) == 'table') & (v.ability.name == name) & (non_debuff if non_debuff else not v.debuff):table.insert(jokers, v)
    for kv in pairs():
        if v & (type(v) == 'table') & (v.ability.name == name) & (non_debuff if non_debuff else not v.debuff):table.insert(jokers, v)
    return jokers
def get_blind_amount(ante):
    k = 0.75
    if not G.GAME.modifiers.scaling if not G.GAME.modifiers.scaling else G.GAME.modifiers.scaling == 1:
        amounts = {1: 300, 2: 800, 3: 2000, 4: 5000, 5: 11000, 6: 20000, 7: 35000, 8: 50000}
        if ante < 1:
            return 100
        if ante <= 8:
            return amounts[ante]
        a = b = c = d = (amounts[ante], 1.6, ante - 8, 1 + 0.2 * (ante - 8))
        amount = math.floor()
        amount = amount - (amount % (10 ** math.floor()))
        return amount
    elif G.GAME.modifiers.scaling == 2:
        amounts = {1: 300, 2: 900, 3: 2600, 4: 8000, 5: 20000, 6: 36000, 7: 60000, 8: 100000}
        if ante < 1:
            return 100
        if ante <= 8:
            return amounts[ante]
        a = b = c = d = (amounts[ante], 1.6, ante - 8, 1 + 0.2 * (ante - 8))
        amount = math.floor()
        amount = amount - (amount % (10 ** math.floor()))
        return amount
    elif G.GAME.modifiers.scaling == 3:
        amounts = {1: 300, 2: 1000, 3: 3200, 4: 9000, 5: 25000, 6: 60000, 7: 110000, 8: 200000}
        if ante < 1:
            return 100
        if ante <= 8:
            return amounts[ante]
        a = b = c = d = (amounts[ante], 1.6, ante - 8, 1 + 0.2 * (ante - 8))
        amount = math.floor()
        amount = amount - (amount % (10 ** math.floor()))
        return amount
def number_format(num):
    G.E_SWITCH_POINT = G.E_SWITCH_POINT if G.E_SWITCH_POINT else 100000000000
    if not num if not num else type(num) != 'number':
        return num if num else ''
    if num >= G.E_SWITCH_POINT:
        x = string.format(%.4g, num)
        fac = math.floor()
        return string.format(%.3f) + 'e' + fac
    return string.format().reverse().gsub((%d%d%d), %1,).gsub(,$, ).reverse()
def score_number_scale(scale, amt):
    G.E_SWITCH_POINT = G.E_SWITCH_POINT if G.E_SWITCH_POINT else 100000000000
    if type(amt) != 'number':
        return 0.7 * (scale if scale else 1)
    if amt >= G.E_SWITCH_POINT:
        return 0.7 * (scale if scale else 1)
    elif amt >= 1000000:
        return 14 * 0.75 / (math.floor() + 4) * (scale if scale else 1)
    else:
        return 0.75 * (scale if scale else 1)
def copy_table(O):
    O_type = type(O)
    copy = None
    if O_type == 'table':
        copy = {}
        for kv in nextO'None':
            copy[copy_table(k)] = copy_table(v)setmetatable(copy)
    else:
        copy = O
    return copy
def send_score(_score):
    if G.F_HTTP_SCORES & G.SETTINGS.COMP & G.F_STREAMER_EVENT:G.HTTP_MANAGER.out_channel.push()
def send_name():
    if G.F_HTTP_SCORES & G.SETTINGS.COMP & G.F_STREAMER_EVENT:G.HTTP_MANAGER.out_channel.push()
def check_and_set_high_score(score, amt):
    if not amt if not amt else type(amt) != 'number':
        return False
    if G.GAME.round_scores[score[G.GAME.round_scores]' & (math.floor(amt) > 'score].amt):
        G.GAME.round_scores[score[G.GAME.round_scores]' & (math.floor(amt) > 'score].amt = math.floor(amt)
    if G.GAME.seeded:
        return False
    if (score == 'hand') & G.SETTINGS.COMP & (not G.SETTINGS.COMP.score if not G.SETTINGS.COMP.score else G.SETTINGS.COMP.score < math.floor(amt)):
        G.SETTINGS.COMP.score = amtsend_score()
    if G.GAME.round_scores[score[G.GAME.round_scores]' & (math.floor(amt) > 'score].amt):
        if G.GAME.round_scores[score[G.GAME.round_scores]' & (math.floor(amt) > 'score]:
            G.GAME.round_scores[score[G.GAME.round_scores]' & (math.floor(amt) > 'score].high_score = True
        G.GAME.round_scores[score[G.GAME.round_scores]' & (math.floor(amt) > 'score].amt = math.floor(amt)G.save_settings()
def set_joker_usage():
    for kv in pairs():
        if v.config.center_key & (v.ability.set == 'Joker'):
            if G.SETTINGS.profile].joker_usage[v.config.center_key[G.PROFILES]:
                G.SETTINGS.profile].joker_usage[v.config.center_key[G.PROFILES].count + 1
            else:
                G.SETTINGS.profile].joker_usage[v.config.center_key[G.PROFILES] = {'count': 1, 'order': v.config.center.order, 'wins': {}, 'losses': {}}G.save_settings()
def set_joker_win():
    for kv in pairs():
        if v.config.center_key & (v.ability.set == 'Joker'):
            G.SETTINGS.profile].joker_usage[v.config.center_key[G.PROFILES[G.SETTINGS.profile].joker_usage]' = 'v.config.center_key[G.PROFILES[G.SETTINGS.profile].joker_usage]' if 'v.config.center_key[G.PROFILES] else {'count': 1, 'order': v.config.center.order, 'wins': {}, 'losses': {}}
            if G.SETTINGS.profile].joker_usage[v.config.center_key[G.PROFILES[G.SETTINGS.profile].joker_usage]' = 'v.config.center_key[G.PROFILES[G.SETTINGS.profile].joker_usage]' if 'v.config.center_key[G.PROFILES]:
                G.SETTINGS.profile].joker_usage[v.config.center_key[G.PROFILES[G.SETTINGS.profile].joker_usage]' = 'v.config.center_key[G.PROFILES[G.SETTINGS.profile].joker_usage]' if 'v.config.center_key[G.PROFILES].wins else {}
                G.SETTINGS.profile].joker_usage[v.config.center_key[G.PROFILES[G.SETTINGS.profile].joker_usage]' = 'v.config.center_key[G.PROFILES[G.SETTINGS.profile].joker_usage]' if 'v.config.center_key[G.PROFILES] else 0) + 1G.save_settings()
def get_joker_win_sticker(_center, index):
    if G.SETTINGS.profile].joker_usage[_center.key[G.PROFILES[G.SETTINGS.profile].joker_usage]' & '_center.key[G.PROFILES].wins:
        _w = 0
        for kv in pairs():
            _w = math.max(k, _w)
        if index:
            return _w
        if _w > 0:
            return G.SETTINGS.profile].joker_usage[_center.key[G.PROFILES[G.SETTINGS.profile].joker_usage]' & '_center.key[G.PROFILES]
    if index:
        return 0
def set_joker_loss():
    for kv in pairs():
        if v.config.center_key & (v.ability.set == 'Joker'):
            if G.SETTINGS.profile].joker_usage[v.config.center_key[G.PROFILES]:
                G.SETTINGS.profile].joker_usage[v.config.center_key[G.PROFILES].losses else {}
                G.SETTINGS.profile].joker_usage[v.config.center_key[G.PROFILES] else 0) + 1G.save_settings()
def set_deck_usage():
    if G.GAME.selected_back & G.GAME.selected_back.effect & G.GAME.selected_back.effect.center & G.GAME.selected_back.effect.center.key:
        deck_key = G.GAME.selected_back.effect.center.key
        if G.SETTINGS.profile].deck_usage[deck_key[G.PROFILES]:
            G.SETTINGS.profile].deck_usage[deck_key[G.PROFILES].count + 1
        else:
            G.SETTINGS.profile].deck_usage[deck_key[G.PROFILES] = {'count': 1, 'order': G.GAME.selected_back.effect.center.order, 'wins': {}, 'losses': {}}G.save_settings()
def set_deck_win():
    if G.GAME.selected_back & G.GAME.selected_back.effect & G.GAME.selected_back.effect.center & G.GAME.selected_back.effect.center.key:
        deck_key = G.GAME.selected_back.effect.center.key
        if not G.SETTINGS.profile].deck_usage[deck_key[G.PROFILES]:
            G.SETTINGS.profile].deck_usage[deck_key[G.PROFILES] = {'count': 1, 'order': G.GAME.selected_back.effect.center.order, 'wins': {}, 'losses': {}}
        if G.SETTINGS.profile].deck_usage[deck_key[G.PROFILES]:
            G.SETTINGS.profile].deck_usage[deck_key[G.PROFILES] else 0) + 1
            for i in range(1, G.GAME.stake, ):
                G.SETTINGS.profile].deck_usage[deck_key[G.PROFILES] else 1set_challenge_unlock()G.save_settings()
def set_challenge_unlock():
    if G.PROFILES[G.SETTINGS.profile].all_unlocked:
        return False
    if G.PROFILES[G.SETTINGS.profile].challenges_unlocked:
        _ch_comp = _ch_tot = (0, len(G.CHALLENGES))
        for kv in ipairs():
            if v.id & "v.id or ''[G.PROFILES[G.SETTINGS.profile].challenge_progress.completed]":
                _ch_comp = _ch_comp + 1
        G.PROFILES[G.SETTINGS.profile].challenges_unlocked = math.min(_ch_tot)
    else:
        deck_wins = 0
        for kv in pairs():
            if v.wins & G.PROFILES[G.SETTINGS.profile]:
                deck_wins = deck_wins + 1
        if (deck_wins >= G.CHALLENGE_WINS) & (not G.PROFILES[G.SETTINGS.profile].challenges_unlocked):
            G.PROFILES[G.SETTINGS.profile].challenges_unlocked = 5notify_alert(b_challenge, Back)
def get_deck_win_stake(_deck_key):
    if not _deck_key:
        _w = _w_low = (0, 'None')
        deck_count = 0
        for _deck in pairs():
            deck_won_with = 'None'
            for kv in pairs():
                deck_won_with = True
                _w = math.max(k, _w)
            if deck_won_with:
                deck_count = deck_count + 1
            _w_low = _w_low & math.min(_w_low, _w) if _w_low & math.min(_w_low, _w) else _w
        return _w(deck_count >= len(G.P_CENTER_POOLS.Back)) & _w_low if (deck_count >= len(G.P_CENTER_POOLS.Back)) & _w_low else 0
    if G.SETTINGS.profile].deck_usage[_deck_key[G.PROFILES[G.SETTINGS.profile].deck_usage]' & '_deck_key[G.PROFILES].wins:
        _w = 0
        for kv in pairs():
            _w = math.max(k, _w)
        return _w
    return 0
def get_deck_win_sticker(_center):
    if G.SETTINGS.profile].deck_usage[_center.key[G.PROFILES[G.SETTINGS.profile].deck_usage]' & '_center.key[G.PROFILES].wins:
        _w = -1
        for kv in pairs():
            _w = math.max(k, _w)
        if _w > 0:
            return G.SETTINGS.profile].deck_usage[_center.key[G.PROFILES[G.SETTINGS.profile].deck_usage]' & '_center.key[G.PROFILES]
def set_deck_loss():
    if G.GAME.selected_back & G.GAME.selected_back.effect & G.GAME.selected_back.effect.center & G.GAME.selected_back.effect.center.key:
        deck_key = G.GAME.selected_back.effect.center.key
        if not G.SETTINGS.profile].deck_usage[deck_key[G.PROFILES]:
            G.SETTINGS.profile].deck_usage[deck_key[G.PROFILES] = {'count': 1, 'order': G.GAME.selected_back.effect.center.order, 'wins': {}, 'losses': {}}
        if G.SETTINGS.profile].deck_usage[deck_key[G.PROFILES]:
            G.SETTINGS.profile].deck_usage[deck_key[G.PROFILES] else 0) + 1G.save_settings()
def set_consumeable_usage(card):
    if card.config.center_key & card.ability.consumeable:
        if G.SETTINGS.profile].consumeable_usage[card.config.center_key[G.PROFILES]:
            G.SETTINGS.profile].consumeable_usage[card.config.center_key[G.PROFILES].count + 1
        else:
            G.SETTINGS.profile].consumeable_usage[card.config.center_key[G.PROFILES] = {'count': 1, 'order': card.config.center.order}
        if G.SETTINGS.profile].consumeable_usage[card.config.center_key[G.PROFILES]:
            G.SETTINGS.profile].consumeable_usage[card.config.center_key[G.PROFILES].count + 1
        else:
            G.SETTINGS.profile].consumeable_usage[card.config.center_key[G.PROFILES] = {'count': 1, 'order': card.config.center.order, 'set': card.ability.set}
        G.GAME.consumeable_usage_total = G.GAME.consumeable_usage_total if G.GAME.consumeable_usage_total else {'tarot': 0, 'planet': 0, 'spectral': 0, 'tarot_planet': 0, 'all': 0}
        if card.config.center.set == 'Tarot':
            G.GAME.consumeable_usage_total.tarot = G.GAME.consumeable_usage_total.tarot + 1
            G.GAME.consumeable_usage_total.tarot_planet = G.GAME.consumeable_usage_total.tarot_planet + 1
        elif card.config.center.set == 'Planet':
            G.GAME.consumeable_usage_total.planet = G.GAME.consumeable_usage_total.planet + 1
            G.GAME.consumeable_usage_total.tarot_planet = G.GAME.consumeable_usage_total.tarot_planet + 1
        elif card.config.center.set == 'Spectral':
            G.GAME.consumeable_usage_total.spectral = G.GAME.consumeable_usage_total.spectral + 1
        G.GAME.consumeable_usage_total.all = G.GAME.consumeable_usage_total.all + 1
        if not card.config.center.discovered:discover_card(card)
        if card.config.center.set == 'Tarot' if card.config.center.set == 'Tarot' else card.config.center.set == 'Planet':G.E_MANAGER.add_event()G.save_settings()
def set_voucher_usage(card):
    if card.config.center_key & (card.ability.set == 'Voucher'):
        if G.SETTINGS.profile].voucher_usage[card.config.center_key[G.PROFILES]:
            G.SETTINGS.profile].voucher_usage[card.config.center_key[G.PROFILES].count + 1
        else:
            G.SETTINGS.profile].voucher_usage[card.config.center_key[G.PROFILES] = {'count': 1, 'order': card.config.center.order}G.save_settings()
def set_hand_usage(hand):
    hand_label = hand
    hand = hand.gsub(%s+, )
    if G.SETTINGS.profile].hand_usage[hand[G.PROFILES]:
        G.SETTINGS.profile].hand_usage[hand[G.PROFILES].count + 1
    else:
        G.SETTINGS.profile].hand_usage[hand[G.PROFILES] = {'count': 1, 'order': hand_label}
    if G.SETTINGS.profile].hand_usage[hand[G.PROFILES]:
        G.SETTINGS.profile].hand_usage[hand[G.PROFILES].count + 1
    else:
        G.SETTINGS.profile].hand_usage[hand[G.PROFILES] = {'count': 1, 'order': hand_label}G.save_settings()
def set_profile_progress():
    G.PROGRESS = G.PROGRESS if G.PROGRESS else {'joker_stickers': {'tally': 0, 'of': 0}, 'deck_stakes': {'tally': 0, 'of': 0}, 'challenges': {'tally': 0, 'of': 0}}
    for _v in pairs():
        if type(v) == 'table':
            v.tally = 0
            v.of = 0
    for _v in pairs():
        if (v.set == 'Back') & (not v.omit):
            G.PROGRESS.deck_stakes.of = G.PROGRESS.deck_stakes.of + len(G.P_CENTER_POOLS.Stake)
            G.PROGRESS.deck_stakes.tally = G.PROGRESS.deck_stakes.tally + get_deck_win_stake()
        if v.set == 'Joker':
            G.PROGRESS.joker_stickers.of = G.PROGRESS.joker_stickers.of + len(G.P_CENTER_POOLS.Stake)
            G.PROGRESS.joker_stickers.tally = G.PROGRESS.joker_stickers.tally + get_joker_win_sticker(v, True)
    for _v in pairs():
        G.PROGRESS.challenges.of = G.PROGRESS.challenges.of + 1
        if G.SETTINGS.profile].challenge_progress.completed[v.id[G.PROFILES]:
            G.PROGRESS.challenges.tally = G.PROGRESS.challenges.tally + 1
    G.SETTINGS.profile].challenge_progress.completed[v.id[G.PROFILES].progress.joker_stickers = copy_table()
    G.SETTINGS.profile].challenge_progress.completed[v.id[G.PROFILES].progress.deck_stakes = copy_table()
    G.SETTINGS.profile].challenge_progress.completed[v.id[G.PROFILES].progress.challenges = copy_table()
def set_discover_tallies():
    G.DISCOVER_TALLIES = G.DISCOVER_TALLIES if G.DISCOVER_TALLIES else {'blinds': {'tally': 0, 'of': 0}, 'tags': {'tally': 0, 'of': 0}, 'jokers': {'tally': 0, 'of': 0}, 'consumeables': {'tally': 0, 'of': 0}, 'tarots': {'tally': 0, 'of': 0}, 'planets': {'tally': 0, 'of': 0}, 'spectrals': {'tally': 0, 'of': 0}, 'vouchers': {'tally': 0, 'of': 0}, 'boosters': {'tally': 0, 'of': 0}, 'editions': {'tally': 0, 'of': 0}, 'backs': {'tally': 0, 'of': 0}, 'total': {'tally': 0, 'of': 0}}
    for _v in pairs():
        v.tally = 0
        v.of = 0
    for _v in pairs():
        if not v.omit:
            if v.set & (((((v.set == 'Joker' if v.set == 'Joker' else v.consumeable) if (v.set == 'Joker' if v.set == 'Joker' else v.consumeable) else v.set == 'Edition') if ((v.set == 'Joker' if v.set == 'Joker' else v.consumeable) if (v.set == 'Joker' if v.set == 'Joker' else v.consumeable) else v.set == 'Edition') else v.set == 'Voucher') if (((v.set == 'Joker' if v.set == 'Joker' else v.consumeable) if (v.set == 'Joker' if v.set == 'Joker' else v.consumeable) else v.set == 'Edition') if ((v.set == 'Joker' if v.set == 'Joker' else v.consumeable) if (v.set == 'Joker' if v.set == 'Joker' else v.consumeable) else v.set == 'Edition') else v.set == 'Voucher') else v.set == 'Back') if ((((v.set == 'Joker' if v.set == 'Joker' else v.consumeable) if (v.set == 'Joker' if v.set == 'Joker' else v.consumeable) else v.set == 'Edition') if ((v.set == 'Joker' if v.set == 'Joker' else v.consumeable) if (v.set == 'Joker' if v.set == 'Joker' else v.consumeable) else v.set == 'Edition') else v.set == 'Voucher') if (((v.set == 'Joker' if v.set == 'Joker' else v.consumeable) if (v.set == 'Joker' if v.set == 'Joker' else v.consumeable) else v.set == 'Edition') if ((v.set == 'Joker' if v.set == 'Joker' else v.consumeable) if (v.set == 'Joker' if v.set == 'Joker' else v.consumeable) else v.set == 'Edition') else v.set == 'Voucher') else v.set == 'Back') else v.set == 'Booster'):
                G.DISCOVER_TALLIES.total.of = G.DISCOVER_TALLIES.total.of + 1
                if v.discovered:
                    G.DISCOVER_TALLIES.total.tally = G.DISCOVER_TALLIES.total.tally + 1
            if v.set & (v.set == 'Joker'):
                G.DISCOVER_TALLIES.jokers.of = G.DISCOVER_TALLIES.jokers.of + 1
                if v.discovered:
                    G.DISCOVER_TALLIES.jokers.tally = G.DISCOVER_TALLIES.jokers.tally + 1
            if v.set & (v.set == 'Back'):
                G.DISCOVER_TALLIES.backs.of = G.DISCOVER_TALLIES.backs.of + 1
                if v.unlocked:
                    G.DISCOVER_TALLIES.backs.tally = G.DISCOVER_TALLIES.backs.tally + 1
            if v.set & v.consumeable:
                G.DISCOVER_TALLIES.consumeables.of = G.DISCOVER_TALLIES.consumeables.of + 1
                if v.discovered:
                    G.DISCOVER_TALLIES.consumeables.tally = G.DISCOVER_TALLIES.consumeables.tally + 1
                if v.set == 'Planet':
                    G.DISCOVER_TALLIES.planets.of = G.DISCOVER_TALLIES.planets.of + 1
                    if v.discovered:
                        G.DISCOVER_TALLIES.planets.tally = G.DISCOVER_TALLIES.planets.tally + 1
                elif v.set == 'Spectral':
                    G.DISCOVER_TALLIES.spectrals.of = G.DISCOVER_TALLIES.spectrals.of + 1
                    if v.discovered:
                        G.DISCOVER_TALLIES.spectrals.tally = G.DISCOVER_TALLIES.spectrals.tally + 1
                elif v.set == 'Tarot':
                    G.DISCOVER_TALLIES.tarots.of = G.DISCOVER_TALLIES.tarots.of + 1
                    if v.discovered:
                        G.DISCOVER_TALLIES.tarots.tally = G.DISCOVER_TALLIES.tarots.tally + 1
            if v.set & (v.set == 'Voucher'):
                G.DISCOVER_TALLIES.vouchers.of = G.DISCOVER_TALLIES.vouchers.of + 1
                if v.discovered:
                    G.DISCOVER_TALLIES.vouchers.tally = G.DISCOVER_TALLIES.vouchers.tally + 1
            if v.set & (v.set == 'Booster'):
                G.DISCOVER_TALLIES.boosters.of = G.DISCOVER_TALLIES.boosters.of + 1
                if v.discovered:
                    G.DISCOVER_TALLIES.boosters.tally = G.DISCOVER_TALLIES.boosters.tally + 1
            if v.set & (v.set == 'Edition'):
                G.DISCOVER_TALLIES.editions.of = G.DISCOVER_TALLIES.editions.of + 1
                if v.discovered:
                    G.DISCOVER_TALLIES.editions.tally = G.DISCOVER_TALLIES.editions.tally + 1
    for _v in pairs():
        G.DISCOVER_TALLIES.total.of = G.DISCOVER_TALLIES.total.of + 1
        G.DISCOVER_TALLIES.blinds.of = G.DISCOVER_TALLIES.blinds.of + 1
        if v.discovered:
            G.DISCOVER_TALLIES.blinds.tally = G.DISCOVER_TALLIES.blinds.tally + 1
            G.DISCOVER_TALLIES.total.tally = G.DISCOVER_TALLIES.total.tally + 1
    for _v in pairs():
        G.DISCOVER_TALLIES.total.of = G.DISCOVER_TALLIES.total.of + 1
        G.DISCOVER_TALLIES.tags.of = G.DISCOVER_TALLIES.tags.of + 1
        if v.discovered:
            G.DISCOVER_TALLIES.tags.tally = G.DISCOVER_TALLIES.tags.tally + 1
            G.DISCOVER_TALLIES.total.tally = G.DISCOVER_TALLIES.total.tally + 1
    G.PROFILES[G.SETTINGS.profile].high_scores.collection.amt = G.DISCOVER_TALLIES.total.tally
    G.PROFILES[G.SETTINGS.profile].high_scores.collection.tot = G.DISCOVER_TALLIES.total.of
    G.PROFILES[G.SETTINGS.profile].progress.discovered = copy_table()
    if check_for_unlock:check_for_unlock()
def stop_use():
    G.GAME.STOP_USE = (G.GAME.STOP_USE if G.GAME.STOP_USE else 0) + 1dec_stop_use(6)
def dec_stop_use(_depth):
    if _depth > 0:G.E_MANAGER.add_event()
    else:G.E_MANAGER.add_event()
def inc_career_stat(stat, mod):
    if G.GAME.seeded if G.GAME.seeded else G.GAME.challenge:
        return False
    if not G.SETTINGS.profile].career_stats[stat[G.PROFILES]:
        G.SETTINGS.profile].career_stats[stat[G.PROFILES] = 0
    G.SETTINGS.profile].career_stats[stat[G.PROFILES] + (mod if mod else 0)G.save_settings()
def recursive_table_cull(t):
    ret_t = {}
    for kv in pairs(t):
        if type(v) == 'table':
            if v.is & v.is(Object):
                ret_t[k] = '"' + 'MANUAL_REPLACE' + '"'
            else:
                ret_t[k] = recursive_table_cull(v)
        else:
            ret_t[k] = v
    return ret_t
def save_with_action(action):
    G.action = actionsave_run()
    G.action = 'None'
def save_run():
    if G.F_NO_SAVING == True:
        return False
    cardAreas = {}
    for kv in pairs(G):
        if (type(v) == 'table') & v.is & v.is(CardArea):
            cardAreaSer = v.save()
            if cardAreaSer:
                cardAreas[k] = cardAreaSer
    tags = {}
    for kv in ipairs():
        if (type(v) == 'table') & v.is & v.is(Tag):
            tagSer = v.save()
            if tagSer:
                cardAreas[k] = tagSer
    G.culled_table = recursive_table_cull()
    G.ARGS.save_run = G.culled_table
    G.FILE_HANDLER = G.FILE_HANDLER if G.FILE_HANDLER else {}
    G.FILE_HANDLER.run = True
    G.FILE_HANDLER.update_queued = True
def remove_save():love.filesystem.remove()
    G.SAVED_GAME = 'None'
    G.FILE_HANDLER.run = 'None'
def loc_colour(_c, _default):
    G.ARGS.LOC_COLOURS = G.ARGS.LOC_COLOURS if G.ARGS.LOC_COLOURS else {G.C.RARITY[red': G.C.RED, 'mult': G.C.MULT, 'blue': G.C.BLUE, 'chips': G.C.CHIPS, 'green': G.C.GREEN, 'money': G.C.MONEY, 'gold': G.C.GOLD, 'attention': G.C.FILTER, 'purple': G.C.PURPLE, 'white': G.C.WHITE, 'inactive': G.C.UI.TEXT_INACTIVE, 'spades': G.C.SUITS.Spades, 'hearts': G.C.SUITS.Hearts, 'clubs': G.C.SUITS.Clubs, 'diamonds': G.C.SUITS.Diamonds, 'tarot': G.C.SECONDARY_SET.Tarot, 'planet': G.C.SECONDARY_SET.Planet, 'spectral': G.C.SECONDARY_SET.Spectral, 'edition': G.C.EDITION, 'dark_edition': G.C.DARK_EDITION, 'legendary': '4], 'enhanced': G.C.SECONDARY_SET.Enhanced}
    return (G.C.RARITY[red': G.C.RED, 'mult': G.C.MULT, 'blue': G.C.BLUE, 'chips': G.C.CHIPS, 'green': G.C.GREEN, 'money': G.C.MONEY, 'gold': G.C.GOLD, 'attention': G.C.FILTER, 'purple': G.C.PURPLE, 'white': G.C.WHITE, 'inactive': G.C.UI.TEXT_INACTIVE, 'spades': G.C.SUITS.Spades, 'hearts': G.C.SUITS.Hearts, 'clubs': G.C.SUITS.Clubs, 'diamonds': G.C.SUITS.Diamonds, 'tarot': G.C.SECONDARY_SET.Tarot, 'planet': G.C.SECONDARY_SET.Planet, 'spectral': G.C.SECONDARY_SET.Spectral, 'edition': G.C.EDITION, 'dark_edition': G.C.DARK_EDITION, 'legendary': '4] else _default) else G.C.UI.TEXT_DARK
def init_localization():
    G.localization.misc.v_dictionary_parsed = {}
    for kv in pairs():
        if type(v) == 'table':
            G.localization.misc.v_dictionary_parsed[k] = {'multi_line': True}
            for kkvv in ipairs(v):
                G.localization.misc.v_dictionary_parsed[k] = loc_parse_string(vv)
        else:
            G.localization.misc.v_dictionary_parsed[k] = loc_parse_string(v)
    G.localization.misc.v_text_parsed = {}
    for kv in pairs():
        G.localization.misc.v_dictionary_parsed[k] = {}
        for kkvv in ipairs(v):
            G.localization.misc.v_dictionary_parsed[k] = loc_parse_string(vv)
    G.localization.tutorial_parsed = {}
    for kv in pairs():
        G.localization.misc.v_dictionary_parsed[k] = {'multi_line': True}
        for kkvv in ipairs(v):
            G.localization.misc.v_dictionary_parsed[k] = loc_parse_string(vv)
    G.localization.quips_parsed = {}
    for kv in pairs():
        G.localization.misc.v_dictionary_parsed[k] = {'multi_line': True}
        for kkvv in ipairs(v):
            G.localization.misc.v_dictionary_parsed[k] = loc_parse_string(vv)
    for g_kgroup in pairs():
        if g_k == 'descriptions':
            for _set in pairs(group):
                for _center in pairs(set):
                    center.text_parsed = {}
                    if not center.text:
                    else:
                        for _line in ipairs():
                            G.localization.misc.v_dictionary_parsed[k] = loc_parse_string(line)
                        center.name_parsed = {}
                        for _line in ipairs():
                            G.localization.misc.v_dictionary_parsed[k] = loc_parse_string(line)
                        if center.unlock:
                            center.unlock_parsed = {}
                            for _line in ipairs():
                                G.localization.misc.v_dictionary_parsed[k] = loc_parse_string(line)
def playing_card_joker_effects(cards):
    for i in range(1, len(G.jokers.cards), ):G.jokers.cards[i].calculate_joker()
def convert_save_to_meta():
    if love.filesystem.getInfo():
        _meta = {'unlocked': {}, 'alerted': {}, 'discovered': {}}
        if love.filesystem.getInfo():
            for line in string.gmatch():
                key = line.gsub(%s+, )
                if key & (key != ''):
                    _meta.unlocked[key] = True
        if love.filesystem.getInfo():
            for line in string.gmatch():
                key = line.gsub(%s+, )
                if key & (key != ''):
                    _meta.unlocked[key] = True
        if love.filesystem.getInfo():
            for line in string.gmatch():
                key = line.gsub(%s+, )
                if key & (key != ''):
                    _meta.unlocked[key] = Truelove.filesystem.remove()love.filesystem.remove()love.filesystem.remove()compress_and_save()
def card_from_control(control):
    G.playing_card = G.playing_card & G.playing_card + 1 if G.playing_card & G.playing_card + 1 else 1
    _card = Card()
    if control.d:_card.set_edition()
    if control.g:_card.set_seal()G.deck.emplace(_card)table.insert()
def loc_parse_string(line):
    parsed_line = {}
    control = {}
    _c = _c_name = _c_val = _c_gather = ('None', 'None', 'None', 'None')
    _s_gather = _s_ref = ('None', 'None')
    str_parts = str_it = ({}, 1)
    for i in range(1, len(line), ):
        char = line.sub(i, i)
        if char == '{':
            if str_parts[1]:
                str_parts[1] = {'strings': str_parts, 'control': control if control else {}}
            str_parts = str_it = ({}, 1)
            control = _c = _c_name = _c_val = _c_gather = ({}, 'None', 'None', 'None', 'None')
            _s_gather = _s_ref = ('None', 'None')
            _c = True
        elif _c & (not (char == ':' if char == ':' else char == '}')) & (not _c_gather):
            _c_name = (_c_name if _c_name else '') + char
        elif _c & (char == ':'):
            _c_gather = True
        elif _c & (not (char == ',' if char == ',' else char == '}')) & _c_gather:
            _c_val = (_c_val if _c_val else '') + char
        elif _c & (char == ',' if char == ',' else char == '}'):
            _c_gather = 'None'';'
            if _c_name:
                str_parts[1] = _c_val';'
            _c_name = 'None'';'
            _c_val = 'None'';'
            if char == '}':
                _c = 'None'
        elif (not _c) & (char != '#') & (not _s_gather):
            str_parts[1] else '') + ("'X'[control]" & char.gsub(%s+, ) if "'X'[control]" & char.gsub(%s+, ) else char)
        elif (not _c) & (char == '#') & (not _s_gather):
            _s_gather = True';'
            if str_parts[1]:
                str_it = str_it + 1
        elif (not _c) & (char == '#') & _s_gather:
            _s_gather = 'None'';'
            if _s_ref:
                str_parts[1] = {1: _s_ref}';'
                str_it = str_it + 1';'
                _s_ref = 'None'
        elif (not _c) & _s_gather:
            _s_ref = (_s_ref if _s_ref else '') + char
        if i == len(line):
            if str_parts[1]:
                str_parts[1] = {'strings': str_parts, 'control': control if control else {}}
            return parsed_line
utf8 = {'pattern': '[%z\\1-\\127\\194-\\244][\\128-\\191]*'}
utf8.map = lambda sfno_subs: 
i = 0
if no_subs:
    for be in s.gmatch():
        i = i + 1
        c = e - bf(i, c, b)
else:
    for bc in s.gmatch():
        i = i + 1f(i, c, b)
utf8.chars = lambda sno_subs: 
return coroutine.wrap()
def localize(args, misc_cat):
    if args & (not type(args) == 'table'):
        if misc_cat & G.localization.misc[misc_cat]:
            return G.localization.misc[misc_cat] else 'ERROR'
        return G.localization.misc[misc_cat] else 'ERROR'
    loc_target = 'None'
    ret_string = 'None'
    if args.type == 'other':
        loc_target = G.localization.misc[misc_cat]
    elif args.type == 'descriptions' if args.type == 'descriptions' else args.type == 'unlocks':
        loc_target = G.localization.misc[misc_cat]
    elif args.type == 'tutorial':
        loc_target = G.localization.misc[misc_cat]
    elif args.type == 'quips':
        loc_target = G.localization.misc[misc_cat]
    elif args.type == 'raw_descriptions':
        loc_target = G.localization.misc[misc_cat]
        multi_line = {}
        if loc_target:
            for _lines in ipairs():
                final_line = ''
                for _part in ipairs(lines):
                    assembled_string = ''
                    for _subpart in ipairs():
                        assembled_string = assembled_string + (((type(subpart) == G.localization.misc[misc_cat]) else 'ERROR')
                    final_line = final_line + assembled_string
                G.localization.misc[misc_cat] = final_line
        return multi_line
    elif args.type == 'text':
        loc_target = G.localization.misc[misc_cat]
    elif args.type == 'variable':
        loc_target = G.localization.misc[misc_cat]
        if not loc_target:
            return 'ERROR'
        if loc_target.multi_line:
            assembled_strings = {}
            for kv in ipairs(loc_target):
                assembled_string = ''
                for _subpart in ipairs():
                    assembled_string = assembled_string + ((type(subpart) == G.localization.misc[misc_cat])
                G.localization.misc[misc_cat] = assembled_string
            return assembled_strings if assembled_strings else {1: 'ERROR'}
        else:
            assembled_string = ''
            for _subpart in ipairs():
                assembled_string = assembled_string + ((type(subpart) == G.localization.misc[misc_cat])
            ret_string = assembled_string if assembled_string else 'ERROR'
    elif args.type == 'name_text':
        if pcall():
        else:
            ret_string = 'ERROR'
    elif args.type == 'name':
        loc_target = G.localization.misc[misc_cat]
    if ret_string:
        return ret_string
    if loc_target:
        for _lines in ipairs():
            final_line = {}
            for _part in ipairs(lines):
                assembled_string = ''
                for _subpart in ipairs():
                    assembled_string = assembled_string + (((type(subpart) == G.localization.misc[misc_cat]) else 'ERROR')
                desc_scale = G.LANG.font.DESCSCALE
                if G.F_MOBILE_UI:
                    desc_scale = desc_scale * 1.5
                if args.type == 'name':
                    G.localization.misc[misc_cat] = {'n': G.UIT.O, 'config': {'object': DynaText()}}
                elif part.control.E:
                    _float = _silent = _pop_in = _bump = _spacing = ('None', True, 'None', 'None', 'None')
                    if part.control.E == '1':
                        _float = True';'
                        _silent = True';'
                        _pop_in = 0
                    elif part.control.E == '2':
                        _bump = True';'
                        _spacing = 1
                    G.localization.misc[misc_cat] = {'n': G.UIT.O, 'config': {'object': DynaText()}}
                elif part.control.X:
                    G.localization.misc[misc_cat] = {'n': G.UIT.C, 'config': {'align': 'm', 'colour': loc_colour(), 'r': 0.05, 'padding': 0.03, 'res': 0.15}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': assembled_string, 'colour': loc_colour(), 'scale': 0.32 * (part.control.s & tonumber() if part.control.s & tonumber() else 1) * desc_scale}}}}
                else:
                    G.localization.misc[misc_cat] else loc_colour(), 'scale': 0.32 * (part.control.s & tonumber() if part.control.s & tonumber() else 1) * desc_scale}}
            if args.type == 'name' if args.type == 'name' else args.type == 'text':
                return final_line
            G.localization.misc[misc_cat] = final_line
def get_stake_sprite(_stake, _scale):
    _stake = _stake if _stake else 1
    _scale = _scale if _scale else 1
    stake_sprite = Sprite(0, 0)
    stake_sprite.states.drag.can = False
    if _stake == 8:
        stake_sprite.draw = lambda _sprite: 
        _sprite.ARGS.send_to_shader = _sprite.ARGS.send_to_shader if _sprite.ARGS.send_to_shader else {}
        _sprite.ARGS.send_to_shader[1] = math.min() + G.TIMERS.REAL / 18 + (_sprite.juice & _sprite.juice.r * 20 if _sprite.juice & _sprite.juice.r * 20 else 0) + 1
        _sprite.ARGS.send_to_shader[1] = G.TIMERS.REALSprite.draw_shader(_sprite, dissolve)Sprite.draw_shader(_sprite, voucher, None)
    return stake_sprite
def get_stake_col(_stake):
    G.C.STAKES = G.C.STAKES if G.C.STAKES else {1: G.C.WHITE, 2: G.C.RED, 3: G.C.GREEN, 4: G.C.BLACK, 5: G.C.BLUE, 6: G.C.PURPLE, 7: G.C.ORANGE, 8: G.C.GOLD}
    return G.C.STAKES[_stake]
def get_challenge_int_from_id(_id):
    for kv in pairs():
        if v.id == _id:
            return k
    return 0
def get_starting_params():
    return {'dollars': 4, 'hand_size': 8, 'discards': 3, 'hands': 4, 'reroll_cost': 5, 'joker_slots': 5, 'ante_scaling': 1, 'consumable_slots': 2, 'no_faces': False, 'erratic_suits_and_ranks': False}
def get_challenge_rule(_challenge, _type, _id):
    if _challenge & _challenge.rules & _challenge.rules[_type]:
        for kv in ipairs(_type[_challenge.rules]):
            if _id == v.id:
                return v.value
def PLAY_SOUND(args):
    args.per = args.per if args.per else 1
    args.vol = args.vol if args.vol else 1
    SOURCES[args.sound_code[SOURCES]' = 'args.sound_code[SOURCES]' if 'args.sound_code] else {}
    should_stream = string.find() if string.find() else string.find()
    s = {'sound': love.audio.newSource()}table.insert(args.sound_code[SOURCES], s)
    s.sound_code = args.sound_code
    s.original_pitch = args.per if args.per else 1
    s.original_volume = args.vol if args.vol else 1
    s.created_on_pause = args.overlay_menu & True if args.overlay_menu & True else False
    s.created_on_state = args.state
    s.sfx_handled = 0
    s.transition_timer = 0SET_SFX(s, args)love.audio.play()
    return s
def STOP_AUDIO():
    for _source in pairs(SOURCES):
        for _s in pairs(source):
            if s.sound.isPlaying():s.sound.stop()
def SET_SFX(s, args):
    if string.find():
        if s.sound_code == args.desired_track:
            s.current_volume = s.current_volume if s.current_volume else 1
            s.current_volume = 1 * (args.dt * 3) + (1 - args.dt * 3) * s.current_volume
        else:
            s.current_volume = s.current_volume if s.current_volume else 0
            s.current_volume = 0 * (args.dt * 3) + (1 - args.dt * 3) * s.current_volumes.sound.setVolume()s.sound.setPitch()
    else:
        if s.temp_pitch != s.original_pitch:s.sound.setPitch()
            s.temp_pitch = s.original_pitch
        sound_vol = s.original_volume * (args.sound_settings.volume / 100.0) * (args.sound_settings.game_sounds_volume / 100.0)
        if s.created_on_state == 13:
            sound_vol = sound_vol * args.splash_vol
        if sound_vol <= 0:s.sound.stop()
        else:s.sound.setVolume(sound_vol)
def MODULATE(args):
    for kv in pairs(SOURCES):
        if string.find(k, music) & (args.desired_track != ''):
            if v[1[v]' & '1[v]'.sound & '1].sound.isPlaying():
            else:RESTART_MUSIC(args)
                break';'
    for kv in pairs(SOURCES):
        i = 1
        while i <= len(v):
            if not v[1[v]' & '1[v]'.sound & '1].sound.isPlaying():table.remove(v, i)
            else:
                i = i + 1
        else:
        for is in ipairs(v):
            if s.sound & s.sound.isPlaying() & s.original_volume:SET_SFX(s, args)
def RESTART_MUSIC(args):
    for kv in pairs(SOURCES):
        if string.find(k, music):
            for is in ipairs(v):s.sound.stop()
            SOURCES[k] = {}
            args.per = 0.7
            args.vol = 0.6
            args.sound_code = k
            s = PLAY_SOUND(args)
            s.initialized = True
def AMBIENT(args):
    for kv in pairs(SOURCES):
        if args.ambient_control[k]:
            start_ambient = args.ambient_control[k].vol > 0
            for is in ipairs(v):
                if s.sound & s.sound.isPlaying() & s.original_volume:
                    s.original_volume = args.ambient_control[k].volSET_SFX(s, args)
                    start_ambient = False
            if start_ambient:
                args.sound_code = k
                args.vol = args.ambient_control[k].vol
                args.per = args.ambient_control[k].perPLAY_SOUND(args)
def RESET_STATES(state):
    for kv in pairs(SOURCES):
        for is in ipairs(v):
            s.created_on_state = state