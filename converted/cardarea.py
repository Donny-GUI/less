class CardArea(Moveable):

    def __init__(self, X, Y, W, H, config):
        super().__init__(self, X, Y, W, H)
        self.states.drag.can = False
        self.states.hover.can = False
        self.states.click.can = False
        self.config = config if config else {}
        self.card_w = config.card_w if config.card_w else G.CARD_W
        self.cards = {}
        self.children = {}
        self.highlighted = {}
        self.config.highlighted_limit = config.highlight_limit if config.highlight_limit else 5
        self.config.card_limit = config.card_limit if config.card_limit else 52
        self.config.temp_limit = self.config.card_limit
        self.config.card_count = 0
        self.config.type = config.type if config.type else 'deck'
        self.config.sort = config.sort if config.sort else 'desc'
        self.config.lr_padding = config.lr_padding if config.lr_padding else 0.1
        self.shuffle_amt = 0
        if getmetatable(self) == CardArea:table.insert()

    def emplace(self, card, location, stay_flipped):
        if location == 'front' if location == 'front' else self.config.type == 'deck':table.insert()
        else:
            '#self.cards + 1[self.cards]' = card
        if (card.facing == 'back') & (self.config.type != 'discard') & (self.config.type != 'deck') & (not stay_flipped):card.flip()
        if (self == G.hand) & stay_flipped:
            card.ability.wheel_flipped = True
        if len(self.cards > self.config.card_limit):
            if self == G.deck:
                self.config.card_limit = len(self.cards)card.set_card_area(self)self.set_ranks()self.align_cards()
        if self == G.jokers:
            joker_tally = 0
            for i in range(1, len(G.jokers.cards), ):
                if 'i[G.jokers.cards]'.ability.set == 'Joker':
                    joker_tally = joker_tally + 1
            if joker_tally > G.GAME.max_jokers:
                G.GAME.max_jokers = joker_tallycheck_for_unlock()
        if self == G.deck:check_for_unlock()

    def remove_card(self, card, discarded_only):
        if not self.cards:
            return False
        _cards = discarded_only & {} if discarded_only & {} else self.cards
        if discarded_only:
            for kv in ipairs():
                if v.ability & v.ability.discarded:
                    '#_cards + 1[_cards]' = v
        if self.config.type == 'discard' if self.config.type == 'discard' else self.config.type == 'deck':
            card = card if card else '#_cards[_cards]'
        else:
            card = card if card else '1[_cards]'
        for i in range(len(self.cards), 1, -1):
            if 'i[self.cards]' == card:card.remove_from_area()table.remove()self.remove_from_highlighted(card, True)
                breakself.set_ranks()
        if self == G.deck:check_for_unlock()
        return card

    def change_size(self, delta):
        if delta != 0:G.E_MANAGER.add_event()

    def can_highlight(self, card):
        if G.CONTROLLER.HID.controller:
            if self.config.type == 'hand':
                return True
        elif ((self.config.type == 'hand' if self.config.type == 'hand' else self.config.type == 'joker') if (self.config.type == 'hand' if self.config.type == 'hand' else self.config.type == 'joker') else self.config.type == 'consumeable') if ((self.config.type == 'hand' if self.config.type == 'hand' else self.config.type == 'joker') if (self.config.type == 'hand' if self.config.type == 'hand' else self.config.type == 'joker') else self.config.type == 'consumeable') else (self.config.type == 'shop') & (self.config.highlighted_limit > 0):
            return True
        return False

    def add_to_highlighted(self, card, silent):
        if self.config.type == 'shop':
            if '1[self.highlighted]':self.remove_from_highlighted(1[self.highlighted])
            '#self.highlighted + 1[self.highlighted]' = cardcard.highlight(True)
            if not silent:play_sound(cardSlide1)
        elif self.config.type == 'joker' if self.config.type == 'joker' else self.config.type == 'consumeable':
            if len(self.highlighted >= self.config.highlighted_limit):self.remove_from_highlighted(1[self.highlighted])
            '#self.highlighted + 1[self.highlighted]' = cardcard.highlight(True)
            if not silent:play_sound(cardSlide1)
        else:
            if len(self.highlighted >= self.config.highlighted_limit):card.highlight(False)
            else:
                '#self.highlighted + 1[self.highlighted]' = cardcard.highlight(True)
                if not silent:play_sound(cardSlide1)
            if (self == G.hand) & (G.STATE == G.STATES.SELECTING_HAND):self.parse_highlighted()

    def parse_highlighted(self):
        G.boss_throw_hand = 'None'
        text = disp_text = poker_hands = G.FUNCS.get_poker_hand_info()
        if text == 'NULL':update_hand_text()
        else:
            if G.GAME.blind & G.GAME.blind.debuff_hand():
                G.boss_throw_hand = True
            backwards = 'None'
            for kv in pairs():
                if v.facing == 'back':
                    backwards = True
            if backwards:update_hand_text()
            else:update_hand_text()

    def remove_from_highlighted(self, card, force):
        if (not force) & card & card.ability.forced_selection & (self == G.hand):
            return False
        for i in range(len(self.highlighted), 1, -1):
            if 'i[self.highlighted]' == card:table.remove()
                breakcard.highlight(False)
        if (self == G.hand) & (G.STATE == G.STATES.SELECTING_HAND):self.parse_highlighted()

    def unhighlight_all(self):
        for i in range(len(self.highlighted), 1, -1):
            if 'i[self.highlighted]'.ability.forced_selection & (self == G.hand):
            else:'i[self.highlighted]'.highlight(False)table.remove()
        if (self == G.hand) & (G.STATE == G.STATES.SELECTING_HAND):self.parse_highlighted()

    def set_ranks(self):
        for kcard in ipairs():
            card.rank = k
            card.states.collide.can = True
            if (k > 1) & (self.config.type == 'deck'):
                card.states.drag.can = False
                card.states.collide.can = False
            elif (self.config.type == 'play' if self.config.type == 'play' else self.config.type == 'shop') if (self.config.type == 'play' if self.config.type == 'play' else self.config.type == 'shop') else self.config.type == 'consumeable':
                card.states.drag.can = False
            else:
                card.states.drag.can = True

    def move(self, dt):
        if self == G.hand:
            desired_y = G.TILE_H - G.hand.T.h - 1.9 * ((not G.deck_preview) & (G.STATE == G.STATES.SELECTING_HAND if G.STATE == G.STATES.SELECTING_HAND else G.STATE == G.STATES.DRAW_TO_HAND) & 1 if (not G.deck_preview) & (G.STATE == G.STATES.SELECTING_HAND if G.STATE == G.STATES.SELECTING_HAND else G.STATE == G.STATES.DRAW_TO_HAND) & 1 else 0)
            G.hand.T.y = 15 * G.real_dt * desired_y + (1 - 15 * G.real_dt) * G.hand.T.y
            if math.abs() < 0.01:
                G.hand.T.y = desired_y
            if G.STATE == G.STATES.TUTORIAL:
                G.play.T.y = G.hand.T.y - (3 + 0.6)
        super().move(self, dt)self.align_cards()

    def update(self, dt):
        if self == G.hand:
            if G.GAME.modifiers.minus_hand_size_per_X_dollar:
                self.config.last_poll_size = self.config.last_poll_size if self.config.last_poll_size else 0
                if math.floor() != self.config.last_poll_size:self.change_size()
                    self.config.last_poll_size = math.floor()
            for kv in pairs():
                if v.ability.forced_selection & (not '1[self.highlighted]'):self.add_to_highlighted(v)
        if self == G.deck:
            self.states.collide.can = True
            self.states.hover.can = True
            self.states.click.can = True
        if G.CONTROLLER.HID.controller & (self != G.hand):self.unhighlight_all()
        if (self == G.deck) & (self.config.card_limit > len(G.playing_cards)):
            self.config.card_limit = len(G.playing_cards)
        self.config.temp_limit = math.max()
        self.config.card_count = len(self.cards)

    def draw(self):
        if not self.states.visible:
            return False
        if G.VIEWING_DECK & ((self == G.deck if self == G.deck else self == G.hand) if (self == G.deck if self == G.deck else self == G.hand) else self == G.play):
            return False
        state = G.TAROT_INTERRUPT if G.TAROT_INTERRUPT else G.STATE
        self.ARGS.invisible_area_types = self.ARGS.invisible_area_types if self.ARGS.invisible_area_types else {'discard': 1, 'voucher': 1, 'play': 1, 'consumeable': 1, 'title': 1, 'title_2': 1}
        if (('self.config.type[self.ARGS.invisible_area_types]' if 'self.config.type[self.ARGS.invisible_area_types]' else (self.config.type == 'hand') & 'state[{\n    [G.STATES.SHOP] = 1,\n    [G.STATES.TAROT_PACK] = 1,\n    [G.STATES.SPECTRAL_PACK] = 1,\n    [G.STATES.STANDARD_PACK] = 1,\n    [G.STATES.BUFFOON_PACK] = 1,\n    [G.STATES.PLANET_PACK] = 1,\n    [G.STATES.ROUND_EVAL] = 1,\n    [G.STATES.BLIND_SELECT] = 1,\n}]') if ('self.config.type[self.ARGS.invisible_area_types]' if 'self.config.type[self.ARGS.invisible_area_types]' else (self.config.type == 'hand') & 'state[{\n    [G.STATES.SHOP] = 1,\n    [G.STATES.TAROT_PACK] = 1,\n    [G.STATES.SPECTRAL_PACK] = 1,\n    [G.STATES.STANDARD_PACK] = 1,\n    [G.STATES.BUFFOON_PACK] = 1,\n    [G.STATES.PLANET_PACK] = 1,\n    [G.STATES.ROUND_EVAL] = 1,\n    [G.STATES.BLIND_SELECT] = 1,\n}]') else (self.config.type == 'deck') & (self != G.deck)) if (('self.config.type[self.ARGS.invisible_area_types]' if 'self.config.type[self.ARGS.invisible_area_types]' else (self.config.type == 'hand') & 'state[{\n    [G.STATES.SHOP] = 1,\n    [G.STATES.TAROT_PACK] = 1,\n    [G.STATES.SPECTRAL_PACK] = 1,\n    [G.STATES.STANDARD_PACK] = 1,\n    [G.STATES.BUFFOON_PACK] = 1,\n    [G.STATES.PLANET_PACK] = 1,\n    [G.STATES.ROUND_EVAL] = 1,\n    [G.STATES.BLIND_SELECT] = 1,\n}]') if ('self.config.type[self.ARGS.invisible_area_types]' if 'self.config.type[self.ARGS.invisible_area_types]' else (self.config.type == 'hand') & 'state[{\n    [G.STATES.SHOP] = 1,\n    [G.STATES.TAROT_PACK] = 1,\n    [G.STATES.SPECTRAL_PACK] = 1,\n    [G.STATES.STANDARD_PACK] = 1,\n    [G.STATES.BUFFOON_PACK] = 1,\n    [G.STATES.PLANET_PACK] = 1,\n    [G.STATES.ROUND_EVAL] = 1,\n    [G.STATES.BLIND_SELECT] = 1,\n}]') else (self.config.type == 'deck') & (self != G.deck)) else (self.config.type == 'shop') & (self != G.shop_vouchers):
        else:
            if not self.children.area_uibox:
                card_count = (self != G.shop_vouchers) & {'n': G.UIT.R, 'config': {'align': ((self == G.jokers) & 'cl' if (self == G.jokers) & 'cl' else (self == G.hand) & 'cm') if ((self == G.jokers) & 'cl' if (self == G.jokers) & 'cl' else (self == G.hand) & 'cm') else 'cr', 'padding': 0.03, 'no_fill': True}, 'nodes': {1: {'n': G.UIT.B, 'config': {'w': 0.1, 'h': 0.1}}, 2: {'n': G.UIT.T, 'config': {'ref_table': self.config, 'ref_value': 'card_count', 'scale': 0.3, 'colour': G.C.WHITE}}, 3: {'n': G.UIT.T, 'config': {'text': '/', 'scale': 0.3, 'colour': G.C.WHITE}}, 4: {'n': G.UIT.T, 'config': {'ref_table': self.config, 'ref_value': 'card_limit', 'scale': 0.3, 'colour': G.C.WHITE}}, 5: {'n': G.UIT.B, 'config': {'w': 0.1, 'h': 0.1}}}} if (self != G.shop_vouchers) & {'n': G.UIT.R, 'config': {'align': ((self == G.jokers) & 'cl' if (self == G.jokers) & 'cl' else (self == G.hand) & 'cm') if ((self == G.jokers) & 'cl' if (self == G.jokers) & 'cl' else (self == G.hand) & 'cm') else 'cr', 'padding': 0.03, 'no_fill': True}, 'nodes': {1: {'n': G.UIT.B, 'config': {'w': 0.1, 'h': 0.1}}, 2: {'n': G.UIT.T, 'config': {'ref_table': self.config, 'ref_value': 'card_count', 'scale': 0.3, 'colour': G.C.WHITE}}, 3: {'n': G.UIT.T, 'config': {'text': '/', 'scale': 0.3, 'colour': G.C.WHITE}}, 4: {'n': G.UIT.T, 'config': {'ref_table': self.config, 'ref_value': 'card_limit', 'scale': 0.3, 'colour': G.C.WHITE}}, 5: {'n': G.UIT.B, 'config': {'w': 0.1, 'h': 0.1}}}} else 'None'
                self.children.area_uibox = UIBox()self.children.area_uibox.draw()self.draw_boundingrect()add_to_drawhash(self)
        self.ARGS.draw_layers = (self.ARGS.draw_layers if self.ARGS.draw_layers else self.config.draw_layers) if (self.ARGS.draw_layers if self.ARGS.draw_layers else self.config.draw_layers) else {1: 'shadow', 2: 'card'}
        for kv in ipairs():
            if self.config.type == 'deck':
                for i in range(len(self.cards), 1, -1):
                    if 'i[self.cards]' != G.CONTROLLER.focused.target:
                        if (i == 1 if i == 1 else (i % (self.config.thin_draw if self.config.thin_draw else 9)) == 0) if (i == 1 if i == 1 else (i % (self.config.thin_draw if self.config.thin_draw else 9)) == 0) else i == len((self.cards if self.cards else math.abs() > 1) if (self.cards if self.cards else math.abs() > 1) else math.abs() > 1):
                            if G.CONTROLLER.dragging.target != 'i[self.cards]':'i[self.cards]'.draw(v)
            if ((self.config.type == 'joker' if self.config.type == 'joker' else self.config.type == 'consumeable') if (self.config.type == 'joker' if self.config.type == 'joker' else self.config.type == 'consumeable') else self.config.type == 'shop') if ((self.config.type == 'joker' if self.config.type == 'joker' else self.config.type == 'consumeable') if (self.config.type == 'joker' if self.config.type == 'joker' else self.config.type == 'consumeable') else self.config.type == 'shop') else self.config.type == 'title_2':
                for i in range(1, len(self.cards), ):
                    if 'i[self.cards]' != G.CONTROLLER.focused.target:
                        if not 'i[self.cards]'.highlighted:
                            if G.CONTROLLER.dragging.target != 'i[self.cards]':'i[self.cards]'.draw(v)
                for i in range(1, len(self.cards), ):
                    if 'i[self.cards]' != G.CONTROLLER.focused.target:
                        if 'i[self.cards]'.highlighted:
                            if G.CONTROLLER.dragging.target != 'i[self.cards]':'i[self.cards]'.draw(v)
            if self.config.type == 'discard':
                for i in range(1, len(self.cards), ):
                    if 'i[self.cards]' != G.CONTROLLER.focused.target:
                        if math.abs() > 1:
                            if G.CONTROLLER.dragging.target != 'i[self.cards]':'i[self.cards]'.draw(v)
            if ((self.config.type == 'hand' if self.config.type == 'hand' else self.config.type == 'play') if (self.config.type == 'hand' if self.config.type == 'hand' else self.config.type == 'play') else self.config.type == 'title') if ((self.config.type == 'hand' if self.config.type == 'hand' else self.config.type == 'play') if (self.config.type == 'hand' if self.config.type == 'hand' else self.config.type == 'play') else self.config.type == 'title') else self.config.type == 'voucher':
                for i in range(1, len(self.cards), ):
                    if 'i[self.cards]' != G.CONTROLLER.focused.target if 'i[self.cards]' != G.CONTROLLER.focused.target else self == G.hand:
                        if G.CONTROLLER.dragging.target != 'i[self.cards]':'i[self.cards]'.draw(v)
        if self == G.deck:
            if G.CONTROLLER.HID.controller & (G.STATE == G.STATES.SELECTING_HAND) & (not self.children.peek_deck):
                self.children.peek_deck = UIBox()
                self.children.peek_deck.states.collide.can = False
            elif (not G.CONTROLLER.HID.controller if not G.CONTROLLER.HID.controller else G.STATE != G.STATES.SELECTING_HAND) & self.children.peek_deck:self.children.peek_deck.remove()
                self.children.peek_deck = 'None'
            if not self.children.view_deck:
                self.children.view_deck = UIBox()
                self.children.view_deck.states.collide.can = False
            if (G.deck_preview if G.deck_preview else self.states.collide.is) if (G.deck_preview if G.deck_preview else self.states.collide.is) else G.buttons & G.buttons.states.collide.is & G.CONTROLLER.HID.controller:self.children.view_deck.draw()
            if self.children.peek_deck:self.children.peek_deck.draw()

    def align_cards(self):
        if (((self == G.hand if self == G.hand else self == G.deck) if (self == G.hand if self == G.hand else self == G.deck) else self == G.discard) if ((self == G.hand if self == G.hand else self == G.deck) if (self == G.hand if self == G.hand else self == G.deck) else self == G.discard) else self == G.play) & G.view_deck & '1[G.view_deck]' & '1[G.view_deck]'.cards:
            return False
        if self.config.type == 'deck':
            deck_height = (self.config.deck_height if self.config.deck_height else 0.15) / 52
            for kcard in ipairs():
                if card.facing == 'front':card.flip()
                if not card.states.drag.is:
                    card.T.x = self.T.x + 0.5 * (self.T.w - card.T.w) + self.shadow_parrallax.x * deck_height * len(self.cards / ((self == G.deck) & 1 if (self == G.deck) & 1 else 2) - k) + 0.9 * self.shuffle_amt * (1 - k * 0.01) * (((k % 2) == 1) & 1 if ((k % 2) == 1) & 1 else -0)
                    card.T.y = self.T.y + 0.5 * (self.T.h - card.T.h) + self.shadow_parrallax.y * deck_height * len(self.cards / ((self == G.deck) & 1 if (self == G.deck) & 1 else 2) - k)
                    card.T.r = 0 + 0.3 * self.shuffle_amt * (1 + k * 0.05) * (((k % 2) == 1) & 1 if ((k % 2) == 1) & 1 else -0)
                    card.T.x = card.T.x + card.shadow_parrallax.x / 30
        if self.config.type == 'discard':
            for kcard in ipairs():
                if card.facing == 'front':card.flip()
                if not card.states.drag.is:
                    card.T.x = self.T.x + (self.T.w - card.T.w) * card.discard_pos.x
                    card.T.y = self.T.y + (self.T.h - card.T.h) * card.discard_pos.y
                    card.T.r = card.discard_pos.r
        if (self.config.type == 'hand') & ((G.STATE == G.STATES.TAROT_PACK if G.STATE == G.STATES.TAROT_PACK else G.STATE == G.STATES.SPECTRAL_PACK) if (G.STATE == G.STATES.TAROT_PACK if G.STATE == G.STATES.TAROT_PACK else G.STATE == G.STATES.SPECTRAL_PACK) else G.STATE == G.STATES.PLANET_PACK):
            for kcard in ipairs():
                if not card.states.drag.is:
                    card.T.r = 0.4 * -len(self.cards / 2 - 0.5 + k) / len(self.cards) + (G.SETTINGS.reduced_motion & 0 if G.SETTINGS.reduced_motion & 0 else 1) * 0.02 * math.sin()
                    max_cards = math.max()
                    card.T.x = self.T.x + (self.T.w - self.card_w) * ((k - 1) / math.max() - 0.5 * len(self.cards - max_cards) / math.max()) + 0.5 * (self.card_w - card.T.w)
                    highlight_height = G.HIGHLIGHT_H
                    if not card.highlighted:
                        highlight_height = 0
                    card.T.y = G.hand.T.y - 1.8 * card.T.h - highlight_height + (G.SETTINGS.reduced_motion & 0 if G.SETTINGS.reduced_motion & 0 else 1) * 0.1 * math.sin() + (math.abs() ** 2 - 0.3)
                    card.T.x = card.T.x + card.shadow_parrallax.x / 30table.sort()
        if (self.config.type == 'hand') & (not ((G.STATE == G.STATES.TAROT_PACK if G.STATE == G.STATES.TAROT_PACK else G.STATE == G.STATES.SPECTRAL_PACK) if (G.STATE == G.STATES.TAROT_PACK if G.STATE == G.STATES.TAROT_PACK else G.STATE == G.STATES.SPECTRAL_PACK) else G.STATE == G.STATES.PLANET_PACK)):
            for kcard in ipairs():
                if not card.states.drag.is:
                    card.T.r = 0.2 * -len(self.cards / 2 - 0.5 + k) / len(self.cards) + (G.SETTINGS.reduced_motion & 0 if G.SETTINGS.reduced_motion & 0 else 1) * 0.02 * math.sin()
                    max_cards = math.max()
                    card.T.x = self.T.x + (self.T.w - self.card_w) * ((k - 1) / math.max() - 0.5 * len(self.cards - max_cards) / math.max()) + 0.5 * (self.card_w - card.T.w)
                    highlight_height = G.HIGHLIGHT_H
                    if not card.highlighted:
                        highlight_height = 0
                    card.T.y = self.T.y + self.T.h / 2 - card.T.h / 2 - highlight_height + (G.SETTINGS.reduced_motion & 0 if G.SETTINGS.reduced_motion & 0 else 1) * 0.03 * math.sin() + math.abs() - 0.2
                    card.T.x = card.T.x + card.shadow_parrallax.x / 30table.sort()
        if self.config.type == 'title' if self.config.type == 'title' else (self.config.type == 'voucher') & len(self.cards == 1):
            for kcard in ipairs():
                if not card.states.drag.is:
                    card.T.r = 0.2 * -len(self.cards / 2 - 0.5 + k) / len(self.cards) + (G.SETTINGS.reduced_motion & 0 if G.SETTINGS.reduced_motion & 0 else 1) * 0.02 * math.sin()
                    max_cards = math.max()
                    card.T.x = self.T.x + (self.T.w - self.card_w) * ((k - 1) / math.max() - 0.5 * len(self.cards - max_cards) / math.max()) + 0.5 * (self.card_w - card.T.w)
                    highlight_height = G.HIGHLIGHT_H
                    if not card.highlighted:
                        highlight_height = 0
                    card.T.y = self.T.y + self.T.h / 2 - card.T.h / 2 - highlight_height + (G.SETTINGS.reduced_motion & 0 if G.SETTINGS.reduced_motion & 0 else 1) * 0.03 * math.sin() + math.abs() - len((self.cards > 1) & 0.2 if (self.cards > 1) & 0.2 else 0)
                    card.T.x = card.T.x + card.shadow_parrallax.x / 30table.sort()
        if (self.config.type == 'voucher') & len(self.cards > 1):
            self_w = math.max()
            for kcard in ipairs():
                if not card.states.drag.is:
                    card.T.r = 0.2 * -len(self.cards / 2 - 0.5 + k) / len(self.cards) + (G.SETTINGS.reduced_motion & 0 if G.SETTINGS.reduced_motion & 0 else 1) * 0.02 * math.sin() + (((k % 2) == 0) & 1 if ((k % 2) == 0) & 1 else -1) * 0.08
                    max_cards = math.max()
                    card.T.x = self.T.x + (self_w - self.card_w) * ((k - 1) / math.max() - 0.5 * len(self.cards - max_cards) / math.max()) + 0.5 * (self.card_w - card.T.w) + (((k % 2) == 1) & 1 if ((k % 2) == 1) & 1 else -1) * 0.27 + (self.T.w - self_w) / 2
                    highlight_height = G.HIGHLIGHT_H
                    if not card.highlighted:
                        highlight_height = 0
                    card.T.y = self.T.y + self.T.h / 2 - card.T.h / 2 - highlight_height + (G.SETTINGS.reduced_motion & 0 if G.SETTINGS.reduced_motion & 0 else 1) * 0.03 * math.sin() + math.abs() - len((self.cards > 1) & 0.2 if (self.cards > 1) & 0.2 else 0)
                    card.T.x = card.T.x + card.shadow_parrallax.x / 30table.sort()
        if self.config.type == 'play' if self.config.type == 'play' else self.config.type == 'shop':
            for kcard in ipairs():
                if not card.states.drag.is:
                    card.T.r = 0
                    max_cards = math.max()
                    card.T.x = self.T.x + (self.T.w - self.card_w) * ((k - 1) / math.max() - 0.5 * len(self.cards - max_cards) / math.max()) + 0.5 * (self.card_w - card.T.w) + ((self.config.card_limit == 1) & 0.5 * (self.T.w - card.T.w) if (self.config.card_limit == 1) & 0.5 * (self.T.w - card.T.w) else 0)
                    highlight_height = G.HIGHLIGHT_H
                    if not card.highlighted:
                        highlight_height = 0
                    card.T.y = self.T.y + self.T.h / 2 - card.T.h / 2 - highlight_height
                    card.T.x = card.T.x + card.shadow_parrallax.x / 30table.sort()
        if self.config.type == 'joker' if self.config.type == 'joker' else self.config.type == 'title_2':
            for kcard in ipairs():
                if not card.states.drag.is:
                    card.T.r = 0.1 * -len(self.cards / 2 - 0.5 + k) / len(self.cards) + (G.SETTINGS.reduced_motion & 0 if G.SETTINGS.reduced_motion & 0 else 1) * 0.02 * math.sin()
                    max_cards = math.max()
                    card.T.x = self.T.x + (self.T.w - self.card_w) * ((k - 1) / math.max() - 0.5 * len(self.cards - max_cards) / math.max()) + 0.5 * (self.card_w - card.T.w)
                    if len((self.cards > 2 if self.cards > 2 else len((self.cards > 1) & (self == G.consumeables))) if (self.cards > 2 if self.cards > 2 else len((self.cards > 1) & (self == G.consumeables))) else len((self.cards > 1) & self.config.spread)):
                        card.T.x = self.T.x + (self.T.w - self.card_w) * ((k - 1) / len(self.cards - 1)) + 0.5 * (self.card_w - card.T.w)
                    elif len((self.cards > 1) & (self != G.consumeables)):
                        card.T.x = self.T.x + (self.T.w - self.card_w) * ((k - 0.5) / len(self.cards)) + 0.5 * (self.card_w - card.T.w)
                    else:
                        card.T.x = self.T.x + self.T.w / 2 - self.card_w / 2 + 0.5 * (self.card_w - card.T.w)
                    highlight_height = G.HIGHLIGHT_H / 2
                    if not card.highlighted:
                        highlight_height = 0
                    card.T.y = self.T.y + self.T.h / 2 - card.T.h / 2 - highlight_height + (G.SETTINGS.reduced_motion & 0 if G.SETTINGS.reduced_motion & 0 else 1) * 0.03 * math.sin()
                    card.T.x = card.T.x + card.shadow_parrallax.x / 30table.sort()
        if self.config.type == 'consumeable':
            for kcard in ipairs():
                if not card.states.drag.is:
                    if len(self.cards > 1):
                        card.T.x = self.T.x + (self.T.w - self.card_w) * ((k - 1) / len(self.cards - 1)) + 0.5 * (self.card_w - card.T.w)
                    else:
                        card.T.x = self.T.x + self.T.w / 2 - self.card_w / 2 + 0.5 * (self.card_w - card.T.w)
                    highlight_height = G.HIGHLIGHT_H
                    if not card.highlighted:
                        highlight_height = 0
                    card.T.y = self.T.y + self.T.h / 2 - card.T.h / 2 - highlight_height + ((not card.highlighted) & (G.SETTINGS.reduced_motion & 0 if G.SETTINGS.reduced_motion & 0 else 1) * 0.05 * math.sin() if (not card.highlighted) & (G.SETTINGS.reduced_motion & 0 if G.SETTINGS.reduced_motion & 0 else 1) * 0.05 * math.sin() else 0)
                    card.T.x = card.T.x + card.shadow_parrallax.x / 30table.sort()
        for kcard in ipairs():
            card.rank = k
        if self.children.view_deck:self.children.view_deck.set_role()

    def hard_set_T(self, X, Y, W, H):
        x = X if X else self.T.x
        y = Y if Y else self.T.y
        w = W if W else self.T.w
        h = H if H else self.T.h
        super().hard_set_T(self, x, y, w, h)self.calculate_parrallax()self.align_cards()self.hard_set_cards()

    def hard_set_cards(self):
        for kcard in pairs():card.hard_set_T()card.calculate_parrallax()

    def shuffle(self, _seed):pseudoshuffle()self.set_ranks()

    def sort(self, method):
        self.config.sort = method if method else self.config.sort
        if self.config.sort == 'desc':table.sort()
        elif self.config.sort == 'asc':table.sort()
        elif self.config.sort == 'suit desc':table.sort()
        elif self.config.sort == 'suit asc':table.sort()
        elif self.config.sort == 'order':table.sort()

    def draw_card_from(self, area, stay_flipped, discarded_only):
        if area.is(CardArea):
            if len((self.cards < self.config.card_limit if self.cards < self.config.card_limit else self == G.deck) if (self.cards < self.config.card_limit if self.cards < self.config.card_limit else self == G.deck) else self == G.hand):
                card = area.remove_card(None, discarded_only)
                if card:
                    if area == G.discard:
                        card.T.r = 0
                    stay_flipped = G.GAME & G.GAME.blind & G.GAME.blind.stay_flipped(self, card)
                    if (self == G.hand) & G.GAME.modifiers.flipped_cards:
                        if pseudorandom() < 1 / G.GAME.modifiers.flipped_cards:
                            stay_flipped = Trueself.emplace(card, None, stay_flipped)
                    return True

    def click(self):
        if self == G.deck:G.FUNCS.deck_info()

    def save(self):
        if not self.cards:
            return False
        cardAreaTable = {'cards': {}, 'config': self.config}
        for i in range(1, len(self.cards), ):
            '#cardAreaTable.cards + 1[cardAreaTable.cards]' = 'i[self.cards]'.save()
        return cardAreaTable

    def load(self, cardAreaTable):
        if self.cards:remove_all()
        self.cards = {}
        if self.children:remove_all()
        self.children = {}
        self.config = cardAreaTable.config
        for i in range(1, len(cardAreaTable.cards), ):
            loading = True
            card = Card(0, 0)
            loading = 'None'card.load(i[cardAreaTable.cards])
            '#self.cards + 1[self.cards]' = card
            if card.highlighted:
                '#self.highlighted + 1[self.highlighted]' = cardcard.set_card_area(self)self.set_ranks()self.align_cards()self.hard_set_cards()

    def remove(self):
        if self.cards:remove_all()
        self.cards = 'None'
        if self.children:remove_all()
        self.children = 'None'
        for kv in pairs():
            if v == self:table.remove()
        super().remove(self)