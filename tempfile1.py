class Back(object):

    def __init__(self, selected_back):
        if not selected_back:
            selected_back = G.P_CENTERS.b_red
        self.name = selected_back.name if selected_back.name else 'Red Deck'
        self.effect = {'center': selected_back, 'text_UI': '', 'config': copy_table()}
        self.loc_name = localize()
        pos = self.effect.center.unlocked & self.effect.center.pos if self.effect.center.unlocked & self.effect.center.pos else {'x': 4, 'y': 0}
        self.pos = self.pos if self.pos else {}
        self.pos.x = pos.x
        self.pos.y = pos.y

    def get_name(self):
        if self.effect.center.unlocked:
            return self.loc_name
        else:
            return localize(k_locked)

    def generate_UI(self, other, ui_scale, min_dims, challenge):
        min_dims = min_dims if min_dims else 0.7
        ui_scale = ui_scale if ui_scale else 0.9
        back_config = other if other else self.effect.center
        name_to_check = other & other.name if other & other.name else self.name
        effect_config = other & other.config if other & other.config else self.effect.config
        challenge = "get_challenge_int_from_id(challenge or '') or ''[G.CHALLENGES]" if "get_challenge_int_from_id(challenge or '') or ''[G.CHALLENGES]" else {'name': 'ERROR'}
        loc_args = loc_nodes = ('None', {})
        if not back_config.unlocked:
            if not back_config.unlock_condition:localize()
            elif back_config.unlock_condition.type == 'win_deck':
                other_name = localize(k_unknown)
                if 'back_config.unlock_condition.deck[G.P_CENTERS]'.unlocked:
                    other_name = localize()
                loc_args = {1: other_name}localize()
            elif back_config.unlock_condition.type == 'discover_amount':
                loc_args = {1: tostring()}localize()
            elif back_config.unlock_condition.type == 'win_stake':
                other_name = localize()
                loc_args = {1: other_name, 'colours': {1: get_stake_col()}}localize()
        else:
            if name_to_check == 'Blue Deck':
                loc_args = {1: effect_config.hands}
            elif name_to_check == 'Red Deck':
                loc_args = {1: effect_config.discards}
            elif name_to_check == 'Yellow Deck':
                loc_args = {1: effect_config.dollars}
            elif name_to_check == 'Green Deck':
                loc_args = {1: effect_config.extra_hand_bonus, 2: effect_config.extra_discard_bonus}
            elif name_to_check == 'Black Deck':
                loc_args = {1: effect_config.joker_slot, 2: -effect_config.hands}
            elif name_to_check == 'Magic Deck':
                loc_args = {1: localize(), 2: localize()}
            elif name_to_check == 'Nebula Deck':
                loc_args = {1: localize(), 2: -1}
            elif name_to_check == 'Ghost Deck':
            elif name_to_check == 'Abandoned Deck':
            elif name_to_check == 'Checkered Deck':
            elif name_to_check == 'Zodiac Deck':
                loc_args = {1: localize(), 2: localize(), 3: localize()}
            elif name_to_check == 'Painted Deck':
                loc_args = {1: effect_config.hand_size, 2: effect_config.joker_slot}
            elif name_to_check == 'Anaglyph Deck':
                loc_args = {1: localize()}
            elif name_to_check == 'Plasma Deck':
                loc_args = {1: effect_config.ante_scaling}
            elif name_to_check == 'Erratic Deck':localize()
        return {'n': G.UIT.ROOT, 'config': {'align': 'cm', 'minw': min_dims * 5, 'minh': min_dims * 2.5, 'id': self.name, 'colour': G.C.CLEAR}, 'nodes': {1: (name_to_check == 'Challenge Deck') & UIBox_button() if (name_to_check == 'Challenge Deck') & UIBox_button() else desc_from_rows(loc_nodes, True)}}

    def change_to(self, new_back):
        if not new_back:
            new_back = G.P_CENTERS.b_red
        self.name = new_back.name if new_back.name else 'Red Deck'
        self.effect = {'center': new_back, 'text_UI': '', 'config': copy_table()}
        self.loc_name = localize()
        pos = self.effect.center.unlocked & copy_table() if self.effect.center.unlocked & copy_table() else {'x': 4, 'y': 0}
        self.pos.x = pos.x
        self.pos.y = pos.y

    def save(self):
        backTable = {'name': self.name, 'pos': self.pos, 'effect': self.effect, 'key': self.effect.center.key if self.effect.center.key else 'b_red'}
        return backTable

    def trigger_effect(self, args):
        if not args:
            return False
        if (self.name == 'Anaglyph Deck') & (args.context == 'eval') & G.GAME.last_blind & G.GAME.last_blind.boss:G.E_MANAGER.add_event()
        if (self.name == 'Plasma Deck') & (args.context == 'blind_amount'):
            return False
        if (self.name == 'Plasma Deck') & (args.context == 'final_scoring_step'):
            tot = args.chips + args.mult
            args.chips = math.floor()
            args.mult = math.floor()update_hand_text()G.E_MANAGER.add_event()delay(0.6)
            return args.chipsargs.mult

    def apply_to_run(self):
        if self.effect.config.voucher:
            'self.effect.config.voucher[G.GAME.used_vouchers]' = True
            G.GAME.starting_voucher_count = (G.GAME.starting_voucher_count if G.GAME.starting_voucher_count else 0) + 1Card.apply_to_run(None, self.effect.config.voucher[G.P_CENTERS])
        if self.effect.config.hands:
            G.GAME.starting_params.hands = G.GAME.starting_params.hands + self.effect.config.hands
        if self.effect.config.consumables:delay(0.4)G.E_MANAGER.add_event()
        if self.effect.config.dollars:
            G.GAME.starting_params.dollars = G.GAME.starting_params.dollars + self.effect.config.dollars
        if self.effect.config.remove_faces:
            G.GAME.starting_params.no_faces = True
        if self.effect.config.spectral_rate:
            G.GAME.spectral_rate = self.effect.config.spectral_rate
        if self.effect.config.discards:
            G.GAME.starting_params.discards = G.GAME.starting_params.discards + self.effect.config.discards
        if self.effect.config.reroll_discount:
            G.GAME.starting_params.reroll_cost = G.GAME.starting_params.reroll_cost - self.effect.config.reroll_discount
        if self.effect.config.edition:G.E_MANAGER.add_event()
        if self.effect.config.vouchers:
            for kv in pairs():
                'v[G.GAME.used_vouchers]' = True
                G.GAME.starting_voucher_count = (G.GAME.starting_voucher_count if G.GAME.starting_voucher_count else 0) + 1Card.apply_to_run(None, v[G.P_CENTERS])
        if self.name == 'Checkered Deck':G.E_MANAGER.add_event()
        if self.effect.config.randomize_rank_suit:
            G.GAME.starting_params.erratic_suits_and_ranks = True
        if self.effect.config.joker_slot:
            G.GAME.starting_params.joker_slots = G.GAME.starting_params.joker_slots + self.effect.config.joker_slot
        if self.effect.config.hand_size:
            G.GAME.starting_params.hand_size = G.GAME.starting_params.hand_size + self.effect.config.hand_size
        if self.effect.config.ante_scaling:
            G.GAME.starting_params.ante_scaling = self.effect.config.ante_scaling
        if self.effect.config.consumable_slot:
            G.GAME.starting_params.consumable_slots = G.GAME.starting_params.consumable_slots + self.effect.config.consumable_slot
        if self.effect.config.no_interest:
            G.GAME.modifiers.no_interest = True
        if self.effect.config.extra_hand_bonus:
            G.GAME.modifiers.money_per_hand = self.effect.config.extra_hand_bonus
        if self.effect.config.extra_discard_bonus:
            G.GAME.modifiers.money_per_discard = self.effect.config.extra_discard_bonus

    def load(self, backTable):
        self.name = backTable.name
        self.pos = backTable.pos
        self.effect = backTable.effect
        self.effect.center = 'backTable.key[G.P_CENTERS]' if 'backTable.key[G.P_CENTERS]' else G.P_CENTERS.b_red
        self.loc_name = localize()
# <ast.ClassDef object at 0x000002276D672610>