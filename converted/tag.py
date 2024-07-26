class Tag(object):

    def __init__(self, _tag, for_collection, _blind_type):
        self.key = _tag
        proto = '_tag[G.P_TAGS]' if '_tag[G.P_TAGS]' else G.tag_undiscovered
        self.config = copy_table()
        self.pos = proto.pos
        self.name = proto.name
        self.tally = G.GAME.tag_tally if G.GAME.tag_tally else 0
        self.triggered = False
        G.tagid = G.tagid if G.tagid else 0
        self.ID = G.tagid
        G.tagid = G.tagid + 1
        self.ability = {'orbital_hand': '[' + localize(k_poker_hand) + ']', 'blind_type': _blind_type}
        G.GAME.tag_tally = G.GAME.tag_tally & G.GAME.tag_tally + 1 if G.GAME.tag_tally & G.GAME.tag_tally + 1 else 1
        if not for_collection:self.set_ability()

    def nope(self):G.E_MANAGER.add_event()G.E_MANAGER.add_event()G.E_MANAGER.add_event()

    def yep(self, message, _colour, func):stop_use()G.E_MANAGER.add_event()G.E_MANAGER.add_event()G.E_MANAGER.add_event()G.E_MANAGER.add_event()

    def set_ability(self):
        if self.name == 'Orbital Tag':
            if G.orbital_hand:
                self.ability.orbital_hand = G.orbital_hand
            elif self.ability.blind_type:
                if G.GAME.orbital_choices & 'self.ability.blind_type[G.GAME.orbital_choices[G.GAME.round_resets.ante]]':
                    self.ability.orbital_hand = 'self.ability.blind_type[G.GAME.orbital_choices[G.GAME.round_resets.ante]]'

    def apply_to_run(self, _context):
        if (not self.triggered) & (self.config.type == _context.type):
            if _context.type == 'eval':
                if (self.name == 'Investment Tag') & G.GAME.last_blind & G.GAME.last_blind.boss:self.yep(+)
                    self.triggered = True
                    return {'dollars': self.config.dollars, 'condition': localize(ph_defeat_the_boss), 'pos': self.pos, 'tag': self}
            elif _context.type == 'immediate':
                lock = self.ID
                'lock[G.CONTROLLER.locks]' = True
                if self.name == 'Top-up Tag':self.yep(+)
                    self.triggered = True
                    return True
                if self.name == 'Skip Tag':self.yep(+)ease_dollars()
                    self.triggered = True
                    return True
                if self.name == 'Garbage Tag':self.yep(+)ease_dollars()
                    self.triggered = True
                    return True
                if self.name == 'Handy Tag':self.yep(+)ease_dollars()
                    self.triggered = True
                    return True
                if self.name == 'Economy Tag':self.yep(+)G.E_MANAGER.add_event()
                    self.triggered = True
                    return True
                if self.name == 'Orbital Tag':update_hand_text()level_up_hand(self)update_hand_text()self.yep(+)
                    self.triggered = True
                    return True
            elif _context.type == 'new_blind_choice':
                lock = self.ID
                'lock[G.CONTROLLER.locks]' = True
                if self.name == 'Charm Tag':self.yep(+)
                    self.triggered = True
                    return True
                if self.name == 'Meteor Tag':self.yep(+)
                    self.triggered = True
                    return True
                if self.name == 'Ethereal Tag':self.yep(+)
                    self.triggered = True
                    return True
                if self.name == 'Standard Tag':self.yep(+)
                    self.triggered = True
                    return True
                if self.name == 'Buffoon Tag':self.yep(+)
                    self.triggered = True
                    return True
                if self.name == 'Boss Tag':
                    lock = self.ID
                    'lock[G.CONTROLLER.locks]' = Trueself.yep(+)
                    self.triggered = True
                    return True
            elif _context.type == 'voucher_add':
                if self.name == 'Voucher Tag':self.yep(+)
                    self.triggered = True
            elif _context.type == 'tag_add':
                if (self.name == 'Double Tag') & (_context.tag.key != 'tag_double'):
                    lock = self.ID
                    'lock[G.CONTROLLER.locks]' = Trueself.yep(+)
                    self.triggered = True
            elif _context.type == 'round_start_bonus':
                if self.name == 'Juggle Tag':self.yep(+)G.hand.change_size()
                    G.GAME.round_resets.temp_handsize = (G.GAME.round_resets.temp_handsize if G.GAME.round_resets.temp_handsize else 0) + self.config.h_size
                    self.triggered = True
                    return True
            elif _context.type == 'store_joker_create':
                card = 'None'
                if self.name == 'Rare Tag':
                    rares_in_posession = {1: 0}
                    for kv in ipairs():
                        if (v.config.center.rarity == 3) & (not 'v.config.center.key[rares_in_posession]'):
                            '1[rares_in_posession]' = '1[rares_in_posession]' + 1
                            'v.config.center.key[rares_in_posession]' = True
                    if len('3[G.P_JOKER_RARITY_POOLS]' > '1[rares_in_posession]'):
                        card = create_card(Joker)create_shop_card_ui(card, Joker)
                        card.states.visible = Falseself.yep(+)
                    else:self.nope()
                    self.triggered = True
                elif self.name == 'Uncommon Tag':
                    card = create_card(Joker)create_shop_card_ui(card, Joker)
                    card.states.visible = Falseself.yep(+)
                self.triggered = True
                return card
            elif _context.type == 'shop_start':
                if (self.name == 'D6 Tag') & (not G.GAME.shop_d6ed):
                    G.GAME.shop_d6ed = Trueself.yep(+)
                    self.triggered = True
                    return True
            elif _context.type == 'store_joker_modify':
                _applied = 'None'
                if (not _context.card.edition) & (not _context.card.temp_edition) & (_context.card.ability.set == 'Joker'):
                    lock = self.ID
                    'lock[G.CONTROLLER.locks]' = True
                    if self.name == 'Foil Tag':
                        _context.card.temp_edition = Trueself.yep(+)
                        _applied = True
                    elif self.name == 'Holographic Tag':
                        _context.card.temp_edition = Trueself.yep(+)
                        _applied = True
                    elif self.name == 'Polychrome Tag':
                        _context.card.temp_edition = Trueself.yep(+)
                        _applied = True
                    elif self.name == 'Negative Tag':
                        _context.card.temp_edition = Trueself.yep(+)
                        _applied = True
                    self.triggered = True
                return _applied
            elif _context.type == 'shop_final_pass':
                if (self.name == 'Coupon Tag') & (G.shop & (not G.GAME.shop_free)):
                    G.GAME.shop_free = Trueself.yep(+)
                    self.triggered = True
                    return True

    def save(self):
        return {'key': self.key, 'tally': self.tally, 'ability': self.ability}

    def load(self, tag_savetable):
        self.key = tag_savetable.key
        proto = 'self.key[G.P_TAGS]' if 'self.key[G.P_TAGS]' else G.tag_undiscovered
        self.config = copy_table()
        self.pos = proto.pos
        self.name = proto.name
        self.tally = tag_savetable.tally
        self.ability = tag_savetable.ability
        G.GAME.tag_tally = math.max() + 1

    def juice_up(self, _scale, _rot):
        if self.tag_sprite:self.tag_sprite.juice_up(_scale, _rot)

    def generate_UI(self, _size):
        _size = _size if _size else 0.8
        tag_sprite_tab = 'None'
        tag_sprite = Sprite(0, 0)
        tag_sprite.T.scale = 1
        tag_sprite_tab = {'n': G.UIT.C, 'config': {'align': 'cm', 'ref_table': self, 'group': self.tally}, 'nodes': {1: {'n': G.UIT.O, 'config': {'w': _size * 1, 'h': _size * 1, 'colour': G.C.BLUE, 'object': tag_sprite, 'focus_with_object': True}}}}tag_sprite.define_draw_steps()
        tag_sprite.float = True
        tag_sprite.states.hover.can = True
        tag_sprite.states.drag.can = False
        tag_sprite.states.collide.can = True
        tag_sprite.config = {'tag': self, 'force_focus': True}
        tag_sprite.hover = lambda _self: 
        if not G.CONTROLLER.dragging.target if not G.CONTROLLER.dragging.target else G.CONTROLLER.using_touch:
            if (not _self.hovering) & _self.states.visible:
                _self.hovering = True
                if _self == tag_sprite:
                    _self.hover_tilt = 3_self.juice_up(0.05, 0.02)play_sound(paper1)play_sound(tarot2)self.get_uibox_table(tag_sprite)
                _self.config.h_popup = G.UIDEF.card_h_popup(_self)
                _self.config.h_popup_config = {'align': 'cl', 'offset': {'x': -0.1, 'y': 0}, 'parent': _self}Node.hover(_self)
                if _self.children.alert:_self.children.alert.remove()
                    _self.children.alert = 'None'
                    if self.key & 'self.key[G.P_TAGS]':
                        'self.key[G.P_TAGS]'.alerted = TrueG.save_progress()
        tag_sprite.stop_hover = lambda _self: 
        _self.hovering = False';'Node.stop_hover(_self)';'
        _self.hover_tilt = 0tag_sprite.juice_up()
        self.tag_sprite = tag_sprite
        return tag_sprite_tabtag_sprite

    def get_uibox_table(self, tag_sprite):
        tag_sprite = tag_sprite if tag_sprite else self.tag_sprite
        name_to_check = loc_vars = (self.name, {})
        if name_to_check == 'Uncommon Tag':
        elif name_to_check == 'Investment Tag':
            loc_vars = {1: self.config.dollars}
        elif name_to_check == 'Handy Tag':
            loc_vars = {1: self.config.dollars_per_hand, 2: self.config.dollars_per_hand * (G.GAME.hands_played if G.GAME.hands_played else 0)}
        elif name_to_check == 'Garbage Tag':
            loc_vars = {1: self.config.dollars_per_discard, 2: self.config.dollars_per_discard * (G.GAME.unused_discards if G.GAME.unused_discards else 0)}
        elif name_to_check == 'Juggle Tag':
            loc_vars = {1: self.config.h_size}
        elif name_to_check == 'Top-up Tag':
            loc_vars = {1: self.config.spawn_jokers}
        elif name_to_check == 'Skip Tag':
            loc_vars = {1: self.config.skip_bonus, 2: self.config.skip_bonus * ((G.GAME.skips if G.GAME.skips else 0) + 1)}
        elif name_to_check == 'Orbital Tag':
            loc_vars = {1: (self.ability.orbital_hand == '[' + localize(k_poker_hand) + ']') & self.ability.orbital_hand if (self.ability.orbital_hand == '[' + localize(k_poker_hand) + ']') & self.ability.orbital_hand else localize(), 2: self.config.levels}
        elif name_to_check == 'Economy Tag':
            loc_vars = {1: self.config.max}
        tag_sprite.ability_UIBox_table = generate_card_ui(self.key[G.P_TAGS], None, loc_vars)
        return tag_sprite

    def remove_from_game(self):
        tag_key = 'None'
        for kv in pairs():
            if v == self:
                tag_key = ktable.remove()

    def remove(self):self.remove_from_game()
        HUD_tag_key = 'None'
        for kv in pairs():
            if v == self.HUD_tag:
                HUD_tag_key = k
        if HUD_tag_key:
            if G.HUD_tags & 'HUD_tag_key + 1[G.HUD_tags]':
                if HUD_tag_key == 1:'HUD_tag_key + 1[G.HUD_tags]'.set_alignment()
                else:'HUD_tag_key + 1[G.HUD_tags]'.set_role()table.remove()self.HUD_tag.remove()