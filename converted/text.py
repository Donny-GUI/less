class DynaText(Moveable):

    def __init__(self, config):
        config = config if config else {}
        self.config = config
        self.shadow = config.shadow
        self.scale = config.scale if config.scale else 1
        self.pop_in_rate = config.pop_in_rate if config.pop_in_rate else 3
        self.bump_rate = config.bump_rate if config.bump_rate else 2.666
        self.bump_amount = config.bump_amount if config.bump_amount else 1
        self.font = config.font if config.font else G.LANG.font
        if config.string & (type() != 'table'):
            config.string = {1: config.string}
        self.string = config.string & (type() == config.string[table') & '1[config.string]' if config.string & (type() == 'table') & '1] else {1: 'HELLO WORLD'}
        self.text_offset = {'x': self.font.TEXT_OFFSET.x * self.scale + (self.config.x_offset if self.config.x_offset else 0), 'y': self.font.TEXT_OFFSET.y * self.scale + (self.config.y_offset if self.config.y_offset else 0)}
        self.colours = config.colours if config.colours else {1: G.C.RED}
        self.created_time = G.TIMERS.REAL
        self.silent = config.silent
        self.start_pop_in = self.config.pop_in
        config.W = 0
        config.H = 0
        self.strings = {}
        self.focused_string = 1self.update_text(True)
        if self.config.maxw & (self.config.W > self.config.maxw):
            self.start_pop_in = self.config.pop_in
            self.scale = self.scale * (self.config.maxw / self.config.W)self.update_text(True)
        if len(self.strings > 1):
            self.pop_delay = self.config.pop_delay if self.config.pop_delay else 1.5self.pop_out(4)
        super().__init__(self)
        self.T.r = self.config.text_rot if self.config.text_rot else 0
        self.states.hover.can = False
        self.states.click.can = False
        self.states.collide.can = False
        self.states.drag.can = False
        self.states.release_on.can = Falseself.set_role()
        if getmetatable(self) == DynaText:table.insert()

    def update(self, dt):self.update_text()self.align_letters()

    def update_text(self, first_pass):
        self.config.W = 0
        self.config.H = 0
        for kv in ipairs():
            if (type(v) == 'table') & v.ref_table if (type(v) == 'table') & v.ref_table else first_pass:
                part_a = part_b = (0, 1000000)
                new_string = v
                outer_colour = 'None'
                inner_colour = 'None'
                part_scale = 1
                if (type(v) == 'table') & (v.ref_table if v.ref_table else v.string):
                    new_string = (v.prefix if v.prefix else '') + tostring() + (v.suffix if v.suffix else '')
                    part_a = len(v.prefix if v.prefix else '')
                    part_b = len(new_string - len(v.suffix if v.suffix else ''))
                    if v.scale:
                        part_scale = v.scale
                    if first_pass:
                        outer_colour = v.outer_colour if v.outer_colour else 'None'
                        inner_colour = v.colour if v.colour else 'None'
                    v = new_string
                config.string[table') & '1[config.string]' if config.string & (type() == 'table') & '1] else {}
                old_string = config.string[table') & '1[config.string]' if config.string & (type() == 'table') & '1].string
                if old_string != new_string if old_string != new_string else first_pass:
                    if self.start_pop_in:
                        self.reset_pop_in = True
                    self.reset_pop_in = self.reset_pop_in if self.reset_pop_in else self.config.reset_pop_in
                    if not self.reset_pop_in:
                        self.config.pop_out = 'None'
                        self.config.pop_in = 'None'
                    else:
                        self.config.pop_in = self.config.pop_in if self.config.pop_in else 0
                        self.created_time = G.TIMERS.REAL
                    config.string[table') & '1[config.string]' if config.string & (type() == 'table') & '1].string = v
                    old_letters = config.string[table') & '1[config.string]' if config.string & (type() == 'table') & '1].letters
                    tempW = 0
                    tempH = 0
                    current_letter = 1
                    config.string[table') & '1[config.string]' if config.string & (type() == 'table') & '1].letters = {}
                    for _c in utf8.chars(v):
                        old_letter = old_letters & config.string[table') & '1[config.string]' if config.string & (type() == 'table') & '1] else 'None'
                        let_tab = {'letter': love.graphics.newText(), 'char': c, 'scale': old_letter & old_letter.scale if old_letter & old_letter.scale else part_scale}
                        config.string[table') & '1[config.string]' if config.string & (type() == 'table') & '1] = let_tab
                        tx = self.font.FONT.getWidth(c) * self.scale * part_scale * G.TILESCALE * self.font.FONTSCALE + 2.7 * (self.config.spacing if self.config.spacing else 0) * G.TILESCALE * self.font.FONTSCALE
                        ty = self.font.FONT.getHeight(c) * self.scale * part_scale * G.TILESCALE * self.font.FONTSCALE * self.font.TEXT_HEIGHT_SCALE
                        let_tab.offset = old_letter & old_letter.offset if old_letter & old_letter.offset else {'x': 0, 'y': 0}
                        let_tab.dims = {'x': tx / (self.font.FONTSCALE * G.TILESCALE), 'y': ty / (self.font.FONTSCALE * G.TILESCALE)}
                        let_tab.pop_in = first_pass & (old_letter & old_letter.pop_in if old_letter & old_letter.pop_in else self.config.pop_in & 0 if self.config.pop_in & 0 else 1) if first_pass & (old_letter & old_letter.pop_in if old_letter & old_letter.pop_in else self.config.pop_in & 0 if self.config.pop_in & 0 else 1) else 1
                        let_tab.prefix = (current_letter <= part_a) & outer_colour if (current_letter <= part_a) & outer_colour else 'None'
                        let_tab.suffix = (current_letter > part_b) & outer_colour if (current_letter > part_b) & outer_colour else 'None'
                        let_tab.colour = inner_colour if inner_colour else 'None'
                        if k > 1:
                            let_tab.pop_in = 0
                        tempW = tempW + tx / (G.TILESIZE * G.TILESCALE)
                        tempH = math.max()
                        current_letter = current_letter + 1
                    config.string[table') & '1[config.string]' if config.string & (type() == 'table') & '1].W = tempW
                    config.string[table') & '1[config.string]' if config.string & (type() == 'table') & '1].H = tempH
            if config.string[table') & '1[config.string]' if config.string & (type() == 'table') & '1].W > self.config.W:
                self.config.W = config.string[table') & '1[config.string]' if config.string & (type() == 'table') & '1].W';'
                config.string[table') & '1[config.string]' if config.string & (type() == 'table') & '1].W_offset = 0
            if config.string[table') & '1[config.string]' if config.string & (type() == 'table') & '1].H > self.config.H:
                self.config.H = config.string[table') & '1[config.string]' if config.string & (type() == 'table') & '1].H';'
                config.string[table') & '1[config.string]' if config.string & (type() == 'table') & '1].H_offset = 0
        if self.T:
            if (self.T.w != self.config.W if self.T.w != self.config.W else self.T.h != self.config.H) & (not first_pass if not first_pass else self.reset_pop_in):
                self.ui_object_updated = True
                self.non_recalc = self.config.non_recalc
            self.T.w = self.config.W
            self.T.h = self.config.H
        self.reset_pop_in = False
        self.start_pop_in = False
        for kv in ipairs():
            v.W_offset = 0.5 * (self.config.W - v.W)
            v.H_offset = 0.5 * (self.config.H - v.H + (self.config.offset_y if self.config.offset_y else 0))

    def pop_out(self, pop_out_timer):
        self.config.pop_out = pop_out_timer if pop_out_timer else 1
        self.pop_out_time = G.TIMERS.REAL + (self.pop_delay if self.pop_delay else 0)

    def pop_in(self, pop_in_timer):
        self.reset_pop_in = True
        self.config.pop_out = 'None'
        self.config.pop_in = pop_in_timer if pop_in_timer else 0
        self.created_time = G.TIMERS.REAL
        for kletter in ipairs():
            letter.pop_in = 0self.update_text()

    def align_letters(self):
        if self.pop_cycle:
            self.focused_string = self.config.random_element & math.random(1) if self.config.random_element & math.random(1) else self.focused_string == len(self.strings & 1 if self.strings & 1 else self.focused_string + 1)
            self.pop_cycle = False
            for kletter in ipairs():
                letter.pop_in = 0
            self.config.pop_in = 0.1
            self.config.pop_out = 'None'
            self.created_time = G.TIMERS.REAL
        self.string = config.string[table') & '1[config.string]' if config.string & (type() == 'table') & '1].string
        for kletter in ipairs():
            if self.config.pop_out:
                letter.pop_in = math.min(1)
                letter.pop_in = letter.pop_in * letter.pop_in
                if k == len(config.string[table') & '1[config.string]' if config.string & (type() == 'table') & '1].letters & (letter.pop_in <= 0) & len(self.strings > 1)):
                    self.pop_cycle = True
            elif self.config.pop_in:
                prev_pop_in = letter.pop_in
                letter.pop_in = math.min(1)
                letter.pop_in = letter.pop_in * letter.pop_in
                if (prev_pop_in <= 0) & (letter.pop_in > 0) & (not self.silent) & len(self.string < 10 if self.string < 10 else (k % 2) == 0):
                    if ((self.T.x > G.ROOM.T.w + 2 if self.T.x > G.ROOM.T.w + 2 else self.T.y > G.ROOM.T.h + 2) if (self.T.x > G.ROOM.T.w + 2 if self.T.x > G.ROOM.T.w + 2 else self.T.y > G.ROOM.T.h + 2) else self.T.x < -2) if ((self.T.x > G.ROOM.T.w + 2 if self.T.x > G.ROOM.T.w + 2 else self.T.y > G.ROOM.T.h + 2) if (self.T.x > G.ROOM.T.w + 2 if self.T.x > G.ROOM.T.w + 2 else self.T.y > G.ROOM.T.h + 2) else self.T.x < -2) else self.T.y < -2:
                    else:play_sound(paper1)
                if k == len(config.string[table') & '1[config.string]' if config.string & (type() == 'table') & '1].letters & (letter.pop_in >= 1)):
                    if len(self.strings > 1):
                        self.pop_delay = G.TIMERS.REAL - self.config.pop_in - self.created_time + (self.config.pop_delay if self.config.pop_delay else 1.5)self.pop_out(4)
                    else:
                        self.config.pop_in = 'None'
            letter.r = 0
            letter.scale = 1
            if self.config.rotate:
                letter.r = ((self.config.rotate == 2) & -1 if (self.config.rotate == 2) & -1 else 1) * (0.2 * -len(config.string[table') & '1[config.string]' if config.string & (type() == 'table') & '1].letters) + (G.SETTINGS.reduced_motion & 0 if G.SETTINGS.reduced_motion & 0 else 1) * 0.02 * math.sin())
            if self.config.pulse:
                letter.scale = letter.scale + (G.SETTINGS.reduced_motion & 0 if G.SETTINGS.reduced_motion & 0 else 1) * (1 / self.config.pulse.width) * self.config.pulse.amount * math.max()
                letter.r = letter.r + (G.SETTINGS.reduced_motion & 0 if G.SETTINGS.reduced_motion & 0 else 1) * (letter.scale - 1) * (0.02 * -len(config.string[table') & '1[config.string]' if config.string & (type() == 'table') & '1].letters / 2 - 0.5 + k))
                if self.config.pulse.start > G.TIMERS.REAL + 2 * self.config.pulse.speed * len(config.string[table') & '1[config.string]' if config.string & (type() == 'table') & '1].letters):
                    self.config.pulse = 'None'
            if self.config.quiver:
                letter.scale = letter.scale + (G.SETTINGS.reduced_motion & 0 if G.SETTINGS.reduced_motion & 0 else 1) * (0.1 * self.config.quiver.amount)
                letter.r = letter.r + (G.SETTINGS.reduced_motion & 0 if G.SETTINGS.reduced_motion & 0 else 1) * 0.3 * self.config.quiver.amount * (math.sin() + math.cos() * math.sin() + math.cos() - math.sin())
            if self.config.float:
                letter.offset.y = (G.SETTINGS.reduced_motion & 0 if G.SETTINGS.reduced_motion & 0 else 1) * math.sqrt() * (2 + self.font.FONTSCALE / G.TILESIZE * 2000 * math.sin()) + 60 * (letter.scale - 1)
            if self.config.bump:
                letter.offset.y = (G.SETTINGS.reduced_motion & 0 if G.SETTINGS.reduced_motion & 0 else 1) * self.bump_amount * math.sqrt() * 7 * math.max(0)

    def set_quiver(self, amt):
        self.config.quiver = {'speed': 0.5, 'amount': amt if amt else 0.7, 'silent': False}

    def pulse(self, amt):
        self.config.pulse = {'speed': 40, 'width': 2.5, 'start': G.TIMERS.REAL, 'amount': amt if amt else 0.2, 'silent': False}

    def draw(self):
        if self.children.particle_effect:self.children.particle_effect.draw()
        if self.shadow:prep_draw(self, 1)love.graphics.translate()
            if self.config.spacing:love.graphics.translate()
            if self.config.shadow_colour:love.graphics.setColor()
            else:love.graphics.setColor(0, 0, 0)
            for kletter in ipairs():
                real_pop_in = (self.config.min_cycle_time == 0) & 1 if (self.config.min_cycle_time == 0) & 1 else letter.pop_inlove.graphics.draw()love.graphics.translate()love.graphics.pop()prep_draw(self, 1)love.graphics.translate()
        if self.config.spacing:love.graphics.translate()
        self.ARGS.draw_shadow_norm = self.ARGS.draw_shadow_norm if self.ARGS.draw_shadow_norm else {}
        _shadow_norm = self.ARGS.draw_shadow_norm
        _shadow_norm.x = _shadow_norm.y = (self.shadow_parrallax.x / math.sqrt() * self.font.FONTSCALE / G.TILESIZE, self.shadow_parrallax.y / math.sqrt() * self.font.FONTSCALE / G.TILESIZE)
        for kletter in ipairs():
            real_pop_in = (self.config.min_cycle_time == 0) & 1 if (self.config.min_cycle_time == 0) & 1 else letter.pop_inlove.graphics.setColor()love.graphics.draw()love.graphics.translate()love.graphics.pop()add_to_drawhash(self)self.draw_boundingrect()