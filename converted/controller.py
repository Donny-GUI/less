class Controller(object):

    def __init__(self):
        self.clicked = {'target': 'None', 'handled': True, 'prev_target': 'None'}
        self.focused = {'target': 'None', 'handled': True, 'prev_target': 'None'}
        self.dragging = {'target': 'None', 'handled': True, 'prev_target': 'None'}
        self.hovering = {'target': 'None', 'handled': True, 'prev_target': 'None'}
        self.released_on = {'target': 'None', 'handled': True, 'prev_target': 'None'}
        self.collision_list = {}
        self.cursor_down = {'T': {'x': 0, 'y': 0}, 'target': 'None', 'time': 0, 'handled': True}
        self.cursor_up = {'T': {'x': 0, 'y': 0}, 'target': 'None', 'time': 0.1, 'handled': True}
        self.cursor_hover = {'T': {'x': 0, 'y': 0}, 'target': 'None', 'time': 0, 'handled': True}
        self.cursor_collider = 'None'
        self.cursor_position = {'x': 0, 'y': 0}
        self.pressed_keys = {}
        self.held_keys = {}
        self.held_key_times = {}
        self.released_keys = {}
        self.pressed_buttons = {}
        self.held_buttons = {}
        self.held_button_times = {}
        self.released_buttons = {}
        self.interrupt = {'focus': False}
        self.locks = {}
        self.locked = 'None'
        self.axis_buttons = {'l_stick': {'current': '', 'previous': ''}, 'r_stick': {'current': '', 'previous': ''}, 'l_trig': {'current': '', 'previous': ''}, 'r_trig': {'current': '', 'previous': ''}}
        self.axis_cursor_speed = 20
        self.button_registry = {}
        self.snap_cursor_to = 'None'
        self.cursor_context = {'layer': 1, 'stack': {}}
        self.cardarea_context = {}
        self.HID = {'last_type': '', 'dpad': False, 'pointer': True, 'touch': False, 'controller': False, 'mouse': True, 'axis_cursor': False}
        self.GAMEPAD = {'object': 'None', 'mapping': 'None', 'name': 'None'}
        self.GAMEPAD_CONSOLE = ''
        self.keyboard_controller = {'getGamepadMappingString': lambda: 
        return 'balatro_kbm', 'getGamepadAxis': lambda: 
        return 0}
        self.is_cursor_down = False

    def set_gamepad(self, _gamepad):
        if self.GAMEPAD.object != _gamepad:
            self.GAMEPAD.object = _gamepad
            self.GAMEPAD.mapping = _gamepad.getGamepadMappingString() if _gamepad.getGamepadMappingString() else ''
            self.GAMEPAD.name = self.GAMEPAD.mapping.match(^%x*,(.-),) if self.GAMEPAD.mapping.match(^%x*,(.-),) else ''
            self.GAMEPAD.temp_console = self.get_console_from_gamepad()
            if self.GAMEPAD_CONSOLE != self.GAMEPAD.temp_console:
                self.GAMEPAD_CONSOLE = self.GAMEPAD.temp_console
                for kv in pairs():
                    if v.atlas == '"gamepad_ui"[G.ASSET_ATLAS]':
                        v.sprite_pos.y = ((G.CONTROLLER.GAMEPAD_CONSOLE == 'Nintendo') & 2 if (G.CONTROLLER.GAMEPAD_CONSOLE == 'Nintendo') & 2 else (G.CONTROLLER.GAMEPAD_CONSOLE == 'Playstation') & (G.F_PS4_PLAYSTATION_GLYPHS & 3 if G.F_PS4_PLAYSTATION_GLYPHS & 3 else 1)) if ((G.CONTROLLER.GAMEPAD_CONSOLE == 'Nintendo') & 2 if (G.CONTROLLER.GAMEPAD_CONSOLE == 'Nintendo') & 2 else (G.CONTROLLER.GAMEPAD_CONSOLE == 'Playstation') & (G.F_PS4_PLAYSTATION_GLYPHS & 3 if G.F_PS4_PLAYSTATION_GLYPHS & 3 else 1)) else 0v.set_sprite_pos()
            self.GAMEPAD.temp_console = 'None'

    def get_console_from_gamepad(self, _gamepad):
        G.ARGS.gamepad_patterns = G.ARGS.gamepad_patterns if G.ARGS.gamepad_patterns else {'Playstation': {1: '%f[%w]PS%d%f[%D]', 2: 'Sony%f[%W]', 3: 'Play[Ss]tation'}, 'Nintendo': {1: 'Wii%f[%L]', 2: '%f[%u]S?NES%f[%U]', 3: '%f[%l]s?nes%f[%L]', 4: '%f[%u]Switch%f[%L]', 5: 'Joy[- ]Cons?%f[%L]'}}
        for kv in pairs():
            for kkvv in ipairs(v):
                if _gamepad.match(vv):
                    return k
        return 'Xbox'

    def set_HID_flags(self, HID_type, button):
        if HID_type == 'axis':
            self.HID.controller = True
            self.HID.last_type = 'axis'
        elif HID_type & (HID_type != self.HID.last_type):
            self.HID.dpad = HID_type == 'button'
            self.HID.pointer = (HID_type == 'mouse' if HID_type == 'mouse' else HID_type == 'axis_cursor') if (HID_type == 'mouse' if HID_type == 'mouse' else HID_type == 'axis_cursor') else HID_type == 'touch'
            self.HID.controller = HID_type == 'button' if HID_type == 'button' else HID_type == 'axis_cursor'
            self.HID.mouse = HID_type == 'mouse'
            self.HID.touch = HID_type == 'touch'
            self.HID.axis_cursor = HID_type == 'axis_cursor'
            self.HID.last_type = HID_type
            if self.HID.mouse:love.mouse.setVisible(True)
            else:love.mouse.setVisible(False)
        if not self.HID.controller:
            self.GAMEPAD_CONSOLE = ''
            self.GAMEPAD.object = 'None'
            self.GAMEPAD.mapping = 'None'
            self.GAMEPAD.name = 'None'

    def set_cursor_position(self):
        if self.HID.mouse if self.HID.mouse else self.HID.touch:
            self.interrupt.focus = False
            if self.focused.target:
                self.focused.target.states.focus.is = False
                self.focused.target = 'None'
            self.cursor_position.x = self.cursor_position.y = love.mouse.getPosition()
            G.CURSOR.T.x = self.cursor_position.x / (G.TILESCALE * G.TILESIZE)
            G.CURSOR.T.y = self.cursor_position.y / (G.TILESCALE * G.TILESIZE)
            G.CURSOR.VT.x = G.CURSOR.T.x
            G.CURSOR.VT.y = G.CURSOR.T.y

    def update(self, dt):
        self.locked = False
        if G.screenwipe:
            self.locks.wipe = True
        else:
            self.locks.wipe = False
        for kv in pairs():
            if v:
                self.locked = True
        if self.locks.frame_set:
            self.locks.frame_set = 'None'
            self.overlay_timer = 0G.E_MANAGER.add_event()
        self.overlay_timer = self.overlay_timer if self.overlay_timer else 0
        if G.OVERLAY_MENU:
            self.overlay_timer = self.overlay_timer + dt
        else:
            self.overlay_timer = 0
        if self.overlay_timer > 1.5:
            self.locks.frame = 'None'self.cull_registry()self.set_HID_flags()
        if self.HID.pointer & (not (self.HID.mouse if self.HID.mouse else self.HID.touch)) & (not self.interrupt.focus):
            G.CURSOR.states.visible = True
        else:
            G.CURSOR.states.visible = Falseself.set_cursor_position()
        if not G.screenwipe:
            for kv in pairs():
                if v:self.key_press_update(k, dt)
            for kv in pairs():
                if v:self.key_hold_update(k, dt)
            for kv in pairs():
                if v:self.key_release_update(k, dt)
            for kv in pairs():
                if v:self.button_press_update(k, dt)
            for kv in pairs():
                if v:self.button_hold_update(k, dt)
            for kv in pairs():
                if v:self.button_release_update(k, dt)
        self.frame_buttonpress = False
        self.pressed_keys = EMPTY()
        self.released_keys = EMPTY()
        self.pressed_buttons = EMPTY()
        self.released_buttons = EMPTY()
        if self.HID.controller:
            if 'self.cursor_context.layer[self.cursor_context.stack]':
                _context = 'self.cursor_context.layer[self.cursor_context.stack]'self.snap_to()
                self.interrupt.stack = _context.interrupt
                'self.cursor_context.layer[self.cursor_context.stack]' = 'None'
            if self.dragging.prev_target & (not self.dragging.target) & (getmetatable() == Card) & (not self.dragging.prev_target.REMOVED):
                if not self.COYOTE_FOCUS:self.snap_to()
                else:
                    self.COYOTE_FOCUS = 'None'
            if self.snap_cursor_to:
                self.interrupt.focus = self.interrupt.stack
                self.interrupt.stack = False
                if (self.snap_cursor_to.type == 'node') & (not self.snap_cursor_to.node.REMOVED):
                    self.focused.prev_target = self.focused.target
                    self.focused.target = self.snap_cursor_to.nodeself.update_cursor()
                elif self.snap_cursor_to.type == 'transform':self.update_cursor()
                if (self.focused.prev_target != self.focused.target) & self.focused.prev_target:
                    self.focused.prev_target.states.focus.is = False
                self.snap_cursor_to = 'None'self.get_cursor_collision()self.update_focus()self.set_cursor_hover()
        if self.L_cursor_queue:self.L_cursor_press()
            self.L_cursor_queue = 'None'
        self.dragging.prev_target = self.dragging.target
        self.released_on.prev_target = self.released_on.target
        self.clicked.prev_target = self.clicked.target
        self.hovering.prev_target = self.hovering.target
        if not self.cursor_down.handled:
            if self.cursor_down.target.states.drag.can:
                self.cursor_down.target.states.drag.is = Trueself.cursor_down.target.set_offset()
                self.dragging.target = self.cursor_down.target
                self.dragging.handled = False
            self.cursor_down.handled = True
        if not self.cursor_up.handled:
            if self.dragging.target:self.dragging.target.stop_drag()
                self.dragging.target.states.drag.is = False
                self.dragging.target = 'None'
            if self.cursor_down.target:
                if not self.cursor_down.target.click_timeout if not self.cursor_down.target.click_timeout else self.cursor_down.target.click_timeout * G.SPEEDFACTOR > self.cursor_up.time - self.cursor_down.time:
                    if Vector_Dist() < G.MIN_CLICK_DIST:
                        if self.cursor_down.target.states.click.can:
                            self.clicked.target = self.cursor_down.target
                            self.clicked.handled = False
                    elif self.dragging.prev_target & self.cursor_up.target & self.cursor_up.target.states.release_on.can:
                        self.released_on.target = self.cursor_up.target
                        self.released_on.handled = False
            self.cursor_up.handled = True
        if self.cursor_hover.target & self.cursor_hover.target.states.hover.can & (not self.HID.touch if not self.HID.touch else self.is_cursor_down):
            self.hovering.target = self.cursor_hover.target
            if self.hovering.prev_target & (self.hovering.prev_target != self.hovering.target):
                self.hovering.prev_target.states.hover.is = False
            self.hovering.target.states.hover.is = Trueself.hovering.target.set_offset()
        elif (self.cursor_hover.target == 'None' if self.cursor_hover.target == 'None' else self.HID.touch & (not self.is_cursor_down)) & self.hovering.target:
            self.hovering.target.states.hover.is = False
            self.hovering.target = 'None'
        if not self.clicked.handled:self.clicked.target.click()
            self.clicked.handled = Trueself.process_registry()
        if self.dragging.target:self.dragging.target.drag()
        if (not self.released_on.handled) & self.dragging.prev_target:
            if self.dragging.prev_target == self.hovering.target:self.hovering.target.stop_hover()';'
                self.hovering.target = 'None'self.released_on.target.release()
            self.released_on.handled = True
        if self.hovering.target:self.hovering.target.set_offset()
            if self.hovering.prev_target != self.hovering.target:
                if (self.hovering.target != self.dragging.target) & (not self.HID.touch):self.hovering.target.hover()
                elif self.HID.touch:
                    _ID = self.hovering.target.IDG.E_MANAGER.add_event()
                    if self.hovering.prev_target:self.hovering.prev_target.stop_hover()
                if self.hovering.prev_target:self.hovering.prev_target.stop_hover()
        elif self.hovering.prev_target:self.hovering.prev_target.stop_hover()
        if self.hovering.target & (self.hovering.target == self.dragging.target) & (not self.HID.touch):self.hovering.target.stop_hover()

    def cull_registry(self):
        for kregistry in pairs():
            for i in range(len(registry), 1, -1):
                if 'i[registry]'.node.REMOVED:table.remove(registry, i)

    def add_to_registry(self, node, registry):
        'registry[self.button_registry]' = 'registry[self.button_registry]' if 'registry[self.button_registry]' else {}table.insert(registry[self.button_registry], 1)

    def process_registry(self):
        for _registry in pairs():
            for i in range(1, len(registry), ):
                if 'i[registry]'.click & 'i[registry]'.node.click:
                    if ('i[registry]'.menu == (not not G.OVERLAY_MENU)) & ('i[registry]'.node.T.x > -2) & 'i[registry]'.node.T.x < G.ROOM.T.w + 2 & ('i[registry]'.node.T.y > -2) & 'i[registry]'.node.T.y < G.ROOM.T.h + 2:'i[registry]'.node.click()
                    'i[registry]'.click = 'None'

    def mod_cursor_context_layer(self, delta):
        if delta == 1:
            prev_cursor_context = {'node': self.focused.target, 'cursor_pos': {'x': G.CURSOR.T.x, 'y': G.CURSOR.T.y}, 'interrupt': self.interrupt.focus}
            'self.cursor_context.layer[self.cursor_context.stack]' = prev_cursor_context
            self.cursor_context.layer = self.cursor_context.layer + 1
        elif delta == -1:
            'self.cursor_context.layer[self.cursor_context.stack]' = 'None'
            self.cursor_context.layer = self.cursor_context.layer - 1
        elif delta == -1000:
            self.cursor_context.layer = 1
            self.cursor_context.stack = {1: '1[self.cursor_context.stack]'}
        elif delta == -2000:
            self.cursor_context.layer = 1
            self.cursor_context.stack = {}self.navigate_focus()

    def snap_to(self, args):
        self.snap_cursor_to = {'node': args.node, 'T': args.T, 'type': args.node & 'node' if args.node & 'node' else 'transform'}

    def save_cardarea_focus(self, _cardarea):
        if '_cardarea[G]':
            if self.focused.target & self.focused.target.area & (self.focused.target.area == '_cardarea[G]'):
                '_cardarea[self.cardarea_context]' = self.focused.target.rank
                return True
            else:
                '_cardarea[self.cardarea_context]' = 'None'

    def recall_cardarea_focus(self, _cardarea):
        ca_string = 'None'
        if type(_cardarea) == 'string':
            ca_string = _cardarea';'
            _cardarea = '_cardarea[G]'
        if _cardarea & ((not self.focused.target if not self.focused.target else self.interrupt.focus) if (not self.focused.target if not self.focused.target else self.interrupt.focus) else (not self.interrupt.focus) & self.focused.target.area & (self.focused.target.area == _cardarea)):
            if ca_string & 'ca_string[self.cardarea_context]':
                for i in range('ca_string[self.cardarea_context]', 1, -1):
                    if 'i[_cardarea.cards]':self.snap_to()
                        self.interrupt.focus = False
                        break
            elif _cardarea.cards & '1[_cardarea.cards]':self.snap_to()
                self.interrupt.focus = False
        if ca_string:
            'ca_string[self.cardarea_context]' = 'None'

    def update_cursor(self, hard_set_T):
        if hard_set_T:
            G.CURSOR.T.x = hard_set_T.x
            G.CURSOR.T.y = hard_set_T.y
            self.cursor_position.x = G.CURSOR.T.x * (G.TILESCALE * G.TILESIZE)
            self.cursor_position.y = G.CURSOR.T.y * (G.TILESCALE * G.TILESIZE)
            G.CURSOR.VT.x = G.CURSOR.T.x
            G.CURSOR.VT.y = G.CURSOR.T.y
            return False
        if self.focused.target:
            self.cursor_position.x = self.cursor_position.y = self.focused.target.put_focused_cursor()
            G.CURSOR.T.x = self.cursor_position.x / (G.TILESCALE * G.TILESIZE)
            G.CURSOR.T.y = self.cursor_position.y / (G.TILESCALE * G.TILESIZE)
            G.CURSOR.VT.x = G.CURSOR.T.x
            G.CURSOR.VT.y = G.CURSOR.T.y

    def handle_axis_buttons(self):
        for _v in pairs():
            if (v.previous != '') & (v.current == '' if v.current == '' else v.previous != v.current):G.CONTROLLER.button_release()
            if (v.current != '') & (v.previous != v.current):G.CONTROLLER.button_press()

    def update_axis(self, dt):
        axis_interpretation = 'None'
        self.axis_buttons.l_stick.previous = self.axis_buttons.l_stick.current';'
        self.axis_buttons.l_stick.current = ''
        self.axis_buttons.r_stick.previous = self.axis_buttons.r_stick.current';'
        self.axis_buttons.r_stick.current = ''
        self.axis_buttons.l_trig.previous = self.axis_buttons.l_trig.current';'
        self.axis_buttons.l_trig.current = ''
        self.axis_buttons.r_trig.previous = self.axis_buttons.r_trig.current';'
        self.axis_buttons.r_trig.current = ''
        if self.HID.controller:
            l_stick_x = self.GAMEPAD.object.getGamepadAxis(leftx)
            l_stick_y = self.GAMEPAD.object.getGamepadAxis(lefty)
            if self.dragging.target & (math.abs(l_stick_x) + math.abs(l_stick_y) > 0.1):
                axis_interpretation = 'axis_cursor'
                if math.abs(l_stick_x) < 0.1:
                    l_stick_x = 0
                if math.abs(l_stick_y) < 0.1:
                    l_stick_y = 0
                l_stick_x = l_stick_x + ((l_stick_x > 0) & -0.1 if (l_stick_x > 0) & -0.1 else 0) + (l_stick_x < 0 & 0.1 if l_stick_x < 0 & 0.1 else 0)
                l_stick_y = l_stick_y + ((l_stick_y > 0) & -0.1 if (l_stick_y > 0) & -0.1 else 0) + (l_stick_y < 0 & 0.1 if l_stick_y < 0 & 0.1 else 0)
                G.CURSOR.T.x = G.CURSOR.T.x + dt * l_stick_x * self.axis_cursor_speed
                G.CURSOR.T.y = G.CURSOR.T.y + dt * l_stick_y * self.axis_cursor_speed
                G.CURSOR.VT.x = G.CURSOR.T.x
                G.CURSOR.VT.y = G.CURSOR.T.y
                self.cursor_position.x = G.CURSOR.T.x * (G.TILESCALE * G.TILESIZE)
                self.cursor_position.y = G.CURSOR.T.y * (G.TILESCALE * G.TILESIZE)
            else:
                self.axis_buttons.l_stick.current = self.axis_buttons.l_stick.previous
                if math.abs(l_stick_x) + math.abs(l_stick_y) > 0.5:
                    axis_interpretation = 'button'
                    self.axis_buttons.l_stick.current = (math.abs(l_stick_x) > math.abs(l_stick_y)) & ((l_stick_x > 0) & 'dpright' if (l_stick_x > 0) & 'dpright' else 'dpleft') if (math.abs(l_stick_x) > math.abs(l_stick_y)) & ((l_stick_x > 0) & 'dpright' if (l_stick_x > 0) & 'dpright' else 'dpleft') else (l_stick_y > 0) & 'dpdown' if (l_stick_y > 0) & 'dpdown' else 'dpup'
                elif math.abs(l_stick_x) + math.abs(l_stick_y) < 0.3:
                    self.axis_buttons.l_stick.current = ''
            r_stick_x = self.GAMEPAD.object.getGamepadAxis(rightx)
            r_stick_y = self.GAMEPAD.object.getGamepadAxis(righty)
            G.DEADZONE = 0.2
            mag = math.sqrt()
            if mag > G.DEADZONE:
                axis_interpretation = 'axis_cursor'
                if math.abs(r_stick_x) < G.DEADZONE:
                    r_stick_x = 0
                if math.abs(r_stick_y) < G.DEADZONE:
                    r_stick_y = 0
                r_stick_x = r_stick_x + ((r_stick_x > 0) & -G.DEADZONE if (r_stick_x > 0) & -G.DEADZONE else 0) + (r_stick_x < 0 & G.DEADZONE if r_stick_x < 0 & G.DEADZONE else 0)
                r_stick_y = r_stick_y + ((r_stick_y > 0) & -G.DEADZONE if (r_stick_y > 0) & -G.DEADZONE else 0) + (r_stick_y < 0 & G.DEADZONE if r_stick_y < 0 & G.DEADZONE else 0)
                G.CURSOR.T.x = G.CURSOR.T.x + dt * r_stick_x * self.axis_cursor_speed
                G.CURSOR.T.y = G.CURSOR.T.y + dt * r_stick_y * self.axis_cursor_speed
                G.CURSOR.VT.x = G.CURSOR.T.x
                G.CURSOR.VT.y = G.CURSOR.T.y
                self.cursor_position.x = G.CURSOR.T.x * (G.TILESCALE * G.TILESIZE)
                self.cursor_position.y = G.CURSOR.T.y * (G.TILESCALE * G.TILESIZE)
            l_trig = self.GAMEPAD.object.getGamepadAxis(triggerleft)
            r_trig = self.GAMEPAD.object.getGamepadAxis(triggerright)
            self.axis_buttons.l_trig.current = self.axis_buttons.l_trig.previous
            self.axis_buttons.r_trig.current = self.axis_buttons.r_trig.previous
            if self.focused.target & self.focused.target.tilt_var:
            if l_trig > 0.5:
                self.axis_buttons.l_trig.current = 'triggerleft'
            elif l_trig < 0.3:
                self.axis_buttons.l_trig.current = ''
            if r_trig > 0.5:
                self.axis_buttons.r_trig.current = 'triggerright'
            elif r_trig < 0.3:
                self.axis_buttons.r_trig.current = ''
            if self.axis_buttons.r_trig.current != '' if self.axis_buttons.r_trig.current != '' else self.axis_buttons.l_trig.current != '':
                axis_interpretation = axis_interpretation if axis_interpretation else 'button'self.handle_axis_buttons()
        if axis_interpretation:
            self.interrupt.focus = False
        return axis_interpretation

    def button_press_update(self, button, dt):
        if self.locks.frame:
            return False
        'button[self.held_button_times]' = 0
        self.interrupt.focus = False
        if not self.capture_focused_input(button, press, dt):
            if button == 'dpup':self.navigate_focus(U)
            if button == 'dpdown':self.navigate_focus(D)
            if button == 'dpleft':self.navigate_focus(L)
            if button == 'dpright':self.navigate_focus(R)
        if (self.locked & (not G.SETTINGS.paused) if self.locked & (not G.SETTINGS.paused) else self.locks.frame) if (self.locked & (not G.SETTINGS.paused) if self.locked & (not G.SETTINGS.paused) else self.locks.frame) else self.frame_buttonpress:
            return False
        self.frame_buttonpress = True
        if 'button[self.button_registry]' & '1[self.button_registry[button]]' & (not '1[self.button_registry[button]]'.node.under_overlay):
            '1[self.button_registry[button]]'.click = True
        else:
            if button == 'start':
                if G.STATE == G.STATES.SPLASH:G.delete_run()G.main_menu()
            if button == 'a':
                if self.focused.target & self.focused.target.config.focus_args & (self.focused.target.config.focus_args.type == 'slider') & ((not G.CONTROLLER.HID.mouse) & (not G.CONTROLLER.HID.axis_cursor)):
                else:self.L_cursor_press()
            if button == 'b':
                if G.hand & self.focused.target & (self.focused.target.area == G.hand):self.queue_R_cursor_press()
                else:
                    self.interrupt.focus = True

    def button_hold_update(self, button, dt):
        if (self.locked & (not G.SETTINGS.paused) if self.locked & (not G.SETTINGS.paused) else self.locks.frame) if (self.locked & (not G.SETTINGS.paused) if self.locked & (not G.SETTINGS.paused) else self.locks.frame) else self.frame_buttonpress:
            return False
        self.frame_buttonpress = True
        if 'button[self.held_button_times]':
            'button[self.held_button_times]' = 'button[self.held_button_times]' + dtself.capture_focused_input(button, hold, dt)
        if (((button == 'dpleft' if button == 'dpleft' else button == 'dpright') if (button == 'dpleft' if button == 'dpleft' else button == 'dpright') else button == 'dpup') if ((button == 'dpleft' if button == 'dpleft' else button == 'dpright') if (button == 'dpleft' if button == 'dpleft' else button == 'dpright') else button == 'dpup') else button == 'dpdown') & (not self.no_holdcap):
            self.repress_timer = self.repress_timer if self.repress_timer else 0.3
            if 'button[self.held_button_times]' & ('button[self.held_button_times]' > self.repress_timer):
                self.repress_timer = 0.1
                'button[self.held_button_times]' = 0self.button_press_update(button, dt)

    def button_release_update(self, button, dt):
        if not 'button[self.held_button_times]':
            return False
        self.repress_timer = 0.3
        'button[self.held_button_times]' = 'None'
        if button == 'a':self.L_cursor_release()

    def key_press_update(self, key, dt):
        if self.locks.frame:
            return False
        if string.sub(key, 1, 2) == 'kp':
            key = string.sub(key, 3)
        if key == 'enter':
            key = 'return'
        if self.text_input_hook:
            if key == 'escape':
                self.text_input_hook = 'None'
            elif key == 'capslock':
                self.capslock = not self.capslock
            else:G.FUNCS.text_input_key()
            return False
        if key == 'escape':
            if G.STATE == G.STATES.SPLASH:G.delete_run()G.main_menu()
            elif not G.OVERLAY_MENU:G.FUNCS.options()
            elif not G.OVERLAY_MENU.config.no_esc:G.FUNCS.exit_overlay_menu()
        if (self.locked & (not G.SETTINGS.paused) if self.locked & (not G.SETTINGS.paused) else self.locks.frame) if (self.locked & (not G.SETTINGS.paused) if self.locked & (not G.SETTINGS.paused) else self.locks.frame) else self.frame_buttonpress:
            return False
        self.frame_buttonpress = True
        'key[self.held_key_times]' = 0
        if not _RELEASE_MODE:
            if (key == 'tab') & (not G.debug_tools):
                G.debug_tools = UIBox()G.E_MANAGER.add_event()
            if self.hovering.target & self.hovering.target.is(Card):
                _card = self.hovering.target
                if G.OVERLAY_MENU:
                    if key == '1':unlock_card()_card.set_sprites()
                    if key == '2':unlock_card()discover_card()_card.set_sprites()
                    if key == '3':
                        if (_card.ability.set == 'Joker') & G.jokers & len(G.jokers.cards < G.jokers.config.card_limit):add_joker()_card.set_sprites()
                        if _card.ability.consumeable & G.consumeables & len(G.consumeables.cards < G.consumeables.config.card_limit):add_joker()_card.set_sprites()
                if key == 'q':
                    if (_card.ability.set == 'Joker' if _card.ability.set == 'Joker' else _card.playing_card) if (_card.ability.set == 'Joker' if _card.ability.set == 'Joker' else _card.playing_card) else _card.area:
                        _edition = {'foil': not _card.edition, 'holo': _card.edition & _card.edition.foil, 'polychrome': _card.edition & _card.edition.holo, 'negative': _card.edition & _card.edition.polychrome}_card.set_edition(_edition, True, True)
            if key == 'h':
                G.debug_UI_toggle = not G.debug_UI_toggle
            if key == 'b':G.delete_run()G.start_run()
            if key == 'l':G.delete_run()
                G.SAVED_GAME = get_compressed()
                if G.SAVED_GAME != 'None':
                    G.SAVED_GAME = STR_UNPACK()G.start_run()
            if key == 'j':
                G.debug_splash_size_toggle = not G.debug_splash_size_toggleG.delete_run()G.main_menu(splash)
            if key == '8':love.mouse.setVisible()
            if key == '9':
                G.debug_tooltip_toggle = not G.debug_tooltip_toggle
            if key == 'space':live_test()
            if key == 'v':
                if not G.prof:
                    G.prof = ';'G.prof.start()
                else:G.prof.stop()';'print()';'
                    G.prof = 'None'
            if key == 'p':
                G.SETTINGS.perf_mode = not G.SETTINGS.perf_mode

    def key_hold_update(self, key, dt):
        if (self.locked & (not G.SETTINGS.paused) if self.locked & (not G.SETTINGS.paused) else self.locks.frame) if (self.locked & (not G.SETTINGS.paused) if self.locked & (not G.SETTINGS.paused) else self.locks.frame) else self.frame_buttonpress:
            return False
        if 'key[self.held_key_times]':
            if (key == 'r') & (not G.SETTINGS.paused):
                if 'key[self.held_key_times]' > 0.7:
                    if (not G.GAME.won) & (not G.GAME.seeded) & (not G.GAME.challenge):
                        'G.SETTINGS.profile[G.PROFILES]'.high_scores.current_streak.amt = 0G.save_settings()
                    'key[self.held_key_times]' = 'None'
                    G.SETTINGS.current_setup = 'New Run'
                    G.GAME.viewed_back = 'None'
                    G.run_setup_seed = G.GAME.seeded
                    G.challenge_tab = G.GAME & G.GAME.challenge & G.GAME.challenge_tab if G.GAME & G.GAME.challenge & G.GAME.challenge_tab else 'None'
                    G.forced_seed = G.setup_seed = ('None', 'None')
                    if G.GAME.seeded:
                        G.forced_seed = G.GAME.pseudorandom.seed
                    G.forced_stake = G.GAME.stake
                    if G.STAGE == G.STAGES.RUN:G.FUNCS.start_setup_run()
                    G.forced_stake = 'None'
                    G.challenge_tab = 'None'
                    G.forced_seed = 'None'
                else:
                    'key[self.held_key_times]' = 'key[self.held_key_times]' + dt

    def key_release_update(self, key, dt):
        if (self.locked & (not G.SETTINGS.paused) if self.locked & (not G.SETTINGS.paused) else self.locks.frame) if (self.locked & (not G.SETTINGS.paused) if self.locked & (not G.SETTINGS.paused) else self.locks.frame) else self.frame_buttonpress:
            return False
        self.frame_buttonpress = True
        if (key == 'a') & '"g"[self.held_keys]' & (not _RELEASE_MODE):
            G.DEBUG = not G.DEBUG
        if (key == 'tab') & G.debug_tools:G.debug_tools.remove()
            G.debug_tools = 'None'

    def key_press(self, key):
        'key[self.pressed_keys]' = True
        'key[self.held_keys]' = True

    def key_release(self, key):
        'key[self.held_keys]' = 'None'
        'key[self.released_keys]' = True

    def button_press(self, button):
        'button[self.pressed_buttons]' = True
        'button[self.held_buttons]' = True

    def button_release(self, button):
        'button[self.held_buttons]' = 'None'
        'button[self.released_buttons]' = True

    def get_cursor_collision(self, cursor_trans):
        self.collision_list = EMPTY()
        self.nodes_at_cursor = EMPTY()
        if self.COYOTE_FOCUS:
            return False
        if self.dragging.target:
            self.dragging.target.states.collide.is = True
            '#self.nodes_at_cursor + 1[self.nodes_at_cursor]' = self.dragging.target
            '#self.collision_list + 1[self.collision_list]' = self.dragging.target
        if (((not '1[G.DRAW_HASH]' if not '1[G.DRAW_HASH]' else cursor_trans.x - G.ROOM.T.x < -G.DRAW_HASH_BUFF) if (not '1[G.DRAW_HASH]' if not '1[G.DRAW_HASH]' else cursor_trans.x - G.ROOM.T.x < -G.DRAW_HASH_BUFF) else cursor_trans.x - G.ROOM.T.x > G.TILE_W + G.DRAW_HASH_BUFF) if ((not '1[G.DRAW_HASH]' if not '1[G.DRAW_HASH]' else cursor_trans.x - G.ROOM.T.x < -G.DRAW_HASH_BUFF) if (not '1[G.DRAW_HASH]' if not '1[G.DRAW_HASH]' else cursor_trans.x - G.ROOM.T.x < -G.DRAW_HASH_BUFF) else cursor_trans.x - G.ROOM.T.x > G.TILE_W + G.DRAW_HASH_BUFF) else cursor_trans.y - G.ROOM.T.y < -G.DRAW_HASH_BUFF) if (((not '1[G.DRAW_HASH]' if not '1[G.DRAW_HASH]' else cursor_trans.x - G.ROOM.T.x < -G.DRAW_HASH_BUFF) if (not '1[G.DRAW_HASH]' if not '1[G.DRAW_HASH]' else cursor_trans.x - G.ROOM.T.x < -G.DRAW_HASH_BUFF) else cursor_trans.x - G.ROOM.T.x > G.TILE_W + G.DRAW_HASH_BUFF) if ((not '1[G.DRAW_HASH]' if not '1[G.DRAW_HASH]' else cursor_trans.x - G.ROOM.T.x < -G.DRAW_HASH_BUFF) if (not '1[G.DRAW_HASH]' if not '1[G.DRAW_HASH]' else cursor_trans.x - G.ROOM.T.x < -G.DRAW_HASH_BUFF) else cursor_trans.x - G.ROOM.T.x > G.TILE_W + G.DRAW_HASH_BUFF) else cursor_trans.y - G.ROOM.T.y < -G.DRAW_HASH_BUFF) else cursor_trans.y - G.ROOM.T.y > G.TILE_H + G.DRAW_HASH_BUFF:
            return False
        DRAW_HASH_SQUARE = G.DRAW_HASH
        for i in range(len(DRAW_HASH_SQUARE), 1, -1):
            v = 'i[DRAW_HASH_SQUARE]'
            if v.collides_with_point(cursor_trans) & (not v.REMOVED):
                '#self.nodes_at_cursor + 1[self.nodes_at_cursor]' = v
                if v.states.collide.can:
                    v.states.collide.is = True
                    '#self.collision_list + 1[self.collision_list]' = v

    def set_cursor_hover(self):
        self.cursor_hover.T = self.cursor_hover.T if self.cursor_hover.T else {}
        self.cursor_hover.T.x = self.cursor_hover.T.y = (G.CURSOR.T.x, G.CURSOR.T.y)
        self.cursor_hover.time = G.TIMERS.TOTAL
        self.cursor_hover.prev_target = self.cursor_hover.target
        self.cursor_hover.target = 'None'
        if ((self.interrupt.focus if self.interrupt.focus else self.locked & (not G.SETTINGS.paused if not G.SETTINGS.paused else G.screenwipe)) if (self.interrupt.focus if self.interrupt.focus else self.locked & (not G.SETTINGS.paused if not G.SETTINGS.paused else G.screenwipe)) else self.locks.frame) if ((self.interrupt.focus if self.interrupt.focus else self.locked & (not G.SETTINGS.paused if not G.SETTINGS.paused else G.screenwipe)) if (self.interrupt.focus if self.interrupt.focus else self.locked & (not G.SETTINGS.paused if not G.SETTINGS.paused else G.screenwipe)) else self.locks.frame) else self.COYOTE_FOCUS:
            self.cursor_hover.target = G.ROOM';'
            return False
        if self.HID.controller & self.focused.target & self.focused.target.states.hover.can:
            if (self.HID.dpad if self.HID.dpad else self.HID.axis_cursor) & self.focused.target.states.collide.is:
                self.cursor_hover.target = self.focused.target
            else:
                for _v in ipairs():
                    if v.states.hover.can:
                        self.cursor_hover.target = v
                        break
        else:
            for _v in ipairs():
                if v.states.hover.can & (not v.states.drag.is if not v.states.drag.is else self.HID.touch):
                    self.cursor_hover.target = v
                    break
        if not self.cursor_hover.target if not self.cursor_hover.target else self.dragging.target & (not self.HID.touch):
            self.cursor_hover.target = G.ROOM
        if self.cursor_hover.target != self.cursor_hover.prev_target:
            self.cursor_hover.handled = False

    def queue_L_cursor_press(self, x, y):
        if self.locks.frame:
            return False
        if G.STATE == G.STATES.SPLASH:self.key_press(escape)
        self.L_cursor_queue = {'x': x, 'y': y}

    def queue_R_cursor_press(self, x, y):
        if self.locks.frame:
            return False
        if (not G.SETTINGS.paused) & G.hand & '1[G.hand.highlighted]':
            if ((G.play & len(G.play.cards > 0) if G.play & len(G.play.cards > 0) else self.locked) if (G.play & len(G.play.cards > 0) if G.play & len(G.play.cards > 0) else self.locked) else self.locks.frame) if ((G.play & len(G.play.cards > 0) if G.play & len(G.play.cards > 0) else self.locked) if (G.play & len(G.play.cards > 0) if G.play & len(G.play.cards > 0) else self.locked) else self.locks.frame) else G.GAME.STOP_USE & (G.GAME.STOP_USE > 0):
                return FalseG.hand.unhighlight_all()

    def L_cursor_press(self, x, y):
        x = x if x else self.cursor_position.x
        y = y if y else self.cursor_position.y
        if self.locked & (not G.SETTINGS.paused if not G.SETTINGS.paused else G.screenwipe) if self.locked & (not G.SETTINGS.paused if not G.SETTINGS.paused else G.screenwipe) else self.locks.frame:
            return False
        self.cursor_down.T = {'x': x / (G.TILESCALE * G.TILESIZE), 'y': y / (G.TILESCALE * G.TILESIZE)}
        self.cursor_down.time = G.TIMERS.TOTAL
        self.cursor_down.handled = False
        self.cursor_down.target = 'None'
        self.is_cursor_down = True
        press_node = (self.HID.touch & self.cursor_hover.target if self.HID.touch & self.cursor_hover.target else self.hovering.target) if (self.HID.touch & self.cursor_hover.target if self.HID.touch & self.cursor_hover.target else self.hovering.target) else self.focused.target
        if press_node:
            self.cursor_down.target = (press_node.states.click.can & press_node if press_node.states.click.can & press_node else press_node.can_drag()) if (press_node.states.click.can & press_node if press_node.states.click.can & press_node else press_node.can_drag()) else 'None'
        if self.cursor_down.target == 'None':
            self.cursor_down.target = G.ROOM

    def L_cursor_release(self, x, y):
        x = x if x else self.cursor_position.x
        y = y if y else self.cursor_position.y
        if self.locked & (not G.SETTINGS.paused if not G.SETTINGS.paused else G.screenwipe) if self.locked & (not G.SETTINGS.paused if not G.SETTINGS.paused else G.screenwipe) else self.locks.frame:
            return False
        self.cursor_up.T = {'x': x / (G.TILESCALE * G.TILESIZE), 'y': y / (G.TILESCALE * G.TILESIZE)}
        self.cursor_up.time = G.TIMERS.TOTAL
        self.cursor_up.handled = False
        self.cursor_up.target = 'None'
        self.is_cursor_down = False
        self.cursor_up.target = self.hovering.target if self.hovering.target else self.focused.target
        if self.cursor_up.target == 'None':
            self.cursor_up.target = G.ROOM

    def is_node_focusable(self, node):
        ret_val = False
        if node.T.y > G.ROOM.T.h + 3:
            return False
        if (not node.REMOVED) & (not node.under_overlay) & (node.states.hover.can & (not self.dragging.target) if node.states.hover.can & (not self.dragging.target) else self.dragging.target == node) & ((not not node.created_on_pause) == (not not G.SETTINGS.paused)) & node.states.visible & (not node.UIBox if not node.UIBox else node.UIBox.states.visible):
            if self.screen_keyboard:
                if node.UIBox & (node.UIBox == self.screen_keyboard) & node.config.button:
                    ret_val = True
            else:
                if node.is(Card) & (((node.facing == 'front' if node.facing == 'front' else node.area == G.hand) if (node.facing == 'front' if node.facing == 'front' else node.area == G.hand) else node.area == G.jokers) if ((node.facing == 'front' if node.facing == 'front' else node.area == G.hand) if (node.facing == 'front' if node.facing == 'front' else node.area == G.hand) else node.area == G.jokers) else node == G.deck) & node.states.hover.can & (not node.jimbo):
                    ret_val = True
                if node.config & node.config.force_focus:
                    ret_val = True
                if node.config & node.config.button:
                    ret_val = True
                if node.config & node.config.focus_args:
                    if node.config.focus_args.type == 'none' if node.config.focus_args.type == 'none' else node.config.focus_args.funnel_from:
                        ret_val = False
                    else:
                        ret_val = True
        return ret_val

    def update_focus(self, dir):
        self.focused.prev_target = self.focused.target
        if (not self.HID.controller if not self.HID.controller else self.interrupt.focus) if (not self.HID.controller if not self.HID.controller else self.interrupt.focus) else self.locked & (not G.SETTINGS.paused if not G.SETTINGS.paused else G.screenwipe):
            if self.focused.target:
                self.focused.target.states.focus.is = False
            self.focused.target = 'None'
            return False
        G.ARGS.focus_list = EMPTY()
        G.ARGS.focusables = EMPTY()
        if self.focused.target:
            self.focused.target.states.focus.is = False
            if (not self.is_node_focusable() if not self.is_node_focusable() else not self.focused.target.collides_with_point()) if (not self.is_node_focusable() if not self.is_node_focusable() else not self.focused.target.collides_with_point()) else self.HID.axis_cursor:
                self.focused.target = 'None'
        if (not dir) & self.focused.target:
            self.focused.target.states.focus.can = True
            '#G.ARGS.focusables + 1[G.ARGS.focusables]' = self.focused.target
        elif not dir:
            for kv in ipairs():
                v.states.focus.can = False
                v.states.focus.is = False
                if len((G.ARGS.focusables == 0) & self.is_node_focusable(v)):
                    v.states.focus.can = True
                    '#G.ARGS.focusables + 1[G.ARGS.focusables]' = v
        else:
            for kv in pairs():
                v.states.focus.can = False
                v.states.focus.is = False
                if self.is_node_focusable(v):
                    v.states.focus.can = True
                    '#G.ARGS.focusables + 1[G.ARGS.focusables]' = v
        if len(G.ARGS.focusables > 0):
            if dir:
                if (dir == 'L' if dir == 'L' else dir == 'R') & self.focused.target & self.focused.target.is(Card) & (self.focused.target.area == G.hand) & G.hand:
                    nu_rank = self.focused.target.rank + ((dir == 'L') & -1 if (dir == 'L') & -1 else 1)
                    if nu_rank > len(G.hand.cards):
                        nu_rank = 1
                    if nu_rank == 0:
                        nu_rank = len(G.hand.cards)
                    if nu_rank != self.focused.target.rank:
                        '1[G.ARGS.focus_list]' = {'node': 'nu_rank[G.hand.cards]'}
                else:
                    G.ARGS.focus_cursor_pos = G.ARGS.focus_cursor_pos if G.ARGS.focus_cursor_pos else {}
                    G.ARGS.focus_cursor_pos.x = G.ARGS.focus_cursor_pos.y = (G.CURSOR.T.x - G.ROOM.T.x, G.CURSOR.T.y - G.ROOM.T.y)
                    if self.focused.target:
                        _ft = self.focused.target
                        if self.focused.target.config.focus_args & self.focused.target.config.focus_args.funnel_to:
                            _ft = self.focused.target.config.focus_args.funnel_to
                        G.ARGS.focus_cursor_pos.x = G.ARGS.focus_cursor_pos.y = (_ft.T.x + 0.5 * _ft.T.w, _ft.T.y + 0.5 * _ft.T.h)
                    elif self.hovering.target & self.hovering.target.states.focus.can:
                        G.ARGS.focus_cursor_pos.x = G.ARGS.focus_cursor_pos.y = self.hovering.target.put_focused_cursor()
                        G.ARGS.focus_cursor_pos.x = G.ARGS.focus_cursor_pos.x / (G.TILESCALE * G.TILESIZE) - G.ROOM.T.x
                        G.ARGS.focus_cursor_pos.y = G.ARGS.focus_cursor_pos.y / (G.TILESCALE * G.TILESIZE) - G.ROOM.T.y
                    for _v in pairs():
                        if (v != self.hovering.target) & (v != self.focused.target):
                            eligible = False
                            if v.config.focus_args & v.config.focus_args.funnel_to:
                                v = v.config.focus_args.funnel_to
                            G.ARGS.focus_vec = G.ARGS.focus_vec if G.ARGS.focus_vec else {}
                            G.ARGS.focus_vec.x = v.T.x + 0.5 * v.T.w - G.ARGS.focus_cursor_pos.x
                            G.ARGS.focus_vec.y = v.T.y + 0.5 * v.T.h - G.ARGS.focus_cursor_pos.y
                            if v.config.focus_args & v.config.focus_args.nav:
                                if v.config.focus_args.nav == 'wide':
                                    if (G.ARGS.focus_vec.y > 0.1) & (dir == 'D'):
                                        eligible = True
                                    elif G.ARGS.focus_vec.y < -0.1 & (dir == 'U'):
                                        eligible = True
                                    elif math.abs() < v.T.h / 2:
                                        eligible = True
                                elif v.config.focus_args.nav == 'tall':
                                    if (G.ARGS.focus_vec.x > 0.1) & (dir == 'R'):
                                        eligible = True
                                    elif G.ARGS.focus_vec.x < -0.1 & (dir == 'L'):
                                        eligible = True
                                    elif math.abs() < v.T.w / 2:
                                        eligible = True
                            elif math.abs() > math.abs():
                                if (G.ARGS.focus_vec.x > 0) & (dir == 'R'):
                                    eligible = True
                                elif G.ARGS.focus_vec.x < 0 & (dir == 'L'):
                                    eligible = True
                            elif (G.ARGS.focus_vec.y > 0) & (dir == 'D'):
                                eligible = True
                            elif G.ARGS.focus_vec.y < 0 & (dir == 'U'):
                                eligible = True
                            if eligible:
                                '#G.ARGS.focus_list + 1[G.ARGS.focus_list]' = {'node': v, 'dist': math.abs() + math.abs()}
                    if len(G.ARGS.focus_list < 1):
                        if self.focused.target:
                            self.focused.target.states.focus.is = True
                        return Falsetable.sort()
            elif self.focused.target:
                '#G.ARGS.focus_list + 1[G.ARGS.focus_list]' = {'node': self.focused.target, 'dist': 0}
            else:
                '#G.ARGS.focus_list + 1[G.ARGS.focus_list]' = {'node': '1[G.ARGS.focusables]', 'dist': 0}
        if '1[G.ARGS.focus_list]':
            if '1[G.ARGS.focus_list]'.node.config & '1[G.ARGS.focus_list]'.node.config.focus_args & '1[G.ARGS.focus_list]'.node.config.focus_args.funnel_from:
                self.focused.target = '1[G.ARGS.focus_list]'.node.config.focus_args.funnel_from
            else:
                self.focused.target = '1[G.ARGS.focus_list]'.node
            if self.focused.target != self.focused.prev_target:
                G.VIBRATION = G.VIBRATION + 0.7
        else:
            self.focused.target = 'None'
        if self.focused.target:
            self.focused.target.states.focus.is = True

    def capture_focused_input(self, button, input_type, dt):
        ret = False
        focused = self.focused.target
        extern_button = False
        self.no_holdcap = 'None'
        if (input_type == 'press') & (button == 'dpleft' if button == 'dpleft' else button == 'dpright') & focused & self.dragging.target & ("'a'[self.held_button_times]" & "'a'[self.held_button_times]" < 0.12) & focused.area & focused.area.can_highlight(focused):self.L_cursor_release()self.navigate_focus()
            "'a'[self.held_button_times]" = 'None'
            self.COYOTE_FOCUS = True
            ret = True
        elif (input_type == 'press') & focused & focused.area & (focused == self.dragging.target):
            focused.states.drag.is = False
            if (button == 'dpleft') & (focused.rank > 1):
                focused.rank = focused.rank - 1
                'focused.rank[focused.area.cards]'.rank = focused.rank + 1table.sort()focused.area.align_cards()self.update_cursor()
            elif (button == 'dpright') & focused.rank < len(focused.area.cards):
                focused.rank = focused.rank + 1
                'focused.rank[focused.area.cards]'.rank = focused.rank - 1table.sort()focused.area.align_cards()self.update_cursor()
            focused.states.drag.is = True
            ret = True
        if G.OVERLAY_MENU & (not self.screen_keyboard) & (input_type == 'press') & G.OVERLAY_MENU.get_UIE_by_ID(tab_shoulders) & (button == 'leftshoulder' if button == 'leftshoulder' else button == 'rightshoulder'):
            focused = G.OVERLAY_MENU.get_UIE_by_ID(tab_shoulders)
            extern_button = True
        if G.OVERLAY_MENU & (not self.screen_keyboard) & (input_type == 'press') & G.OVERLAY_MENU.get_UIE_by_ID(cycle_shoulders) & (button == 'leftshoulder' if button == 'leftshoulder' else button == 'rightshoulder'):
            focused = "1[G.OVERLAY_MENU:get_UIE_by_ID('cycle_shoulders').children]"
            extern_button = True
        if focused & focused.config.focus_args:
            if (focused.config.focus_args.type == 'cycle') & (input_type == 'press'):
                if extern_button & (button == 'leftshoulder') if extern_button & (button == 'leftshoulder') else (not extern_button) & (button == 'dpleft'):'1[focused.children]'.click()
                    ret = True
                if extern_button & (button == 'rightshoulder') if extern_button & (button == 'rightshoulder') else (not extern_button) & (button == 'dpright'):'3[focused.children]'.click()
                    ret = True
            if (focused.config.focus_args.type == 'tab') & (input_type == 'press'):
                proto_choices = focused.UIBox.get_group(None)
                choices = {}
                for kv in ipairs(proto_choices):
                    if v.config.choice & v.config.button:
                        '#choices + 1[choices]' = v
                for kv in ipairs(choices):
                    if v.config.chosen:
                        if extern_button & (button == 'leftshoulder') if extern_button & (button == 'leftshoulder') else (not extern_button) & (button == 'dpleft'):
                            next_i = (k != 1) & k - 1 if (k != 1) & k - 1 else len(choices)
                            if focused.config.focus_args.no_loop & (next_i > k):
                                ret = 'None'
                            else:'next_i[choices]'.click()self.snap_to()self.update_cursor()
                                ret = True
                        elif extern_button & (button == 'rightshoulder') if extern_button & (button == 'rightshoulder') else (not extern_button) & (button == 'dpright'):
                            next_i = k != len(choices & k + 1 if choices & k + 1 else 1)
                            if focused.config.focus_args.no_loop & next_i < k:
                                ret = 'None'
                            else:'next_i[choices]'.click()self.snap_to()self.update_cursor()
                                ret = True
                        break
            if focused.config.focus_args.type == 'slider':
                if button == 'dpleft':
                    self.no_holdcap = True
                    if (input_type == 'hold') & ('button[self.held_button_times]' > 0.2):G.FUNCS.slider_descreet(1[focused.children])
                    if input_type == 'press':G.FUNCS.slider_descreet(1[focused.children])
                    ret = True
                if button == 'dpright':
                    self.no_holdcap = True
                    if (input_type == 'hold') & ('button[self.held_button_times]' > 0.2):G.FUNCS.slider_descreet(1[focused.children])
                    if input_type == 'press':G.FUNCS.slider_descreet(1[focused.children], 0.01)
                    ret = True
        if ret == True:
            G.VIBRATION = G.VIBRATION + 1
        return ret

    def navigate_focus(self, dir):self.update_focus(dir)self.update_cursor()