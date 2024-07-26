class Blind(Moveable):

    def __init__(self, X, Y, W, H):
        super().__init__(self, X, Y, W, H)
        self.children = {}
        self.config = {}
        self.tilt_var = {'mx': 0, 'my': 0, 'amt': 0}
        self.ambient_tilt = 0.3
        self.chips = 0
        self.zoom = True
        self.states.collide.can = True
        self.colour = copy_table()
        self.dark_colour = darken()
        self.children.animatedSprite = AnimatedSprite()
        self.children.animatedSprite.states = self.states
        self.children.animatedSprite.states.visible = False
        self.children.animatedSprite.states.drag.can = True
        self.states.collide.can = True
        self.states.drag.can = True
        self.loc_debuff_lines = {1: '', 2: ''}
        self.shadow_height = 0
        if getmetatable(self) == Blind:table.insert()

    def change_colour(self, blind_col):
        blind_col = blind_col if blind_col else get_blind_main_colour()
        dark_col = mix_colours(blind_col)ease_colour()ease_colour()
        if (not self.boss) & self.name:
            blind_col = darken()
            dark_col = lighten()
        else:
            dark_col = mix_colours(blind_col)ease_colour()ease_colour()

    def set_text(self):
        if self.config.blind:
            if self.disabled:
                self.loc_name = (self.name == '') & self.name if (self.name == '') & self.name else localize()
                self.loc_debuff_text = ''
                self.loc_debuff_lines[1] = ''
                self.loc_debuff_lines[1] = ''
            else:
                loc_vars = 'None'
                if self.name == 'The Ox':
                    loc_vars = {1: localize()}
                loc_target = localize()
                if loc_target:
                    self.loc_name = (self.name == '') & self.name if (self.name == '') & self.name else localize()
                    self.loc_debuff_text = ''
                    for kv in ipairs(loc_target):
                        self.loc_debuff_text = self.loc_debuff_text + v + (k <= len(loc_target & ' ' if loc_target & ' ' else ''))
                    self.loc_debuff_lines[1] else ''
                    self.loc_debuff_lines[1] else ''
                else:
                    self.loc_name = ''';'
                    self.loc_debuff_text = ''
                    self.loc_debuff_lines[1] = ''
                    self.loc_debuff_lines[1] = ''

    def set_blind(self, blind, reset, silent):
        if not reset:
            self.config.blind = blind if blind else {}
            self.name = blind & blind.name if blind & blind.name else ''
            self.dollars = blind & blind.dollars if blind & blind.dollars else 0
            self.sound_pings = self.dollars + 2
            if G.GAME.modifiers.no_blind_reward & self.loc_debuff_lines[1]:
                self.dollars = 0
            self.debuff = blind & blind.debuff if blind & blind.debuff else {}
            self.pos = blind & blind.pos
            self.mult = blind & blind.mult if blind & blind.mult else 0
            self.disabled = False
            self.discards_sub = 'None'
            self.hands_sub = 'None'
            self.boss = blind & (not not blind.boss)
            self.blind_set = False
            self.triggered = 'None'
            self.prepped = Trueself.set_text()
            G.GAME.last_blind = G.GAME.last_blind if G.GAME.last_blind else {}
            G.GAME.last_blind.boss = self.boss
            G.GAME.last_blind.name = self.name
            if blind & blind.name:self.change_colour()
            else:self.change_colour()
            self.chips = get_blind_amount() * self.mult * G.GAME.starting_params.ante_scaling
            self.chip_text = number_format()
            if not blind:
                self.chips = 0
            G.GAME.current_round.dollars_to_be_earned = (self.dollars > 0) & string.rep() + '' if (self.dollars > 0) & string.rep() + '' else ''
            G.HUD_blind.alignment.offset.y = -10G.HUD_blind.recalculate(False)
            if blind & blind.name & (blind.name != ''):self.alert_debuff(True)G.E_MANAGER.add_event()
            self.config.h_popup_config = {'align': 'tm', 'offset': {'x': 0, 'y': -0.1}, 'parent': self}
        if (self.name == 'The Eye') & (not reset):
            self.hands = {'Flush Five': False, 'Flush House': False, 'Five of a Kind': False, 'Straight Flush': False, 'Four of a Kind': False, 'Full House': False, 'Flush': False, 'Straight': False, 'Three of a Kind': False, 'Two Pair': False, 'Pair': False, 'High Card': False}
        if (self.name == 'The Mouth') & (not reset):
            self.only_hand = False
        if (self.name == 'The Fish') & (not reset):
            self.prepped = 'None'
        if (self.name == 'The Water') & (not reset):
            self.discards_sub = G.GAME.current_round.discards_leftease_discard()
        if (self.name == 'The Needle') & (not reset):
            self.hands_sub = G.GAME.round_resets.hands - 1ease_hands_played()
        if (self.name == 'The Manacle') & (not reset):G.hand.change_size()
        if (self.name == 'Amber Acorn') & (not reset) & len(G.jokers.cards > 0):G.jokers.unhighlight_all()
            for kv in ipairs():v.flip()
            if len(G.jokers.cards > 1):G.E_MANAGER.add_event()
        for _v in ipairs():self.debuff_card(v)
        for _v in ipairs():
            if not reset:self.debuff_card(v, True)
        G.ARGS.spin.real = (G.SETTINGS.reduced_motion & 0 if G.SETTINGS.reduced_motion & 0 else 1) * (self.config.blind.boss & (self.config.blind.boss.showdown & 0.5 if self.config.blind.boss.showdown & 0.5 else 0.25) if self.config.blind.boss & (self.config.blind.boss.showdown & 0.5 if self.config.blind.boss.showdown & 0.5 else 0.25) else 0)

    def alert_debuff(self, first):
        if self.loc_debuff_text & (self.loc_debuff_text != ''):
            self.block_play = TrueG.E_MANAGER.add_event()

    def get_loc_debuff_text(self):
        disp_text = ((self.config.blind.name == 'The Wheel') & G.GAME.probabilities.normal if (self.config.blind.name == 'The Wheel') & G.GAME.probabilities.normal else '') + self.loc_debuff_text
        if (self.config.blind.name == 'The Mouth') & self.only_hand:
            disp_text = disp_text + self.loc_debuff_lines[1]
        return disp_text

    def defeat(self, silent):
        dissolve_time = 1.3
        extra_time = 0
        self.dissolve = 0
        self.dissolve_colours = {1: G.C.BLACK, 2: G.C.RED}self.juice_up()
        self.children.particles = Particles(0, 0, 0, 0)
        blind_name_dynatext = G.HUD_blind.get_UIE_by_ID(HUD_blind_name).config.objectblind_name_dynatext.pop_out(2)G.E_MANAGER.add_event()
        if not silent:
            for i in range(1, math.min(), ):
                extra_time = extra_time + (0.4 + 0.15 * i) * dissolve_timeG.E_MANAGER.add_event()G.E_MANAGER.add_event()G.E_MANAGER.add_event()G.E_MANAGER.add_event()
        for kv in ipairs():
            if v.facing == 'back':v.flip()
        if (self.name == 'The Manacle') & (not self.disabled):G.hand.change_size(1)

    def get_type(self):
        if self.name == 'Small Blind':
            return 'Small'
        elif self.name == 'Big Blind':
            return 'Big'
        elif self.name & (self.name != ''):
            return 'Boss'

    def disable(self):
        self.disabled = True
        for kv in ipairs():
            if v.facing == 'back':v.flip()
        if self.name == 'The Water':ease_discard()
        if ((self.name == 'The Wheel' if self.name == 'The Wheel' else self.name == 'The House') if (self.name == 'The Wheel' if self.name == 'The Wheel' else self.name == 'The House') else self.name == 'The Mark') if ((self.name == 'The Wheel' if self.name == 'The Wheel' else self.name == 'The House') if (self.name == 'The Wheel' if self.name == 'The Wheel' else self.name == 'The House') else self.name == 'The Mark') else self.name == 'The Fish':
            for i in range(1, len(G.hand.cards), ):
                if self.loc_debuff_lines[1].flip()
            for kv in pairs():
                v.ability.wheel_flipped = 'None'
        if self.name == 'The Needle':ease_hands_played()
        if self.name == 'The Wall':
            self.chips = self.chips / 2
            self.chip_text = number_format()
        if self.name == 'Cerulean Bell':
            for kv in ipairs():
                v.ability.forced_selection = 'None'
        if self.name == 'The Manacle':G.hand.change_size(1)G.FUNCS.draw_from_deck_to_hand(1)
        if self.name == 'The Serpent':
        if self.name == 'Violet Vessel':
            self.chips = self.chips / 3
            self.chip_text = number_format()G.E_MANAGER.add_event()
        for _v in ipairs():self.debuff_card(v)
        for _v in ipairs():self.debuff_card(v)self.set_text()self.wiggle()

    def wiggle(self):self.children.animatedSprite.juice_up(0.3)G.E_MANAGER.add_event()play_sound(tarot2, 1, 0.4)

    def juice_up(self, _a, _b):self.children.animatedSprite.juice_up()

    def hover(self):
        if not G.CONTROLLER.dragging.target if not G.CONTROLLER.dragging.target else G.CONTROLLER.using_touch:
            if (not self.hovering) & self.states.visible & self.children.animatedSprite.states.visible:
                self.hovering = True
                self.hover_tilt = 2self.children.animatedSprite.juice_up(0.05, 0.02)play_sound(chips1)Node.hover(self)

    def stop_hover(self):
        self.hovering = False
        self.hover_tilt = 0Node.stop_hover(self)

    def draw(self):
        if not self.states.visible:
            return False
        self.tilt_var = self.tilt_var if self.tilt_var else {}
        self.tilt_var.mx = self.tilt_var.my = (G.CONTROLLER.cursor_position.x, G.CONTROLLER.cursor_position.y)
        self.children.animatedSprite.role.draw_major = selfself.children.animatedSprite.draw_shader(dissolve, 0.1)self.children.animatedSprite.draw_shader(dissolve)
        for kv in pairs():
            if k != 'animatedSprite':
                v.VT.scale = self.VT.scalev.draw()add_to_drawhash(self)

    def press_play(self):
        if self.disabled:
            return False
        if self.name == 'The Hook':G.E_MANAGER.add_event()
            self.triggered = Truedelay(0.7)
            return True
        if self.name == 'Crimson Heart':
            if self.loc_debuff_lines[1]:
                self.triggered = True
                self.prepped = True
        if self.name == 'The Fish':
            self.prepped = True
        if self.name == 'The Tooth':G.E_MANAGER.add_event()
            self.triggered = True
            return True

    def modify_hand(self, cards, poker_hands, text, mult, hand_chips):
        if self.disabled:
            return multhand_chipsFalse
        if self.name == 'The Flint':
            self.triggered = True
            return math.max()math.max()True
        return multhand_chipsFalse

    def debuff_hand(self, cards, hand, handname, check):
        if self.disabled:
            return False
        if self.debuff:
            self.triggered = False
            if self.debuff.hand & next(self.debuff.hand[hand]):
                self.triggered = True
                return True
            if self.debuff.h_size_ge & len(cards < self.debuff.h_size_ge):
                self.triggered = True
                return True
            if self.debuff.h_size_le & len(cards > self.debuff.h_size_le):
                self.triggered = True
                return True
            if self.name == 'The Eye':
                if self.loc_debuff_lines[1]:
                    self.triggered = True
                    return True
                if not check:
                    self.loc_debuff_lines[1] = True
            if self.name == 'The Mouth':
                if self.only_hand & (self.only_hand != handname):
                    self.triggered = True
                    return True
                if not check:
                    self.only_hand = handname
        if self.name == 'The Arm':
            self.triggered = False
            if self.loc_debuff_lines[1].level > 1:
                self.triggered = True
                if not check:level_up_hand()self.wiggle()
        if self.name == 'The Ox':
            self.triggered = False
            if handname == G.GAME.current_round.most_played_poker_hand:
                self.triggered = True
                if not check:ease_dollars()self.wiggle()

    def drawn_to_hand(self):
        if not self.disabled:
            if self.name == 'Cerulean Bell':
                any_forced = 'None'
                for kv in ipairs():
                    if v.ability.forced_selection:
                        any_forced = True
                if not any_forced:G.hand.unhighlight_all()
                    forced_card = pseudorandom_element()
                    forced_card.ability.forced_selection = TrueG.hand.add_to_highlighted(forced_card)
            if (self.name == self.loc_debuff_lines[1]:
                jokers = {}
                for i in range(1, len(G.jokers.cards), ):
                    if not self.loc_debuff_lines[1].debuff else len(G.jokers.cards < 2):
                        self.loc_debuff_lines[1].set_debuff(False)
                _card = pseudorandom_element(jokers)
                if _card:_card.set_debuff(True)_card.juice_up()self.wiggle()
        self.prepped = 'None'

    def stay_flipped(self, area, card):
        if not self.disabled:
            if area == G.hand:
                if (self.name == 'The Wheel') & pseudorandom() < G.GAME.probabilities.normal / 7:
                    return True
                if (self.name == 'The House') & (G.GAME.current_round.hands_played == 0) & (G.GAME.current_round.discards_used == 0):
                    return True
                if (self.name == 'The Mark') & card.is_face(True):
                    return True
                if (self.name == 'The Fish') & self.prepped:
                    return True

    def debuff_card(self, card, from_blind):
        if self.debuff & (not self.disabled) & (card.area != G.jokers):
            if self.debuff.suit & card.is_suit():card.set_debuff(True)
                return False
            if (self.debuff.is_face == 'face') & card.is_face(True):card.set_debuff(True)
                return False
            if (self.name == 'The Pillar') & card.ability.played_this_ante:card.set_debuff(True)
                return False
            if self.debuff.value & (self.debuff.value == card.base.value):card.set_debuff(True)
                return False
            if self.debuff.nominal & (self.debuff.nominal == card.base.nominal):card.set_debuff(True)
                return False
        if (self.name == 'Crimson Heart') & (not self.disabled) & (card.area == G.jokers):
            return False
        if (self.name == 'Verdant Leaf') & (not self.disabled) & (card.area != G.jokers):card.set_debuff(True)';'
            return Falsecard.set_debuff(False)

    def move(self, dt):
        super().move(self, dt)self.align()

    def change_dim(self, w, h):
        self.T.w = w if w else self.T.w
        self.T.h = h if h else self.T.h
        self.children.animatedSprite.T.w = w if w else self.T.w
        self.children.animatedSprite.T.h = h if h else self.T.hself.children.animatedSprite.rescale()

    def align(self):
        for kv in pairs():
            if k == 'animatedSprite':
                if not v.states.drag.is:
                    v.T.r = 0.02 * math.sin()
                    v.T.y = self.T.y + 0.03 * math.sin()
                    self.shadow_height = 0.1 - (0.04 + 0.03 * math.sin())
                    v.T.x = self.T.x + 0.03 * math.sin()
            else:
                v.T.x = self.T.x
                v.T.y = self.T.y
                v.T.r = self.T.r

    def save(self):
        blindTable = {'name': self.name, 'dollars': self.dollars, 'debuff': self.debuff, 'pos': self.pos, 'mult': self.mult, 'disabled': self.disabled, 'discards_sub': self.discards_sub, 'hands_sub': self.hands_sub, 'boss': self.boss, 'config_blind': '', 'chips': self.chips, 'chip_text': self.chip_text, 'hands': self.hands, 'only_hand': self.only_hand, 'triggered': self.triggered}
        for kv in pairs():
            if v & v.name & (v.name == blindTable.name):
                blindTable.config_blind = k
        return blindTable

    def load(self, blindTable):
        self.config.blind = self.loc_debuff_lines[1] else {}
        self.name = blindTable.name
        self.dollars = blindTable.dollars
        self.debuff = blindTable.debuff
        self.pos = blindTable.pos
        self.mult = blindTable.mult
        self.disabled = blindTable.disabled
        self.discards_sub = blindTable.discards_sub
        self.hands_sub = blindTable.hands_sub
        self.boss = blindTable.boss
        self.chips = blindTable.chips
        self.chip_text = blindTable.chip_text
        self.hands = blindTable.hands
        self.only_hand = blindTable.only_hand
        self.triggered = blindTable.triggered
        G.ARGS.spin.real = (G.SETTINGS.reduced_motion & 0 if G.SETTINGS.reduced_motion & 0 else 1) * (self.config.blind.boss & (self.config.blind.boss.showdown & 1 if self.config.blind.boss.showdown & 1 else 0.3) if self.config.blind.boss & (self.config.blind.boss.showdown & 1 if self.config.blind.boss.showdown & 1 else 0.3) else 0)
        if self.loc_debuff_lines[1]:
            self.blind_set = True
            self.children.animatedSprite.states.visible = Trueself.children.animatedSprite.set_sprite_pos()self.children.animatedSprite.juice_up(0.3)self.align()self.children.animatedSprite.hard_set_VT()
        else:
            self.children.animatedSprite.states.visible = False
        self.children.animatedSprite.states = self.statesself.change_colour()
        if self.dollars > 0:
            G.GAME.current_round.dollars_to_be_earned = string.rep() + ''G.HUD_blind.get_UIE_by_ID(dollars_to_be_earned).config.object.pop_in(0)
            G.HUD_blind.alignment.offset.y = 0self.set_text()