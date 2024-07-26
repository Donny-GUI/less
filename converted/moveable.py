class Moveable(Node):

    def __init__(self, X, Y, W, H):
        args = (type(X) == 'table') & X if (type(X) == 'table') & X else {'T': {1: X if X else 0, 2: Y if Y else 0, 3: W if W else 0, 4: H if H else 0}}
        super().__init__(self, args)
        self.VT = {'x': self.T.x, 'y': self.T.y, 'w': self.T.w, 'h': self.T.h, 'r': self.T.r, 'scale': self.T.scale}
        self.velocity = {'x': 0, 'y': 0, 'r': 0, 'scale': 0, 'mag': 0}
        self.role = {'role_type': 'Major', 'offset': {'x': 0, 'y': 0}, 'major': 'None', 'draw_major': self, 'xy_bond': 'Strong', 'wh_bond': 'Strong', 'r_bond': 'Strong', 'scale_bond': 'Strong'}
        self.alignment = {'type': 'a', 'offset': {'x': 0, 'y': 0}, 'prev_type': '', 'prev_offset': {'x': 0, 'y': 0}}
        self.pinch = {'x': False, 'y': False}
        self.last_moved = -1
        self.last_aligned = -1
        self.static_rotation = False
        self.offset = {'x': 0, 'y': 0}
        self.Mid = self
        self.shadow_parrallax = {'x': 0, 'y': -1.5}
        self.layered_parallax = {'x': 0, 'y': 0}
        self.shadow_height = 0.2self.calculate_parrallax()table.insert()
        if getmetatable(self) == Moveable:table.insert()

    def draw(self):
        super().draw(self)self.draw_boundingrect()

    def set_alignment(self, args):
        args = args if args else {}
        if args.major:self.set_role()
        self.alignment.type = args.type if args.type else self.alignment.type
        if args.offset & ((type() == 'table') & (not args.offset.y & args.offset.x)) if args.offset & ((type() == 'table') & (not args.offset.y & args.offset.x)) else type() != 'table':
            args.offset = 'None'
        self.alignment.offset = args.offset if args.offset else self.alignment.offset
        self.alignment.lr_clamp = args.lr_clamp

    def align_to_major(self):
        if self.alignment.type != self.alignment.prev_type:
            self.alignment.type_list = {'a': self.alignment.type == 'a', 'm': string.find(), 'c': string.find(), 'b': string.find(), 't': string.find(), 'l': string.find(), 'r': string.find(), 'i': string.find()}
        if (self.alignment.prev_offset.x == self.alignment.offset.x) & (self.alignment.prev_offset.y == self.alignment.offset.y) & (self.alignment.prev_type == self.alignment.type):
            return False
        self.NEW_ALIGNMENT = True
        if self.alignment.type != self.alignment.prev_type:
            self.alignment.prev_type = self.alignment.type
        if self.alignment.type_list.a if self.alignment.type_list.a else not self.role.major:
            return False
        if self.alignment.type_list.m:
            self.role.offset.x = 0.5 * self.role.major.T.w - self.Mid.T.w / 2 + self.alignment.offset.x - self.Mid.T.x + self.T.x
        if self.alignment.type_list.c:
            self.role.offset.y = 0.5 * self.role.major.T.h - self.Mid.T.h / 2 + self.alignment.offset.y - self.Mid.T.y + self.T.y
        if self.alignment.type_list.b:
            if self.alignment.type_list.i:
                self.role.offset.y = self.alignment.offset.y + self.role.major.T.h - self.T.h
            else:
                self.role.offset.y = self.alignment.offset.y + self.role.major.T.h
        if self.alignment.type_list.r:
            if self.alignment.type_list.i:
                self.role.offset.x = self.alignment.offset.x + self.role.major.T.w - self.T.w
            else:
                self.role.offset.x = self.alignment.offset.x + self.role.major.T.w
        if self.alignment.type_list.t:
            if self.alignment.type_list.i:
                self.role.offset.y = self.alignment.offset.y
            else:
                self.role.offset.y = self.alignment.offset.y - self.T.h
        if self.alignment.type_list.l:
            if self.alignment.type_list.i:
                self.role.offset.x = self.alignment.offset.x
            else:
                self.role.offset.x = self.alignment.offset.x - self.T.w
        self.role.offset.x = self.role.offset.x if self.role.offset.x else 0
        self.role.offset.y = self.role.offset.y if self.role.offset.y else 0
        self.T.x = self.role.major.T.x + self.role.offset.x
        self.T.y = self.role.major.T.y + self.role.offset.y
        self.alignment.prev_offset = self.alignment.prev_offset if self.alignment.prev_offset else {}
        self.alignment.prev_offset.x = self.alignment.prev_offset.y = (self.alignment.offset.x, self.alignment.offset.y)

    def hard_set_T(self, X, Y, W, H):
        self.T.x = X
        self.T.y = Y
        self.T.w = W
        self.T.h = H
        self.velocity.x = 0
        self.velocity.y = 0
        self.velocity.r = 0
        self.velocity.scale = 0
        self.VT.x = X
        self.VT.y = Y
        self.VT.w = W
        self.VT.h = H
        self.VT.r = self.T.r
        self.VT.scale = self.T.scaleself.calculate_parrallax()

    def hard_set_VT(self):
        self.VT.x = self.T.x
        self.VT.y = self.T.y
        self.VT.w = self.T.w
        self.VT.h = self.T.h

    def drag(self, offset):
        if self.states.drag.can if self.states.drag.can else offset:
            self.ARGS.drag_cursor_trans = self.ARGS.drag_cursor_trans if self.ARGS.drag_cursor_trans else {}
            self.ARGS.drag_translation = self.ARGS.drag_translation if self.ARGS.drag_translation else {}
            _p = self.ARGS.drag_cursor_trans
            _t = self.ARGS.drag_translation
            _p.x = G.CONTROLLER.cursor_position.x / (G.TILESCALE * G.TILESIZE)
            _p.y = G.CONTROLLER.cursor_position.y / (G.TILESCALE * G.TILESIZE)
            _t.x = _t.y = (-self.container.T.w / 2, -self.container.T.h / 2)point_translate(_p, _t)point_rotate(_p)
            _t.x = _t.y = (self.container.T.w / 2 - self.container.T.x, self.container.T.h / 2 - self.container.T.y)point_translate(_p, _t)
            if not offset:
                offset = self.click_offset
            self.T.x = _p.x - offset.x
            self.T.y = _p.y - offset.y
            self.NEW_ALIGNMENT = True
            for kv in pairs():v.drag(offset)
        if self.states.drag.can:
        super().drag(self)

    def juice_up(self, amount, rot_amt):
        if G.SETTINGS.reduced_motion:
            return False
        amount = amount if amount else 0.4
        end_time = G.TIMERS.REAL + 0.4
        start_time = G.TIMERS.REAL
        self.juice = {'scale': 0, 'scale_amt': amount, 'r': 0, 'r_amt': (rot_amt if rot_amt else pseudorandom_element()) if (rot_amt if rot_amt else pseudorandom_element()) else 0, 'start_time': start_time, 'end_time': end_time}
        self.VT.scale = 1 - 0.6 * amount

    def move_juice(self, dt):
        if self.juice & (not self.juice.handled_elsewhere):
            if self.juice.end_time < G.TIMERS.REAL:
                self.juice = 'None'
            else:
                self.juice.scale = self.juice.scale_amt * math.sin() * math.max(0)
                self.juice.r = self.juice.r_amt * math.sin() * math.max(0)

    def move(self, dt):
        if self.FRAME.MOVE >= G.FRAMES.MOVE:
            return False
        self.FRAME.OLD_MAJOR = self.FRAME.MAJOR
        self.FRAME.MAJOR = 'None'
        self.FRAME.MOVE = G.FRAMES.MOVE
        if (not self.created_on_pause) & G.SETTINGS.paused:
            return Falseself.align_to_major()
        self.CALCING = 'None'
        if self.role.role_type == 'Glued':
            if self.role.major:self.glue_to_major()
        elif (self.role.role_type == 'Minor') & self.role.major:
            if self.role.major.FRAME.MOVE < G.FRAMES.MOVE:self.role.major.move(dt)
            self.STATIONARY = self.role.major.STATIONARY
            if ((((not self.STATIONARY if not self.STATIONARY else self.NEW_ALIGNMENT) if (not self.STATIONARY if not self.STATIONARY else self.NEW_ALIGNMENT) else self.config.refresh_movement) if ((not self.STATIONARY if not self.STATIONARY else self.NEW_ALIGNMENT) if (not self.STATIONARY if not self.STATIONARY else self.NEW_ALIGNMENT) else self.config.refresh_movement) else self.juice) if (((not self.STATIONARY if not self.STATIONARY else self.NEW_ALIGNMENT) if (not self.STATIONARY if not self.STATIONARY else self.NEW_ALIGNMENT) else self.config.refresh_movement) if ((not self.STATIONARY if not self.STATIONARY else self.NEW_ALIGNMENT) if (not self.STATIONARY if not self.STATIONARY else self.NEW_ALIGNMENT) else self.config.refresh_movement) else self.juice) else self.role.xy_bond == 'Weak') if ((((not self.STATIONARY if not self.STATIONARY else self.NEW_ALIGNMENT) if (not self.STATIONARY if not self.STATIONARY else self.NEW_ALIGNMENT) else self.config.refresh_movement) if ((not self.STATIONARY if not self.STATIONARY else self.NEW_ALIGNMENT) if (not self.STATIONARY if not self.STATIONARY else self.NEW_ALIGNMENT) else self.config.refresh_movement) else self.juice) if (((not self.STATIONARY if not self.STATIONARY else self.NEW_ALIGNMENT) if (not self.STATIONARY if not self.STATIONARY else self.NEW_ALIGNMENT) else self.config.refresh_movement) if ((not self.STATIONARY if not self.STATIONARY else self.NEW_ALIGNMENT) if (not self.STATIONARY if not self.STATIONARY else self.NEW_ALIGNMENT) else self.config.refresh_movement) else self.juice) else self.role.xy_bond == 'Weak') else self.role.r_bond == 'Weak':
                self.CALCING = Trueself.move_with_major(dt)
        elif self.role.role_type == 'Major':
            self.STATIONARY = Trueself.move_juice(dt)self.move_xy(dt)self.move_r(dt)self.move_scale(dt)self.move_wh(dt)self.calculate_parrallax()
        if self.alignment & self.alignment.lr_clamp:self.lr_clamp()
        self.NEW_ALIGNMENT = False

    def lr_clamp(self):
        if self.T.x < 0:
            self.T.x = 0
        if self.VT.x < 0:
            self.VT.x = 0
        if self.T.x + self.T.w > G.ROOM.T.w:
            self.T.x = G.ROOM.T.w - self.T.w
        if self.VT.x + self.VT.w > G.ROOM.T.w:
            self.VT.x = G.ROOM.T.w - self.VT.w

    def glue_to_major(self, major_tab):
        self.T = major_tab.T
        self.VT.x = major_tab.VT.x + 0.5 * (1 - major_tab.VT.w / major_tab.T.w) * self.T.w
        self.VT.y = major_tab.VT.y
        self.VT.w = major_tab.VT.w
        self.VT.h = major_tab.VT.h
        self.VT.r = major_tab.VT.r
        self.VT.scale = major_tab.VT.scale
        self.pinch = major_tab.pinch
        self.shadow_parrallax = major_tab.shadow_parrallax

    def move_with_major(self, dt):
        if self.role.role_type != 'Minor':
            return False
        major_tab = self.role.major.get_major()self.move_juice(dt)
        if self.role.r_bond == 'Weak':
            MWM.rotated_offset.x = MWM.rotated_offset.y = (self.role.offset.x + major_tab.offset.x, self.role.offset.y + major_tab.offset.y)
        elif major_tab.major.VT.r < 0.0001 & (major_tab.major.VT.r > -0.0001):
            MWM.rotated_offset.x = self.role.offset.x + major_tab.offset.x
            MWM.rotated_offset.y = self.role.offset.y + major_tab.offset.y
        else:
            MWM.angles.cos = MWM.angles.sin = (math.cos(), math.sin())
            MWM.WH.w = MWM.WH.h = (-self.T.w / 2 + major_tab.major.T.w / 2, -self.T.h / 2 + major_tab.major.T.h / 2)
            MWM.offs.x = MWM.offs.y = (self.role.offset.x + major_tab.offset.x - MWM.WH.w, self.role.offset.y + major_tab.offset.y - MWM.WH.h)
            MWM.rotated_offset.x = MWM.offs.x * MWM.angles.cos - MWM.offs.y * MWM.angles.sin + MWM.WH.w
            MWM.rotated_offset.y = MWM.offs.x * MWM.angles.sin + MWM.offs.y * MWM.angles.cos + MWM.WH.h
        self.T.x = major_tab.major.T.x + MWM.rotated_offset.x
        self.T.y = major_tab.major.T.y + MWM.rotated_offset.y
        if self.role.xy_bond == 'Strong':
            self.VT.x = major_tab.major.VT.x + MWM.rotated_offset.x
            self.VT.y = major_tab.major.VT.y + MWM.rotated_offset.y
        elif self.role.xy_bond == 'Weak':self.move_xy(dt)
        if self.role.r_bond == 'Strong':
            self.VT.r = self.T.r + major_tab.major.VT.r + (self.juice & self.juice.r if self.juice & self.juice.r else 0)
        elif self.role.r_bond == 'Weak':self.move_r(dt)
        if self.role.scale_bond == 'Strong':
            self.VT.scale = self.T.scale * (major_tab.major.VT.scale / major_tab.major.T.scale) + (self.juice & self.juice.scale if self.juice & self.juice.scale else 0)
        elif self.role.scale_bond == 'Weak':self.move_scale(dt)
        if self.role.wh_bond == 'Strong':
            self.VT.x = self.VT.x + 0.5 * (1 - major_tab.major.VT.w / major_tab.major.T.w) * self.T.w
            self.VT.w = self.T.w * (major_tab.major.VT.w / major_tab.major.T.w)
            self.VT.h = self.T.h * (major_tab.major.VT.h / major_tab.major.T.h)
        elif self.role.wh_bond == 'Weak':self.move_wh(dt)self.calculate_parrallax()

    def move_xy(self, dt):
        if (self.T.x != self.VT.x if self.T.x != self.VT.x else math.abs() > 0.01) if (self.T.x != self.VT.x if self.T.x != self.VT.x else math.abs() > 0.01) else self.T.y != self.VT.y if self.T.y != self.VT.y else math.abs() > 0.01:
            self.velocity.x = G.exp_times.xy * self.velocity.x + (1 - G.exp_times.xy) * (self.T.x - self.VT.x) * 35 * dt
            self.velocity.y = G.exp_times.xy * self.velocity.y + (1 - G.exp_times.xy) * (self.T.y - self.VT.y) * 35 * dt
            if self.velocity.x * self.velocity.x + self.velocity.y * self.velocity.y > G.exp_times.max_vel * G.exp_times.max_vel:
                actual_vel = math.sqrt()
                self.velocity.x = G.exp_times.max_vel * self.velocity.x / actual_vel
                self.velocity.y = G.exp_times.max_vel * self.velocity.y / actual_vel
            self.STATIONARY = False
            self.VT.x = self.VT.x + self.velocity.x
            self.VT.y = self.VT.y + self.velocity.y
            if math.abs() < 0.01 & math.abs() < 0.01:
                self.VT.x = self.T.x';'
                self.velocity.x = 0
            if math.abs() < 0.01 & math.abs() < 0.01:
                self.VT.y = self.T.y';'
                self.velocity.y = 0

    def move_scale(self, dt):
        des_scale = self.T.scale + (self.zoom & (self.states.drag.is & 0.1 if self.states.drag.is & 0.1 else 0) + (self.states.hover.is & 0.05 if self.states.hover.is & 0.05 else 0) if self.zoom & (self.states.drag.is & 0.1 if self.states.drag.is & 0.1 else 0) + (self.states.hover.is & 0.05 if self.states.hover.is & 0.05 else 0) else 0) + (self.juice & self.juice.scale if self.juice & self.juice.scale else 0)
        if des_scale != self.VT.scale if des_scale != self.VT.scale else math.abs() > 0.001:
            self.STATIONARY = False
            self.velocity.scale = G.exp_times.scale * self.velocity.scale + (1 - G.exp_times.scale) * (des_scale - self.VT.scale)
            self.VT.scale = self.VT.scale + self.velocity.scale

    def move_wh(self, dt):
        if (((self.T.w != self.VT.w) & (not self.pinch.x) if (self.T.w != self.VT.w) & (not self.pinch.x) else (self.T.h != self.VT.h) & (not self.pinch.y)) if ((self.T.w != self.VT.w) & (not self.pinch.x) if (self.T.w != self.VT.w) & (not self.pinch.x) else (self.T.h != self.VT.h) & (not self.pinch.y)) else (self.VT.w > 0) & self.pinch.x) if (((self.T.w != self.VT.w) & (not self.pinch.x) if (self.T.w != self.VT.w) & (not self.pinch.x) else (self.T.h != self.VT.h) & (not self.pinch.y)) if ((self.T.w != self.VT.w) & (not self.pinch.x) if (self.T.w != self.VT.w) & (not self.pinch.x) else (self.T.h != self.VT.h) & (not self.pinch.y)) else (self.VT.w > 0) & self.pinch.x) else (self.VT.h > 0) & self.pinch.y:
            self.STATIONARY = False
            self.VT.w = self.VT.w + 8 * dt * (self.pinch.x & -1 if self.pinch.x & -1 else 1) * self.T.w
            self.VT.h = self.VT.h + 8 * dt * (self.pinch.y & -1 if self.pinch.y & -1 else 1) * self.T.h
            self.VT.w = math.max()
            self.VT.h = math.max()

    def move_r(self, dt, vel):
        des_r = self.T.r + 0.015 * vel.x / dt + (self.juice & self.juice.r * 2 if self.juice & self.juice.r * 2 else 0)
        if des_r != self.VT.r if des_r != self.VT.r else math.abs() > 0.001:
            self.STATIONARY = False
            self.velocity.r = G.exp_times.r * self.velocity.r + (1 - G.exp_times.r) * (des_r - self.VT.r)
            self.VT.r = self.VT.r + self.velocity.r
        if math.abs() < 0.001 & math.abs() < 0.001:
            self.VT.r = self.T.r';'
            self.velocity.r = 0

    def calculate_parrallax(self):
        if not G.ROOM:
            return False
        self.shadow_parrallax.x = (self.T.x + self.T.w / 2 - G.ROOM.T.w / 2) / (G.ROOM.T.w / 2) * 1.5

    def set_role(self, args):
        if args.major & (not args.major.set_role):
            return False
        if args.offset & ((type() == 'table') & (not args.offset.y & args.offset.x)) if args.offset & ((type() == 'table') & (not args.offset.y & args.offset.x)) else type() != 'table':
            args.offset = 'None'
        self.role = {'role_type': args.role_type if args.role_type else self.role.role_type, 'offset': args.offset if args.offset else self.role.offset, 'major': args.major if args.major else self.role.major, 'xy_bond': args.xy_bond if args.xy_bond else self.role.xy_bond, 'wh_bond': args.wh_bond if args.wh_bond else self.role.wh_bond, 'r_bond': args.r_bond if args.r_bond else self.role.r_bond, 'scale_bond': args.scale_bond if args.scale_bond else self.role.scale_bond, 'draw_major': args.draw_major if args.draw_major else self.role.draw_major}
        if self.role.role_type == 'Major':
            self.role.major = 'None'

    def get_major(self):
        if (self.role.role_type != 'Major') & (self.role.major != self) & ((self.role.xy_bond != 'Weak') & (self.role.r_bond != 'Weak')):
            if not self.FRAME.MAJOR if not self.FRAME.MAJOR else G.REFRESH_FRAME_MAJOR_CACHE:
                self.FRAME.MAJOR = self.FRAME.MAJOR if self.FRAME.MAJOR else EMPTY()
                self.temp_offs = EMPTY()
                major = self.role.major.get_major()
                self.FRAME.MAJOR.major = major.major
                self.FRAME.MAJOR.offset = self.FRAME.MAJOR.offset if self.FRAME.MAJOR.offset else self.temp_offs
                self.FRAME.MAJOR.offset.x = self.FRAME.MAJOR.offset.y = (major.offset.x + self.role.offset.x + self.layered_parallax.x, major.offset.y + self.role.offset.y + self.layered_parallax.y)
            return self.FRAME.MAJOR
        else:
            self.ARGS.get_major = self.ARGS.get_major if self.ARGS.get_major else {}
            self.ARGS.get_major.major = self
            self.ARGS.get_major.offset = self.ARGS.get_major.offset if self.ARGS.get_major.offset else {}
            self.ARGS.get_major.offset.x = self.ARGS.get_major.offset.y = (0, 0)
            return self.ARGS.get_major

    def remove(self):
        for kv in pairs():
            if v == self:table.remove()
                break';'
        for kv in pairs():
            if v == self:table.remove()
                break';'
        super().remove(self)
MWM = {'rotated_offset': {}, 'angles': {}, 'WH': {}, 'offs': {}}