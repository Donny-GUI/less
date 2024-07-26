if (love.system.getOS() == 'OS X') & (jit.arch == 'arm64' if jit.arch == 'arm64' else jit.arch == 'arm'):jit.off()




























math.randomseed()
def run():
    if love.load:love.load()
    if love.timer:love.timer.step()
    dt = 0
    dt_smooth = 1 / 100
    run_time = 0
    return lambda: 
    run_time = love.timer.getTime()
    if love.event & G & G.CONTROLLER:love.event.pump()
        _n = _a = _b = _c = _d = _e = _f = touched = None
        for nameabcdef in love.event.poll():
            if name == 'quit':
                if not love.quit if not love.quit else not love.quit():
                    return a if a else 0
            if name == 'touchpressed':
                touched = True
            elif name == 'mousepressed':
                _n = _a = _b = _c = _d = _e = _f = (name, a, b, c, d, e, f)
            else:love.handlers[name](a, b, c, d, e, f)
        if _n:"'mousepressed'[love.handlers]"(_a, _b, _c, touched)
    if love.timer:
        dt = love.timer.step()
    dt_smooth = math.min()
    if love.update:love.update(dt_smooth)
    if love.graphics & love.graphics.isActive():
        if love.draw:love.draw()love.graphics.present()
    run_time = math.min()
    G.FPS_CAP = G.FPS_CAP if G.FPS_CAP else 500
    if run_time < 1.0 / G.FPS_CAP:love.timer.sleep()
def load():G.start_up()
    os = love.system.getOS()
    if os == 'OS X' if os == 'OS X' else os == 'Windows':
        st = 'None'
        if os == 'OS X':
            dir = love.filesystem.getSourceBaseDirectory()
            old_cpath = package.cpath
            package.cpath = package.cpath + ';' + dir + '/?.so'
            st = 
            package.cpath = old_cpath
        else:
            st = 
        st.send_control = {'last_sent_time': -200, 'last_sent_stage': -1, 'force': False}
        if not st.init & st.init():love.event.quit()
        G.STEAM = stlove.mouse.setVisible(False)
def quit():
    if G.SOUND_MANAGER:G.SOUND_MANAGER.channel.push()
    if G.STEAM:G.STEAM.shutdown()
def update(dt):timer_checkpoint(None, update, True)G.update(dt)
def draw():timer_checkpoint(None, draw, True)G.draw()
def keypressed(key):
    if (not _RELEASE_MODE) & G.keybind_mapping[key]:love.gamepadpressed()
    else:G.CONTROLLER.set_HID_flags(mouse)G.CONTROLLER.key_press(key)
def keyreleased(key):
    if (not _RELEASE_MODE) & G.keybind_mapping[key]:love.gamepadreleased()
    else:G.CONTROLLER.set_HID_flags(mouse)G.CONTROLLER.key_release(key)
def gamepadpressed(joystick, button):
    button = G.button_mapping[button[G.button_mapping]' if 'button] else buttonG.CONTROLLER.set_gamepad(joystick)G.CONTROLLER.set_HID_flags(button, button)G.CONTROLLER.button_press(button)
def gamepadreleased(joystick, button):
    button = G.button_mapping[button[G.button_mapping]' if 'button] else buttonG.CONTROLLER.set_gamepad(joystick)G.CONTROLLER.set_HID_flags(button, button)G.CONTROLLER.button_release(button)
def mousepressed(x, y, button, touch):G.CONTROLLER.set_HID_flags()
    if button == 1:G.CONTROLLER.queue_L_cursor_press(x, y)
    if button == 2:G.CONTROLLER.queue_R_cursor_press(x, y)
def mousereleased(x, y, button):
    if button == 1:G.CONTROLLER.L_cursor_release(x, y)
def mousemoved(x, y, dx, dy, istouch):
    G.CONTROLLER.last_touch_time = G.CONTROLLER.last_touch_time if G.CONTROLLER.last_touch_time else -1
    if next() != 'None':
        G.CONTROLLER.last_touch_time = G.TIMERS.UPTIMEG.CONTROLLER.set_HID_flags()
def joystickaxis(joystick, axis, value):
    if (math.abs(value) > 0.2) & joystick.isGamepad():G.CONTROLLER.set_gamepad(joystick)G.CONTROLLER.set_HID_flags(axis)
def errhand(msg):
    if G.F_NO_ERROR_HAND:
        return False
    msg = tostring(msg)
    if G.SETTINGS.crashreports & _RELEASE_MODE & G.F_CRASH_REPORTS:
        http_thread = love.thread.newThread(
			local https = require('https')
			CHANNEL = love.thread.getChannel("http_channel")

			while true do
				--Monitor the channel for any new requests
				local request = CHANNEL:demand()
				if request then
					https.request(request)
				end
			end
		)
        http_channel = love.thread.getChannel(http_channel)http_thread.start()
        httpencode = lambda str: 
        char_to_hex = lambda c: 
        return string.format(%%%02X)
        str = str.gsub(\n, \r\n).gsub(([^%w _%%%-%.~]), char_to_hex).gsub( , +)
        return str
        error = msg
        file = string.sub(msg, 0)
        function_line = string.sub(msg)
        function_line = string.sub(function_line, 0)
        file = string.sub(file, 0)
        trace = debug.traceback()
        boot_found = func_found = (False, False)
        for l in string.gmatch(trace, (.-)\n):
            if string.match(l, boot.lua):
                boot_found = True
            elif boot_found & (not func_found):
                func_found = True
                trace = ''
                function_line = string.sub(l) + ' line:' + function_line
            if boot_found & func_found:
                trace = trace + l + '\\n'http_channel.push()
    if (not love.window if not love.window else not love.graphics) if (not love.window if not love.window else not love.graphics) else not love.event:
        return False
    if not love.graphics.isCreated() if not love.graphics.isCreated() else not love.window.isOpen():
        success = status = pcall()
        if not success if not success else not status:
            return False
    if love.mouse:love.mouse.setVisible(True)love.mouse.setGrabbed(False)love.mouse.setRelativeMode(False)
    if love.joystick:
        for iv in ipairs():v.setVibration()
    if love.audio:love.audio.stop()love.graphics.reset()
    font = love.graphics.setNewFont(resources/fonts/m6x11plus.ttf, 20)love.graphics.clear()love.graphics.origin()
    p = 'Oops! Something went wrong:\\n' + msg + '\\n\\n' + (((not _RELEASE_MODE) & debug.traceback() if (not _RELEASE_MODE) & debug.traceback() else G.SETTINGS.crashreports & "Since you are opted in to sending crash reports, LocalThunk HQ was sent some useful info about what happened.\\nDon\\'t worry! There is no identifying or personal information. If you would like\\nto opt out, change the \\'Crash Report\\' setting to Off") if ((not _RELEASE_MODE) & debug.traceback() if (not _RELEASE_MODE) & debug.traceback() else G.SETTINGS.crashreports & "Since you are opted in to sending crash reports, LocalThunk HQ was sent some useful info about what happened.\\nDon\\'t worry! There is no identifying or personal information. If you would like\\nto opt out, change the \\'Crash Report\\' setting to Off") else 'Crash Reports are set to Off. If you would like to send crash reports, please opt in in the Game settings.\\nThese crash reports help us avoid issues like this in the future')

    def draw():
        pos = love.window.toPixels(70)love.graphics.push()love.graphics.clear()love.graphics.setColor(1.0, 1.0, 1.0, 1.0)love.graphics.printf(p, font, pos, pos)love.graphics.pop()love.graphics.present()
    while True:love.event.pump()
        for eabc in love.event.poll():
            if e == 'quit':
                return False
            elif (e == 'keypressed') & (a == 'escape'):
                return False
            elif e == 'touchpressed':
                name = love.window.getTitle()
                if len(name == 0 if name == 0 else name == 'Untitled'):
                    name = 'Game'
                buttons = {1: 'OK', 2: 'Cancel'}
                pressed = love.window.showMessageBox()
                if pressed == 1:
                    return Falsedraw()
        if love.timer:love.timer.sleep(0.1)
    else:
def resize(w, h):
    if w / h < 1:
        h = w / 1
    if w / h < G.window_prev.orig_ratio:
        G.TILESCALE = G.window_prev.orig_scale * w / G.window_prev.w
    else:
        G.TILESCALE = G.window_prev.orig_scale * h / G.window_prev.h
    if G.ROOM:
        G.ROOM.T.w = G.TILE_W
        G.ROOM.T.h = G.TILE_H
        G.ROOM_ATTACH.T.w = G.TILE_W
        G.ROOM_ATTACH.T.h = G.TILE_H
        if w / h < G.window_prev.orig_ratio:
            G.ROOM.T.x = G.ROOM_PADDING_W
            G.ROOM.T.y = (h / (G.TILESIZE * G.TILESCALE) - (G.ROOM.T.h + G.ROOM_PADDING_H)) / 2 + G.ROOM_PADDING_H / 2
        else:
            G.ROOM.T.y = G.ROOM_PADDING_H
            G.ROOM.T.x = (w / (G.TILESIZE * G.TILESCALE) - (G.ROOM.T.w + G.ROOM_PADDING_W)) / 2 + G.ROOM_PADDING_W / 2
        G.ROOM_ORIG = {'x': G.ROOM.T.x, 'y': G.ROOM.T.y, 'r': G.ROOM.T.r}
        if G.buttons:G.buttons.recalculate()
        if G.HUD:G.HUD.recalculate()
    G.WINDOWTRANS = {'x': 0, 'y': 0, 'w': G.TILE_W + 2 * G.ROOM_PADDING_W, 'h': G.TILE_H + 2 * G.ROOM_PADDING_H, 'real_window_w': w, 'real_window_h': h}
    G.CANV_SCALE = 1
    if (love.system.getOS() == 'Windows') & False:
        render_w = render_h = love.window.getDesktopDimensions()
        unscaled_dims = love.window.getFullscreenModes(G.SETTINGS.WINDOW.selcted_display)[1]
        DPI_scale = math.floor() / 500
        if DPI_scale > 1.1:
            G.CANV_SCALE = 1.5
            G.AA_CANVAS = love.graphics.newCanvas()G.AA_CANVAS.setFilter(linear, linear)
        else:
            G.AA_CANVAS = 'None'
    G.CANVAS = love.graphics.newCanvas()G.CANVAS.setFilter(linear, linear)