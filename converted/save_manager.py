
if (love.system.getOS() == 'OS X') & (jit.arch == 'arm64' if jit.arch == 'arm64' else jit.arch == 'arm'):jit.off()





CHANNEL = love.thread.getChannel(save_request)
while True:
    request = CHANNEL.demand()
    if request:
        if request.type == 'save_progress':
            prefix_profile = (request.save_progress.SETTINGS.profile if request.save_progress.SETTINGS.profile else 1) + ''
            if not love.filesystem.getInfo(prefix_profile):love.filesystem.createDirectory(prefix_profile)
            prefix_profile = prefix_profile + '/'
            if not love.filesystem.getInfo():love.filesystem.append()
            meta = STR_UNPACK()
            meta.unlocked = meta.unlocked if meta.unlocked else {}
            meta.discovered = meta.discovered if meta.discovered else {}
            meta.alerted = meta.alerted if meta.alerted else {}
            _append = False
            for kv in pairs():
                if string.find(v, u) & (not 'k[meta.unlocked]'):
                    'k[meta.unlocked]' = True
                    _append = True
                if string.find(v, d) & (not 'k[meta.discovered]'):
                    'k[meta.discovered]' = True
                    _append = True
                if string.find(v, a) & (not 'k[meta.alerted]'):
                    'k[meta.alerted]' = True
                    _append = True
            if _append:compress_and_save()compress_and_save(settings.jkr)compress_and_save()CHANNEL.push(done)
        elif request.type == 'save_settings':compress_and_save(settings.jkr)compress_and_save()
        elif request.type == 'save_metrics':compress_and_save(metrics.jkr)
        elif request.type == 'save_notify':
            prefix_profile = (request.profile_num if request.profile_num else 1) + ''
            if not love.filesystem.getInfo(prefix_profile):love.filesystem.createDirectory(prefix_profile)
            prefix_profile = prefix_profile + '/'
            if not love.filesystem.getInfo():love.filesystem.append()
            unlock_notify = get_compressed() if get_compressed() else ''
            if request.save_notify & (not string.find(unlock_notify)):compress_and_save()
        elif request.type == 'save_run':
            prefix_profile = (request.profile_num if request.profile_num else 1) + ''
            if not love.filesystem.getInfo(prefix_profile):love.filesystem.createDirectory(prefix_profile)
            prefix_profile = prefix_profile + '/'compress_and_save()
else: