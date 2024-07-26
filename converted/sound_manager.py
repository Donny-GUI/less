


if (love.system.getOS() == 'OS X') & (jit.arch == 'arm64' if jit.arch == 'arm64' else jit.arch == 'arm'):jit.off()
CHANNEL = love.thread.getChannel(sound_request)
LOAD_CHANNEL = love.thread.getChannel(load_channel)
LOAD_CHANNEL.push(audio thread start)
DISABLE_SFX = False
SOURCES = {}
sound_files = love.filesystem.getDirectoryItems(resources/sounds)
for _filename in ipairs(sound_files):
    extension = string.sub(filename)
    for i in range(1, 1, ):
        if extension == '.ogg':LOAD_CHANNEL.push()
            sound_code = string.sub(filename, 1)
            s = {'sound': love.audio.newSource(), 'filepath': 'resources/sounds/' + filename}
            SOURCES[sound_code] = {}table.insert(sound_code[SOURCES], s)
            s.sound_code = sound_codes.sound.setVolume(0)love.audio.play()s.sound.stop()
def PLAY_SOUND(args):
    args.per = args.per if args.per else 1
    args.vol = args.vol if args.vol else 1
    SOURCES[args.sound_code[SOURCES]' = 'args.sound_code[SOURCES]' if 'args.sound_code] else {}
    for _s in ipairs(args.sound_code[SOURCES]):
        if s.sound & (not s.sound.isPlaying()):
            s.original_pitch = args.per
            s.original_volume = args.vol
            s.created_on_pause = args.overlay_menu
            s.created_on_state = args.state
            s.sfx_handled = 0
            s.transition_timer = 0SET_SFX(s, args)love.audio.play()
            return s
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
            if not v[1[v]' & '1[v]'.sound & '1].sound.release()table.remove(v, i)
            else:
                i = i + 1
        else:
        for _s in pairs(v):
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
            start_ambient = args.ambient_control[k].vol * (args.sound_settings.volume / 100.0) * (args.sound_settings.game_sounds_volume / 100.0) > 0
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
LOAD_CHANNEL.push(finished)
while True:
    request = CHANNEL.demand()
    if request:
        if False:
        elif request.type == 'sound':PLAY_SOUND(request)
        elif request.type == 'stop':STOP_AUDIO()
        elif request.type == 'modulate':MODULATE(request)
            if request.ambient_control:AMBIENT(request)
        elif request.type == 'restart_music':RESTART_MUSIC()
        elif request.type == 'reset_states':
            for kv in pairs(SOURCES):
                for is in ipairs(v):
                    s.created_on_state = request.state
else: