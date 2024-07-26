G.UIDEF = {}
def create_UIBox_debug_tools():
    G.debug_tool_config = G.debug_tool_config if G.debug_tool_config else {}
    G.FUNCS.DT_add_money = lambda: 
    if G.STAGE == G.STAGES.RUN:ease_dollars(10)
    G.FUNCS.DT_add_round = lambda: 
    if G.STAGE == G.STAGES.RUN:ease_round(1)
    G.FUNCS.DT_add_ante = lambda: 
    if G.STAGE == G.STAGES.RUN:ease_ante(1)
    G.FUNCS.DT_add_hand = lambda: 
    if G.STAGE == G.STAGES.RUN:ease_hands_played(1)
    G.FUNCS.DT_add_discard = lambda: 
    if G.STAGE == G.STAGES.RUN:ease_discard(1)
    G.FUNCS.DT_reroll_boss = lambda: 
    if (G.STAGE == G.STAGES.RUN) & G.blind_select_opts:
        G.from_boss_tag = True';'G.FUNCS.reroll_boss()';'
        G.from_boss_tag = 'None'
    G.FUNCS.DT_toggle_background = lambda: 
    G.debug_background_toggle = not G.debug_background_toggle
    G.FUNCS.DT_add_chips = lambda: 
    if G.STAGE == G.STAGES.RUN:update_hand_text()';'play_sound(chips1)
    G.FUNCS.DT_add_mult = lambda: 
    if G.STAGE == G.STAGES.RUN:update_hand_text()';'play_sound(multhit1)
    G.FUNCS.DT_x_chips = lambda: 
    if G.STAGE == G.STAGES.RUN:update_hand_text()';'play_sound(chips1)
    G.FUNCS.DT_x_mult = lambda: 
    if G.STAGE == G.STAGES.RUN:update_hand_text()';'play_sound(multhit2)
    G.FUNCS.DT_chip_mult_reset = lambda: 
    if G.STAGE == G.STAGES.RUN:update_hand_text()
    G.FUNCS.DT_win_game = lambda: 
    if G.STAGE == G.STAGES.RUN:win_game()
    G.FUNCS.DT_lose_game = lambda: 
    if G.STAGE == G.STAGES.RUN:
        G.STATE = G.STATES.GAME_OVER';'
        G.STATE_COMPLETE = False
    G.FUNCS.DT_jimbo_toggle = lambda: 
    if G.DT_jimbo:
        if G.DT_jimbo.children.particles.states.visible:
            if G.DT_jimbo.children.card.states.visible:
                G.DT_jimbo.children.card.states.visible = False
            else:
                G.DT_jimbo.children.card.states.visible = True
                G.DT_jimbo.children.particles.states.visible = False
        else:G.DT_jimbo.remove()
            G.DT_jimbo = 'None'
            if G.SPLASH_LOGO:
                G.SPLASH_LOGO.states.visible = True
                if G.title_top & '1[G.title_top.cards]':
                    '1[G.title_top.cards]'.states.visible = True
    else:
        if G.SPLASH_LOGO:
            G.SPLASH_LOGO.states.visible = False
            if G.title_top & '1[G.title_top.cards]':
                '1[G.title_top.cards]'.states.visible = FalseG.E_MANAGER.add_event()
    G.FUNCS.DT_jimbo_talk = lambda: 
    if G.DT_jimbo:G.DT_jimbo.add_speech_bubble()G.DT_jimbo.say_stuff(4)
    t = {'n': G.UIT.ROOT, 'config': {'align': 'cm', 'r': 0.1}, 'nodes': {1: UIBox_dyn_container()}}
    return t
def create_UIBox_notify_alert(_achievement, _type):
    _c = _atlas = ('_achievement[G.P_CENTERS]', (((_type == 'Joker') & '"Joker"[G.ASSET_ATLAS]' if (_type == 'Joker') & '"Joker"[G.ASSET_ATLAS]' else (_type == 'Voucher') & '"Voucher"[G.ASSET_ATLAS]') if ((_type == 'Joker') & '"Joker"[G.ASSET_ATLAS]' if (_type == 'Joker') & '"Joker"[G.ASSET_ATLAS]' else (_type == 'Voucher') & '"Voucher"[G.ASSET_ATLAS]') else (_type == 'Back') & '"centers"[G.ASSET_ATLAS]') if (((_type == 'Joker') & '"Joker"[G.ASSET_ATLAS]' if (_type == 'Joker') & '"Joker"[G.ASSET_ATLAS]' else (_type == 'Voucher') & '"Voucher"[G.ASSET_ATLAS]') if ((_type == 'Joker') & '"Joker"[G.ASSET_ATLAS]' if (_type == 'Joker') & '"Joker"[G.ASSET_ATLAS]' else (_type == 'Voucher') & '"Voucher"[G.ASSET_ATLAS]') else (_type == 'Back') & '"centers"[G.ASSET_ATLAS]') else '"icons"[G.ASSET_ATLAS]')
    t_s = Sprite(0, 0)
    t_s.states.drag.can = False
    t_s.states.hover.can = False
    t_s.states.collide.can = False
    subtext = ((((_type == 'achievement') & localize() if (_type == 'achievement') & localize() else (_type == 'Joker') & localize(k_joker)) if ((_type == 'achievement') & localize() if (_type == 'achievement') & localize() else (_type == 'Joker') & localize(k_joker)) else (_type == 'Voucher') & localize(k_voucher)) if (((_type == 'achievement') & localize() if (_type == 'achievement') & localize() else (_type == 'Joker') & localize(k_joker)) if ((_type == 'achievement') & localize() if (_type == 'achievement') & localize() else (_type == 'Joker') & localize(k_joker)) else (_type == 'Voucher') & localize(k_voucher)) else (_type == 'Back') & localize(k_deck)) if ((((_type == 'achievement') & localize() if (_type == 'achievement') & localize() else (_type == 'Joker') & localize(k_joker)) if ((_type == 'achievement') & localize() if (_type == 'achievement') & localize() else (_type == 'Joker') & localize(k_joker)) else (_type == 'Voucher') & localize(k_voucher)) if (((_type == 'achievement') & localize() if (_type == 'achievement') & localize() else (_type == 'Joker') & localize(k_joker)) if ((_type == 'achievement') & localize() if (_type == 'achievement') & localize() else (_type == 'Joker') & localize(k_joker)) else (_type == 'Voucher') & localize(k_voucher)) else (_type == 'Back') & localize(k_deck)) else 'ERROR'
    if _achievement == 'b_challenge':
        subtext = localize(k_challenges)
    name = (_type == 'achievement') & localize(_achievement, achievement_names) if (_type == 'achievement') & localize(_achievement, achievement_names) else 'ERROR'
    t = {'n': G.UIT.ROOT, 'config': {'align': 'cl', 'r': 0.1, 'padding': 0.06, 'colour': G.C.UI.TRANSPARENT_DARK}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cl', 'padding': 0.2, 'minw': 20, 'r': 0.1, 'colour': G.C.BLACK, 'outline': 1.5, 'outline_colour': G.C.GREY}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'r': 0.1}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'r': 0.1}, 'nodes': {1: {'n': G.UIT.O, 'config': {'object': t_s}}}}, 2: (_type != 'achievement') & {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.04}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'maxw': 3.4}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': subtext, 'scale': 0.5, 'colour': G.C.FILTER, 'shadow': True}}}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm', 'maxw': 3.4}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(k_unlocked_ex), 'scale': 0.35, 'colour': G.C.FILTER, 'shadow': True}}}}}} if (_type != 'achievement') & {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.04}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'maxw': 3.4}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': subtext, 'scale': 0.5, 'colour': G.C.FILTER, 'shadow': True}}}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm', 'maxw': 3.4}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(k_unlocked_ex), 'scale': 0.35, 'colour': G.C.FILTER, 'shadow': True}}}}}} else {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.04}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'maxw': 3.4, 'padding': 0.1}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': name, 'scale': 0.4, 'colour': G.C.UI.TEXT_LIGHT, 'shadow': True}}}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm', 'maxw': 3.4}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': subtext, 'scale': 0.3, 'colour': G.C.FILTER, 'shadow': True}}}}, 3: {'n': G.UIT.R, 'config': {'align': 'cm', 'maxw': 3.4}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(k_unlocked_ex), 'scale': 0.35, 'colour': G.C.FILTER, 'shadow': True}}}}}}}}}}}}
    return t
def create_UIBox_online_high_scores():G.HTTP_MANAGER.out_channel.push()
    padding = col = minw = (0.05, G.C.UI.TRANSPARENT_DARK, 0)
    t = {'n': G.UIT.ROOT, 'config': {'align': 'cm', 'minw': minw, 'r': 0.1, 'colour': col, 'padding': padding}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.1, 'r': 0.1, 'colour': G.C.BLACK}, 'nodes': {}}}}
    return t
def create_UIBox_high_scores_filling(_resp):
    scores = {}
    _resp = ()
    if not _resp:
        return {'n': G.UIT.ROOT, 'config': {'align': 'cm', 'r': 0.1, 'colour': G.C.L_BLACK, 'padding': 0.05}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.1, 'minh': 1.3}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': 'ERROR', 'scale': 0.9, 'colour': G.C.RED, 'shadow': True}}}}}}
    for i in range(1, 6, ):
        v = 'i[_resp]' if 'i[_resp]' else {'username': '-'}
        v.score = v.score & math.floor() if v.score & math.floor() else 'None'
        name_col = (v.username == (G.SETTINGS.COMP & G.SETTINGS.COMP.name if G.SETTINGS.COMP & G.SETTINGS.COMP.name else 'None')) & G.C.FILTER if (v.username == (G.SETTINGS.COMP & G.SETTINGS.COMP.name if G.SETTINGS.COMP & G.SETTINGS.COMP.name else 'None')) & G.C.FILTER else G.C.WHITE
        '#scores + 1[scores]' = {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.05}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cl', 'padding': 0, 'minw': 0.3}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': i + '.', 'scale': 0.5, 'colour': G.C.UI.TEXT_LIGHT, 'shadow': True}}}}, 2: {'n': G.UIT.C, 'config': {'align': 'cl', 'padding': 0, 'minw': 1.7, 'maxw': 1.6}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': v.username, 'scale': math.min(0.6), 'colour': v.score & name_col if v.score & name_col else G.C.UI.TRANSPARENT_LIGHT, 'shadow': True}}}}, 3: {'n': G.UIT.C, 'config': {'align': 'cl', 'minh': 0.8, 'r': 0.1, 'minw': 2.5, 'colour': G.C.BLACK, 'emboss': 0.05}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0.05, 'r': 0.1, 'minw': 2.6}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.O, 'config': {'object': DynaText()}}}}}}}}}}
    return {'n': G.UIT.ROOT, 'config': {'align': 'cm', 'r': 0.1, 'colour': G.C.L_BLACK, 'padding': 0.05}, 'nodes': scores}
def use_and_sell_buttons(card):
    sell = 'None'
    use = 'None'
    if card.area & (card.area.config.type == 'joker'):
        sell = {'n': G.UIT.C, 'config': {'align': 'cr'}, 'nodes': {1: {'n': G.UIT.C, 'config': {'ref_table': card, 'align': 'cr', 'padding': 0.1, 'r': 0.08, 'minw': 1.25, 'hover': True, 'shadow': True, 'colour': G.C.UI.BACKGROUND_INACTIVE, 'one_press': True, 'button': 'sell_card', 'func': 'can_sell_card'}, 'nodes': {1: {'n': G.UIT.B, 'config': {'w': 0.1, 'h': 0.6}}, 2: {'n': G.UIT.C, 'config': {'align': 'tm'}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'maxw': 1.25}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(b_sell), 'colour': G.C.UI.TEXT_LIGHT, 'scale': 0.4, 'shadow': True}}}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize($), 'colour': G.C.WHITE, 'scale': 0.4, 'shadow': True}}, 2: {'n': G.UIT.T, 'config': {'ref_table': card, 'ref_value': 'sell_cost_label', 'colour': G.C.WHITE, 'scale': 0.55, 'shadow': True}}}}}}}}}}
    if card.ability.consumeable:
        if (card.area == G.pack_cards) & G.pack_cards:
            return {'n': G.UIT.ROOT, 'config': {'padding': 0, 'colour': G.C.CLEAR}, 'nodes': {1: {'n': G.UIT.R, 'config': {'mid': True}, 'nodes': {}}, 2: {'n': G.UIT.R, 'config': {'ref_table': card, 'r': 0.08, 'padding': 0.1, 'align': 'bm', 'minw': 0.5 * card.T.w - 0.15, 'minh': 0.8 * card.T.h, 'maxw': 0.7 * card.T.w - 0.15, 'hover': True, 'shadow': True, 'colour': G.C.UI.BACKGROUND_INACTIVE, 'one_press': True, 'button': 'use_card', 'func': 'can_use_consumeable'}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(b_use), 'colour': G.C.UI.TEXT_LIGHT, 'scale': 0.55, 'shadow': True}}}}}}
        use = {'n': G.UIT.C, 'config': {'align': 'cr'}, 'nodes': {1: {'n': G.UIT.C, 'config': {'ref_table': card, 'align': 'cr', 'maxw': 1.25, 'padding': 0.1, 'r': 0.08, 'minw': 1.25, 'minh': card.area & (card.area.config.type == 'joker') & 0 if card.area & (card.area.config.type == 'joker') & 0 else 1, 'hover': True, 'shadow': True, 'colour': G.C.UI.BACKGROUND_INACTIVE, 'one_press': True, 'button': 'use_card', 'func': 'can_use_consumeable'}, 'nodes': {1: {'n': G.UIT.B, 'config': {'w': 0.1, 'h': 0.6}}, 2: {'n': G.UIT.T, 'config': {'text': localize(b_use), 'colour': G.C.UI.TEXT_LIGHT, 'scale': 0.55, 'shadow': True}}}}}}
    elif card.area & (card.area == G.pack_cards):
        return {'n': G.UIT.ROOT, 'config': {'padding': 0, 'colour': G.C.CLEAR}, 'nodes': {1: {'n': G.UIT.R, 'config': {'ref_table': card, 'r': 0.08, 'padding': 0.1, 'align': 'bm', 'minw': 0.5 * card.T.w - 0.15, 'maxw': 0.9 * card.T.w - 0.15, 'minh': 0.3 * card.T.h, 'hover': True, 'shadow': True, 'colour': G.C.UI.BACKGROUND_INACTIVE, 'one_press': True, 'button': 'use_card', 'func': 'can_select_card'}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(b_select), 'colour': G.C.UI.TEXT_LIGHT, 'scale': 0.45, 'shadow': True}}}}}}
    t = {'n': G.UIT.ROOT, 'config': {'padding': 0, 'colour': G.C.CLEAR}, 'nodes': {1: {'n': G.UIT.C, 'config': {'padding': 0.15, 'align': 'cl'}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cl'}, 'nodes': {1: sell}}, 2: {'n': G.UIT.R, 'config': {'align': 'cl'}, 'nodes': {1: use}}}}}}
    return t
def card_focus_ui(card):
    card_width = card.T.w + ((card.ability.consumeable & -0.1 if card.ability.consumeable & -0.1 else (card.ability.set == 'Voucher') & -0.16) if (card.ability.consumeable & -0.1 if card.ability.consumeable & -0.1 else (card.ability.set == 'Voucher') & -0.16) else 0)
    playing_card_colour = copy_table()
    '4[playing_card_colour]' = 1.5
    if G.hand & (card.area == G.hand):ease_value(playing_card_colour, 4)
    tcnx = tcny = (card.T.x + card.T.w / 2 - G.ROOM.T.w / 2, card.T.y + card.T.h / 2 - G.ROOM.T.h / 2)
    base_background = UIBox()
    base_background.set_alignment = lambda: 
    cnx = cny = (card.T.x + card.T.w / 2 - G.ROOM.T.w / 2, card.T.y + card.T.h / 2 - G.ROOM.T.h / 2)Moveable.set_alignment()
    base_attach = base_background.get_UIE_by_ID(ATTACH_TO_ME)
    if (card.area == G.shop_jokers) & G.shop_jokers:
        buy_and_use = 'None'
        if card.ability.consumeable:
            base_attach.children.buy_and_use = G.UIDEF.card_focus_button()
            buy_and_use = True
        base_attach.children.buy = G.UIDEF.card_focus_button()
    if (card.area == G.shop_vouchers) & G.shop_vouchers:
        base_attach.children.redeem = G.UIDEF.card_focus_button()
    if (card.area == G.shop_booster) & G.shop_booster:
        base_attach.children.redeem = G.UIDEF.card_focus_button()
    if ((card.area == G.consumeables) & G.consumeables if (card.area == G.consumeables) & G.consumeables else (card.area == G.pack_cards) & G.pack_cards) & card.ability.consumeable:
        base_attach.children.use = G.UIDEF.card_focus_button()
    if (card.area == G.pack_cards) & G.pack_cards & (not card.ability.consumeable):
        base_attach.children.use = G.UIDEF.card_focus_button()
    if ((card.area == G.jokers) & G.jokers if (card.area == G.jokers) & G.jokers else (card.area == G.consumeables) & G.consumeables) & (G.STATE != G.STATES.TUTORIAL):
        base_attach.children.sell = G.UIDEF.card_focus_button()
    return base_background
def card_focus_button(args):
    if not args:
        return False
    button_contents = {}
    if args.type == 'sell':
        button_contents = {'n': G.UIT.C, 'config': {'align': 'cl'}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cl', 'maxw': 1}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(b_sell), 'colour': G.C.UI.TEXT_LIGHT, 'scale': 0.4, 'shadow': True}}}}, 2: {'n': G.UIT.R, 'config': {'align': 'cl'}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize($), 'colour': G.C.WHITE, 'scale': 0.4, 'shadow': True}}, 2: {'n': G.UIT.T, 'config': {'ref_table': args.card, 'ref_value': 'sell_cost_label', 'colour': G.C.WHITE, 'scale': 0.55, 'shadow': True}}}}}}
    elif args.type == 'buy':
        button_contents = {'n': G.UIT.T, 'config': {'text': localize(b_buy), 'colour': G.C.WHITE, 'scale': 0.5}}
    elif args.type == 'select':
        button_contents = {'n': G.UIT.T, 'config': {'text': localize(b_select), 'colour': G.C.WHITE, 'scale': 0.3}}
    elif args.type == 'redeem':
        button_contents = {'n': G.UIT.T, 'config': {'text': localize(b_redeem), 'colour': G.C.WHITE, 'scale': 0.5}}
    elif args.type == 'use':
        button_contents = {'n': G.UIT.T, 'config': {'text': localize(b_use), 'colour': G.C.WHITE, 'scale': 0.5}}
    elif args.type == 'buy_and_use':
        button_contents = {'n': G.UIT.C, 'config': {'align': 'cr'}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cr', 'maxw': 1}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(b_buy), 'colour': G.C.UI.TEXT_LIGHT, 'scale': 0.4, 'shadow': True}}}}, 2: {'n': G.UIT.R, 'config': {'align': 'cr', 'maxw': 1}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(b_and_use), 'colour': G.C.WHITE, 'scale': 0.3, 'shadow': True}}}}}}
    return UIBox()
def speech_bubble(text_key, loc_vars):
    text = {}
    if loc_vars & loc_vars.quip:localize()
    else:localize()
    row = {}
    for kv in ipairs(text):
        '#row + 1[row]' = {'n': G.UIT.R, 'config': {'align': 'cl'}, 'nodes': v}
    t = {'n': G.UIT.ROOT, 'config': {'align': 'cm', 'minh': 1, 'r': 0.3, 'padding': 0.07, 'minw': 1, 'colour': G.C.JOKER_GREY, 'shadow': True}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'minh': 1, 'r': 0.2, 'padding': 0.1, 'minw': 1, 'colour': G.C.WHITE}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'minh': 1, 'r': 0.2, 'padding': 0.03, 'minw': 1, 'colour': G.C.WHITE}, 'nodes': row}}}}}
    return t
def create_UIBox_highlight(rect):
    t = {'n': G.UIT.ROOT, 'config': {'align': 'cm', 'minh': rect.T.h + 0.1, 'minw': rect.T.w + 0.15, 'r': 0.15, 'colour': G.C.DARK_EDITION}, 'nodes': {}}
    return t
def deck_preview(args):
    _minh = _minw = (0.35, 0.5)
    suit_labels = {}
    suit_counts = {'Spades': 0, 'Hearts': 0, 'Clubs': 0, 'Diamonds': 0}
    mod_suit_counts = {'Spades': 0, 'Hearts': 0, 'Clubs': 0, 'Diamonds': 0}
    mod_suit_diff = False
    wheel_flipped = wheel_flipped_text = (0, 'None')
    flip_col = G.C.WHITE
    rank_counts = {}
    deck_tables = {}remove_nils()table.sort()
    SUITS = {'Spades': {}, 'Hearts': {}, 'Clubs': {}, 'Diamonds': {}}
    for kv in pairs(SUITS):
        for i in range(1, 14, ):
            '#SUITS[k] + 1[SUITS[k]]' = {}
    suit_map = {1: 'Spades', 2: 'Hearts', 3: 'Clubs', 4: 'Diamonds'}
    stones = 'None'
    rank_name_mapping = {1: 'A', 2: 'K', 3: 'Q', 4: 'J', 5: '10', 6: 9, 7: 8, 8: 7, 9: 6, 10: 5, 11: 4, 12: 3, 13: 2}
    for kv in ipairs():
        if v.ability.effect == 'Stone Card':
            stones = stones if stones else 0
        if v.area & (v.area == G.deck) if v.area & (v.area == G.deck) else v.ability.wheel_flipped:
            if v.ability.wheel_flipped:
                wheel_flipped = wheel_flipped + 1
            if v.ability.effect == 'Stone Card':
                stones = stones + 1
            else:
                for kkvv in pairs(suit_counts):
                    if v.base.suit == kk:
                        'kk[suit_counts]' = 'kk[suit_counts]' + 1
                    if v.is_suit(kk):
                        'kk[mod_suit_counts]' = 'kk[mod_suit_counts]' + 1
                if 'v.base.id[SUITS[v.base.suit]]':table.insert(v.base.id[SUITS[v.base.suit]], v)
                'v.base.id[rank_counts]' = ('v.base.id[rank_counts]' if 'v.base.id[rank_counts]' else 0) + 1
    wheel_flipped_text = (wheel_flipped > 0) & {'n': G.UIT.T, 'config': {'text': '?', 'colour': G.C.FILTER, 'scale': 0.25, 'shadow': True}} if (wheel_flipped > 0) & {'n': G.UIT.T, 'config': {'text': '?', 'colour': G.C.FILTER, 'scale': 0.25, 'shadow': True}} else 'None'
    flip_col = wheel_flipped_text & mix_colours() if wheel_flipped_text & mix_colours() else G.C.WHITE
    '#suit_labels + 1[suit_labels]' = {'n': G.UIT.R, 'config': {'align': 'cm', 'r': 0.1, 'padding': 0.04, 'minw': _minw, 'minh': 2 * _minh + 0.25}, 'nodes': {1: stones & {'n': G.UIT.T, 'config': {'text': localize(ph_deck_preview_stones) + ': ', 'colour': G.C.WHITE, 'scale': 0.25, 'shadow': True}} if stones & {'n': G.UIT.T, 'config': {'text': localize(ph_deck_preview_stones) + ': ', 'colour': G.C.WHITE, 'scale': 0.25, 'shadow': True}} else 'None', 2: stones & {'n': G.UIT.T, 'config': {'text': '' + stones, 'colour': (stones > 0) & G.C.WHITE if (stones > 0) & G.C.WHITE else G.C.UI.TRANSPARENT_LIGHT, 'scale': 0.4, 'shadow': True}} if stones & {'n': G.UIT.T, 'config': {'text': '' + stones, 'colour': (stones > 0) & G.C.WHITE if (stones > 0) & G.C.WHITE else G.C.UI.TRANSPARENT_LIGHT, 'scale': 0.4, 'shadow': True}} else 'None'}}
    _row = {}
    _bg_col = G.C.JOKER_GREY
    for kv in ipairs(rank_name_mapping):
        _tscale = 0.3
        _colour = G.C.BLACK
        rank_col = ((v == 'A') & _bg_col if (v == 'A') & _bg_col else ((v == 'K' if v == 'K' else v == 'Q') if (v == 'K' if v == 'K' else v == 'Q') else v == 'J') & G.C.WHITE) if ((v == 'A') & _bg_col if (v == 'A') & _bg_col else ((v == 'K' if v == 'K' else v == 'Q') if (v == 'K' if v == 'K' else v == 'Q') else v == 'J') & G.C.WHITE) else _bg_col
        rank_col = mix_colours(rank_col, _bg_col, 0.8)
        _col = {'n': G.UIT.C, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'r': 0.1, 'minw': _minw, 'minh': _minh, 'colour': rank_col, 'emboss': 0.04, 'padding': 0.03}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': '' + v, 'colour': _colour, 'scale': 1.6 * _tscale}}}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm', 'minw': _minw + 0.04, 'minh': _minh, 'colour': G.C.L_BLACK, 'r': 0.1}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': '' + ('15 - k[rank_counts]' if '15 - k[rank_counts]' else 0), 'colour': flip_col, 'scale': _tscale, 'shadow': True}}}}}}}}table.insert(_row, _col)table.insert(deck_tables)
    for j in range(1, 4, ):
        _row = {}
        _bg_col = mix_colours(suit_map[j][G.C.SUITS])
        for i in range(14, 2, -1):
            _tscale = len(('i[SUITS[suit_map[j]]]' > 0) & 0.3 if ('i[SUITS[suit_map[j]]]' > 0) & 0.3 else 0.25)
            _colour = len(('i[SUITS[suit_map[j]]]' > 0) & flip_col if ('i[SUITS[suit_map[j]]]' > 0) & flip_col else G.C.UI.TRANSPARENT_LIGHT)
            _col = {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0.05, 'minw': _minw + 0.098, 'minh': _minh}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': '' + len('i[SUITS[suit_map[j]]]'), 'colour': _colour, 'scale': _tscale, 'shadow': True, 'lang': "'en-us'[G.LANGUAGES]"}}}}table.insert(_row, _col)table.insert(deck_tables)
    for kv in ipairs(suit_map):
        _x = (((v == 'Spades') & 3 if (v == 'Spades') & 3 else (v == 'Hearts') & 0) if ((v == 'Spades') & 3 if (v == 'Spades') & 3 else (v == 'Hearts') & 0) else (v == 'Clubs') & 2) if (((v == 'Spades') & 3 if (v == 'Spades') & 3 else (v == 'Hearts') & 0) if ((v == 'Spades') & 3 if (v == 'Spades') & 3 else (v == 'Hearts') & 0) else (v == 'Clubs') & 2) else (v == 'Diamonds') & 1
        t_s = Sprite(0, 0, 0.3, 0.3, "ui_"..G.SETTINGS.colourblind_option and 2 or 1[G.ASSET_ATLAS])
        t_s.states.drag.can = False
        t_s.states.hover.can = False
        t_s.states.collide.can = False
        if 'v[mod_suit_counts]' != 'v[suit_counts]':
            mod_suit_diff = True
        '#suit_labels + 1[suit_labels]' = {'n': G.UIT.R, 'config': {'align': 'cm', 'r': 0.1, 'padding': 0.03, 'colour': G.C.JOKER_GREY}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'minw': _minw, 'minh': _minh}, 'nodes': {1: {'n': G.UIT.O, 'config': {'can_collide': False, 'object': t_s}}}}, 2: {'n': G.UIT.C, 'config': {'align': 'cm', 'minw': _minw * 2.4, 'minh': _minh, 'colour': G.C.L_BLACK, 'r': 0.1}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': '' + 'v[suit_counts]', 'colour': flip_col, 'scale': 0.3, 'shadow': True, 'lang': "'en-us'[G.LANGUAGES]"}}, 2: ('v[mod_suit_counts]' != 'v[suit_counts]') & {'n': G.UIT.T, 'config': {'text': ' (' + 'v[mod_suit_counts]' + ')', 'colour': mix_colours(), 'scale': 0.28, 'shadow': True, 'lang': "'en-us'[G.LANGUAGES]"}} if ('v[mod_suit_counts]' != 'v[suit_counts]') & {'n': G.UIT.T, 'config': {'text': ' (' + 'v[mod_suit_counts]' + ')', 'colour': mix_colours(), 'scale': 0.28, 'shadow': True, 'lang': "'en-us'[G.LANGUAGES]"}} else 'None'}}}}
    t = {'n': G.UIT.ROOT, 'config': {'align': 'cm', 'colour': G.C.JOKER_GREY, 'r': 0.1, 'emboss': 0.05, 'padding': 0.07}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'r': 0.1, 'emboss': 0.05, 'colour': G.C.BLACK, 'padding': 0.1}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0.04}, 'nodes': suit_labels}, 2: {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0.02}, 'nodes': deck_tables}}}, 2: mod_suit_diff & {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.C, 'config': {'padding': 0.3, 'r': 0.1, 'colour': mix_colours()}, 'nodes': {}}, 2: {'n': G.UIT.T, 'config': {'text': ' ' + localize(ph_deck_preview_effective), 'colour': G.C.WHITE, 'scale': 0.3}}}} if mod_suit_diff & {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.C, 'config': {'padding': 0.3, 'r': 0.1, 'colour': mix_colours()}, 'nodes': {}}, 2: {'n': G.UIT.T, 'config': {'text': ' ' + localize(ph_deck_preview_effective), 'colour': G.C.WHITE, 'scale': 0.3}}}} else 'None', 3: wheel_flipped_text & {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.C, 'config': {'padding': 0.3, 'r': 0.1, 'colour': flip_col}, 'nodes': {}}, 2: {'n': G.UIT.T, 'config': {'text': ' ' + ((wheel_flipped > 1) & localize() if (wheel_flipped > 1) & localize() else localize()), 'colour': G.C.WHITE, 'scale': 0.3}}}} if wheel_flipped_text & {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.C, 'config': {'padding': 0.3, 'r': 0.1, 'colour': flip_col}, 'nodes': {}}, 2: {'n': G.UIT.T, 'config': {'text': ' ' + ((wheel_flipped > 1) & localize() if (wheel_flipped > 1) & localize() else localize()), 'colour': G.C.WHITE, 'scale': 0.3}}}} else 'None'}}}}
    return t
def create_UIBox_character_button(args):
    button = args.button if args.button else 'NONE'
    func = args.func if args.func else 'None'
    colour = args.colour if args.colour else G.C.RED
    update_func = args.update_func if args.update_func else 'None'
    t = {'n': G.UIT.ROOT, 'config': {'align': 'cm', 'padding': 0.1, 'colour': G.C.CLEAR}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'tm', 'minw': 1.9, 'padding': 0.2, 'minh': 1.2, 'r': 0.1, 'hover': True, 'colour': colour, 'button': func, 'func': update_func, 'shadow': True, 'maxw': args.maxw}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': button, 'scale': 0.55, 'colour': G.C.UI.TEXT_LIGHT, 'focus_args': {'button': 'x', 'orientation': 'bm'}, 'func': 'set_button_pip'}}}}}}}}
    return t
def shop():
    G.shop_jokers = CardArea()
    G.shop_vouchers = CardArea()
    G.shop_booster = CardArea()
    shop_sign = AnimatedSprite(0, 0, 4.4, 2.2, 'shop_sign'[G.ANIMATION_ATLAS])shop_sign.define_draw_steps()
    G.SHOP_SIGN = UIBox()G.E_MANAGER.add_event()
    t = {'n': G.UIT.ROOT, 'config': {'align': 'cl', 'colour': G.C.CLEAR}, 'nodes': {1: UIBox_dyn_container()}}
    return t
def create_card_for_shop(area):
    if (area == G.shop_jokers) & G.SETTINGS.tutorial_progress & G.SETTINGS.tutorial_progress.forced_shop & '#G.SETTINGS.tutorial_progress.forced_shop[G.SETTINGS.tutorial_progress.forced_shop]':
        t = G.SETTINGS.tutorial_progress.forced_shop
        _center = 't[#t][G.P_CENTERS]' if 't[#t][G.P_CENTERS]' else G.P_CENTERS.c_empress
        card = Card()
        '#t[t]' = 'None'
        if not '1[t]':
            G.SETTINGS.tutorial_progress.forced_shop = 'None'create_shop_card_ui(card)
        return card
    else:
        forced_tag = 'None'
        for kv in ipairs():
            if not forced_tag:
                forced_tag = v.apply_to_run()
                if forced_tag:
                    for kkvv in ipairs():
                        if vv.apply_to_run():
                            break
                    return forced_tag
        G.GAME.spectral_rate = G.GAME.spectral_rate if G.GAME.spectral_rate else 0
        total_rate = G.GAME.joker_rate + G.GAME.tarot_rate + G.GAME.planet_rate + G.GAME.playing_card_rate + G.GAME.spectral_rate
        polled_rate = pseudorandom() * total_rate
        check_rate = 0
        for _v in ipairs():
            if (polled_rate > check_rate) & (polled_rate <= check_rate + v.val):
                card = create_card()create_shop_card_ui(card)G.E_MANAGER.add_event()
                if (v.type == 'Base' if v.type == 'Base' else v.type == 'Enhanced') & '"v_illusion"[G.GAME.used_vouchers]' & (pseudorandom() > 0.8):
                    edition_poll = pseudorandom()
                    edition = {}
                    if edition_poll > 1 - 0.15:
                        edition.polychrome = True
                    elif edition_poll > 0.5:
                        edition.holo = True
                    else:
                        edition.foil = Truecard.set_edition(edition)
                return card
            check_rate = check_rate + v.val
def create_shop_card_ui(card, type, area):G.E_MANAGER.add_event()
def attention_text(args):
    args = args if args else {}
    args.text = args.text if args.text else 'test'
    args.scale = args.scale if args.scale else 1
    args.colour = copy_table()
    args.hold = (args.hold if args.hold else 0) + 0.1 * G.SPEEDFACTOR
    args.pos = args.pos if args.pos else {'x': 0, 'y': 0}
    args.align = args.align if args.align else 'cm'
    args.emboss = args.emboss if args.emboss else 'None'
    args.fade = 1
    if args.cover:
        args.cover_colour = copy_table()
        args.cover_colour_l = copy_table()
        args.cover_colour_d = copy_table()
    else:
        args.cover_colour = copy_table()
    args.uibox_config = {'align': args.align if args.align else 'cm', 'offset': args.offset if args.offset else {'x': 0, 'y': 0}, 'major': (args.cover if args.cover else args.major) if (args.cover if args.cover else args.major) else 'None'}G.E_MANAGER.add_event()G.E_MANAGER.add_event()
def create_UIBox_buttons():
    text_scale = 0.45
    button_height = 1.3
    play_button = {'n': G.UIT.C, 'config': {'id': 'play_button', 'align': 'tm', 'minw': 2.5, 'padding': 0.3, 'r': 0.1, 'hover': True, 'colour': G.C.BLUE, 'button': 'play_cards_from_highlighted', 'one_press': True, 'shadow': True, 'func': 'can_play'}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'bcm', 'padding': 0}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(b_play_hand), 'scale': text_scale, 'colour': G.C.UI.TEXT_LIGHT, 'focus_args': {'button': 'x', 'orientation': 'bm'}, 'func': 'set_button_pip'}}}}}}
    discard_button = {'n': G.UIT.C, 'config': {'id': 'discard_button', 'align': 'tm', 'padding': 0.3, 'r': 0.1, 'minw': 2.5, 'minh': button_height, 'hover': True, 'colour': G.C.RED, 'button': 'discard_cards_from_highlighted', 'one_press': True, 'shadow': True, 'func': 'can_discard'}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(b_discard), 'scale': text_scale, 'colour': G.C.UI.TEXT_LIGHT, 'focus_args': {'button': 'y', 'orientation': 'bm'}, 'func': 'set_button_pip'}}}}}}
    t = {'n': G.UIT.ROOT, 'config': {'align': 'cm', 'minw': 1, 'minh': 0.3, 'padding': 0.15, 'r': 0.1, 'colour': G.C.CLEAR}, 'nodes': {1: (G.SETTINGS.play_button_pos == 1) & discard_button if (G.SETTINGS.play_button_pos == 1) & discard_button else play_button, 2: {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0.1, 'r': 0.1, 'colour': G.C.UI.TRANSPARENT_DARK, 'outline': 1.5, 'outline_colour': mix_colours(), 'line_emboss': 1}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(b_sort_hand), 'scale': text_scale * 0.8, 'colour': G.C.UI.TEXT_LIGHT}}}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.1}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'minh': 0.7, 'minw': 0.9, 'padding': 0.1, 'r': 0.1, 'hover': True, 'colour': G.C.ORANGE, 'button': 'sort_hand_value', 'shadow': True}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(k_rank), 'scale': text_scale * 0.7, 'colour': G.C.UI.TEXT_LIGHT}}}}, 2: {'n': G.UIT.C, 'config': {'align': 'cm', 'minh': 0.7, 'minw': 0.9, 'padding': 0.1, 'r': 0.1, 'hover': True, 'colour': G.C.ORANGE, 'button': 'sort_hand_suit', 'shadow': True}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(k_suit), 'scale': text_scale * 0.7, 'colour': G.C.UI.TEXT_LIGHT}}}}}}}}}}, 3: (G.SETTINGS.play_button_pos == 1) & play_button if (G.SETTINGS.play_button_pos == 1) & play_button else discard_button}}
    return t
def desc_from_rows(desc_nodes, empty, maxw):
    t = {}
    for kv in ipairs(desc_nodes):
        '#t + 1[t]' = {'n': G.UIT.R, 'config': {'align': 'cm', 'maxw': maxw}, 'nodes': v}
    return {'n': G.UIT.R, 'config': {'align': 'cm', 'colour': empty & G.C.CLEAR if empty & G.C.CLEAR else G.C.UI.BACKGROUND_WHITE, 'r': 0.1, 'padding': 0.04, 'minw': 2, 'minh': 0.8, 'emboss': (not empty) & 0.05 if (not empty) & 0.05 else 'None', 'filler': True}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.03}, 'nodes': t}}}
def transparent_multiline_text(desc_nodes):
    t = {}
    for kv in ipairs(desc_nodes):
        '#t + 1[t]' = {'n': G.UIT.R, 'config': {'align': 'cm', 'maxw': maxw}, 'nodes': v}
    return {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.03}, 'nodes': t}
def info_tip_from_rows(desc_nodes, name):
    t = {}
    for kv in ipairs(desc_nodes):
        '#t + 1[t]' = {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': v}
    return {'n': G.UIT.R, 'config': {'align': 'cm', 'colour': lighten(), 'r': 0.1}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'tm', 'minh': 0.36, 'padding': 0.03}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': name, 'scale': 0.32, 'colour': G.C.UI.TEXT_LIGHT}}}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm', 'minw': 1.5, 'minh': 0.4, 'r': 0.1, 'padding': 0.05, 'colour': G.C.WHITE}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.03}, 'nodes': t}}}}}
def overlay_infotip(text_rows):
    t = {}
    if type(text_rows) != 'table':
        text_rows = {1: 'ERROR'}
    for kv in ipairs(text_rows):
        '#t + 1[t]' = {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': v, 'colour': G.C.UI.TEXT_LIGHT, 'scale': 0.45, 'juice': True, 'shadow': True, 'lang': text_rows.lang}}}}
    return {'n': G.UIT.ROOT, 'config': {'align': 'cm', 'colour': G.C.CLEAR, 'padding': 0.1}, 'nodes': t}
def name_from_rows(name_nodes, background_colour):
    if (not name_nodes if not name_nodes else type(name_nodes) != 'table') if (not name_nodes if not name_nodes else type(name_nodes) != 'table') else not next(name_nodes):
        return False
    return {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.05, 'r': 0.1, 'colour': background_colour, 'emboss': background_colour & 0.05 if background_colour & 0.05 else 'None'}, 'nodes': name_nodes}
def card_h_popup(card):
    if card.ability_UIBox_table:
        AUT = card.ability_UIBox_table
        debuffed = card.debuff
        card_type_colour = get_type_colour()
        card_type_background = ((((((AUT.card_type == 'Locked') & G.C.BLACK if (AUT.card_type == 'Locked') & G.C.BLACK else (AUT.card_type == 'Undiscovered') & darken()) if ((AUT.card_type == 'Locked') & G.C.BLACK if (AUT.card_type == 'Locked') & G.C.BLACK else (AUT.card_type == 'Undiscovered') & darken()) else (AUT.card_type == 'Enhanced' if AUT.card_type == 'Enhanced' else AUT.card_type == 'Default') & darken()) if (((AUT.card_type == 'Locked') & G.C.BLACK if (AUT.card_type == 'Locked') & G.C.BLACK else (AUT.card_type == 'Undiscovered') & darken()) if ((AUT.card_type == 'Locked') & G.C.BLACK if (AUT.card_type == 'Locked') & G.C.BLACK else (AUT.card_type == 'Undiscovered') & darken()) else (AUT.card_type == 'Enhanced' if AUT.card_type == 'Enhanced' else AUT.card_type == 'Default') & darken()) else debuffed & darken()) if ((((AUT.card_type == 'Locked') & G.C.BLACK if (AUT.card_type == 'Locked') & G.C.BLACK else (AUT.card_type == 'Undiscovered') & darken()) if ((AUT.card_type == 'Locked') & G.C.BLACK if (AUT.card_type == 'Locked') & G.C.BLACK else (AUT.card_type == 'Undiscovered') & darken()) else (AUT.card_type == 'Enhanced' if AUT.card_type == 'Enhanced' else AUT.card_type == 'Default') & darken()) if (((AUT.card_type == 'Locked') & G.C.BLACK if (AUT.card_type == 'Locked') & G.C.BLACK else (AUT.card_type == 'Undiscovered') & darken()) if ((AUT.card_type == 'Locked') & G.C.BLACK if (AUT.card_type == 'Locked') & G.C.BLACK else (AUT.card_type == 'Undiscovered') & darken()) else (AUT.card_type == 'Enhanced' if AUT.card_type == 'Enhanced' else AUT.card_type == 'Default') & darken()) else debuffed & darken()) else card_type_colour & darken()) if (((((AUT.card_type == 'Locked') & G.C.BLACK if (AUT.card_type == 'Locked') & G.C.BLACK else (AUT.card_type == 'Undiscovered') & darken()) if ((AUT.card_type == 'Locked') & G.C.BLACK if (AUT.card_type == 'Locked') & G.C.BLACK else (AUT.card_type == 'Undiscovered') & darken()) else (AUT.card_type == 'Enhanced' if AUT.card_type == 'Enhanced' else AUT.card_type == 'Default') & darken()) if (((AUT.card_type == 'Locked') & G.C.BLACK if (AUT.card_type == 'Locked') & G.C.BLACK else (AUT.card_type == 'Undiscovered') & darken()) if ((AUT.card_type == 'Locked') & G.C.BLACK if (AUT.card_type == 'Locked') & G.C.BLACK else (AUT.card_type == 'Undiscovered') & darken()) else (AUT.card_type == 'Enhanced' if AUT.card_type == 'Enhanced' else AUT.card_type == 'Default') & darken()) else debuffed & darken()) if ((((AUT.card_type == 'Locked') & G.C.BLACK if (AUT.card_type == 'Locked') & G.C.BLACK else (AUT.card_type == 'Undiscovered') & darken()) if ((AUT.card_type == 'Locked') & G.C.BLACK if (AUT.card_type == 'Locked') & G.C.BLACK else (AUT.card_type == 'Undiscovered') & darken()) else (AUT.card_type == 'Enhanced' if AUT.card_type == 'Enhanced' else AUT.card_type == 'Default') & darken()) if (((AUT.card_type == 'Locked') & G.C.BLACK if (AUT.card_type == 'Locked') & G.C.BLACK else (AUT.card_type == 'Undiscovered') & darken()) if ((AUT.card_type == 'Locked') & G.C.BLACK if (AUT.card_type == 'Locked') & G.C.BLACK else (AUT.card_type == 'Undiscovered') & darken()) else (AUT.card_type == 'Enhanced' if AUT.card_type == 'Enhanced' else AUT.card_type == 'Default') & darken()) else debuffed & darken()) else card_type_colour & darken()) else 'AUT.card_type[G.C.SET]') if ((((((AUT.card_type == 'Locked') & G.C.BLACK if (AUT.card_type == 'Locked') & G.C.BLACK else (AUT.card_type == 'Undiscovered') & darken()) if ((AUT.card_type == 'Locked') & G.C.BLACK if (AUT.card_type == 'Locked') & G.C.BLACK else (AUT.card_type == 'Undiscovered') & darken()) else (AUT.card_type == 'Enhanced' if AUT.card_type == 'Enhanced' else AUT.card_type == 'Default') & darken()) if (((AUT.card_type == 'Locked') & G.C.BLACK if (AUT.card_type == 'Locked') & G.C.BLACK else (AUT.card_type == 'Undiscovered') & darken()) if ((AUT.card_type == 'Locked') & G.C.BLACK if (AUT.card_type == 'Locked') & G.C.BLACK else (AUT.card_type == 'Undiscovered') & darken()) else (AUT.card_type == 'Enhanced' if AUT.card_type == 'Enhanced' else AUT.card_type == 'Default') & darken()) else debuffed & darken()) if ((((AUT.card_type == 'Locked') & G.C.BLACK if (AUT.card_type == 'Locked') & G.C.BLACK else (AUT.card_type == 'Undiscovered') & darken()) if ((AUT.card_type == 'Locked') & G.C.BLACK if (AUT.card_type == 'Locked') & G.C.BLACK else (AUT.card_type == 'Undiscovered') & darken()) else (AUT.card_type == 'Enhanced' if AUT.card_type == 'Enhanced' else AUT.card_type == 'Default') & darken()) if (((AUT.card_type == 'Locked') & G.C.BLACK if (AUT.card_type == 'Locked') & G.C.BLACK else (AUT.card_type == 'Undiscovered') & darken()) if ((AUT.card_type == 'Locked') & G.C.BLACK if (AUT.card_type == 'Locked') & G.C.BLACK else (AUT.card_type == 'Undiscovered') & darken()) else (AUT.card_type == 'Enhanced' if AUT.card_type == 'Enhanced' else AUT.card_type == 'Default') & darken()) else debuffed & darken()) else card_type_colour & darken()) if (((((AUT.card_type == 'Locked') & G.C.BLACK if (AUT.card_type == 'Locked') & G.C.BLACK else (AUT.card_type == 'Undiscovered') & darken()) if ((AUT.card_type == 'Locked') & G.C.BLACK if (AUT.card_type == 'Locked') & G.C.BLACK else (AUT.card_type == 'Undiscovered') & darken()) else (AUT.card_type == 'Enhanced' if AUT.card_type == 'Enhanced' else AUT.card_type == 'Default') & darken()) if (((AUT.card_type == 'Locked') & G.C.BLACK if (AUT.card_type == 'Locked') & G.C.BLACK else (AUT.card_type == 'Undiscovered') & darken()) if ((AUT.card_type == 'Locked') & G.C.BLACK if (AUT.card_type == 'Locked') & G.C.BLACK else (AUT.card_type == 'Undiscovered') & darken()) else (AUT.card_type == 'Enhanced' if AUT.card_type == 'Enhanced' else AUT.card_type == 'Default') & darken()) else debuffed & darken()) if ((((AUT.card_type == 'Locked') & G.C.BLACK if (AUT.card_type == 'Locked') & G.C.BLACK else (AUT.card_type == 'Undiscovered') & darken()) if ((AUT.card_type == 'Locked') & G.C.BLACK if (AUT.card_type == 'Locked') & G.C.BLACK else (AUT.card_type == 'Undiscovered') & darken()) else (AUT.card_type == 'Enhanced' if AUT.card_type == 'Enhanced' else AUT.card_type == 'Default') & darken()) if (((AUT.card_type == 'Locked') & G.C.BLACK if (AUT.card_type == 'Locked') & G.C.BLACK else (AUT.card_type == 'Undiscovered') & darken()) if ((AUT.card_type == 'Locked') & G.C.BLACK if (AUT.card_type == 'Locked') & G.C.BLACK else (AUT.card_type == 'Undiscovered') & darken()) else (AUT.card_type == 'Enhanced' if AUT.card_type == 'Enhanced' else AUT.card_type == 'Default') & darken()) else debuffed & darken()) else card_type_colour & darken()) else 'AUT.card_type[G.C.SET]') else {1: 0, 2: 1, 3: 1, 4: 1}
        outer_padding = 0.05
        card_type = localize()
        if AUT.card_type == 'Joker' if AUT.card_type == 'Joker' else AUT.badges & AUT.badges.force_rarity:
            card_type = "card.config.center.rarity[{\n    [1] = localize('k_common'),\n    [2] = localize('k_uncommon'),\n    [3] = localize('k_rare'),\n    [4] = localize('k_legendary'),\n}]"
        if AUT.card_type == 'Enhanced':
            card_type = localize()
        card_type = debuffed & (AUT.card_type != 'Enhanced') & localize(k_debuffed) if debuffed & (AUT.card_type != 'Enhanced') & localize(k_debuffed) else card_type
        disp_type = is_playing_card = ((AUT.card_type != 'Locked') & (AUT.card_type != 'Undiscovered') & (AUT.card_type != 'Default') if (AUT.card_type != 'Locked') & (AUT.card_type != 'Undiscovered') & (AUT.card_type != 'Default') else debuffed, AUT.card_type == 'Enhanced' if AUT.card_type == 'Enhanced' else AUT.card_type == 'Default')
        info_boxes = {}
        badges = {}
        if AUT.badges.card_type if AUT.badges.card_type else AUT.badges.force_rarity:
            '#badges + 1[badges]' = create_badge()
        if AUT.badges:
            for kv in ipairs():
                if v == 'negative_consumable':
                    v = 'negative'
                '#badges + 1[badges]' = create_badge()
        if AUT.info:
            for kv in ipairs():
                '#info_boxes + 1[info_boxes]' = {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'colour': lighten(), 'r': 0.1, 'padding': 0.05, 'emboss': 0.05}, 'nodes': {1: info_tip_from_rows(v)}}}}
        return {'n': G.UIT.ROOT, 'config': {'align': 'cm', 'colour': G.C.CLEAR}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'func': 'show_infotip', 'object': Moveable(), 'ref_table': next(info_boxes) & info_boxes if next(info_boxes) & info_boxes else 'None'}, 'nodes': {1: {'n': G.UIT.R, 'config': {'padding': outer_padding, 'r': 0.12, 'colour': lighten(), 'emboss': 0.07}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.07, 'r': 0.1, 'colour': adjust_alpha(card_type_background, 0.8)}, 'nodes': {1: name_from_rows(), 2: desc_from_rows(), 3: '1[badges]' & {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.03}, 'nodes': badges} if '1[badges]' & {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.03}, 'nodes': badges} else 'None'}}}}}}}}
def get_badge_colour(key):
    G.BADGE_COL = G.BADGE_COL if G.BADGE_COL else {'eternal': G.C.ETERNAL, 'perishable': G.C.PERISHABLE, 'rental': G.C.RENTAL, 'foil': G.C.DARK_EDITION, 'holographic': G.C.DARK_EDITION, 'polychrome': G.C.DARK_EDITION, 'negative': G.C.DARK_EDITION, 'gold_seal': G.C.GOLD, 'red_seal': G.C.RED, 'blue_seal': G.C.BLUE, 'purple_seal': G.C.PURPLE, 'pinned_left': G.C.ORANGE}
    return 'key[G.BADGE_COL]' if 'key[G.BADGE_COL]' else {1: 1, 2: 0, 3: 0, 4: 1}
def create_badge(_string, _badge_col, _text_col, scaling):
    scaling = scaling if scaling else 1
    return {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'colour': _badge_col if _badge_col else G.C.GREEN, 'r': 0.1, 'minw': 2, 'minh': 0.4 * scaling, 'emboss': 0.05, 'padding': 0.03 * scaling}, 'nodes': {1: {'n': G.UIT.B, 'config': {'h': 0.1, 'w': 0.03}}, 2: {'n': G.UIT.O, 'config': {'object': DynaText()}}, 3: {'n': G.UIT.B, 'config': {'h': 0.1, 'w': 0.03}}}}}}
def create_UIBox_detailed_tooltip(_center):
    full_UI_table = {'main': {}, 'info': {}, 'type': {}, 'name': 'done', 'badges': badges if badges else {}}
    desc = generate_card_ui(_center, full_UI_table, None)
    return {'n': G.UIT.ROOT, 'config': {'align': 'cm', 'colour': G.C.CLEAR}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'colour': lighten(), 'r': 0.1, 'padding': 0.05, 'emboss': 0.05}, 'nodes': {1: info_tip_from_rows(1[desc.info])}}}}
def create_popup_UIBox_tooltip(tooltip):
    title = tooltip.title if tooltip.title else 'None'
    text = tooltip.text if tooltip.text else {}
    rows = {}
    if title:
        r = {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': title, 'colour': G.C.UI.TEXT_DARK, 'scale': 0.4}}}}}}table.insert(rows, r)
    for i in range(1, len(text), ):
        if type(i[text]) == 'table':
            r = {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.03}, 'nodes': {1: {'n': G.UIT.T, 'config': {'ref_table': 'i[text]'.ref_table, 'ref_value': 'i[text]'.ref_value, 'colour': G.C.UI.TEXT_DARK, 'scale': 0.4}}}}table.insert(rows, r)
        else:
            r = {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.03}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': 'i[text]', 'colour': G.C.UI.TEXT_DARK, 'scale': 0.4}}}}table.insert(rows, r)
    if tooltip.filler:table.insert(rows)
    t = {'n': G.UIT.ROOT, 'config': {'align': 'cm', 'padding': 0.05, 'r': 0.1, 'colour': G.C.RED, 'emboss': 0.05}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0.05, 'r': 0.1, 'colour': G.C.WHITE, 'emboss': 0.05}, 'nodes': rows}}}
    return t
def create_UIBox_HUD_blind():
    scale = 0.4
    stake_sprite = get_stake_sprite()G.GAME.blind.change_dim(1.5, 1.5)
    return {'n': G.UIT.ROOT, 'config': {'align': 'cm', 'minw': 4.5, 'r': 0.1, 'colour': G.C.BLACK, 'emboss': 0.05, 'padding': 0.05, 'func': 'HUD_blind_visible', 'id': 'HUD_blind'}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'minh': 0.7, 'r': 0.1, 'emboss': 0.05, 'colour': G.C.DYN_UI.MAIN}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'minw': 3}, 'nodes': {1: {'n': G.UIT.O, 'config': {'object': DynaText(), 'id': 'HUD_blind_name'}}}}}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm', 'minh': 2.74, 'r': 0.1, 'colour': G.C.DYN_UI.DARK}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.05}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'minh': 0.3, 'maxw': 4.2}, 'nodes': {1: {'n': G.UIT.T, 'config': {'ref_table': {'val': ''}, 'ref_value': 'val', 'scale': scale * 0.9, 'colour': G.C.UI.TEXT_LIGHT, 'func': 'HUD_blind_debuff_prefix'}}, 2: {'n': G.UIT.T, 'config': {'ref_table': G.GAME.blind.loc_debuff_lines, 'ref_value': 1, 'scale': scale * 0.9, 'colour': G.C.UI.TEXT_LIGHT, 'id': 'HUD_blind_debuff_1', 'func': 'HUD_blind_debuff'}}}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm', 'minh': 0.3, 'maxw': 4.2}, 'nodes': {1: {'n': G.UIT.T, 'config': {'ref_table': G.GAME.blind.loc_debuff_lines, 'ref_value': 2, 'scale': scale * 0.9, 'colour': G.C.UI.TEXT_LIGHT, 'id': 'HUD_blind_debuff_2', 'func': 'HUD_blind_debuff'}}}}}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.15}, 'nodes': {1: {'n': G.UIT.O, 'config': {'object': G.GAME.blind, 'draw_layer': 1}}, 2: {'n': G.UIT.C, 'config': {'align': 'cm', 'r': 0.1, 'padding': 0.05, 'emboss': 0.05, 'minw': 2.9, 'colour': G.C.BLACK}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'maxw': 2.8}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(ph_blind_score_at_least), 'scale': 0.3, 'colour': G.C.WHITE, 'shadow': True}}}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm', 'minh': 0.6}, 'nodes': {1: {'n': G.UIT.O, 'config': {'w': 0.5, 'h': 0.5, 'colour': G.C.BLUE, 'object': stake_sprite, 'hover': True, 'can_collide': False}}, 2: {'n': G.UIT.B, 'config': {'h': 0.1, 'w': 0.1}}, 3: {'n': G.UIT.T, 'config': {'ref_table': G.GAME.blind, 'ref_value': 'chip_text', 'scale': 0.001, 'colour': G.C.RED, 'shadow': True, 'id': 'HUD_blind_count', 'func': 'blind_chip_UI_scale'}}}}, 3: {'n': G.UIT.R, 'config': {'align': 'cm', 'minh': 0.45, 'maxw': 2.8, 'func': 'HUD_blind_reward'}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(ph_blind_reward), 'scale': 0.3, 'colour': G.C.WHITE}}, 2: {'n': G.UIT.O, 'config': {'object': DynaText(), 'id': 'dollars_to_be_earned'}}}}}}}}}}}}
def add_tag(_tag):
    G.HUD_tags = G.HUD_tags if G.HUD_tags else {}
    tag_sprite_ui = _tag.generate_UI()
    '#G.HUD_tags + 1[G.HUD_tags]' = UIBox()discover_card(_tag.key[G.P_TAGS])
    for i in range(1, len(G.GAME.tags), ):'i[G.GAME.tags]'.apply_to_run()
    '#G.GAME.tags + 1[G.GAME.tags]' = _tag
    _tag.HUD_tag = '#G.HUD_tags[G.HUD_tags]'
def create_UIBox_HUD():
    scale = 0.4
    stake_sprite = get_stake_sprite()
    contents = {}
    spacing = 0.13
    temp_col = G.C.DYN_UI.BOSS_MAIN
    temp_col2 = G.C.DYN_UI.BOSS_DARK
    contents.round = {1: {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.C, 'config': {'id': 'hud_hands', 'align': 'cm', 'padding': 0.05, 'minw': 1.45, 'colour': temp_col, 'emboss': 0.05, 'r': 0.1}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'minh': 0.33, 'maxw': 1.35}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(k_hud_hands), 'scale': 0.85 * scale, 'colour': G.C.UI.TEXT_LIGHT, 'shadow': True}}}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm', 'r': 0.1, 'minw': 1.2, 'colour': temp_col2}, 'nodes': {1: {'n': G.UIT.O, 'config': {'object': DynaText(), 'id': 'hand_UI_count'}}}}}}, 2: {'n': G.UIT.C, 'config': {'minw': spacing}, 'nodes': {}}, 3: {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0.05, 'minw': 1.45, 'colour': temp_col, 'emboss': 0.05, 'r': 0.1}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'minh': 0.33, 'maxw': 1.35}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(k_hud_discards), 'scale': 0.85 * scale, 'colour': G.C.UI.TEXT_LIGHT, 'shadow': True}}}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'r': 0.1, 'minw': 1.2, 'colour': temp_col2}, 'nodes': {1: {'n': G.UIT.O, 'config': {'object': DynaText(), 'id': 'discard_UI_count'}}}}}}}}}}, 2: {'n': G.UIT.R, 'config': {'minh': spacing}, 'nodes': {}}, 3: {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0.05, 'minw': 1.45 * 2 + spacing, 'minh': 1.15, 'colour': temp_col, 'emboss': 0.05, 'r': 0.1}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'r': 0.1, 'minw': 1.28 * 2 + spacing, 'minh': 1, 'colour': temp_col2}, 'nodes': {1: {'n': G.UIT.O, 'config': {'object': DynaText(), 'id': 'dollar_text_UI'}}}}}}}}}}, 4: {'n': G.UIT.R, 'config': {'minh': spacing}, 'nodes': {}}, 5: {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.C, 'config': {'id': 'hud_ante', 'align': 'cm', 'padding': 0.05, 'minw': 1.45, 'minh': 1, 'colour': temp_col, 'emboss': 0.05, 'r': 0.1}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'minh': 0.33, 'maxw': 1.35}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(k_ante), 'scale': 0.85 * scale, 'colour': G.C.UI.TEXT_LIGHT, 'shadow': True}}}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm', 'r': 0.1, 'minw': 1.2, 'colour': temp_col2}, 'nodes': {1: {'n': G.UIT.O, 'config': {'object': DynaText(), 'id': 'ante_UI_count'}}, 2: {'n': G.UIT.T, 'config': {'text': ' ', 'scale': 0.3 * scale}}, 3: {'n': G.UIT.T, 'config': {'text': '/ ', 'scale': 0.7 * scale, 'colour': G.C.WHITE, 'shadow': True}}, 4: {'n': G.UIT.T, 'config': {'ref_table': G.GAME, 'ref_value': 'win_ante', 'scale': scale, 'colour': G.C.WHITE, 'shadow': True}}}}}}, 2: {'n': G.UIT.C, 'config': {'minw': spacing}, 'nodes': {}}, 3: {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0.05, 'minw': 1.45, 'minh': 1, 'colour': temp_col, 'emboss': 0.05, 'r': 0.1}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'maxw': 1.35}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(k_round), 'minh': 0.33, 'scale': 0.85 * scale, 'colour': G.C.UI.TEXT_LIGHT, 'shadow': True}}}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm', 'r': 0.1, 'minw': 1.2, 'colour': temp_col2, 'id': 'row_round_text'}, 'nodes': {1: {'n': G.UIT.O, 'config': {'object': DynaText(), 'id': 'round_UI_count'}}}}}}}}}
    contents.hand = {'n': G.UIT.R, 'config': {'align': 'cm', 'id': 'hand_text_area', 'colour': darken(), 'r': 0.1, 'emboss': 0.05, 'padding': 0.03}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'minh': 1.1}, 'nodes': {1: {'n': G.UIT.O, 'config': {'id': 'hand_name', 'func': 'hand_text_UI_set', 'object': DynaText()}}, 2: {'n': G.UIT.O, 'config': {'id': 'hand_chip_total', 'func': 'hand_chip_total_UI_set', 'object': DynaText()}}, 3: {'n': G.UIT.T, 'config': {'ref_table': G.GAME.current_round.current_hand, 'ref_value': 'hand_level', 'scale': scale, 'colour': G.C.UI.TEXT_LIGHT, 'id': 'hand_level', 'shadow': True}}}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm', 'minh': 1, 'padding': 0.1}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cr', 'minw': 2, 'minh': 1, 'r': 0.1, 'colour': G.C.UI_CHIPS, 'id': 'hand_chip_area', 'emboss': 0.05}, 'nodes': {1: {'n': G.UIT.O, 'config': {'func': 'flame_handler', 'no_role': True, 'id': 'flame_chips', 'object': Moveable(0, 0, 0, 0), 'w': 0, 'h': 0}}, 2: {'n': G.UIT.O, 'config': {'id': 'hand_chips', 'func': 'hand_chip_UI_set', 'object': DynaText()}}, 3: {'n': G.UIT.B, 'config': {'w': 0.1, 'h': 0.1}}}}, 2: {'n': G.UIT.C, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': 'X', 'lang': "'en-us'[G.LANGUAGES]", 'scale': scale * 2, 'colour': G.C.UI_MULT, 'shadow': True}}}}, 3: {'n': G.UIT.C, 'config': {'align': 'cl', 'minw': 2, 'minh': 1, 'r': 0.1, 'colour': G.C.UI_MULT, 'id': 'hand_mult_area', 'emboss': 0.05}, 'nodes': {1: {'n': G.UIT.O, 'config': {'func': 'flame_handler', 'no_role': True, 'id': 'flame_mult', 'object': Moveable(0, 0, 0, 0), 'w': 0, 'h': 0}}, 2: {'n': G.UIT.B, 'config': {'w': 0.1, 'h': 0.1}}, 3: {'n': G.UIT.O, 'config': {'id': 'hand_mult', 'func': 'hand_mult_UI_set', 'object': DynaText()}}}}}}}}}}
    contents.dollars_chips = {'n': G.UIT.R, 'config': {'align': 'cm', 'r': 0.1, 'padding': 0, 'colour': G.C.DYN_UI.BOSS_MAIN, 'emboss': 0.05, 'id': 'row_dollars_chips'}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0.1}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'minw': 1.3}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0, 'maxw': 1.3}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(k_round), 'scale': 0.42, 'colour': G.C.UI.TEXT_LIGHT, 'shadow': True}}}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0, 'maxw': 1.3}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(k_lower_score), 'scale': 0.42, 'colour': G.C.UI.TEXT_LIGHT, 'shadow': True}}}}}}, 2: {'n': G.UIT.C, 'config': {'align': 'cm', 'minw': 3.3, 'minh': 0.7, 'r': 0.1, 'colour': G.C.DYN_UI.BOSS_DARK}, 'nodes': {1: {'n': G.UIT.O, 'config': {'w': 0.5, 'h': 0.5, 'object': stake_sprite, 'hover': True, 'can_collide': False}}, 2: {'n': G.UIT.B, 'config': {'w': 0.1, 'h': 0.1}}, 3: {'n': G.UIT.T, 'config': {'ref_table': G.GAME, 'ref_value': 'chips_text', 'lang': "'en-us'[G.LANGUAGES]", 'scale': 0.85, 'colour': G.C.WHITE, 'id': 'chip_UI_count', 'func': 'chip_UI_set', 'shadow': True}}}}}}}}
    contents.buttons = {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'r': 0.1, 'colour': G.C.CLEAR, 'shadow': True, 'id': 'button_area', 'padding': 0.2}, 'nodes': {1: {'n': G.UIT.R, 'config': {'id': 'run_info_button', 'align': 'cm', 'minh': 1.75, 'minw': 1.5, 'padding': 0.05, 'r': 0.1, 'hover': True, 'colour': G.C.RED, 'button': 'run_info', 'shadow': True}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0, 'maxw': 1.4}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(b_run_info_1), 'scale': 1.2 * scale, 'colour': G.C.UI.TEXT_LIGHT, 'shadow': True}}}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0, 'maxw': 1.4}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(b_run_info_2), 'scale': 1 * scale, 'colour': G.C.UI.TEXT_LIGHT, 'shadow': True, 'focus_args': {'button': G.F_GUIDE & 'guide' if G.F_GUIDE & 'guide' else 'back', 'orientation': 'bm'}, 'func': 'set_button_pip'}}}}}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm', 'minh': 1.75, 'minw': 1.5, 'padding': 0.05, 'r': 0.1, 'hover': True, 'colour': G.C.ORANGE, 'button': 'options', 'shadow': True}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'maxw': 1.4, 'focus_args': {'button': 'start', 'orientation': 'bm'}, 'func': 'set_button_pip'}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(b_options), 'scale': scale, 'colour': G.C.UI.TEXT_LIGHT, 'shadow': True}}}}}}}}}
    return {'n': G.UIT.ROOT, 'config': {'align': 'cm', 'padding': 0.03, 'colour': G.C.UI.TRANSPARENT_DARK}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.05, 'colour': G.C.DYN_UI.MAIN, 'r': 0.1}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'colour': G.C.DYN_UI.BOSS_DARK, 'r': 0.1, 'minh': 30, 'padding': 0.08}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'minh': 0.3}, 'nodes': {}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm', 'id': 'row_blind', 'minw': 1, 'minh': 3.75}, 'nodes': {}}, 3: contents.dollars_chips, 4: contents.hand, 5: {'n': G.UIT.R, 'config': {'align': 'cm', 'id': 'row_round'}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm'}, 'nodes': contents.buttons}, 2: {'n': G.UIT.C, 'config': {'align': 'cm'}, 'nodes': contents.round}}}}}}}}}
def create_UIBox_blind_select():
    G.blind_prompt_box = UIBox()G.E_MANAGER.add_event()
    width = G.hand.T.w
    G.GAME.blind_on_deck = ((not ((G.GAME.round_resets.blind_states.Small == 'Defeated' if G.GAME.round_resets.blind_states.Small == 'Defeated' else G.GAME.round_resets.blind_states.Small == 'Skipped') if (G.GAME.round_resets.blind_states.Small == 'Defeated' if G.GAME.round_resets.blind_states.Small == 'Defeated' else G.GAME.round_resets.blind_states.Small == 'Skipped') else G.GAME.round_resets.blind_states.Small == 'Hide')) & 'Small' if (not ((G.GAME.round_resets.blind_states.Small == 'Defeated' if G.GAME.round_resets.blind_states.Small == 'Defeated' else G.GAME.round_resets.blind_states.Small == 'Skipped') if (G.GAME.round_resets.blind_states.Small == 'Defeated' if G.GAME.round_resets.blind_states.Small == 'Defeated' else G.GAME.round_resets.blind_states.Small == 'Skipped') else G.GAME.round_resets.blind_states.Small == 'Hide')) & 'Small' else (not ((G.GAME.round_resets.blind_states.Big == 'Defeated' if G.GAME.round_resets.blind_states.Big == 'Defeated' else G.GAME.round_resets.blind_states.Big == 'Skipped') if (G.GAME.round_resets.blind_states.Big == 'Defeated' if G.GAME.round_resets.blind_states.Big == 'Defeated' else G.GAME.round_resets.blind_states.Big == 'Skipped') else G.GAME.round_resets.blind_states.Big == 'Hide')) & 'Big') if ((not ((G.GAME.round_resets.blind_states.Small == 'Defeated' if G.GAME.round_resets.blind_states.Small == 'Defeated' else G.GAME.round_resets.blind_states.Small == 'Skipped') if (G.GAME.round_resets.blind_states.Small == 'Defeated' if G.GAME.round_resets.blind_states.Small == 'Defeated' else G.GAME.round_resets.blind_states.Small == 'Skipped') else G.GAME.round_resets.blind_states.Small == 'Hide')) & 'Small' if (not ((G.GAME.round_resets.blind_states.Small == 'Defeated' if G.GAME.round_resets.blind_states.Small == 'Defeated' else G.GAME.round_resets.blind_states.Small == 'Skipped') if (G.GAME.round_resets.blind_states.Small == 'Defeated' if G.GAME.round_resets.blind_states.Small == 'Defeated' else G.GAME.round_resets.blind_states.Small == 'Skipped') else G.GAME.round_resets.blind_states.Small == 'Hide')) & 'Small' else (not ((G.GAME.round_resets.blind_states.Big == 'Defeated' if G.GAME.round_resets.blind_states.Big == 'Defeated' else G.GAME.round_resets.blind_states.Big == 'Skipped') if (G.GAME.round_resets.blind_states.Big == 'Defeated' if G.GAME.round_resets.blind_states.Big == 'Defeated' else G.GAME.round_resets.blind_states.Big == 'Skipped') else G.GAME.round_resets.blind_states.Big == 'Hide')) & 'Big') else 'Boss'
    G.blind_select_opts = {}
    G.blind_select_opts.small = ("'Small'[G.GAME.round_resets.blind_states]" != 'Hide') & UIBox() if ("'Small'[G.GAME.round_resets.blind_states]" != 'Hide') & UIBox() else 'None'
    G.blind_select_opts.big = ("'Big'[G.GAME.round_resets.blind_states]" != 'Hide') & UIBox() if ("'Big'[G.GAME.round_resets.blind_states]" != 'Hide') & UIBox() else 'None'
    G.blind_select_opts.boss = ("'Boss'[G.GAME.round_resets.blind_states]" != 'Hide') & UIBox() if ("'Boss'[G.GAME.round_resets.blind_states]" != 'Hide') & UIBox() else 'None'
    t = {'n': G.UIT.ROOT, 'config': {'align': 'tm', 'minw': width, 'r': 0.15, 'colour': G.C.CLEAR}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.5}, 'nodes': {1: ("'Small'[G.GAME.round_resets.blind_states]" != 'Hide') & {'n': G.UIT.O, 'config': {'align': 'cm', 'object': G.blind_select_opts.small}} if ("'Small'[G.GAME.round_resets.blind_states]" != 'Hide') & {'n': G.UIT.O, 'config': {'align': 'cm', 'object': G.blind_select_opts.small}} else 'None', 2: ("'Big'[G.GAME.round_resets.blind_states]" != 'Hide') & {'n': G.UIT.O, 'config': {'align': 'cm', 'object': G.blind_select_opts.big}} if ("'Big'[G.GAME.round_resets.blind_states]" != 'Hide') & {'n': G.UIT.O, 'config': {'align': 'cm', 'object': G.blind_select_opts.big}} else 'None', 3: ("'Boss'[G.GAME.round_resets.blind_states]" != 'Hide') & {'n': G.UIT.O, 'config': {'align': 'cm', 'object': G.blind_select_opts.boss}} if ("'Boss'[G.GAME.round_resets.blind_states]" != 'Hide') & {'n': G.UIT.O, 'config': {'align': 'cm', 'object': G.blind_select_opts.boss}} else 'None'}}}}
    return t
def create_UIBox_blind_tag(blind_choice, run_info):
    G.GAME.round_resets.blind_tags = G.GAME.round_resets.blind_tags if G.GAME.round_resets.blind_tags else {}
    if not 'blind_choice[G.GAME.round_resets.blind_tags]':
        return 'None'
    _tag = Tag(blind_choice[G.GAME.round_resets.blind_tags], None, blind_choice)
    _tag_ui = _tag_sprite = _tag.generate_UI()
    _tag_sprite.states.collide.can = not not run_info
    return {'n': G.UIT.R, 'config': {'id': 'tag_container', 'ref_table': _tag, 'align': 'cm'}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'tm', 'minh': 0.65}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(k_or), 'scale': 0.55, 'colour': disabled & G.C.UI.TEXT_INACTIVE if disabled & G.C.UI.TEXT_INACTIVE else G.C.WHITE, 'shadow': not disabled}}}}, 2: {'n': G.UIT.R, 'config': {'id': 'tag_' + blind_choice, 'align': 'cm', 'r': 0.1, 'padding': 0.1, 'minw': 1, 'can_collide': True, 'ref_table': _tag_sprite}, 'nodes': {1: {'n': G.UIT.C, 'config': {'id': 'tag_desc', 'align': 'cm', 'minh': 1}, 'nodes': {1: _tag_ui}}, 2: (not run_info) & {'n': G.UIT.C, 'config': {'align': 'cm', 'colour': G.C.UI.BACKGROUND_INACTIVE, 'minh': 0.6, 'minw': 2, 'maxw': 2, 'padding': 0.07, 'r': 0.1, 'shadow': True, 'hover': True, 'one_press': True, 'button': 'skip_blind', 'func': 'hover_tag_proxy', 'ref_table': _tag}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(b_skip_blind), 'scale': 0.4, 'colour': G.C.UI.TEXT_INACTIVE}}}} if (not run_info) & {'n': G.UIT.C, 'config': {'align': 'cm', 'colour': G.C.UI.BACKGROUND_INACTIVE, 'minh': 0.6, 'minw': 2, 'maxw': 2, 'padding': 0.07, 'r': 0.1, 'shadow': True, 'hover': True, 'one_press': True, 'button': 'skip_blind', 'func': 'hover_tag_proxy', 'ref_table': _tag}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(b_skip_blind), 'scale': 0.4, 'colour': G.C.UI.TEXT_INACTIVE}}}} else {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0.1, 'emboss': 0.05, 'colour': mix_colours(), 'r': 0.1, 'maxw': 2}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(b_skip_reward), 'scale': 0.35, 'colour': G.C.WHITE}}}}}}}}
def create_UIBox_blind_choice(type, run_info):
    if not G.GAME.blind_on_deck:
        G.GAME.blind_on_deck = 'Small'
    if not run_info:
        'G.GAME.blind_on_deck[G.GAME.round_resets.blind_states]' = 'Select'
    disabled = False
    type = type if type else 'Small'
    blind_choice = {'config': 'G.GAME.round_resets.blind_choices[type][G.P_BLINDS]'}
    blind_choice.animation = AnimatedSprite(0, 0, 1.4, 1.4, 'blind_chips'[G.ANIMATION_ATLAS])blind_choice.animation.define_draw_steps()
    extras = 'None'
    stake_sprite = get_stake_sprite()
    G.GAME.orbital_choices = G.GAME.orbital_choices if G.GAME.orbital_choices else {}
    'G.GAME.round_resets.ante[G.GAME.orbital_choices]' = 'G.GAME.round_resets.ante[G.GAME.orbital_choices]' if 'G.GAME.round_resets.ante[G.GAME.orbital_choices]' else {}
    if not 'type[G.GAME.orbital_choices[G.GAME.round_resets.ante]]':
        _poker_hands = {}
        for kv in pairs():
            if v.visible:
                '#_poker_hands + 1[_poker_hands]' = k
        'type[G.GAME.orbital_choices[G.GAME.round_resets.ante]]' = pseudorandom_element(_poker_hands)
    if type == 'Small':
        extras = create_UIBox_blind_tag(type, run_info)
    elif type == 'Big':
        extras = create_UIBox_blind_tag(type, run_info)
    elif not run_info:
        dt1 = DynaText()
        dt2 = DynaText()
        dt3 = DynaText()
        extras = {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.07, 'r': 0.1, 'colour': {1: 0, 2: 0, 3: 0, 4: 0.12}, 'minw': 2.9}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.O, 'config': {'object': dt1}}}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.O, 'config': {'object': dt2}}}}, 3: {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.O, 'config': {'object': dt3}}}}}}}}
    G.GAME.round_resets.blind_ante = G.GAME.round_resets.blind_ante if G.GAME.round_resets.blind_ante else G.GAME.round_resets.ante
    loc_target = localize()
    loc_name = localize()
    text_table = loc_target
    blind_col = get_blind_main_colour(type)
    blind_amt = get_blind_amount() * blind_choice.config.mult * G.GAME.starting_params.ante_scaling
    blind_state = 'type[G.GAME.round_resets.blind_states]'
    _reward = True
    if G.GAME.modifiers.no_blind_reward & 'type[G.GAME.modifiers.no_blind_reward]':
        _reward = 'None'
    if blind_state == 'Select':
        blind_state = 'Current'
    run_info_colour = run_info & (((((blind_state == 'Defeated') & G.C.GREY if (blind_state == 'Defeated') & G.C.GREY else (blind_state == 'Skipped') & G.C.BLUE) if ((blind_state == 'Defeated') & G.C.GREY if (blind_state == 'Defeated') & G.C.GREY else (blind_state == 'Skipped') & G.C.BLUE) else (blind_state == 'Upcoming') & G.C.ORANGE) if (((blind_state == 'Defeated') & G.C.GREY if (blind_state == 'Defeated') & G.C.GREY else (blind_state == 'Skipped') & G.C.BLUE) if ((blind_state == 'Defeated') & G.C.GREY if (blind_state == 'Defeated') & G.C.GREY else (blind_state == 'Skipped') & G.C.BLUE) else (blind_state == 'Upcoming') & G.C.ORANGE) else (blind_state == 'Current') & G.C.RED) if ((((blind_state == 'Defeated') & G.C.GREY if (blind_state == 'Defeated') & G.C.GREY else (blind_state == 'Skipped') & G.C.BLUE) if ((blind_state == 'Defeated') & G.C.GREY if (blind_state == 'Defeated') & G.C.GREY else (blind_state == 'Skipped') & G.C.BLUE) else (blind_state == 'Upcoming') & G.C.ORANGE) if (((blind_state == 'Defeated') & G.C.GREY if (blind_state == 'Defeated') & G.C.GREY else (blind_state == 'Skipped') & G.C.BLUE) if ((blind_state == 'Defeated') & G.C.GREY if (blind_state == 'Defeated') & G.C.GREY else (blind_state == 'Skipped') & G.C.BLUE) else (blind_state == 'Upcoming') & G.C.ORANGE) else (blind_state == 'Current') & G.C.RED) else G.C.GOLD)
    t = {'n': G.UIT.R, 'config': {'id': type, 'align': 'tm', 'func': 'blind_choice_handler', 'minh': (not run_info) & 10 if (not run_info) & 10 else 'None', 'ref_table': {'deck': 'None', 'run_info': run_info}, 'r': 0.1, 'padding': 0.05}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'colour': mix_colours(), 'r': 0.1, 'outline': 1, 'outline_colour': G.C.L_BLACK}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.2}, 'nodes': {1: (not run_info) & {'n': G.UIT.R, 'config': {'id': 'select_blind_button', 'align': 'cm', 'ref_table': blind_choice.config, 'colour': disabled & G.C.UI.BACKGROUND_INACTIVE if disabled & G.C.UI.BACKGROUND_INACTIVE else G.C.ORANGE, 'minh': 0.6, 'minw': 2.7, 'padding': 0.07, 'r': 0.1, 'shadow': True, 'hover': True, 'one_press': True, 'button': 'select_blind'}, 'nodes': {1: {'n': G.UIT.T, 'config': {'ref_table': G.GAME.round_resets.loc_blind_states, 'ref_value': type, 'scale': 0.45, 'colour': disabled & G.C.UI.TEXT_INACTIVE if disabled & G.C.UI.TEXT_INACTIVE else G.C.UI.TEXT_LIGHT, 'shadow': not disabled}}}} if (not run_info) & {'n': G.UIT.R, 'config': {'id': 'select_blind_button', 'align': 'cm', 'ref_table': blind_choice.config, 'colour': disabled & G.C.UI.BACKGROUND_INACTIVE if disabled & G.C.UI.BACKGROUND_INACTIVE else G.C.ORANGE, 'minh': 0.6, 'minw': 2.7, 'padding': 0.07, 'r': 0.1, 'shadow': True, 'hover': True, 'one_press': True, 'button': 'select_blind'}, 'nodes': {1: {'n': G.UIT.T, 'config': {'ref_table': G.GAME.round_resets.loc_blind_states, 'ref_value': type, 'scale': 0.45, 'colour': disabled & G.C.UI.TEXT_INACTIVE if disabled & G.C.UI.TEXT_INACTIVE else G.C.UI.TEXT_LIGHT, 'shadow': not disabled}}}} else {'n': G.UIT.R, 'config': {'id': 'select_blind_button', 'align': 'cm', 'ref_table': blind_choice.config, 'colour': run_info_colour, 'minh': 0.6, 'minw': 2.7, 'padding': 0.07, 'r': 0.1, 'emboss': 0.08}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(blind_state, blind_states), 'scale': 0.45, 'colour': G.C.UI.TEXT_LIGHT, 'shadow': True}}}}}}, 2: {'n': G.UIT.R, 'config': {'id': 'blind_name', 'align': 'cm', 'padding': 0.07}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'r': 0.1, 'outline': 1, 'outline_colour': blind_col, 'colour': darken(blind_col, 0.3), 'minw': 2.9, 'emboss': 0.1, 'padding': 0.07, 'line_emboss': 1}, 'nodes': {1: {'n': G.UIT.O, 'config': {'object': DynaText()}}}}}}, 3: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.05}, 'nodes': {1: {'n': G.UIT.R, 'config': {'id': 'blind_desc', 'align': 'cm', 'padding': 0.05}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'minh': 1.5}, 'nodes': {1: {'n': G.UIT.O, 'config': {'object': blind_choice.animation}}}}, 2: '1[text_table]' & {'n': G.UIT.R, 'config': {'align': 'cm', 'minh': 0.7, 'padding': 0.05, 'minw': 2.9}, 'nodes': {1: '1[text_table]' & {'n': G.UIT.R, 'config': {'align': 'cm', 'maxw': 2.8}, 'nodes': {1: {'n': G.UIT.T, 'config': {'id': blind_choice.config.key, 'ref_table': {'val': ''}, 'ref_value': 'val', 'scale': 0.32, 'colour': disabled & G.C.UI.TEXT_INACTIVE if disabled & G.C.UI.TEXT_INACTIVE else G.C.WHITE, 'shadow': not disabled, 'func': 'HUD_blind_debuff_prefix'}}, 2: {'n': G.UIT.T, 'config': {'text': '1[text_table]' if '1[text_table]' else '-', 'scale': 0.32, 'colour': disabled & G.C.UI.TEXT_INACTIVE if disabled & G.C.UI.TEXT_INACTIVE else G.C.WHITE, 'shadow': not disabled}}}} if '1[text_table]' & {'n': G.UIT.R, 'config': {'align': 'cm', 'maxw': 2.8}, 'nodes': {1: {'n': G.UIT.T, 'config': {'id': blind_choice.config.key, 'ref_table': {'val': ''}, 'ref_value': 'val', 'scale': 0.32, 'colour': disabled & G.C.UI.TEXT_INACTIVE if disabled & G.C.UI.TEXT_INACTIVE else G.C.WHITE, 'shadow': not disabled, 'func': 'HUD_blind_debuff_prefix'}}, 2: {'n': G.UIT.T, 'config': {'text': '1[text_table]' if '1[text_table]' else '-', 'scale': 0.32, 'colour': disabled & G.C.UI.TEXT_INACTIVE if disabled & G.C.UI.TEXT_INACTIVE else G.C.WHITE, 'shadow': not disabled}}}} else 'None', 2: '2[text_table]' & {'n': G.UIT.R, 'config': {'align': 'cm', 'maxw': 2.8}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': '2[text_table]' if '2[text_table]' else '-', 'scale': 0.32, 'colour': disabled & G.C.UI.TEXT_INACTIVE if disabled & G.C.UI.TEXT_INACTIVE else G.C.WHITE, 'shadow': not disabled}}}} if '2[text_table]' & {'n': G.UIT.R, 'config': {'align': 'cm', 'maxw': 2.8}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': '2[text_table]' if '2[text_table]' else '-', 'scale': 0.32, 'colour': disabled & G.C.UI.TEXT_INACTIVE if disabled & G.C.UI.TEXT_INACTIVE else G.C.WHITE, 'shadow': not disabled}}}} else 'None'}} if '1[text_table]' & {'n': G.UIT.R, 'config': {'align': 'cm', 'minh': 0.7, 'padding': 0.05, 'minw': 2.9}, 'nodes': {1: '1[text_table]' & {'n': G.UIT.R, 'config': {'align': 'cm', 'maxw': 2.8}, 'nodes': {1: {'n': G.UIT.T, 'config': {'id': blind_choice.config.key, 'ref_table': {'val': ''}, 'ref_value': 'val', 'scale': 0.32, 'colour': disabled & G.C.UI.TEXT_INACTIVE if disabled & G.C.UI.TEXT_INACTIVE else G.C.WHITE, 'shadow': not disabled, 'func': 'HUD_blind_debuff_prefix'}}, 2: {'n': G.UIT.T, 'config': {'text': '1[text_table]' if '1[text_table]' else '-', 'scale': 0.32, 'colour': disabled & G.C.UI.TEXT_INACTIVE if disabled & G.C.UI.TEXT_INACTIVE else G.C.WHITE, 'shadow': not disabled}}}} if '1[text_table]' & {'n': G.UIT.R, 'config': {'align': 'cm', 'maxw': 2.8}, 'nodes': {1: {'n': G.UIT.T, 'config': {'id': blind_choice.config.key, 'ref_table': {'val': ''}, 'ref_value': 'val', 'scale': 0.32, 'colour': disabled & G.C.UI.TEXT_INACTIVE if disabled & G.C.UI.TEXT_INACTIVE else G.C.WHITE, 'shadow': not disabled, 'func': 'HUD_blind_debuff_prefix'}}, 2: {'n': G.UIT.T, 'config': {'text': '1[text_table]' if '1[text_table]' else '-', 'scale': 0.32, 'colour': disabled & G.C.UI.TEXT_INACTIVE if disabled & G.C.UI.TEXT_INACTIVE else G.C.WHITE, 'shadow': not disabled}}}} else 'None', 2: '2[text_table]' & {'n': G.UIT.R, 'config': {'align': 'cm', 'maxw': 2.8}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': '2[text_table]' if '2[text_table]' else '-', 'scale': 0.32, 'colour': disabled & G.C.UI.TEXT_INACTIVE if disabled & G.C.UI.TEXT_INACTIVE else G.C.WHITE, 'shadow': not disabled}}}} if '2[text_table]' & {'n': G.UIT.R, 'config': {'align': 'cm', 'maxw': 2.8}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': '2[text_table]' if '2[text_table]' else '-', 'scale': 0.32, 'colour': disabled & G.C.UI.TEXT_INACTIVE if disabled & G.C.UI.TEXT_INACTIVE else G.C.WHITE, 'shadow': not disabled}}}} else 'None'}} else 'None'}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm', 'r': 0.1, 'padding': 0.05, 'minw': 3.1, 'colour': G.C.BLACK, 'emboss': 0.05}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'maxw': 3}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(ph_blind_score_at_least), 'scale': 0.3, 'colour': disabled & G.C.UI.TEXT_INACTIVE if disabled & G.C.UI.TEXT_INACTIVE else G.C.WHITE, 'shadow': not disabled}}}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm', 'minh': 0.6}, 'nodes': {1: {'n': G.UIT.O, 'config': {'w': 0.5, 'h': 0.5, 'colour': G.C.BLUE, 'object': stake_sprite, 'hover': True, 'can_collide': False}}, 2: {'n': G.UIT.B, 'config': {'h': 0.1, 'w': 0.1}}, 3: {'n': G.UIT.T, 'config': {'text': number_format(blind_amt), 'scale': score_number_scale(0.9, blind_amt), 'colour': disabled & G.C.UI.TEXT_INACTIVE if disabled & G.C.UI.TEXT_INACTIVE else G.C.RED, 'shadow': not disabled}}}}, 3: _reward & {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(ph_blind_reward), 'scale': 0.35, 'colour': disabled & G.C.UI.TEXT_INACTIVE if disabled & G.C.UI.TEXT_INACTIVE else G.C.WHITE, 'shadow': not disabled}}, 2: {'n': G.UIT.T, 'config': {'text': string.rep() + '+', 'scale': 0.35, 'colour': disabled & G.C.UI.TEXT_INACTIVE if disabled & G.C.UI.TEXT_INACTIVE else G.C.MONEY, 'shadow': not disabled}}}} if _reward & {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(ph_blind_reward), 'scale': 0.35, 'colour': disabled & G.C.UI.TEXT_INACTIVE if disabled & G.C.UI.TEXT_INACTIVE else G.C.WHITE, 'shadow': not disabled}}, 2: {'n': G.UIT.T, 'config': {'text': string.rep() + '+', 'scale': 0.35, 'colour': disabled & G.C.UI.TEXT_INACTIVE if disabled & G.C.UI.TEXT_INACTIVE else G.C.MONEY, 'shadow': not disabled}}}} else 'None'}}}}}}}}, 2: {'n': G.UIT.R, 'config': {'id': 'blind_extras', 'align': 'cm'}, 'nodes': {1: extras}}}}
    return t
def create_UIBox_round_evaluation():
    width = G.hand.T.w - 2
    t = {'n': G.UIT.ROOT, 'config': {'align': 'tm', 'colour': G.C.CLEAR}, 'nodes': {1: UIBox_dyn_container()}}
    return t
def create_UIBox_arcana_pack():
    _size = G.GAME.pack_size
    G.pack_cards = CardArea()
    t = {'n': G.UIT.ROOT, 'config': {'align': 'tm', 'r': 0.15, 'colour': G.C.CLEAR, 'padding': 0.15}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cl', 'colour': G.C.CLEAR, 'r': 0.15, 'padding': 0.1, 'minh': 2, 'shadow': True}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0.1}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'r': 0.2, 'colour': G.C.CLEAR, 'shadow': True}, 'nodes': {1: {'n': G.UIT.O, 'config': {'object': G.pack_cards}}}}}}}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {}}, 3: {'n': G.UIT.R, 'config': {'align': 'tm'}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'tm', 'padding': 0.05, 'minw': 2.4}, 'nodes': {}}, 2: {'n': G.UIT.C, 'config': {'align': 'tm', 'padding': 0.05}, 'nodes': {1: UIBox_dyn_container()}}, 3: {'n': G.UIT.C, 'config': {'align': 'tm', 'padding': 0.05, 'minw': 2.4}, 'nodes': {1: {'n': G.UIT.R, 'config': {'minh': 0.2}, 'nodes': {}}, 2: {'n': G.UIT.R, 'config': {'align': 'tm', 'padding': 0.2, 'minh': 1.2, 'minw': 1.8, 'r': 0.15, 'colour': G.C.GREY, 'one_press': True, 'button': 'skip_booster', 'hover': True, 'shadow': True, 'func': 'can_skip_booster'}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(b_skip), 'scale': 0.5, 'colour': G.C.WHITE, 'shadow': True, 'focus_args': {'button': 'y', 'orientation': 'bm'}, 'func': 'set_button_pip'}}}}}}}}}}}}
    return t
def create_UIBox_spectral_pack():
    _size = G.GAME.pack_size
    G.pack_cards = CardArea()
    t = {'n': G.UIT.ROOT, 'config': {'align': 'tm', 'r': 0.15, 'colour': G.C.CLEAR, 'padding': 0.15}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cl', 'colour': G.C.CLEAR, 'r': 0.15, 'padding': 0.1, 'minh': 2, 'shadow': True}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0.1}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'r': 0.2, 'colour': G.C.CLEAR, 'shadow': True}, 'nodes': {1: {'n': G.UIT.O, 'config': {'object': G.pack_cards}}}}}}}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {}}, 3: {'n': G.UIT.R, 'config': {'align': 'tm'}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'tm', 'padding': 0.05, 'minw': 2.4}, 'nodes': {}}, 2: {'n': G.UIT.C, 'config': {'align': 'tm', 'padding': 0.05}, 'nodes': {1: UIBox_dyn_container()}}, 3: {'n': G.UIT.C, 'config': {'align': 'tm', 'padding': 0.05, 'minw': 2.4}, 'nodes': {1: {'n': G.UIT.R, 'config': {'minh': 0.2}, 'nodes': {}}, 2: {'n': G.UIT.R, 'config': {'align': 'tm', 'padding': 0.2, 'minh': 1.2, 'minw': 1.8, 'r': 0.15, 'colour': G.C.GREY, 'one_press': True, 'button': 'skip_booster', 'hover': True, 'shadow': True, 'func': 'can_skip_booster'}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(b_skip), 'scale': 0.5, 'colour': G.C.WHITE, 'shadow': True, 'focus_args': {'button': 'y', 'orientation': 'bm'}, 'func': 'set_button_pip'}}}}}}}}}}}}
    return t
def create_UIBox_standard_pack():
    _size = G.GAME.pack_size
    G.pack_cards = CardArea()
    t = {'n': G.UIT.ROOT, 'config': {'align': 'tm', 'r': 0.15, 'colour': G.C.CLEAR, 'padding': 0.15}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cl', 'colour': G.C.CLEAR, 'r': 0.15, 'padding': 0.1, 'minh': 2, 'shadow': True}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0.1}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'r': 0.2, 'colour': G.C.CLEAR, 'shadow': True}, 'nodes': {1: {'n': G.UIT.O, 'config': {'object': G.pack_cards}}}}}}}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {}}, 3: {'n': G.UIT.R, 'config': {'align': 'tm'}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'tm', 'padding': 0.05, 'minw': 2.4}, 'nodes': {}}, 2: {'n': G.UIT.C, 'config': {'align': 'tm', 'padding': 0.05}, 'nodes': {1: UIBox_dyn_container()}}, 3: {'n': G.UIT.C, 'config': {'align': 'tm', 'padding': 0.05, 'minw': 2.4}, 'nodes': {1: {'n': G.UIT.R, 'config': {'minh': 0.2}, 'nodes': {}}, 2: {'n': G.UIT.R, 'config': {'align': 'tm', 'padding': 0.2, 'minh': 1.2, 'minw': 1.8, 'r': 0.15, 'colour': G.C.GREY, 'one_press': True, 'button': 'skip_booster', 'hover': True, 'shadow': True, 'func': 'can_skip_booster'}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(b_skip), 'scale': 0.5, 'colour': G.C.WHITE, 'shadow': True, 'focus_args': {'button': 'y', 'orientation': 'bm'}, 'func': 'set_button_pip'}}}}}}}}}}}}
    return t
def create_UIBox_buffoon_pack():
    _size = G.GAME.pack_size
    G.pack_cards = CardArea()
    t = {'n': G.UIT.ROOT, 'config': {'align': 'tm', 'r': 0.15, 'colour': G.C.CLEAR, 'padding': 0.15}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cl', 'colour': G.C.CLEAR, 'r': 0.15, 'padding': 0.1, 'minh': 2, 'shadow': True}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0.1}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'r': 0.2, 'colour': G.C.CLEAR, 'shadow': True}, 'nodes': {1: {'n': G.UIT.O, 'config': {'object': G.pack_cards}}}}}}}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {}}, 3: {'n': G.UIT.R, 'config': {'align': 'tm'}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'tm', 'padding': 0.05, 'minw': 2.4}, 'nodes': {}}, 2: {'n': G.UIT.C, 'config': {'align': 'tm', 'padding': 0.05}, 'nodes': {1: UIBox_dyn_container()}}, 3: {'n': G.UIT.C, 'config': {'align': 'tm', 'padding': 0.05, 'minw': 2.4}, 'nodes': {1: {'n': G.UIT.R, 'config': {'minh': 0.2}, 'nodes': {}}, 2: {'n': G.UIT.R, 'config': {'align': 'tm', 'padding': 0.2, 'minh': 1.2, 'minw': 1.8, 'r': 0.15, 'colour': G.C.GREY, 'one_press': True, 'button': 'skip_booster', 'hover': True, 'shadow': True, 'func': 'can_skip_booster'}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(b_skip), 'scale': 0.5, 'colour': G.C.WHITE, 'shadow': True, 'focus_args': {'button': 'y', 'orientation': 'bm'}, 'func': 'set_button_pip'}}}}}}}}}}}}
    return t
def create_UIBox_celestial_pack():
    _size = G.GAME.pack_size
    G.pack_cards = CardArea()
    t = {'n': G.UIT.ROOT, 'config': {'align': 'tm', 'r': 0.15, 'colour': G.C.CLEAR, 'padding': 0.15}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cl', 'colour': G.C.CLEAR, 'r': 0.15, 'padding': 0.1, 'minh': 2, 'shadow': True}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0.1}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'r': 0.2, 'colour': G.C.CLEAR, 'shadow': True}, 'nodes': {1: {'n': G.UIT.O, 'config': {'object': G.pack_cards}}}}}}}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {}}, 3: {'n': G.UIT.R, 'config': {'align': 'tm'}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'tm', 'padding': 0.05, 'minw': 2.4}, 'nodes': {}}, 2: {'n': G.UIT.C, 'config': {'align': 'tm', 'padding': 0.05}, 'nodes': {1: UIBox_dyn_container()}}, 3: {'n': G.UIT.C, 'config': {'align': 'tm', 'padding': 0.05, 'minw': 2.4}, 'nodes': {1: {'n': G.UIT.R, 'config': {'minh': 0.2}, 'nodes': {}}, 2: {'n': G.UIT.R, 'config': {'align': 'tm', 'padding': 0.2, 'minh': 1.2, 'minw': 1.8, 'r': 0.15, 'colour': G.C.GREY, 'one_press': True, 'button': 'skip_booster', 'hover': True, 'shadow': True, 'func': 'can_skip_booster'}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(b_skip), 'scale': 0.5, 'colour': G.C.WHITE, 'shadow': True, 'focus_args': {'button': 'y', 'orientation': 'bm'}, 'func': 'set_button_pip'}}}}}}}}}}}}
    return t
def create_UIBox_card_alert(args):
    args = args if args else {}
    return {'n': G.UIT.ROOT, 'config': {'align': 'cm', 'colour': G.C.CLEAR, 'refresh_movement': True}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'r': 0.15, 'minw': 0.42, 'minh': 0.42, 'colour': (args.no_bg & G.C.CLEAR if args.no_bg & G.C.CLEAR else args.bg_col) if (args.no_bg & G.C.CLEAR if args.no_bg & G.C.CLEAR else args.bg_col) else args.red_bad & darken() if args.red_bad & darken() else G.C.RED, 'draw_layer': 1, 'emboss': 0.05, 'refresh_movement': True}, 'nodes': {1: {'n': G.UIT.O, 'config': {'object': DynaText()}}}}}}
def create_slider(args):
    args = args if args else {}
    args.colour = args.colour if args.colour else G.C.RED
    args.w = args.w if args.w else 1
    args.h = args.h if args.h else 0.5
    args.label_scale = args.label_scale if args.label_scale else 0.5
    args.text_scale = args.text_scale if args.text_scale else 0.3
    args.min = args.min if args.min else 0
    args.max = args.max if args.max else 1
    args.decimal_places = args.decimal_places if args.decimal_places else 0
    args.text = string.format()
    startval = args.w * ('args.ref_value[args.ref_table]' - args.min) / (args.max - args.min)
    t = {'n': G.UIT.C, 'config': {'align': 'cm', 'minw': args.w, 'min_h': args.h, 'padding': 0.1, 'r': 0.1, 'colour': G.C.CLEAR, 'focus_args': {'type': 'slider'}}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cl', 'minw': args.w, 'r': 0.1, 'min_h': args.h, 'collideable': True, 'hover': True, 'colour': G.C.BLACK, 'emboss': 0.05, 'func': 'slider', 'refresh_movement': True}, 'nodes': {1: {'n': G.UIT.B, 'config': {'w': startval, 'h': args.h, 'r': 0.1, 'colour': args.colour, 'ref_table': args, 'refresh_movement': True}}}}, 2: {'n': G.UIT.C, 'config': {'align': 'cm', 'minh': args.h, 'r': 0.1, 'minw': 0.8, 'colour': args.colour, 'shadow': True}, 'nodes': {1: {'n': G.UIT.T, 'config': {'ref_table': args, 'ref_value': 'text', 'scale': args.text_scale, 'colour': G.C.UI.TEXT_LIGHT, 'decimal_places': args.decimal_places}}}}}}
    if args.label:
        t = {'n': G.UIT.R, 'config': {'align': 'cm', 'minh': 1, 'minw': 1, 'padding': 0.1 * args.label_scale, 'colour': G.C.CLEAR}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': args.label, 'scale': args.label_scale, 'colour': G.C.UI.TEXT_LIGHT}}}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0}, 'nodes': {1: t}}}}
    return t
def create_toggle(args):
    args = args if args else {}
    args.active_colour = args.active_colour if args.active_colour else G.C.RED
    args.inactive_colour = args.inactive_colour if args.inactive_colour else G.C.BLACK
    args.w = args.w if args.w else 3
    args.h = args.h if args.h else 0.5
    args.scale = args.scale if args.scale else 1
    args.label = args.label if args.label else 'TEST?'
    args.label_scale = args.label_scale if args.label_scale else 0.4
    args.ref_table = args.ref_table if args.ref_table else {}
    args.ref_value = args.ref_value if args.ref_value else 'test'
    check = Sprite(0, 0)
    check.states.drag.can = False
    check.states.visible = False
    info = 'None'
    if args.info:
        info = {}
        for kv in ipairs():table.insert(info)
        info = {'n': G.UIT.R, 'config': {'align': 'cm', 'minh': 0.05}, 'nodes': info}
    t = {'n': args.col & G.UIT.C if args.col & G.UIT.C else G.UIT.R, 'config': {'align': 'cm', 'padding': 0.1, 'r': 0.1, 'colour': G.C.CLEAR, 'focus_args': {'funnel_from': True}}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cr', 'minw': args.w}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': args.label, 'scale': args.label_scale, 'colour': G.C.UI.TEXT_LIGHT}}, 2: {'n': G.UIT.B, 'config': {'w': 0.1, 'h': 0.1}}}}, 2: {'n': G.UIT.C, 'config': {'align': 'cl', 'minw': 0.3 * args.w}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'r': 0.1, 'colour': G.C.BLACK}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'r': 0.1, 'padding': 0.03, 'minw': 0.4 * args.scale, 'minh': 0.4 * args.scale, 'outline_colour': G.C.WHITE, 'outline': 1.2 * args.scale, 'line_emboss': 0.5 * args.scale, 'ref_table': args, 'colour': args.inactive_colour, 'button': 'toggle_button', 'button_dist': 0.2, 'hover': True, 'toggle_callback': args.callback, 'func': 'toggle', 'focus_args': {'funnel_to': True}}, 'nodes': {1: {'n': G.UIT.O, 'config': {'object': check}}}}}}}}}}
    if args.info:
        t = {'n': args.col & G.UIT.C if args.col & G.UIT.C else G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: t, 2: info}}
    return t
def create_option_cycle(args):
    args = args if args else {}
    args.colour = args.colour if args.colour else G.C.RED
    args.options = args.options if args.options else {1: 'Option 1', 2: 'Option 2'}
    args.current_option = args.current_option if args.current_option else 1
    args.current_option_val = 'args.current_option[args.options]'
    args.opt_callback = args.opt_callback if args.opt_callback else 'None'
    args.scale = args.scale if args.scale else 1
    args.ref_table = args.ref_table if args.ref_table else 'None'
    args.ref_value = args.ref_value if args.ref_value else 'None'
    args.w = (args.w if args.w else 2.5) * args.scale
    args.h = (args.h if args.h else 0.8) * args.scale
    args.text_scale = (args.text_scale if args.text_scale else 0.5) * args.scale
    args.l = '<'
    args.r = '>'
    args.focus_args = args.focus_args if args.focus_args else {}
    args.focus_args.type = 'cycle'
    info = 'None'
    if args.info:
        info = {}
        for kv in ipairs():table.insert(info)
        info = {'n': G.UIT.R, 'config': {'align': 'cm', 'minh': 0.05}, 'nodes': info}
    disabled = len(args.options < 2)
    pips = {}
    for i in range(1, len(args.options), ):
        '#pips + 1[pips]' = {'n': G.UIT.B, 'config': {'w': 0.1 * args.scale, 'h': 0.1 * args.scale, 'r': 0.05, 'id': 'pip_' + i, 'colour': (args.current_option == i) & G.C.WHITE if (args.current_option == i) & G.C.WHITE else G.C.BLACK}}
    choice_pips = (not args.no_pips) & {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': (0.05 - len((args.options > 15) & 0.03 if (args.options > 15) & 0.03 else 0)) * args.scale}, 'nodes': pips} if (not args.no_pips) & {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': (0.05 - len((args.options > 15) & 0.03 if (args.options > 15) & 0.03 else 0)) * args.scale}, 'nodes': pips} else 'None'
    t = {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0.1, 'r': 0.1, 'colour': G.C.CLEAR, 'id': args.id & ((not args.label) & args.id if (not args.label) & args.id else 'None') if args.id & ((not args.label) & args.id if (not args.label) & args.id else 'None') else 'None', 'focus_args': args.focus_args}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'r': 0.1, 'minw': 0.6 * args.scale, 'hover': not disabled, 'colour': (not disabled) & args.colour if (not disabled) & args.colour else G.C.BLACK, 'shadow': not disabled, 'button': (not disabled) & 'option_cycle' if (not disabled) & 'option_cycle' else 'None', 'ref_table': args, 'ref_value': 'l', 'focus_args': {'type': 'none'}}, 'nodes': {1: {'n': G.UIT.T, 'config': {'ref_table': args, 'ref_value': 'l', 'scale': args.text_scale, 'colour': (not disabled) & G.C.UI.TEXT_LIGHT if (not disabled) & G.C.UI.TEXT_LIGHT else G.C.UI.TEXT_INACTIVE}}}}, 2: args.mid & {'n': G.UIT.C, 'config': {'id': 'cycle_main'}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'minh': 0.05}, 'nodes': {1: args.mid}}, 2: (not disabled) & choice_pips if (not disabled) & choice_pips else 'None'}} if args.mid & {'n': G.UIT.C, 'config': {'id': 'cycle_main'}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'minh': 0.05}, 'nodes': {1: args.mid}}, 2: (not disabled) & choice_pips if (not disabled) & choice_pips else 'None'}} else {'n': G.UIT.C, 'config': {'id': 'cycle_main', 'align': 'cm', 'minw': args.w, 'minh': args.h, 'r': 0.1, 'padding': 0.05, 'colour': args.colour, 'emboss': 0.1, 'hover': True, 'can_collide': True, 'on_demand_tooltip': args.on_demand_tooltip}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.O, 'config': {'object': DynaText()}}}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm', 'minh': 0.05}, 'nodes': {}}, 3: (not disabled) & choice_pips if (not disabled) & choice_pips else 'None'}}}}, 3: {'n': G.UIT.C, 'config': {'align': 'cm', 'r': 0.1, 'minw': 0.6 * args.scale, 'hover': not disabled, 'colour': (not disabled) & args.colour if (not disabled) & args.colour else G.C.BLACK, 'shadow': not disabled, 'button': (not disabled) & 'option_cycle' if (not disabled) & 'option_cycle' else 'None', 'ref_table': args, 'ref_value': 'r', 'focus_args': {'type': 'none'}}, 'nodes': {1: {'n': G.UIT.T, 'config': {'ref_table': args, 'ref_value': 'r', 'scale': args.text_scale, 'colour': (not disabled) & G.C.UI.TEXT_LIGHT if (not disabled) & G.C.UI.TEXT_LIGHT else G.C.UI.TEXT_INACTIVE}}}}}}
    if args.cycle_shoulders:
        t = {'n': G.UIT.R, 'config': {'align': 'cm', 'colour': G.C.CLEAR}, 'nodes': {1: {'n': G.UIT.C, 'config': {'minw': 0.7, 'align': 'cm', 'colour': G.C.CLEAR, 'func': 'set_button_pip', 'focus_args': {'button': 'leftshoulder', 'type': 'none', 'orientation': 'cm', 'scale': 0.7, 'offset': {'x': -0.1, 'y': 0}}}, 'nodes': {}}, 2: {'n': G.UIT.C, 'config': {'id': 'cycle_shoulders', 'padding': 0.1}, 'nodes': {1: t}}, 3: {'n': G.UIT.C, 'config': {'minw': 0.7, 'align': 'cm', 'colour': G.C.CLEAR, 'func': 'set_button_pip', 'focus_args': {'button': 'rightshoulder', 'type': 'none', 'orientation': 'cm', 'scale': 0.7, 'offset': {'x': 0.1, 'y': 0}}}, 'nodes': {}}}}
    else:
        t = {'n': G.UIT.R, 'config': {'align': 'cm', 'colour': G.C.CLEAR, 'padding': 0.0}, 'nodes': {1: t}}
    if args.label if args.label else args.info:
        t = {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.05, 'id': args.id if args.id else 'None'}, 'nodes': {1: args.label & {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': args.label, 'scale': 0.5 * args.scale, 'colour': G.C.UI.TEXT_LIGHT}}}} if args.label & {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': args.label, 'scale': 0.5 * args.scale, 'colour': G.C.UI.TEXT_LIGHT}}}} else 'None', 2: t, 3: info}}
    return t
def create_tabs(args):
    args = args if args else {}
    args.colour = args.colour if args.colour else G.C.RED
    args.tab_alignment = args.tab_alignment if args.tab_alignment else 'cm'
    args.opt_callback = args.opt_callback if args.opt_callback else 'None'
    args.scale = args.scale if args.scale else 1
    args.tab_w = args.tab_w if args.tab_w else 0
    args.tab_h = args.tab_h if args.tab_h else 0
    args.text_scale = args.text_scale if args.text_scale else 0.5
    args.tabs = args.tabs if args.tabs else {1: {'label': 'tab 1', 'chosen': True, 'func': 'None', 'tab_definition_function': lambda: 
    return {'n': G.UIT.ROOT, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': 'A', 'scale': 1, 'colour': G.C.UI.TEXT_LIGHT}}}}}, 2: {'label': 'tab 2', 'chosen': False, 'tab_definition_function': lambda: 
    return {'n': G.UIT.ROOT, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': 'B', 'scale': 1, 'colour': G.C.UI.TEXT_LIGHT}}}}}, 3: {'label': 'tab 3', 'chosen': False, 'tab_definition_function': lambda: 
    return {'n': G.UIT.ROOT, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': 'C', 'scale': 1, 'colour': G.C.UI.TEXT_LIGHT}}}}}}
    tab_buttons = {}
    for kv in ipairs():
        if v.chosen:
            args.current = {'k': k, 'v': v}
        '#tab_buttons + 1[tab_buttons]' = UIBox_button()
    t = {'n': G.UIT.R, 'config': {'padding': 0.0, 'align': 'cm', 'colour': G.C.CLEAR}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'colour': G.C.CLEAR}, 'nodes': {1: len((args.tabs > 1) & (not args.no_shoulders)) & {'n': G.UIT.C, 'config': {'minw': 0.7, 'align': 'cm', 'colour': G.C.CLEAR, 'func': 'set_button_pip', 'focus_args': {'button': 'leftshoulder', 'type': 'none', 'orientation': 'cm', 'scale': 0.7, 'offset': {'x': -0.1, 'y': 0}}}, 'nodes': {}} if len((args.tabs > 1) & (not args.no_shoulders)) & {'n': G.UIT.C, 'config': {'minw': 0.7, 'align': 'cm', 'colour': G.C.CLEAR, 'func': 'set_button_pip', 'focus_args': {'button': 'leftshoulder', 'type': 'none', 'orientation': 'cm', 'scale': 0.7, 'offset': {'x': -0.1, 'y': 0}}}, 'nodes': {}} else 'None', 2: {'n': G.UIT.C, 'config': {'id': args.no_shoulders & 'no_shoulders' if args.no_shoulders & 'no_shoulders' else 'tab_shoulders', 'ref_table': args, 'align': 'cm', 'padding': 0.15, 'group': 1, 'collideable': True, 'focus_args': len((args.tabs > 1) & {'type': 'tab', 'nav': 'wide', 'snap_to': args.snap_to_nav, 'no_loop': args.no_loop} if (args.tabs > 1) & {'type': 'tab', 'nav': 'wide', 'snap_to': args.snap_to_nav, 'no_loop': args.no_loop} else 'None')}, 'nodes': tab_buttons}, 3: len((args.tabs > 1) & (not args.no_shoulders)) & {'n': G.UIT.C, 'config': {'minw': 0.7, 'align': 'cm', 'colour': G.C.CLEAR, 'func': 'set_button_pip', 'focus_args': {'button': 'rightshoulder', 'type': 'none', 'orientation': 'cm', 'scale': 0.7, 'offset': {'x': 0.1, 'y': 0}}}, 'nodes': {}} if len((args.tabs > 1) & (not args.no_shoulders)) & {'n': G.UIT.C, 'config': {'minw': 0.7, 'align': 'cm', 'colour': G.C.CLEAR, 'func': 'set_button_pip', 'focus_args': {'button': 'rightshoulder', 'type': 'none', 'orientation': 'cm', 'scale': 0.7, 'offset': {'x': 0.1, 'y': 0}}}, 'nodes': {}} else 'None'}}, 2: {'n': G.UIT.R, 'config': {'align': args.tab_alignment, 'padding': args.padding if args.padding else 0.1, 'no_fill': True, 'minh': args.tab_h, 'minw': args.tab_w}, 'nodes': {1: {'n': G.UIT.O, 'config': {'id': 'tab_contents', 'object': UIBox()}}}}}}
    return t
def create_text_input(args):
    args = args if args else {}
    args.colour = copy_table() if copy_table() else copy_table()
    args.hooked_colour = copy_table() if copy_table() else darken()
    args.w = args.w if args.w else 2.5
    args.h = args.h if args.h else 0.7
    args.text_scale = args.text_scale if args.text_scale else 0.4
    args.max_length = args.max_length if args.max_length else 16
    args.all_caps = args.all_caps if args.all_caps else False
    args.prompt_text = args.prompt_text if args.prompt_text else localize(k_enter_text)
    args.current_prompt_text = ''
    text = {'ref_table': args.ref_table, 'ref_value': args.ref_value, 'letters': {}, 'current_position': string.len(args.ref_value[args.ref_table])}
    ui_letters = {}
    for i in range(1, args.max_length, ):
        'i[text.letters]' = 'args.ref_value[args.ref_table]' & (string.sub(args.ref_value[args.ref_table], i, i) if string.sub(args.ref_value[args.ref_table], i, i) else '') if 'args.ref_value[args.ref_table]' & (string.sub(args.ref_value[args.ref_table], i, i) if string.sub(args.ref_value[args.ref_table], i, i) else '') else ''
        'i[ui_letters]' = {'n': G.UIT.T, 'config': {'ref_table': text.letters, 'ref_value': i, 'scale': args.text_scale, 'colour': G.C.UI.TEXT_LIGHT, 'id': 'letter_' + i}}
    args.text = text
    position_text_colour = lighten()
    '#ui_letters + 1[ui_letters]' = {'n': G.UIT.T, 'config': {'ref_table': args, 'ref_value': 'current_prompt_text', 'scale': args.text_scale, 'colour': lighten(), 'id': 'prompt'}}
    '#ui_letters + 1[ui_letters]' = {'n': G.UIT.B, 'config': {'r': 0.03, 'w': 0.1, 'h': 0.4, 'colour': position_text_colour, 'id': 'position', 'func': 'flash'}}
    t = {'n': G.UIT.C, 'config': {'align': 'cm', 'draw_layer': 1, 'colour': G.C.CLEAR}, 'nodes': {1: {'n': G.UIT.C, 'config': {'id': 'text_input', 'align': 'cm', 'padding': 0.05, 'r': 0.1, 'draw_layer': 2, 'hover': True, 'colour': args.colour, 'minw': args.w, 'min_h': args.h, 'button': 'select_text_input', 'shadow': True}, 'nodes': {1: {'n': G.UIT.R, 'config': {'ref_table': args, 'padding': 0.05, 'align': 'cm', 'r': 0.1, 'colour': G.C.CLEAR}, 'nodes': {1: {'n': G.UIT.R, 'config': {'ref_table': args, 'align': 'cm', 'r': 0.1, 'colour': G.C.CLEAR, 'func': 'text_input'}, 'nodes': ui_letters}}}}}}}
    return t
def create_keyboard_input(args):
    keyboard_rows = {1: '1234567890', 2: 'QWERTYUIOP', 3: 'ASDFGHJKL', 4: 'ZXCVBNM', 5: args.space_key & ' ' if args.space_key & ' ' else 'None'}
    keyboard_button_rows = {1: {}, 2: {}, 3: {}, 4: {}, 5: {}}
    for kv in ipairs(keyboard_rows):
        for i in range(1, len(v), ):
            c = v.sub(i, i)
            '#keyboard_button_rows[k] + 1[keyboard_button_rows[k]]' = create_keyboard_button(c)
    return {'n': G.UIT.ROOT, 'config': {'align': 'cm', 'padding': 15, 'r': 0.1, 'colour': {1: '1[G.C.GREY]', 2: '2[G.C.GREY]', 3: '3[G.C.GREY]', 4: 0.7}}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0.05, 'colour': G.C.CLEAR}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0.05, 'colour': G.C.BLACK, 'emboss': 0.05, 'r': 0.1, 'mid': True}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.05}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0.05, 'colour': G.C.CLEAR}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.07, 'colour': G.C.CLEAR}, 'nodes': '1[keyboard_button_rows]'}, 2: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.07, 'colour': G.C.CLEAR}, 'nodes': '2[keyboard_button_rows]'}, 3: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.07, 'colour': G.C.CLEAR}, 'nodes': '3[keyboard_button_rows]'}, 4: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.07, 'colour': G.C.CLEAR}, 'nodes': '4[keyboard_button_rows]'}, 5: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.07, 'colour': G.C.CLEAR}, 'nodes': '5[keyboard_button_rows]'}}}, 2: (args.backspace_key if args.backspace_key else args.return_key) & {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0.05, 'colour': G.C.CLEAR}, 'nodes': {1: args.backspace_key & {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.05, 'colour': G.C.CLEAR}, 'nodes': {1: create_keyboard_button(backspace, x)}} if args.backspace_key & {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.05, 'colour': G.C.CLEAR}, 'nodes': {1: create_keyboard_button(backspace, x)}} else 'None', 2: args.return_key & {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.05, 'colour': G.C.CLEAR}, 'nodes': {1: create_keyboard_button(return, start)}} if args.return_key & {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.05, 'colour': G.C.CLEAR}, 'nodes': {1: create_keyboard_button(return, start)}} else 'None', 3: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.05, 'colour': G.C.CLEAR}, 'nodes': {1: create_keyboard_button(back, b)}}}} if (args.backspace_key if args.backspace_key else args.return_key) & {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0.05, 'colour': G.C.CLEAR}, 'nodes': {1: args.backspace_key & {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.05, 'colour': G.C.CLEAR}, 'nodes': {1: create_keyboard_button(backspace, x)}} if args.backspace_key & {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.05, 'colour': G.C.CLEAR}, 'nodes': {1: create_keyboard_button(backspace, x)}} else 'None', 2: args.return_key & {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.05, 'colour': G.C.CLEAR}, 'nodes': {1: create_keyboard_button(return, start)}} if args.return_key & {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.05, 'colour': G.C.CLEAR}, 'nodes': {1: create_keyboard_button(return, start)}} else 'None', 3: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.05, 'colour': G.C.CLEAR}, 'nodes': {1: create_keyboard_button(back, b)}}}} else 'None'}}}}}}}}
def create_keyboard_button(key, binding):
    key_label = ((((key == 'backspace') & 'Backspace' if (key == 'backspace') & 'Backspace' else (key == ' ') & 'Space') if ((key == 'backspace') & 'Backspace' if (key == 'backspace') & 'Backspace' else (key == ' ') & 'Space') else (key == 'back') & 'Back') if (((key == 'backspace') & 'Backspace' if (key == 'backspace') & 'Backspace' else (key == ' ') & 'Space') if ((key == 'backspace') & 'Backspace' if (key == 'backspace') & 'Backspace' else (key == ' ') & 'Space') else (key == 'back') & 'Back') else (key == 'return') & 'Enter') if ((((key == 'backspace') & 'Backspace' if (key == 'backspace') & 'Backspace' else (key == ' ') & 'Space') if ((key == 'backspace') & 'Backspace' if (key == 'backspace') & 'Backspace' else (key == ' ') & 'Space') else (key == 'back') & 'Back') if (((key == 'backspace') & 'Backspace' if (key == 'backspace') & 'Backspace' else (key == ' ') & 'Space') if ((key == 'backspace') & 'Backspace' if (key == 'backspace') & 'Backspace' else (key == ' ') & 'Space') else (key == 'back') & 'Back') else (key == 'return') & 'Enter') else key
    return UIBox_button()
def create_dynatext_pips(args):
    args = args if args else {}
    args.active_colour = copy_table() if copy_table() else G.C.RED
    args.inactive_colour = copy_table() if copy_table() else {1: 0, 2: 0, 3: 0, 4: 0.08}
    args.w = args.w if args.w else 0.07
    args.h = args.h if args.h else 0.07
    if not args.dynatext if not args.dynatext else not len(args.dynatext.strings > 1):
        return False
    pips = {}
    for i in range(1, len(args.dynatext.strings), ):
        'i[pips]' = {'n': G.UIT.C, 'config': {'ref_table': args.dynatext, 'minw': args.w, 'minh': args.h, 'colour': G.C.UI.TEXT_INACTIVE, 'r': 0.1, 'id': 'pip_' + i, 'pipcol1': args.active_colour, 'pipcol2': args.inactive_colour, 'func': 'pip_dynatext'}}
    return {'n': G.UIT.R, 'config': {'padding': 0.05, 'align': 'cm'}, 'nodes': pips}
def create_UIBox_options():
    current_seed = 'None'
    restart = 'None'
    main_menu = 'None'
    your_collection = 'None'
    credits = 'None'G.E_MANAGER.add_event()
    if G.STAGE == G.STAGES.RUN:
        restart = UIBox_button()
        main_menu = UIBox_button()
        your_collection = UIBox_button()
        current_seed = {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.05}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(b_seed) + ': ', 'scale': 0.4, 'colour': G.C.WHITE}}}}, 2: {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0, 'minh': 0.8}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0, 'minh': 0.8}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'r': 0.1, 'colour': G.GAME.seeded & G.C.RED if G.GAME.seeded & G.C.RED else G.C.BLACK, 'minw': 1.8, 'minh': 0.5, 'padding': 0.1, 'emboss': 0.05}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': tostring(), 'scale': 0.43, 'colour': G.C.UI.TEXT_LIGHT, 'shadow': True}}}}}}}}}}, 3: UIBox_button()}}
    if G.STAGE == G.STAGES.MAIN_MENU:
        credits = UIBox_button()
    settings = UIBox_button()
    high_scores = UIBox_button()
    t = create_UIBox_generic_options()
    return t
def create_UIBox_settings():
    tabs = {}
    '#tabs + 1[tabs]' = {'label': localize(b_set_game), 'chosen': True, 'tab_definition_function': G.UIDEF.settings_tab, 'tab_definition_function_args': 'Game'}
    if G.F_VIDEO_SETTINGS:
        '#tabs + 1[tabs]' = {'label': localize(b_set_video), 'tab_definition_function': G.UIDEF.settings_tab, 'tab_definition_function_args': 'Video'}
    '#tabs + 1[tabs]' = {'label': localize(b_set_graphics), 'tab_definition_function': G.UIDEF.settings_tab, 'tab_definition_function_args': 'Graphics'}
    '#tabs + 1[tabs]' = {'label': localize(b_set_audio), 'tab_definition_function': G.UIDEF.settings_tab, 'tab_definition_function_args': 'Audio'}
    t = create_UIBox_generic_options()
    return t
def settings_tab(tab):
    if tab == 'Game':
        return {'n': G.UIT.ROOT, 'config': {'align': 'cm', 'padding': 0.05, 'colour': G.C.CLEAR}, 'nodes': {1: create_option_cycle(), 2: create_option_cycle(), 3: G.F_RUMBLE & create_toggle() if G.F_RUMBLE & create_toggle() else 'None', 4: create_slider(), 5: create_toggle(), 6: create_toggle(), 7: G.F_CRASH_REPORTS & create_toggle() if G.F_CRASH_REPORTS & create_toggle() else 'None'}}
    elif tab == 'Video':
        G.SETTINGS.QUEUED_CHANGE = {}
        res_option = GET_DISPLAYINFO()
        return {'n': G.UIT.ROOT, 'config': {'align': 'cm', 'padding': 0.05, 'colour': G.C.CLEAR}, 'nodes': {1: create_option_cycle(), 2: create_option_cycle(), 3: {'n': G.UIT.R, 'config': {'align': 'cm', 'id': 'resolution_cycle'}, 'nodes': {1: create_option_cycle()}}, 4: {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: create_option_cycle()}}, 5: UIBox_button()}}
    elif tab == 'Audio':
        return {'n': G.UIT.ROOT, 'config': {'align': 'cm', 'padding': 0.05, 'colour': G.C.CLEAR}, 'nodes': {1: create_slider(), 2: create_slider(), 3: create_slider()}}
    elif tab == 'Graphics':
        return {'n': G.UIT.ROOT, 'config': {'align': 'cm', 'padding': 0.05, 'colour': G.C.CLEAR}, 'nodes': {1: create_option_cycle(), 2: create_option_cycle(), 3: create_slider(), 4: create_option_cycle()}}
    return {'n': G.UIT.ROOT, 'config': {'align': 'cm', 'padding': 0.05, 'colour': G.C.CLEAR, 'minh': 5, 'minw': 5}, 'nodes': {}}
def create_UIBox_test_framework(variables):
    variables = variables if variables else {}';'
    nodes = {}
    for kv in pairs(variables):
        if v.type == 'cycle':table.insert(nodes)
        elif v.type == 'slider':table.insert(nodes)
        elif v.type == 'text_input':table.insert(nodes)
    t = {'n': G.UIT.ROOT, 'config': {'align': 'cm', 'minw': G.ROOM.T.w * 5, 'minh': G.ROOM.T.h * 5, 'padding': 0.15, 'r': 0.1, 'colour': {1: '1[G.C.BLACK]', 2: '2[G.C.BLACK]', 3: '3[G.C.BLACK]', 4: 0.6}}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'minh': 1, 'r': 0.3, 'padding': 0.1, 'minw': 1, 'colour': G.C.WHITE, 'shadow': True}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'minh': 1, 'r': 0.2, 'padding': 0.2, 'minw': 1, 'colour': G.C.CLEAR, 'outline': 1, 'outline_colour': G.C.BLACK}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.05}, 'nodes': nodes}, 2: {'n': G.UIT.R, 'config': {'align': 'cm', 'minw': 2.5, 'padding': 0.1, 'r': 0.1, 'hover': True, 'colour': G.C.ORANGE, 'button': 'exit_overlay_menu', 'shadow': True}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0, 'no_fill': True}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': 'Back', 'scale': 0.5, 'colour': G.C.UI.TEXT_LIGHT}}}}}}}}}}}}
    return t
def usage_tabs():
    return create_UIBox_generic_options()
def create_UIBox_usage(args):
    args = args if args else {}
    _type = _set = ('1[args]', '2[args]')
    used_cards = {}
    max_amt = 0
    for kv in pairs(_type[G.PROFILES[G.SETTINGS.profile]]):
        if 'k[G.P_CENTERS]' & (not _set if not _set else 'k[G.P_CENTERS]'.set == _set) & 'k[G.P_CENTERS]'.discovered:
            '#used_cards + 1[used_cards]' = {'count': v.count, 'key': k}
            if v.count > max_amt:
                max_amt = v.count
    _col = '_set[G.C.SECONDARY_SET]' if '_set[G.C.SECONDARY_SET]' else G.C.REDtable.sort(used_cards)
    histograms = {}
    for i in range(1, 10, ):
        v = 'i[used_cards]'
        if v:
            card = Card(0, 0)
            card.ambient_tilt = 0.8
            cardarea = CardArea()cardarea.emplace(card)
            '#histograms + 1[histograms]' = {'n': G.UIT.C, 'config': {'align': 'bm', 'minh': 6.2, 'colour': G.C.UI.TRANSPARENT_DARK, 'r': 0.1}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'bm'}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'minh': 0.7 * G.CARD_H + 0.1}, 'nodes': {1: {'n': G.UIT.O, 'config': {'object': cardarea}}}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.1}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': v.count, 'scale': 0.35, 'colour': mix_colours(), 'shadow': True}}}}, 3: {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'minh': v.count / max_amt * 3.6, 'minw': 0.8, 'colour': 'G.P_CENTERS[v.key].set[G.C.SECONDARY_SET]' if 'G.P_CENTERS[v.key].set[G.C.SECONDARY_SET]' else G.C.RED, 'res': 0.15, 'r': 0.001}, 'nodes': {}}}}}}}}
        else:
            '#histograms + 1[histograms]' = {'n': G.UIT.C, 'config': {'align': 'bm', 'minh': 6.2, 'colour': G.C.UI.TRANSPARENT_DARK, 'r': 0.1}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'bm'}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'minh': 0.7 * G.CARD_H + 0.1, 'minw': 0.7 * G.CARD_W}, 'nodes': {}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.1}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': '-', 'scale': 0.35, 'colour': mix_colours(), 'shadow': True}}}}, 3: {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'minh': 0.2, 'minw': 0.8, 'colour': G.C.UI.TRANSPARENT_LIGHT, 'res': 0.15, 'r': 0.001}, 'nodes': {}}}}}}}}
    t = {'n': G.UIT.ROOT, 'config': {'align': 'cm', 'minw': 3, 'padding': 0.1, 'r': 0.1, 'colour': G.C.UI.TRANSPARENT_DARK}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.1}, 'nodes': {1: {'n': G.UIT.B, 'config': {'w': 0.2, 'h': 0.2, 'r': 0.1, 'colour': G.C.FILTER}}, 2: {'n': G.UIT.T, 'config': {'text': ((_type == 'joker_usage') & localize(ph_stat_joker) if (_type == 'joker_usage') & localize(ph_stat_joker) else (_type == 'consumeable_usage') & localize(ph_stat_consumable)) if ((_type == 'joker_usage') & localize(ph_stat_joker) if (_type == 'joker_usage') & localize(ph_stat_joker) else (_type == 'consumeable_usage') & localize(ph_stat_consumable)) else (_type == 'voucher_usage') & localize(ph_stat_voucher), 'scale': 0.35, 'colour': G.C.WHITE}}}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.1}, 'nodes': histograms}}}
    return t
def create_UIBox_high_scores():fetch_achievements()set_profile_progress()set_discover_tallies()
    scores = {1: create_UIBox_high_scores_row(hand), 2: create_UIBox_high_scores_row(furthest_round), 3: create_UIBox_high_scores_row(furthest_ante), 4: create_UIBox_high_scores_row(poker_hand), 5: create_UIBox_high_scores_row(most_money), 6: create_UIBox_high_scores_row(win_streak)}
    G.focused_profile = G.SETTINGS.profile
    cheevs = {}
    t = create_UIBox_generic_options()
    return t
def create_progress_box(_profile_progress, smaller):
    rows = protos = ({}, {1: 'collection', 2: 'challenges', 3: 'joker_stickers', 4: 'deck_stake_wins'})
    _profile_progress = _profile_progress if _profile_progress else 'G.SETTINGS.profile[G.PROFILES]'.progress
    _profile_progress.overall_tally = _profile_progress.overall_of = (_profile_progress.discovered.tally / _profile_progress.discovered.of + _profile_progress.deck_stakes.tally / _profile_progress.deck_stakes.of + _profile_progress.joker_stickers.tally / _profile_progress.joker_stickers.of + _profile_progress.challenges.tally / _profile_progress.challenges.of, 4)
    text_scale = smaller & 0.7 if smaller & 0.7 else 1
    bar_colour = 'G.focused_profile[G.PROFILES]'.all_unlocked & G.C.RED if 'G.focused_profile[G.PROFILES]'.all_unlocked & G.C.RED else G.C.BLUE
    for _v in ipairs(protos):
        tab = val = max = ('None', 'None', 'None')
        if v == 'collection':
            tab = val = max = (_profile_progress.discovered, 'tally', _profile_progress.discovered.of)
        elif v == 'deck_stake_wins':
            tab = val = max = (_profile_progress.deck_stakes, 'tally', _profile_progress.deck_stakes.of)
        elif v == 'joker_stickers':
            tab = val = max = (_profile_progress.joker_stickers, 'tally', _profile_progress.joker_stickers.of)
        elif v == 'challenges':
            tab = val = max = (_profile_progress.challenges, 'tally', _profile_progress.challenges.of)
        filling = (((v == 'collection') & {1: {'n': G.UIT.O, 'config': {'object': DynaText()}}, 2: {'n': G.UIT.T, 'config': {'text': ' (' + _profile_progress.discovered.tally + '/' + _profile_progress.discovered.of + ')', 'scale': 0.35, 'colour': G.C.JOKER_GREY}}} if (v == 'collection') & {1: {'n': G.UIT.O, 'config': {'object': DynaText()}}, 2: {'n': G.UIT.T, 'config': {'text': ' (' + _profile_progress.discovered.tally + '/' + _profile_progress.discovered.of + ')', 'scale': 0.35, 'colour': G.C.JOKER_GREY}}} else (v == 'deck_stake_wins') & {1: {'n': G.UIT.O, 'config': {'object': DynaText()}}, 2: {'n': G.UIT.T, 'config': {'text': ' (' + _profile_progress.deck_stakes.tally + '/' + _profile_progress.deck_stakes.of + ')', 'scale': 0.35, 'colour': G.C.JOKER_GREY}}}) if ((v == 'collection') & {1: {'n': G.UIT.O, 'config': {'object': DynaText()}}, 2: {'n': G.UIT.T, 'config': {'text': ' (' + _profile_progress.discovered.tally + '/' + _profile_progress.discovered.of + ')', 'scale': 0.35, 'colour': G.C.JOKER_GREY}}} if (v == 'collection') & {1: {'n': G.UIT.O, 'config': {'object': DynaText()}}, 2: {'n': G.UIT.T, 'config': {'text': ' (' + _profile_progress.discovered.tally + '/' + _profile_progress.discovered.of + ')', 'scale': 0.35, 'colour': G.C.JOKER_GREY}}} else (v == 'deck_stake_wins') & {1: {'n': G.UIT.O, 'config': {'object': DynaText()}}, 2: {'n': G.UIT.T, 'config': {'text': ' (' + _profile_progress.deck_stakes.tally + '/' + _profile_progress.deck_stakes.of + ')', 'scale': 0.35, 'colour': G.C.JOKER_GREY}}}) else (v == 'joker_stickers') & {1: {'n': G.UIT.O, 'config': {'object': DynaText()}}, 2: {'n': G.UIT.T, 'config': {'text': ' (' + _profile_progress.joker_stickers.tally + '/' + _profile_progress.joker_stickers.of + ')', 'scale': 0.35, 'colour': G.C.JOKER_GREY}}}) if (((v == 'collection') & {1: {'n': G.UIT.O, 'config': {'object': DynaText()}}, 2: {'n': G.UIT.T, 'config': {'text': ' (' + _profile_progress.discovered.tally + '/' + _profile_progress.discovered.of + ')', 'scale': 0.35, 'colour': G.C.JOKER_GREY}}} if (v == 'collection') & {1: {'n': G.UIT.O, 'config': {'object': DynaText()}}, 2: {'n': G.UIT.T, 'config': {'text': ' (' + _profile_progress.discovered.tally + '/' + _profile_progress.discovered.of + ')', 'scale': 0.35, 'colour': G.C.JOKER_GREY}}} else (v == 'deck_stake_wins') & {1: {'n': G.UIT.O, 'config': {'object': DynaText()}}, 2: {'n': G.UIT.T, 'config': {'text': ' (' + _profile_progress.deck_stakes.tally + '/' + _profile_progress.deck_stakes.of + ')', 'scale': 0.35, 'colour': G.C.JOKER_GREY}}}) if ((v == 'collection') & {1: {'n': G.UIT.O, 'config': {'object': DynaText()}}, 2: {'n': G.UIT.T, 'config': {'text': ' (' + _profile_progress.discovered.tally + '/' + _profile_progress.discovered.of + ')', 'scale': 0.35, 'colour': G.C.JOKER_GREY}}} if (v == 'collection') & {1: {'n': G.UIT.O, 'config': {'object': DynaText()}}, 2: {'n': G.UIT.T, 'config': {'text': ' (' + _profile_progress.discovered.tally + '/' + _profile_progress.discovered.of + ')', 'scale': 0.35, 'colour': G.C.JOKER_GREY}}} else (v == 'deck_stake_wins') & {1: {'n': G.UIT.O, 'config': {'object': DynaText()}}, 2: {'n': G.UIT.T, 'config': {'text': ' (' + _profile_progress.deck_stakes.tally + '/' + _profile_progress.deck_stakes.of + ')', 'scale': 0.35, 'colour': G.C.JOKER_GREY}}}) else (v == 'joker_stickers') & {1: {'n': G.UIT.O, 'config': {'object': DynaText()}}, 2: {'n': G.UIT.T, 'config': {'text': ' (' + _profile_progress.joker_stickers.tally + '/' + _profile_progress.joker_stickers.of + ')', 'scale': 0.35, 'colour': G.C.JOKER_GREY}}}) else (v == 'challenges') & {1: {'n': G.UIT.O, 'config': {'object': DynaText()}}, 2: {'n': G.UIT.T, 'config': {'text': ' (' + _profile_progress.challenges.tally + '/' + _profile_progress.challenges.of + ')', 'scale': 0.35, 'colour': G.C.JOKER_GREY}}}
        '#rows + 1[rows]' = {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.05, 'r': 0.1, 'colour': darken(), 'emboss': 0.05}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0.05, 'minw': 3.5 * text_scale, 'maxw': 3.5 * text_scale}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(), 'scale': 0.5 * text_scale, 'colour': G.C.UI.TEXT_LIGHT, 'shadow': True}}}}, 2: {'n': G.UIT.C, 'config': {'align': 'cl', 'minh': smaller & 0.5 if smaller & 0.5 else 0.8, 'r': 0.1, 'minw': 3.5 * text_scale, 'colour': G.C.BLACK, 'emboss': 0.05, 'progress_bar': {'max': max, 'ref_table': tab, 'ref_value': val, 'empty_col': G.C.BLACK, 'filled_col': adjust_alpha(bar_colour, 0.5)}}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0.05, 'r': 0.1, 'minw': 3.5 * text_scale}, 'nodes': filling}}}}}
    return {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.05, 'r': 0.1, 'colour': G.C.BLACK, 'emboss': 0.05}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.05}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0.05, 'minw': 3.5 * text_scale, 'maxw': 3.5 * text_scale}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(k_progress), 'scale': 0.5, 'colour': G.C.UI.TEXT_LIGHT, 'shadow': True}}}}, 2: {'n': G.UIT.C, 'config': {'align': 'cl', 'minh': 0.6, 'r': 0.1, 'minw': 3.5 * text_scale, 'colour': G.C.BLACK, 'emboss': 0.05, 'progress_bar': {'max': _profile_progress.overall_of, 'ref_table': _profile_progress, 'ref_value': 'overall_tally', 'empty_col': G.C.BLACK, 'filled_col': adjust_alpha(bar_colour, 0.5)}}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0.05, 'r': 0.1, 'minw': 3.5 * text_scale}, 'nodes': {1: {'n': G.UIT.O, 'config': {'object': DynaText()}}}}}}}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.05}, 'nodes': rows}}}
def create_UIBox_high_scores_row(score):
    if not 'score[G.PROFILES[G.SETTINGS.profile].high_scores]':
        return 'None'
    label_scale = 0.65 - 0.025 * math.max()
    label_w = score_w = h = (3.5, 4, 0.8)
    score_tab = {}
    if score == 'poker_hand':
        handname = amount = (localize(k_none), 0)
        for kv in pairs():
            if v.count > amount:
                handname = v.order';'
                amount = v.count
        score_tab = {1: {'n': G.UIT.O, 'config': {'object': DynaText()}}, 2: {'n': G.UIT.T, 'config': {'text': ' (' + amount + ')', 'scale': 0.45, 'colour': G.C.JOKER_GREY}}}
    elif score == 'most_money':
        score_tab = {1: {'n': G.UIT.O, 'config': {'object': DynaText()}}}
    elif score == 'win_streak':
        score_tab = {1: {'n': G.UIT.O, 'config': {'object': DynaText()}}, 2: {'n': G.UIT.T, 'config': {'text': ' (' + '"current_streak"[G.PROFILES[G.SETTINGS.profile].high_scores]'.amt + ')', 'scale': 0.45, 'colour': G.C.JOKER_GREY}}}
    elif score == 'hand':
        chip_sprite = Sprite(0, 0, 0.4, 0.4, "ui_"..G.SETTINGS.colourblind_option and 2 or 1[G.ASSET_ATLAS])
        chip_sprite.states.drag.can = False
        score_tab = {1: {'n': G.UIT.C, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.O, 'config': {'w': 0.4, 'h': 0.4, 'object': chip_sprite}}}}, 2: {'n': G.UIT.C, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.O, 'config': {'object': DynaText()}}}}}
    elif score == 'collection':
        score_tab = {1: {'n': G.UIT.C, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.O, 'config': {'object': DynaText()}}, 2: {'n': G.UIT.T, 'config': {'text': ' (' + 'score[G.PROFILES[G.SETTINGS.profile].high_scores]'.amt + '/' + 'score[G.PROFILES[G.SETTINGS.profile].high_scores]'.tot + ')', 'scale': 0.45, 'colour': G.C.JOKER_GREY}}}}}
    else:
        score_tab = {1: {'n': G.UIT.O, 'config': {'object': DynaText()}}}
    return {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.05, 'r': 0.1, 'colour': darken(), 'emboss': 0.05}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0.05, 'minw': label_w, 'maxw': label_w}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(score, high_scores), 'scale': label_scale, 'colour': G.C.UI.TEXT_LIGHT, 'shadow': True}}}}, 2: {'n': G.UIT.C, 'config': {'align': 'cl', 'minh': h, 'r': 0.1, 'minw': score_w, 'colour': G.C.BLACK, 'emboss': 0.05}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0.05, 'r': 0.1, 'minw': score_w, 'maxw': score_w}, 'nodes': score_tab}}}}}
def create_UIBox_win():
    show_lose_cta = False
    eased_green = copy_table()
    '4[eased_green]' = 0ease_value(eased_green, 4, 0.5, None, None, True)
    t = create_UIBox_generic_options()
    '1[t.nodes]' = {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.1}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 2}, 'nodes': {1: {'n': G.UIT.O, 'config': {'padding': 0, 'id': 'jimbo_spot', 'object': Moveable(0, 0)}}}}, 2: {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0.1}, 'nodes': {1: '1[t.nodes]'}}}}
    t.config.id = 'you_win_UI'
    return t
def create_UIBox_exit_CTA():
    t = create_UIBox_generic_options()
    '2[t.nodes]' = '1[t.nodes]'
    '1[t.nodes]' = {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 2}, 'nodes': {1: {'n': G.UIT.O, 'config': {'padding': 0, 'id': 'jimbo_spot', 'object': Moveable(0, 0)}}}}
    return t
def create_UIBox_small_cta():
    return {'n': G.UIT.ROOT, 'config': {'align': 'cm', 'minw': 4, 'minh': 3}, 'nodes': {1: {'n': G.UIT.O, 'config': {'object': DynaText()}}}}
def create_UIBox_demo_video_CTA():G.E_MANAGER.add_event()RESTART_MUSIC()
    video_file = love.graphics.newVideo(resources/democta.ogv)
    vid_sprite = Sprite(0, 0)video_file.getSource().setVolume()
    vid_sprite.video = video_filevideo_file.play()
    t = create_UIBox_generic_options()
    return t
def create_UIBox_game_over():
    show_lose_cta = False
    eased_red = copy_table()
    '4[eased_red]' = 0ease_value(eased_red, 4, 0.8, None, None, True)
    t = create_UIBox_generic_options()
    '1[t.nodes]' = {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.1}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 2}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.O, 'config': {'padding': 0, 'id': 'jimbo_spot', 'object': Moveable(0, 0)}}}}}}, 2: {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0.1}, 'nodes': {1: '1[t.nodes]'}}}}
    return t
def create_UIBox_round_scores_row(score, text_colour):
    label = 'score[G.GAME.round_scores]' & localize() if 'score[G.GAME.round_scores]' & localize() else ''
    check_high_score = False
    score_tab = {}
    label_w = score_w = h = ('score[{\n    hand = true,\n    poker_hand = true,\n}]' & 3.5 if 'score[{\n    hand = true,\n    poker_hand = true,\n}]' & 3.5 else 2.9, 'score[{\n    hand = true,\n    poker_hand = true,\n}]' & 3.5 if 'score[{\n    hand = true,\n    poker_hand = true,\n}]' & 3.5 else 1, 0.5)
    if score == 'furthest_ante':
        label_w = 1.9
        check_high_score = True
        label = localize(k_ante)
        score_tab = {1: {'n': G.UIT.O, 'config': {'object': DynaText()}}}
    if score == 'furthest_round':
        label_w = 1.9
        check_high_score = True
        label = localize(k_round)
        score_tab = {1: {'n': G.UIT.O, 'config': {'object': DynaText()}}}
    if score == 'seed':
        label_w = 1.9
        score_w = 1.9
        label = localize(k_seed)
        score_tab = {1: {'n': G.UIT.O, 'config': {'object': DynaText()}}}
    if score == 'defeated_by':
        label = localize(k_defeated_by)
        blind_choice = {'config': G.GAME.blind.config.blind if G.GAME.blind.config.blind else G.P_BLINDS.bl_small}
        blind_choice.animation = AnimatedSprite(0, 0, 1.4, 1.4, 'blind_chips'[G.ANIMATION_ATLAS])blind_choice.animation.define_draw_steps()
        score_tab = {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'minh': 0.6}, 'nodes': {1: {'n': G.UIT.O, 'config': {'object': DynaText()}}}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.1}, 'nodes': {1: {'n': G.UIT.O, 'config': {'object': blind_choice.animation}}}}}
    label_scale = 0.5
    if score == 'poker_hand':
        handname = amount = (localize(k_none), 0)
        for kv in pairs():
            if v.count > amount:
                handname = v.order';'
                amount = v.count
        score_tab = {1: {'n': G.UIT.O, 'config': {'object': DynaText()}}, 2: {'n': G.UIT.T, 'config': {'text': ' (' + amount + ')', 'scale': 0.35, 'colour': G.C.JOKER_GREY}}}
    elif score == 'hand':
        check_high_score = True
        chip_sprite = Sprite(0, 0, 0.3, 0.3, "ui_"..G.SETTINGS.colourblind_option and 2 or 1[G.ASSET_ATLAS])
        chip_sprite.states.drag.can = False
        score_tab = {1: {'n': G.UIT.C, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.O, 'config': {'w': 0.3, 'h': 0.3, 'object': chip_sprite}}}}, 2: {'n': G.UIT.C, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.O, 'config': {'object': DynaText()}}}}}
    elif 'score[G.GAME.round_scores]' & (not '1[score_tab]'):
        score_tab = {1: {'n': G.UIT.O, 'config': {'object': DynaText()}}}
    return {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.05, 'r': 0.1, 'colour': darken(), 'emboss': 0.05, 'func': check_high_score & 'high_score_alert' if check_high_score & 'high_score_alert' else 'None', 'id': score}, 'nodes': {1: {'n': (score == 'defeated_by') & G.UIT.R if (score == 'defeated_by') & G.UIT.R else G.UIT.C, 'config': {'align': 'cm', 'padding': 0.02, 'minw': label_w, 'maxw': label_w}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': label, 'scale': label_scale, 'colour': G.C.UI.TEXT_LIGHT, 'shadow': True}}}}, 2: {'n': (score == 'defeated_by') & G.UIT.R if (score == 'defeated_by') & G.UIT.R else G.UIT.C, 'config': {'align': 'cr'}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'minh': h, 'r': 0.1, 'minw': (score == 'defeated_by') & label_w if (score == 'defeated_by') & label_w else score_w, 'colour': (score == 'seed') & G.GAME.seeded & G.C.RED if (score == 'seed') & G.GAME.seeded & G.C.RED else G.C.BLACK, 'emboss': 0.05}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0.05, 'r': 0.1, 'minw': score_w}, 'nodes': score_tab}}}}}}}
def create_UIBox_hand_tip(handname):
    if not 'handname[G.GAME.hands]'.example:
        return {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {}}
    cardarea = CardArea(2, 2)
    for kv in ipairs():
        card = Card(0, 0)
        if '2[v]':card.juice_up(0.3, 0.2)
        if k == 1:play_sound(paper1)ease_value()cardarea.emplace(card)
    return {'n': G.UIT.R, 'config': {'align': 'cm', 'colour': G.C.WHITE, 'r': 0.1}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.O, 'config': {'object': cardarea}}}}}}
def create_UIBox_current_hand_row(handname, simple):
    return 'handname[G.GAME.hands]'.visible & ((not simple) & {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.05, 'r': 0.1, 'colour': darken(), 'emboss': 0.05, 'hover': True, 'force_focus': True, 'on_demand_tooltip': {'text': localize(handname, poker_hand_descriptions), 'filler': {'func': create_UIBox_hand_tip, 'args': handname}}}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cl', 'padding': 0, 'minw': 5}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0.01, 'r': 0.1, 'colour': 'math.min(7, G.GAME.hands[handname].level)[G.C.HAND_LEVELS]', 'minw': 1.5, 'outline': 0.8, 'outline_colour': G.C.WHITE}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(k_level_prefix) + 'handname[G.GAME.hands]'.level, 'scale': 0.5, 'colour': G.C.UI.TEXT_DARK}}}}, 2: {'n': G.UIT.C, 'config': {'align': 'cm', 'minw': 4.5, 'maxw': 4.5}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': ' ' + localize(handname, poker_hands), 'scale': 0.45, 'colour': G.C.UI.TEXT_LIGHT, 'shadow': True}}}}}}, 2: {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0.05, 'colour': G.C.BLACK, 'r': 0.1}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cr', 'padding': 0.01, 'r': 0.1, 'colour': G.C.CHIPS, 'minw': 1.1}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': 'handname[G.GAME.hands]'.chips, 'scale': 0.45, 'colour': G.C.UI.TEXT_LIGHT}}, 2: {'n': G.UIT.B, 'config': {'w': 0.08, 'h': 0.01}}}}, 2: {'n': G.UIT.T, 'config': {'text': 'X', 'scale': 0.45, 'colour': G.C.MULT}}, 3: {'n': G.UIT.C, 'config': {'align': 'cl', 'padding': 0.01, 'r': 0.1, 'colour': G.C.MULT, 'minw': 1.1}, 'nodes': {1: {'n': G.UIT.B, 'config': {'w': 0.08, 'h': 0.01}}, 2: {'n': G.UIT.T, 'config': {'text': 'handname[G.GAME.hands]'.mult, 'scale': 0.45, 'colour': G.C.UI.TEXT_LIGHT}}}}}}, 3: {'n': G.UIT.C, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': '  #', 'scale': 0.45, 'colour': G.C.UI.TEXT_LIGHT, 'shadow': True}}}}, 4: {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0.05, 'colour': G.C.L_BLACK, 'r': 0.1, 'minw': 0.9}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': 'handname[G.GAME.hands]'.played, 'scale': 0.45, 'colour': G.C.FILTER, 'shadow': True}}}}}} if (not simple) & {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.05, 'r': 0.1, 'colour': darken(), 'emboss': 0.05, 'hover': True, 'force_focus': True, 'on_demand_tooltip': {'text': localize(handname, poker_hand_descriptions), 'filler': {'func': create_UIBox_hand_tip, 'args': handname}}}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cl', 'padding': 0, 'minw': 5}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0.01, 'r': 0.1, 'colour': 'math.min(7, G.GAME.hands[handname].level)[G.C.HAND_LEVELS]', 'minw': 1.5, 'outline': 0.8, 'outline_colour': G.C.WHITE}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(k_level_prefix) + 'handname[G.GAME.hands]'.level, 'scale': 0.5, 'colour': G.C.UI.TEXT_DARK}}}}, 2: {'n': G.UIT.C, 'config': {'align': 'cm', 'minw': 4.5, 'maxw': 4.5}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': ' ' + localize(handname, poker_hands), 'scale': 0.45, 'colour': G.C.UI.TEXT_LIGHT, 'shadow': True}}}}}}, 2: {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0.05, 'colour': G.C.BLACK, 'r': 0.1}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cr', 'padding': 0.01, 'r': 0.1, 'colour': G.C.CHIPS, 'minw': 1.1}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': 'handname[G.GAME.hands]'.chips, 'scale': 0.45, 'colour': G.C.UI.TEXT_LIGHT}}, 2: {'n': G.UIT.B, 'config': {'w': 0.08, 'h': 0.01}}}}, 2: {'n': G.UIT.T, 'config': {'text': 'X', 'scale': 0.45, 'colour': G.C.MULT}}, 3: {'n': G.UIT.C, 'config': {'align': 'cl', 'padding': 0.01, 'r': 0.1, 'colour': G.C.MULT, 'minw': 1.1}, 'nodes': {1: {'n': G.UIT.B, 'config': {'w': 0.08, 'h': 0.01}}, 2: {'n': G.UIT.T, 'config': {'text': 'handname[G.GAME.hands]'.mult, 'scale': 0.45, 'colour': G.C.UI.TEXT_LIGHT}}}}}}, 3: {'n': G.UIT.C, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': '  #', 'scale': 0.45, 'colour': G.C.UI.TEXT_LIGHT, 'shadow': True}}}}, 4: {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0.05, 'colour': G.C.L_BLACK, 'r': 0.1, 'minw': 0.9}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': 'handname[G.GAME.hands]'.played, 'scale': 0.45, 'colour': G.C.FILTER, 'shadow': True}}}}}} else {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.05, 'r': 0.1, 'colour': darken(), 'force_focus': True, 'emboss': 0.05, 'hover': True, 'on_demand_tooltip': {'text': localize(handname, poker_hand_descriptions), 'filler': {'func': create_UIBox_hand_tip, 'args': handname}}, 'focus_args': {'snap_to': simple & (handname == 'Straight Flush')}}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0, 'minw': 5}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(handname, poker_hands), 'scale': 0.5, 'colour': G.C.UI.TEXT_LIGHT, 'shadow': True}}}}}}) if 'handname[G.GAME.hands]'.visible & ((not simple) & {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.05, 'r': 0.1, 'colour': darken(), 'emboss': 0.05, 'hover': True, 'force_focus': True, 'on_demand_tooltip': {'text': localize(handname, poker_hand_descriptions), 'filler': {'func': create_UIBox_hand_tip, 'args': handname}}}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cl', 'padding': 0, 'minw': 5}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0.01, 'r': 0.1, 'colour': 'math.min(7, G.GAME.hands[handname].level)[G.C.HAND_LEVELS]', 'minw': 1.5, 'outline': 0.8, 'outline_colour': G.C.WHITE}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(k_level_prefix) + 'handname[G.GAME.hands]'.level, 'scale': 0.5, 'colour': G.C.UI.TEXT_DARK}}}}, 2: {'n': G.UIT.C, 'config': {'align': 'cm', 'minw': 4.5, 'maxw': 4.5}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': ' ' + localize(handname, poker_hands), 'scale': 0.45, 'colour': G.C.UI.TEXT_LIGHT, 'shadow': True}}}}}}, 2: {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0.05, 'colour': G.C.BLACK, 'r': 0.1}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cr', 'padding': 0.01, 'r': 0.1, 'colour': G.C.CHIPS, 'minw': 1.1}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': 'handname[G.GAME.hands]'.chips, 'scale': 0.45, 'colour': G.C.UI.TEXT_LIGHT}}, 2: {'n': G.UIT.B, 'config': {'w': 0.08, 'h': 0.01}}}}, 2: {'n': G.UIT.T, 'config': {'text': 'X', 'scale': 0.45, 'colour': G.C.MULT}}, 3: {'n': G.UIT.C, 'config': {'align': 'cl', 'padding': 0.01, 'r': 0.1, 'colour': G.C.MULT, 'minw': 1.1}, 'nodes': {1: {'n': G.UIT.B, 'config': {'w': 0.08, 'h': 0.01}}, 2: {'n': G.UIT.T, 'config': {'text': 'handname[G.GAME.hands]'.mult, 'scale': 0.45, 'colour': G.C.UI.TEXT_LIGHT}}}}}}, 3: {'n': G.UIT.C, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': '  #', 'scale': 0.45, 'colour': G.C.UI.TEXT_LIGHT, 'shadow': True}}}}, 4: {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0.05, 'colour': G.C.L_BLACK, 'r': 0.1, 'minw': 0.9}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': 'handname[G.GAME.hands]'.played, 'scale': 0.45, 'colour': G.C.FILTER, 'shadow': True}}}}}} if (not simple) & {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.05, 'r': 0.1, 'colour': darken(), 'emboss': 0.05, 'hover': True, 'force_focus': True, 'on_demand_tooltip': {'text': localize(handname, poker_hand_descriptions), 'filler': {'func': create_UIBox_hand_tip, 'args': handname}}}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cl', 'padding': 0, 'minw': 5}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0.01, 'r': 0.1, 'colour': 'math.min(7, G.GAME.hands[handname].level)[G.C.HAND_LEVELS]', 'minw': 1.5, 'outline': 0.8, 'outline_colour': G.C.WHITE}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(k_level_prefix) + 'handname[G.GAME.hands]'.level, 'scale': 0.5, 'colour': G.C.UI.TEXT_DARK}}}}, 2: {'n': G.UIT.C, 'config': {'align': 'cm', 'minw': 4.5, 'maxw': 4.5}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': ' ' + localize(handname, poker_hands), 'scale': 0.45, 'colour': G.C.UI.TEXT_LIGHT, 'shadow': True}}}}}}, 2: {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0.05, 'colour': G.C.BLACK, 'r': 0.1}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cr', 'padding': 0.01, 'r': 0.1, 'colour': G.C.CHIPS, 'minw': 1.1}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': 'handname[G.GAME.hands]'.chips, 'scale': 0.45, 'colour': G.C.UI.TEXT_LIGHT}}, 2: {'n': G.UIT.B, 'config': {'w': 0.08, 'h': 0.01}}}}, 2: {'n': G.UIT.T, 'config': {'text': 'X', 'scale': 0.45, 'colour': G.C.MULT}}, 3: {'n': G.UIT.C, 'config': {'align': 'cl', 'padding': 0.01, 'r': 0.1, 'colour': G.C.MULT, 'minw': 1.1}, 'nodes': {1: {'n': G.UIT.B, 'config': {'w': 0.08, 'h': 0.01}}, 2: {'n': G.UIT.T, 'config': {'text': 'handname[G.GAME.hands]'.mult, 'scale': 0.45, 'colour': G.C.UI.TEXT_LIGHT}}}}}}, 3: {'n': G.UIT.C, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': '  #', 'scale': 0.45, 'colour': G.C.UI.TEXT_LIGHT, 'shadow': True}}}}, 4: {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0.05, 'colour': G.C.L_BLACK, 'r': 0.1, 'minw': 0.9}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': 'handname[G.GAME.hands]'.played, 'scale': 0.45, 'colour': G.C.FILTER, 'shadow': True}}}}}} else {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.05, 'r': 0.1, 'colour': darken(), 'force_focus': True, 'emboss': 0.05, 'hover': True, 'on_demand_tooltip': {'text': localize(handname, poker_hand_descriptions), 'filler': {'func': create_UIBox_hand_tip, 'args': handname}}, 'focus_args': {'snap_to': simple & (handname == 'Straight Flush')}}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0, 'minw': 5}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(handname, poker_hands), 'scale': 0.5, 'colour': G.C.UI.TEXT_LIGHT, 'shadow': True}}}}}}) else 'None'
def create_UIBox_current_hands(simple):
    hands = {1: create_UIBox_current_hand_row(Flush Five, simple), 2: create_UIBox_current_hand_row(Flush House, simple), 3: create_UIBox_current_hand_row(Five of a Kind, simple), 4: create_UIBox_current_hand_row(Straight Flush, simple), 5: create_UIBox_current_hand_row(Four of a Kind, simple), 6: create_UIBox_current_hand_row(Full House, simple), 7: create_UIBox_current_hand_row(Flush, simple), 8: create_UIBox_current_hand_row(Straight, simple), 9: create_UIBox_current_hand_row(Three of a Kind, simple), 10: create_UIBox_current_hand_row(Two Pair, simple), 11: create_UIBox_current_hand_row(Pair, simple), 12: create_UIBox_current_hand_row(High Card, simple)}
    t = {'n': G.UIT.ROOT, 'config': {'align': 'cm', 'minw': 3, 'padding': 0.1, 'r': 0.1, 'colour': G.C.CLEAR}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.04}, 'nodes': hands}}}
    return t
def deck_info(_show_remaining):
    return create_UIBox_generic_options()
def run_info():
    return create_UIBox_generic_options()
def current_blinds():
    return {'n': G.UIT.ROOT, 'config': {'align': 'cm', 'colour': G.C.CLEAR, 'padding': 0.2}, 'nodes': {1: ("'Small'[G.GAME.round_resets.blind_states]" != 'Hide') & {'n': G.UIT.C, 'config': {'align': 'tm', 'padding': 0.1, 'outline': 2, 'r': 0.1, 'line_emboss': 0.2, 'outline_colour': G.C.BLACK}, 'nodes': {1: create_UIBox_blind_choice(Small, True)}} if ("'Small'[G.GAME.round_resets.blind_states]" != 'Hide') & {'n': G.UIT.C, 'config': {'align': 'tm', 'padding': 0.1, 'outline': 2, 'r': 0.1, 'line_emboss': 0.2, 'outline_colour': G.C.BLACK}, 'nodes': {1: create_UIBox_blind_choice(Small, True)}} else 'None', 2: ("'Big'[G.GAME.round_resets.blind_states]" != 'Hide') & {'n': G.UIT.C, 'config': {'align': 'tm', 'padding': 0.1, 'outline': 2, 'r': 0.1, 'line_emboss': 0.2, 'outline_colour': G.C.BLACK}, 'nodes': {1: create_UIBox_blind_choice(Big, True)}} if ("'Big'[G.GAME.round_resets.blind_states]" != 'Hide') & {'n': G.UIT.C, 'config': {'align': 'tm', 'padding': 0.1, 'outline': 2, 'r': 0.1, 'line_emboss': 0.2, 'outline_colour': G.C.BLACK}, 'nodes': {1: create_UIBox_blind_choice(Big, True)}} else 'None', 3: ("'Boss'[G.GAME.round_resets.blind_states]" != 'Hide') & {'n': G.UIT.C, 'config': {'align': 'tm', 'padding': 0.1, 'outline': 2, 'r': 0.1, 'line_emboss': 0.2, 'outline_colour': G.C.BLACK}, 'nodes': {1: create_UIBox_blind_choice(Boss, True)}} if ("'Boss'[G.GAME.round_resets.blind_states]" != 'Hide') & {'n': G.UIT.C, 'config': {'align': 'tm', 'padding': 0.1, 'outline': 2, 'r': 0.1, 'line_emboss': 0.2, 'outline_colour': G.C.BLACK}, 'nodes': {1: create_UIBox_blind_choice(Boss, True)}} else 'None'}}
def deck_stake_column(_deck_key):
    deck_usage = '_deck_key[G.PROFILES[G.SETTINGS.profile].deck_usage]'
    stake_col = {}
    valid_option = 'None'
    for i in range(len("'Stake'[G.P_CENTER_POOLS]"), 1, -1):
        _wins = deck_usage & 'i[deck_usage.wins]' if deck_usage & 'i[deck_usage.wins]' else 0
        if (deck_usage & 'i - 1[deck_usage.wins]' if deck_usage & 'i - 1[deck_usage.wins]' else i == 1) if (deck_usage & 'i - 1[deck_usage.wins]' if deck_usage & 'i - 1[deck_usage.wins]' else i == 1) else 'G.SETTINGS.profile[G.PROFILES]'.all_unlocked:
            valid_option = True
        '#stake_col + 1[stake_col]' = {'n': G.UIT.R, 'config': {'id': i, 'align': 'cm', 'colour': (_wins > 0) & G.C.GREY if (_wins > 0) & G.C.GREY else G.C.CLEAR, 'outline': 0, 'outline_colour': G.C.WHITE, 'r': 0.1, 'minh': 0.25, 'minw': valid_option & 0.45 if valid_option & 0.45 else 0.25, 'func': 'RUN_SETUP_check_back_stake_highlight'}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'minh': valid_option & 0.17 if valid_option & 0.17 else 0.13, 'minw': valid_option & 0.37 if valid_option & 0.37 else 0.13, 'colour': (_wins > 0) & get_stake_col(i) if (_wins > 0) & get_stake_col(i) else G.C.UI.TRANSPARENT_LIGHT, 'r': 0.1}, 'nodes': {}}}}
        if i > 1:
            '#stake_col + 1[stake_col]' = {'n': G.UIT.R, 'config': {'align': 'cm', 'minh': 0.1, 'minw': 0.04}, 'nodes': {}}
    return {'n': G.UIT.ROOT, 'config': {'align': 'cm', 'colour': G.C.CLEAR}, 'nodes': stake_col}
def current_stake():
    other_col = 'None'
    if G.GAME.stake > 2:
        stake_desc_rows = {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.05}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(k_also_applied), 'scale': 0.4, 'colour': G.C.WHITE}}}}}
        for i in range(G.GAME.stake - 1, 2, -1):
            _stake_desc = {}
            _stake_center = 'i[G.P_CENTER_POOLS.Stake]'localize()
            _full_desc = {}
            for kv in ipairs(_stake_desc):
                '#_full_desc + 1[_full_desc]' = {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': v}
            '#_full_desc[_full_desc]' = 'None'
            '#stake_desc_rows + 1[stake_desc_rows]' = {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'colour': get_stake_col(i), 'r': 0.1, 'minh': 0.35, 'minw': 0.35, 'emboss': 0.05}, 'nodes': {}}, 2: {'n': G.UIT.B, 'config': {'w': 0.1, 'h': 0.1}}}}, 2: {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0.03, 'colour': G.C.WHITE, 'r': 0.1, 'minh': 0.7, 'minw': 4.8}, 'nodes': _full_desc}}}
        other_col = {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.05, 'r': 0.1, 'colour': G.C.L_BLACK}, 'nodes': stake_desc_rows}
    stake_sprite = get_stake_sprite()
    _stake_desc = {}
    _stake_center = 'G.GAME.stake[G.P_CENTER_POOLS.Stake]'localize()
    _full_desc = {}
    for kv in ipairs(_stake_desc):
        '#_full_desc + 1[_full_desc]' = {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': v}
    '#_full_desc[_full_desc]' = 'None'
    current_col = {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.1, 'minw': 4}, 'nodes': {1: {'n': G.UIT.O, 'config': {'colour': G.C.BLUE, 'object': stake_sprite, 'hover': True, 'can_collide': False}}, 2: {'n': G.UIT.T, 'config': {'text': localize(), 'scale': 0.45, 'colour': G.C.WHITE}}}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.05, 'colour': get_stake_col(), 'r': 0.05}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.05, 'colour': G.C.WHITE, 'r': 0.05}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.03, 'minh': 0.7, 'minw': 3.8}, 'nodes': _full_desc}}}}}}}
    return {'n': G.UIT.ROOT, 'config': {'align': 'cm', 'colour': G.C.BLACK, 'r': 0.1, 'padding': 0.1}, 'nodes': {1: current_col, 2: other_col}}
def view_deck(unplayed_only):
    deck_tables = {}remove_nils()
    G.VIEWING_DECK = Truetable.sort()
    SUITS = {'Spades': {}, 'Hearts': {}, 'Clubs': {}, 'Diamonds': {}}
    suit_map = {1: 'Spades', 2: 'Hearts', 3: 'Clubs', 4: 'Diamonds'}
    for kv in ipairs():table.insert(v.base.suit[SUITS], v)
    for j in range(1, 4, ):
        if '1[SUITS[suit_map[j]]]':
            view_deck = CardArea()table.insert(deck_tables)
            for i in range(1, len('suit_map[j][SUITS]'), ):
                if 'i[SUITS[suit_map[j]]]':
                    greyed = _scale = ('None', 0.7)
                    if unplayed_only & (not ('i[SUITS[suit_map[j]]]'.area & ('i[SUITS[suit_map[j]]]'.area == G.deck) if 'i[SUITS[suit_map[j]]]'.area & ('i[SUITS[suit_map[j]]]'.area == G.deck) else 'i[SUITS[suit_map[j]]]'.ability.wheel_flipped)):
                        greyed = True
                    copy = copy_card(i[SUITS[suit_map[j]]], None, _scale)
                    copy.greyed = greyed
                    copy.T.x = view_deck.T.x + view_deck.T.w / 2
                    copy.T.y = view_deck.T.ycopy.hard_set_T()view_deck.emplace(copy)
    flip_col = G.C.WHITE
    suit_tallies = {'Spades': 0, 'Hearts': 0, 'Clubs': 0, 'Diamonds': 0}
    mod_suit_tallies = {'Spades': 0, 'Hearts': 0, 'Clubs': 0, 'Diamonds': 0}
    rank_tallies = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0}
    mod_rank_tallies = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0}
    rank_name_mapping = {1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9, 9: 10, 10: 'J', 11: 'Q', 12: 'K', 13: 'A'}
    face_tally = 0
    mod_face_tally = 0
    num_tally = 0
    mod_num_tally = 0
    ace_tally = 0
    mod_ace_tally = 0
    wheel_flipped = 0
    for kv in ipairs():
        if (v.ability.name != 'Stone Card') & (not unplayed_only if not unplayed_only else v.area & (v.area == G.deck) if v.area & (v.area == G.deck) else v.ability.wheel_flipped):
            if v.ability.wheel_flipped & unplayed_only:
                wheel_flipped = wheel_flipped + 1
            'v.base.suit[suit_tallies]' = ('v.base.suit[suit_tallies]' if 'v.base.suit[suit_tallies]' else 0) + 1
            "'Spades'[mod_suit_tallies]" = ("'Spades'[mod_suit_tallies]" if "'Spades'[mod_suit_tallies]" else 0) + (v.is_suit(Spades) & 1 if v.is_suit(Spades) & 1 else 0)
            "'Hearts'[mod_suit_tallies]" = ("'Hearts'[mod_suit_tallies]" if "'Hearts'[mod_suit_tallies]" else 0) + (v.is_suit(Hearts) & 1 if v.is_suit(Hearts) & 1 else 0)
            "'Clubs'[mod_suit_tallies]" = ("'Clubs'[mod_suit_tallies]" if "'Clubs'[mod_suit_tallies]" else 0) + (v.is_suit(Clubs) & 1 if v.is_suit(Clubs) & 1 else 0)
            "'Diamonds'[mod_suit_tallies]" = ("'Diamonds'[mod_suit_tallies]" if "'Diamonds'[mod_suit_tallies]" else 0) + (v.is_suit(Diamonds) & 1 if v.is_suit(Diamonds) & 1 else 0)
            card_id = v.get_id()
            face_tally = face_tally + (((card_id == 11 if card_id == 11 else card_id == 12) if (card_id == 11 if card_id == 11 else card_id == 12) else card_id == 13) & 1 if ((card_id == 11 if card_id == 11 else card_id == 12) if (card_id == 11 if card_id == 11 else card_id == 12) else card_id == 13) & 1 else 0)
            mod_face_tally = mod_face_tally + (v.is_face() & 1 if v.is_face() & 1 else 0)
            if (card_id > 1) & card_id < 11:
                num_tally = num_tally + 1
                if not v.debuff:
                    mod_num_tally = mod_num_tally + 1
            if card_id == 14:
                ace_tally = ace_tally + 1
                if not v.debuff:
                    mod_ace_tally = mod_ace_tally + 1
            'card_id - 1[rank_tallies]' = 'card_id - 1[rank_tallies]' + 1
            if not v.debuff:
                'card_id - 1[mod_rank_tallies]' = 'card_id - 1[mod_rank_tallies]' + 1
    modded = (((face_tally != mod_face_tally if face_tally != mod_face_tally else "'Spades'[mod_suit_tallies]" != "'Spades'[suit_tallies]") if (face_tally != mod_face_tally if face_tally != mod_face_tally else "'Spades'[mod_suit_tallies]" != "'Spades'[suit_tallies]") else "'Hearts'[mod_suit_tallies]" != "'Hearts'[suit_tallies]") if ((face_tally != mod_face_tally if face_tally != mod_face_tally else "'Spades'[mod_suit_tallies]" != "'Spades'[suit_tallies]") if (face_tally != mod_face_tally if face_tally != mod_face_tally else "'Spades'[mod_suit_tallies]" != "'Spades'[suit_tallies]") else "'Hearts'[mod_suit_tallies]" != "'Hearts'[suit_tallies]") else "'Clubs'[mod_suit_tallies]" != "'Clubs'[suit_tallies]") if (((face_tally != mod_face_tally if face_tally != mod_face_tally else "'Spades'[mod_suit_tallies]" != "'Spades'[suit_tallies]") if (face_tally != mod_face_tally if face_tally != mod_face_tally else "'Spades'[mod_suit_tallies]" != "'Spades'[suit_tallies]") else "'Hearts'[mod_suit_tallies]" != "'Hearts'[suit_tallies]") if ((face_tally != mod_face_tally if face_tally != mod_face_tally else "'Spades'[mod_suit_tallies]" != "'Spades'[suit_tallies]") if (face_tally != mod_face_tally if face_tally != mod_face_tally else "'Spades'[mod_suit_tallies]" != "'Spades'[suit_tallies]") else "'Hearts'[mod_suit_tallies]" != "'Hearts'[suit_tallies]") else "'Clubs'[mod_suit_tallies]" != "'Clubs'[suit_tallies]") else "'Diamonds'[mod_suit_tallies]" != "'Diamonds'[suit_tallies]"
    if wheel_flipped > 0:
        flip_col = mix_colours()
    rank_cols = {}
    for i in range(13, 1, -1):
        mod_delta = 'i[mod_rank_tallies]' != 'i[rank_tallies]'
        '#rank_cols + 1[rank_cols]' = {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.07}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'r': 0.1, 'padding': 0.04, 'emboss': 0.04, 'minw': 0.5, 'colour': G.C.L_BLACK}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': 'i[rank_name_mapping]', 'colour': G.C.JOKER_GREY, 'scale': 0.35, 'shadow': True}}}}, 2: {'n': G.UIT.C, 'config': {'align': 'cr', 'minw': 0.4}, 'nodes': {1: mod_delta & {'n': G.UIT.O, 'config': {'object': DynaText()}} if mod_delta & {'n': G.UIT.O, 'config': {'object': DynaText()}} else {'n': G.UIT.T, 'config': {'text': 'i[rank_tallies]' if 'i[rank_tallies]' else 'NIL', 'colour': flip_col, 'scale': 0.45, 'shadow': True}}}}}}
    t = {'n': G.UIT.ROOT, 'config': {'align': 'cm', 'colour': G.C.CLEAR}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.05}, 'nodes': {}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'minw': 1.5, 'minh': 2, 'r': 0.1, 'colour': G.C.BLACK, 'emboss': 0.05}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0.1}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'r': 0.1, 'colour': G.C.L_BLACK, 'emboss': 0.05, 'padding': 0.15}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.O, 'config': {'object': DynaText()}}}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm', 'r': 0.1, 'padding': 0.1, 'minw': 2.5, 'minh': 1.3, 'colour': G.C.WHITE, 'emboss': 0.05}, 'nodes': {1: {'n': G.UIT.O, 'config': {'object': UIBox()}}}}}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm', 'r': 0.1, 'outline_colour': G.C.L_BLACK, 'line_emboss': 0.05, 'outline': 1.5}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'minh': 0.05, 'padding': 0.07}, 'nodes': {1: {'n': G.UIT.O, 'config': {'object': DynaText()}}}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm', 'minh': 0.05, 'padding': 0.1}, 'nodes': {1: tally_sprite(), 2: tally_sprite(), 3: tally_sprite()}}, 3: {'n': G.UIT.R, 'config': {'align': 'cm', 'minh': 0.05, 'padding': 0.1}, 'nodes': {1: tally_sprite(), 2: tally_sprite()}}, 4: {'n': G.UIT.R, 'config': {'align': 'cm', 'minh': 0.05, 'padding': 0.1}, 'nodes': {1: tally_sprite(), 2: tally_sprite()}}}}}}, 2: {'n': G.UIT.C, 'config': {'align': 'cm'}, 'nodes': rank_cols}, 3: {'n': G.UIT.B, 'config': {'w': 0.1, 'h': 0.1}}}}, 2: {'n': G.UIT.B, 'config': {'w': 0.2, 'h': 0.1}}, 3: {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0.1, 'r': 0.1, 'colour': G.C.BLACK, 'emboss': 0.05}, 'nodes': deck_tables}}}, 3: {'n': G.UIT.R, 'config': {'align': 'cm', 'minh': 0.8, 'padding': 0.05}, 'nodes': {1: modded & {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.C, 'config': {'padding': 0.3, 'r': 0.1, 'colour': mix_colours()}, 'nodes': {}}, 2: {'n': G.UIT.T, 'config': {'text': ' ' + localize(ph_deck_preview_effective), 'colour': G.C.WHITE, 'scale': 0.3}}}} if modded & {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.C, 'config': {'padding': 0.3, 'r': 0.1, 'colour': mix_colours()}, 'nodes': {}}, 2: {'n': G.UIT.T, 'config': {'text': ' ' + localize(ph_deck_preview_effective), 'colour': G.C.WHITE, 'scale': 0.3}}}} else 'None', 2: (wheel_flipped > 0) & {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.C, 'config': {'padding': 0.3, 'r': 0.1, 'colour': flip_col}, 'nodes': {}}, 2: {'n': G.UIT.T, 'config': {'text': ' ' + ((wheel_flipped > 1) & localize() if (wheel_flipped > 1) & localize() else localize()), 'colour': G.C.WHITE, 'scale': 0.3}}}} if (wheel_flipped > 0) & {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.C, 'config': {'padding': 0.3, 'r': 0.1, 'colour': flip_col}, 'nodes': {}}, 2: {'n': G.UIT.T, 'config': {'text': ' ' + ((wheel_flipped > 1) & localize() if (wheel_flipped > 1) & localize() else localize()), 'colour': G.C.WHITE, 'scale': 0.3}}}} else 'None'}}}}
    return t
def tally_sprite(pos, value, tooltip):
    text_colour = G.C.BLACK
    if (type(value) == 'table') & ('1[value]'.string == '2[value]'.string):
        text_colour = '1[value]'.colour if '1[value]'.colour else G.C.WHITE
        value = '1[value]'.string
    t_s = Sprite(0, 0, 0.5, 0.5, "ui_"..G.SETTINGS.colourblind_option and 2 or 1[G.ASSET_ATLAS])
    t_s.states.drag.can = False
    t_s.states.hover.can = False
    t_s.states.collide.can = False
    return {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0.07, 'force_focus': True, 'focus_args': {'type': 'tally_sprite'}, 'tooltip': {'text': tooltip}}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'r': 0.1, 'padding': 0.04, 'emboss': 0.05, 'colour': G.C.JOKER_GREY}, 'nodes': {1: {'n': G.UIT.O, 'config': {'w': 0.5, 'h': 0.5, 'can_collide': False, 'object': t_s, 'tooltip': {'text': tooltip}}}}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: (type(value) == 'table') & {'n': G.UIT.O, 'config': {'object': DynaText()}} if (type(value) == 'table') & {'n': G.UIT.O, 'config': {'object': DynaText()}} else {'n': G.UIT.T, 'config': {'text': value if value else 'NIL', 'colour': text_colour, 'scale': 0.4, 'shadow': True}}}}}}
def used_vouchers():
    silent = False
    keys_used = {}
    area_count = 0
    voucher_areas = {}
    voucher_tables = {}
    voucher_table_rows = {}
    for kv in ipairs("Voucher"[G.P_CENTER_POOLS]):
        key = 1 + math.floor()
        'key[keys_used]' = 'key[keys_used]' if 'key[keys_used]' else {}
        if 'v.key[G.GAME.used_vouchers]':
            '#keys_used[key] + 1[keys_used[key]]' = v
    for kv in ipairs(keys_used):
        if next(v):
            area_count = area_count + 1
    for kv in ipairs(keys_used):
        if next(v):
            if len(voucher_areas == 5 if voucher_areas == 5 else len(voucher_areas == 10)):table.insert(voucher_table_rows)
                voucher_tables = {}
            '#voucher_areas + 1[voucher_areas]' = CardArea()
            for kkvv in ipairs(v):
                center = 'vv.key[G.P_CENTERS]'
                card = Card()
                card.ability.order = vv.ordercard.start_materialize(None, silent)
                silent = True'#voucher_areas[voucher_areas]'.emplace(card)table.insert(voucher_tables)table.insert(voucher_table_rows)
    t = silent & {'n': G.UIT.ROOT, 'config': {'align': 'cm', 'colour': G.C.CLEAR}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.O, 'config': {'object': DynaText()}}}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm', 'minh': 0.5}, 'nodes': {}}, 3: {'n': G.UIT.R, 'config': {'align': 'cm', 'colour': G.C.BLACK, 'r': 1, 'padding': 0.15, 'emboss': 0.05}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': voucher_table_rows}}}}} if silent & {'n': G.UIT.ROOT, 'config': {'align': 'cm', 'colour': G.C.CLEAR}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.O, 'config': {'object': DynaText()}}}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm', 'minh': 0.5}, 'nodes': {}}, 3: {'n': G.UIT.R, 'config': {'align': 'cm', 'colour': G.C.BLACK, 'r': 1, 'padding': 0.15, 'emboss': 0.05}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': voucher_table_rows}}}}} else {'n': G.UIT.ROOT, 'config': {'align': 'cm', 'colour': G.C.CLEAR}, 'nodes': {1: {'n': G.UIT.O, 'config': {'object': DynaText()}}}}
    return t
def create_UIBox_your_collection():set_discover_tallies()G.E_MANAGER.add_event()
    t = create_UIBox_generic_options()
    return t
def create_UIBox_your_collection_jokers():
    deck_tables = {}
    G.your_collection = {}
    for j in range(1, 3, ):
        'j[G.your_collection]' = CardArea()table.insert(deck_tables)
    joker_options = {}
    for i in range(1, math.ceil(), ):table.insert(joker_options)
    for i in range(1, 5, ):
        for j in range(1, len(G.your_collection), ):
            center = 'i + j - 1 * 5[G.P_CENTER_POOLS["Joker"]]'
            card = Card()
            card.sticker = get_joker_win_sticker(center)'j[G.your_collection]'.emplace(card)INIT_COLLECTION_CARD_ALERTS()
    t = create_UIBox_generic_options()
    return t
def create_UIBox_your_collection_tarots():
    deck_tables = {}
    G.your_collection = {}
    for j in range(1, 2, ):
        'j[G.your_collection]' = CardArea()table.insert(deck_tables)
    tarot_options = {}
    for i in range(1, math.floor(), ):table.insert(tarot_options)
    for j in range(1, len(G.your_collection), ):
        for i in range(1, 4 + j, ):
            center = 'i + j - 1 * 5[G.P_CENTER_POOLS["Tarot"]]'
            card = Card()card.start_materialize(None)'j[G.your_collection]'.emplace(card)INIT_COLLECTION_CARD_ALERTS()
    t = create_UIBox_generic_options()
    return t
def create_UIBox_your_collection_boosters():
    deck_tables = {}
    G.your_collection = {}
    for j in range(1, 2, ):
        'j[G.your_collection]' = CardArea()table.insert(deck_tables)
    booster_options = {}
    for i in range(1, math.ceil(), ):table.insert(booster_options)
    for j in range(1, len(G.your_collection), ):
        for i in range(1, 4, ):
            center = 'i + j - 1 * 4[G.P_CENTER_POOLS["Booster"]]'
            card = Card()card.start_materialize(None)'j[G.your_collection]'.emplace(card)INIT_COLLECTION_CARD_ALERTS()
    t = create_UIBox_generic_options()
    return t
def create_UIBox_your_collection_planets():
    deck_tables = {}
    G.your_collection = {}
    for j in range(1, 2, ):
        'j[G.your_collection]' = CardArea()table.insert(deck_tables)
    for j in range(1, len(G.your_collection), ):
        for i in range(1, 6, ):
            center = 'i + j - 1 * 6[G.P_CENTER_POOLS["Planet"]]'
            card = Card()card.start_materialize(None)'j[G.your_collection]'.emplace(card)INIT_COLLECTION_CARD_ALERTS()
    t = create_UIBox_generic_options()
    return t
def create_UIBox_your_collection_spectrals():
    deck_tables = {}
    G.your_collection = {}
    for j in range(1, 2, ):
        'j[G.your_collection]' = CardArea()table.insert(deck_tables)
    for j in range(1, len(G.your_collection), ):
        for i in range(1, 3 + j, ):
            center = 'i + j - 1 * 3 + j - 1[G.P_CENTER_POOLS["Spectral"]]'
            card = Card()card.start_materialize(None)'j[G.your_collection]'.emplace(card)
    spectral_options = {}
    for i in range(1, math.floor(), ):table.insert(spectral_options)INIT_COLLECTION_CARD_ALERTS()
    t = create_UIBox_generic_options()
    return t
def create_UIBox_your_collection_vouchers(exit):
    deck_tables = {}
    G.your_collection = {}
    for j in range(1, 2, ):
        'j[G.your_collection]' = CardArea()table.insert(deck_tables)
    voucher_options = {}
    for i in range(1, math.ceil(), ):table.insert(voucher_options)
    for i in range(1, 4, ):
        for j in range(1, len(G.your_collection), ):
            center = 'i + j - 1 * 4[G.P_CENTER_POOLS["Voucher"]]'
            card = Card()
            card.ability.order = i + (j - 1) * 4card.start_materialize(None)'j[G.your_collection]'.emplace(card)INIT_COLLECTION_CARD_ALERTS()
    t = create_UIBox_generic_options()
    return t
def create_UIBox_your_collection_seals(exit):
    deck_tables = {}
    G.your_collection = CardArea()table.insert(deck_tables)
    for kv in ipairs('Seal'[G.P_CENTER_POOLS]):
        center = G.P_CENTERS.c_base
        card = Card()card.set_seal()G.your_collection.emplace(card)
    t = create_UIBox_generic_options()
    return t
def create_UIBox_your_collection_enhancements(exit):
    deck_tables = {}
    G.your_collection = {}
    for j in range(1, 2, ):
        'j[G.your_collection]' = CardArea()table.insert(deck_tables)
    for i in range(1, 4, ):
        for j in range(1, len(G.your_collection), ):
            center = 'i + j - 1 * 4[G.P_CENTER_POOLS["Enhanced"]]'
            card = Card()'j[G.your_collection]'.emplace(card)
    t = create_UIBox_generic_options()
    return t
def create_UIBox_your_collection_editions():
    G.your_collection = {}
    '1[G.your_collection]' = CardArea()
    deck_tables = {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0, 'no_fill': True}, 'nodes': {1: {'n': G.UIT.O, 'config': {'object': '1[G.your_collection]'}}}}
    editions = {1: 'base', 2: 'foil', 3: 'holo', 4: 'polychrome', 5: 'negative'}
    for i in range(1, 5, ):
        card = Card()card.start_materialize()
        if "'e_'..editions[i][G.P_CENTERS]".discovered:card.set_edition()'1[G.your_collection]'.emplace(card)INIT_COLLECTION_CARD_ALERTS()
    t = create_UIBox_generic_options()
    return t
def create_UIBox_your_collection_decks():
    G.GAME.viewed_back = Back()
    area = CardArea()
    for i in range(1, 52, ):
        card = Card()
        card.sprite_facing = 'back'
        card.facing = 'back'area.emplace(card)
        if i == 52:
            G.sticker_card = card';'
            card.sticker = get_deck_win_sticker()
    ordered_names = {}
    for kv in ipairs():
        '#ordered_names + 1[ordered_names]' = v.name
    t = create_UIBox_generic_options()
    return t
def create_UIBox_your_collection_tags():
    tag_matrix = {1: {}, 2: {}, 3: {}, 4: {}}
    tag_tab = {}
    for kv in pairs():
        '#tag_tab + 1[tag_tab]' = vtable.sort(tag_tab)
    tags_to_be_alerted = {}
    for kv in ipairs(tag_tab):
        discovered = v.discovered
        temp_tag = Tag()
        if not v.discovered:
            temp_tag.hide_ability = True
        temp_tag_ui = temp_tag_sprite = temp_tag.generate_UI()
        '1 + k - 1 % 6[tag_matrix[math.ceil(k - 1 / 6 + 0.001)]]' = {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0.1}, 'nodes': {1: temp_tag_ui}}
        if discovered & (not v.alerted):
            '#tags_to_be_alerted + 1[tags_to_be_alerted]' = temp_tag_spriteG.E_MANAGER.add_event()
    t = create_UIBox_generic_options()
    return t
def create_UIBox_your_collection_blinds(exit):
    blind_matrix = {1: {}, 2: {}, 3: {}, 4: {}, 5: {}, 6: {}}
    blind_tab = {}
    for kv in pairs():
        '#blind_tab + 1[blind_tab]' = vtable.sort(blind_tab)
    blinds_to_be_alerted = {}
    for kv in ipairs(blind_tab):
        discovered = v.discovered
        temp_blind = AnimatedSprite(0, 0, 1.3, 1.3, 'blind_chips'[G.ANIMATION_ATLAS])temp_blind.define_draw_steps()
        if k == 1:G.E_MANAGER.add_event()
        temp_blind.float = True
        temp_blind.states.hover.can = True
        temp_blind.states.drag.can = False
        temp_blind.states.collide.can = True
        temp_blind.config = {'blind': v, 'force_focus': True}
        if discovered & (not v.alerted):
            '#blinds_to_be_alerted + 1[blinds_to_be_alerted]' = temp_blind
        temp_blind.hover = lambda: 
        if not G.CONTROLLER.dragging.target if not G.CONTROLLER.dragging.target else G.CONTROLLER.using_touch:
            if (not temp_blind.hovering) & temp_blind.states.visible:
                temp_blind.hovering = True
                temp_blind.hover_tilt = 3temp_blind.juice_up(0.05, 0.02)play_sound(chips1)
                temp_blind.config.h_popup = create_UIBox_blind_popup(v, discovered)
                temp_blind.config.h_popup_config = {'align': 'cl', 'offset': {'x': -0.1, 'y': 0}, 'parent': temp_blind}Node.hover(temp_blind)
                if temp_blind.children.alert:temp_blind.children.alert.remove()
                    temp_blind.children.alert = 'None'
                    temp_blind.config.blind.alerted = TrueG.save_progress()
        temp_blind.stop_hover = lambda: 
        temp_blind.hovering = False';'Node.stop_hover(temp_blind)';'
        temp_blind.hover_tilt = 0
        '1 + k - 1 % 5[blind_matrix[math.ceil(k - 1 / 5 + 0.001)]]' = {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0.1}, 'nodes': {1: ((k == 6 if k == 6 else k == 16) if (k == 6 if k == 6 else k == 16) else k == 26) & {'n': G.UIT.B, 'config': {'h': 0.2, 'w': 0.5}} if ((k == 6 if k == 6 else k == 16) if (k == 6 if k == 6 else k == 16) else k == 26) & {'n': G.UIT.B, 'config': {'h': 0.2, 'w': 0.5}} else 'None', 2: {'n': G.UIT.O, 'config': {'object': temp_blind, 'focus_with_object': True}}, 3: ((k == 5 if k == 5 else k == 15) if (k == 5 if k == 5 else k == 15) else k == 25) & {'n': G.UIT.B, 'config': {'h': 0.2, 'w': 0.5}} if ((k == 5 if k == 5 else k == 15) if (k == 5 if k == 5 else k == 15) else k == 25) & {'n': G.UIT.B, 'config': {'h': 0.2, 'w': 0.5}} else 'None'}}G.E_MANAGER.add_event()
    ante_amounts = {}
    for i in range(1, math.min(16), ):
        spacing = 1 - math.min(20) * 0.06
        if (spacing > 0) & (i > 1):
            '#ante_amounts + 1[ante_amounts]' = {'n': G.UIT.R, 'config': {'minh': spacing}, 'nodes': {}}
        blind_chip = Sprite(0, 0, 0.2, 0.2, "ui_"..G.SETTINGS.colourblind_option and 2 or 1[G.ASSET_ATLAS])
        blind_chip.states.drag.can = False
        '#ante_amounts + 1[ante_amounts]' = {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.03}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'minw': 0.7}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': i, 'scale': 0.4, 'colour': G.C.FILTER, 'shadow': True}}}}, 2: {'n': G.UIT.C, 'config': {'align': 'cr', 'minw': 2.8}, 'nodes': {1: {'n': G.UIT.O, 'config': {'object': blind_chip}}, 2: {'n': G.UIT.C, 'config': {'align': 'cm', 'minw': 0.03, 'minh': 0.01}, 'nodes': {}}, 3: {'n': G.UIT.T, 'config': {'text': number_format(), 'scale': 0.4, 'colour': (i <= 'G.SETTINGS.profile[G.PROFILES]'.high_scores.furthest_ante.amt) & G.C.RED if (i <= 'G.SETTINGS.profile[G.PROFILES]'.high_scores.furthest_ante.amt) & G.C.RED else G.C.JOKER_GREY, 'shadow': True}}}}}}
    extras = 'None'
    t = create_UIBox_generic_options()
    return t
def create_UIBox_blind_popup(blind, discovered, vars):
    blind_text = {}
    _dollars = blind.dollars
    loc_target = localize()
    loc_name = localize()
    if discovered:
        ability_text = {}
        if loc_target:
            for kv in ipairs(loc_target):
                '#ability_text + 1[ability_text]' = {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': ((k == 1) & (blind.name == 'The Wheel') & '1' if (k == 1) & (blind.name == 'The Wheel') & '1' else '') + v, 'scale': 0.35, 'shadow': True, 'colour': G.C.WHITE}}}}
        stake_sprite = get_stake_sprite()
        '#blind_text + 1[blind_text]' = {'n': G.UIT.R, 'config': {'align': 'cm', 'emboss': 0.05, 'r': 0.1, 'minw': 2.5, 'padding': 0.07, 'colour': G.C.WHITE}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'maxw': 2.4}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(ph_blind_score_at_least), 'scale': 0.35, 'colour': G.C.UI.TEXT_DARK}}}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.O, 'config': {'object': stake_sprite}}, 2: {'n': G.UIT.T, 'config': {'text': blind.mult + localize(k_x_base), 'scale': 0.4, 'colour': G.C.RED}}}}, 3: {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(ph_blind_reward), 'scale': 0.35, 'colour': G.C.UI.TEXT_DARK}}, 2: {'n': G.UIT.O, 'config': {'object': DynaText()}}}}, 4: '1[ability_text]' & {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.08, 'colour': mix_colours(), 'r': 0.1, 'emboss': 0.05, 'minw': 2.5, 'minh': 0.9}, 'nodes': ability_text} if '1[ability_text]' & {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.08, 'colour': mix_colours(), 'r': 0.1, 'emboss': 0.05, 'minw': 2.5, 'minh': 0.9}, 'nodes': ability_text} else 'None'}}
    else:
        '#blind_text + 1[blind_text]' = {'n': G.UIT.R, 'config': {'align': 'cm', 'emboss': 0.05, 'r': 0.1, 'minw': 2.5, 'padding': 0.1, 'colour': G.C.WHITE}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(ph_defeat_this_blind_1), 'scale': 0.4, 'colour': G.C.UI.TEXT_DARK}}}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(ph_defeat_this_blind_2), 'scale': 0.4, 'colour': G.C.UI.TEXT_DARK}}}}}}
    return {'n': G.UIT.ROOT, 'config': {'align': 'cm', 'padding': 0.05, 'colour': lighten(), 'r': 0.1, 'emboss': 0.05}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'emboss': 0.05, 'r': 0.1, 'minw': 2.5, 'padding': 0.1, 'colour': ((not discovered) & G.C.JOKER_GREY if (not discovered) & G.C.JOKER_GREY else blind.boss_colour) if ((not discovered) & G.C.JOKER_GREY if (not discovered) & G.C.JOKER_GREY else blind.boss_colour) else G.C.GREY}, 'nodes': {1: {'n': G.UIT.O, 'config': {'object': DynaText()}}}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': blind_text}}}
def create_UIBox_card_unlock(card_center):
    G.your_collection = CardArea()
    card = Card()
    locked_card = Card()locked_card.remove_UI()
    locked_card.ID = card.ID
    card.states.click.can = False
    locked_card.states.click.can = False
    card.states.visible = False
    card.no_ui = TrueG.E_MANAGER.add_event()G.E_MANAGER.add_event()G.E_MANAGER.add_event()G.E_MANAGER.add_event()G.E_MANAGER.add_event()G.E_MANAGER.add_event()G.E_MANAGER.add_event()G.E_MANAGER.add_event()G.your_collection.emplace(card)G.your_collection.emplace(locked_card)
    t = create_UIBox_generic_options()
    return t
def create_UIBox_deck_unlock(deck_center):
    G.GAME.viewed_back = Back(deck_center)
    area = CardArea()
    for i in range(1, 52, ):
        card = Card()area.emplace(card)
        'deck_center.key[card]' = True
        card.sprite_facing = 'back'
        card.facing = 'back'
    deck_criteria = {}
    if deck_center.unlock_condition.type == 'win_deck':
        other_name = localize()localize()
    elif deck_center.unlock_condition.type == 'win_stake':
        other_name = localize()localize()
    elif deck_center.unlock_condition.type == 'discover_amount':localize()
    deck_criteria_cols = {}
    for kv in ipairs(deck_criteria):
        if k > 1:
            '#deck_criteria_cols + 1[deck_criteria_cols]' = {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0, 'minw': 0.1}, 'nodes': {}}
        '#deck_criteria_cols + 1[deck_criteria_cols]' = {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0}, 'nodes': v}
    t = create_UIBox_generic_options()
    return t
def credits():
    text_scale = 0.75
    t = create_UIBox_generic_options()
    return t
def challenges(from_game_over):
    if 'G.SETTINGS.profile[G.PROFILES]'.all_unlocked:
        'G.SETTINGS.profile[G.PROFILES]'.challenges_unlocked = len(G.CHALLENGES)
    if not 'G.SETTINGS.profile[G.PROFILES]'.challenges_unlocked:
        deck_wins = 0
        for kv in pairs():
            if v.wins & '1[v.wins]':
                deck_wins = deck_wins + 1
        loc_nodes = {}localize()
        return {'n': G.UIT.ROOT, 'config': {'align': 'cm', 'padding': 0.1, 'colour': G.C.CLEAR, 'minh': 8.02, 'minw': 7}, 'nodes': {1: transparent_multiline_text(loc_nodes)}}
    G.run_setup_seed = 'None'
    if G.OVERLAY_MENU:
        seed_toggle = G.OVERLAY_MENU.get_UIE_by_ID(run_setup_seed)
        if seed_toggle:
            seed_toggle.states.visible = False
    _ch_comp = _ch_tot = (0, len(G.CHALLENGES))
    for kv in ipairs():
        if v.id & "v.id or ''[G.PROFILES[G.SETTINGS.profile].challenge_progress.completed]":
            _ch_comp = _ch_comp + 1
    _ch_tab = {'comp': _ch_comp, 'unlocked': 'G.SETTINGS.profile[G.PROFILES]'.challenges_unlocked}
    return {'n': G.UIT.ROOT, 'config': {'align': 'cm', 'padding': 0.1, 'colour': G.C.CLEAR, 'minh': 8, 'minw': 7}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.1, 'r': 0.1, 'colour': G.C.BLACK}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.1}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(k_challenge_mode), 'scale': 0.4, 'colour': G.C.UI.TEXT_LIGHT, 'shadow': True}}}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm', 'minw': 8.5, 'minh': 1.5, 'padding': 0.2}, 'nodes': {1: UIBox_button()}}, 3: {'n': G.UIT.R, 'config': {'align': 'cm', 'minh': 0.8, 'r': 0.1, 'minw': 4.5, 'colour': G.C.L_BLACK, 'emboss': 0.05, 'progress_bar': {'max': _ch_tot, 'ref_table': _ch_tab, 'ref_value': 'unlocked', 'empty_col': G.C.L_BLACK, 'filled_col': G.C.FILTER}}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0.05, 'r': 0.1, 'minw': 4.5}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(), 'scale': 0.3, 'colour': G.C.WHITE, 'shadow': True}}}}}}, 4: {'n': G.UIT.R, 'config': {'align': 'cm', 'minh': 0.8, 'r': 0.1, 'minw': 4.5, 'colour': G.C.L_BLACK, 'emboss': 0.05, 'progress_bar': {'max': _ch_tot, 'ref_table': _ch_tab, 'ref_value': 'comp', 'empty_col': G.C.L_BLACK, 'filled_col': adjust_alpha()}}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0.05, 'r': 0.1, 'minw': 4.5}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(), 'scale': 0.3, 'colour': G.C.WHITE, 'shadow': True}}}}}}}}, 2: G.F_DAILIES & {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.1, 'r': 0.1, 'colour': G.C.BLACK}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.1}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(k_daily_run), 'scale': 0.4, 'colour': G.C.UI.TEXT_LIGHT, 'shadow': True}}}}, 2: {'n': G.UIT.R, 'config': {'align': 'cl', 'minw': 8.5, 'minh': 4}, 'nodes': {1: G.UIDEF.daily_overview()}}}} if G.F_DAILIES & {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.1, 'r': 0.1, 'colour': G.C.BLACK}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.1}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(k_daily_run), 'scale': 0.4, 'colour': G.C.UI.TEXT_LIGHT, 'shadow': True}}}}, 2: {'n': G.UIT.R, 'config': {'align': 'cl', 'minw': 8.5, 'minh': 4}, 'nodes': {1: G.UIDEF.daily_overview()}}}} else 'None'}}
def daily_overview():
    hist_height = hist_width = (3, 3)
    daily_results = {'score': {'me': {'val': 20000, 'percentile': 75}, 'hist': {1: 0.05, 2: 0.05, 3: 0.05, 4: 0.05, 5: 0.05, 6: 0.05, 7: 0.05, 8: 0.05, 9: 0.05, 10: 0.05, 11: 0.05, 12: 0.05, 13: 0.15, 14: 0.1, 15: 0.1, 16: 0.05, 17: 0.05, 18: 0.05, 19: 0.05, 20: 0.05}}}
    score_hist = max_score_hist = ({}, 0)
    for kv in ipairs():
        if max_score_hist < v:
            max_score_hist = v
    for kv in ipairs():
        '#score_hist + 1[score_hist]' = {'n': G.UIT.C, 'config': {'align': 'bm'}, 'nodes': {1: {'n': G.UIT.C, 'config': {'colour': G.C.BLUE, 'minw': hist_width / len(daily_results.score.hist), 'minh': (v + 0.05 * math.random()) / max_score_hist * hist_height}}}}
    return {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': score_hist}
def run_setup(from_game_over):
    G.run_setup_seed = 'None'
    _challenge_chosen = from_game_over == 'challenge_list'
    from_game_over = from_game_over & (not from_game_over == 'challenge_list')
    _can_continue = G.MAIN_MENU_UI & G.FUNCS.can_continue()
    G.FUNCS.false_ret = lambda: 
    return False
    t = create_UIBox_generic_options()
    return t
def profile_select():
    G.focused_profile = (G.focused_profile if G.focused_profile else G.SETTINGS.profile) if (G.focused_profile if G.focused_profile else G.SETTINGS.profile) else 1
    t = create_UIBox_generic_options()
    return t
def profile_option(_profile):set_discover_tallies()
    G.focused_profile = _profile
    profile_data = get_compressed()
    if profile_data != 'None':
        profile_data = STR_UNPACK(profile_data)
        profile_data.name = profile_data.name if profile_data.name else 'P' + _profile
    '_profile[G.PROFILES]'.name = profile_data & profile_data.name if profile_data & profile_data.name else ''
    lwidth = rwidth = scale = (1, 1, 1)
    G.CHECK_PROFILE_DATA = 'None'
    t = {'n': G.UIT.ROOT, 'config': {'align': 'cm', 'colour': G.C.CLEAR}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.1, 'minh': 0.8}, 'nodes': {1: (_profile == G.SETTINGS.profile if _profile == G.SETTINGS.profile else not profile_data) & {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: create_text_input()}} if (_profile == G.SETTINGS.profile if _profile == G.SETTINGS.profile else not profile_data) & {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: create_text_input()}} else {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.1, 'minw': 4, 'r': 0.1, 'colour': G.C.BLACK, 'minh': 0.6}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': '_profile[G.PROFILES]'.name, 'scale': 0.45, 'colour': G.C.WHITE}}}}}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.1}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'minw': 6}, 'nodes': {1: '_profile[G.PROFILES]'.progress & '_profile[G.PROFILES]'.progress.discovered & create_progress_box() if '_profile[G.PROFILES]'.progress & '_profile[G.PROFILES]'.progress.discovered & create_progress_box() else {'n': G.UIT.C, 'config': {'align': 'cm', 'minh': 4, 'minw': 5.2, 'colour': G.C.BLACK, 'r': 0.1}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(k_empty_caps), 'scale': 0.5, 'colour': G.C.UI.TRANSPARENT_LIGHT}}}}}}, 2: {'n': G.UIT.C, 'config': {'align': 'cm', 'minh': 4}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'minh': 1}, 'nodes': {1: profile_data & {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'minw': lwidth}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(k_wins), 'colour': G.C.UI.TEXT_LIGHT, 'scale': scale * 0.7}}}}, 2: {'n': G.UIT.C, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': ': ', 'colour': G.C.UI.TEXT_LIGHT, 'scale': scale * 0.7}}}}, 3: {'n': G.UIT.C, 'config': {'align': 'cl', 'minw': rwidth}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': tostring(), 'colour': G.C.RED, 'shadow': True, 'scale': 1 * scale}}}}}} if profile_data & {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'minw': lwidth}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(k_wins), 'colour': G.C.UI.TEXT_LIGHT, 'scale': scale * 0.7}}}}, 2: {'n': G.UIT.C, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': ': ', 'colour': G.C.UI.TEXT_LIGHT, 'scale': scale * 0.7}}}}, 3: {'n': G.UIT.C, 'config': {'align': 'cl', 'minw': rwidth}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': tostring(), 'colour': G.C.RED, 'shadow': True, 'scale': 1 * scale}}}}}} else 'None'}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.2}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'minw': 4, 'maxw': 4, 'minh': 0.8, 'padding': 0.2, 'r': 0.1, 'hover': True, 'colour': G.C.BLUE, 'func': 'can_load_profile', 'button': 'load_profile', 'shadow': True, 'focus_args': {'nav': 'wide'}}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': ((_profile == G.SETTINGS.profile) & localize(b_current_profile) if (_profile == G.SETTINGS.profile) & localize(b_current_profile) else profile_data & localize(b_load_profile)) if ((_profile == G.SETTINGS.profile) & localize(b_current_profile) if (_profile == G.SETTINGS.profile) & localize(b_current_profile) else profile_data & localize(b_load_profile)) else localize(b_create_profile), 'ref_value': 'load_button_text', 'scale': 0.5, 'colour': G.C.UI.TEXT_LIGHT}}}}}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0, 'minh': 0.7}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'minw': 3, 'maxw': 4, 'minh': 0.6, 'padding': 0.2, 'r': 0.1, 'hover': True, 'colour': G.C.RED, 'func': 'can_delete_profile', 'button': 'delete_profile', 'shadow': True, 'focus_args': {'nav': 'wide'}}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': (_profile == G.SETTINGS.profile) & localize(b_reset_profile) if (_profile == G.SETTINGS.profile) & localize(b_reset_profile) else localize(b_delete_profile), 'scale': 0.3, 'colour': G.C.UI.TEXT_LIGHT}}}}}}, 3: (_profile == G.SETTINGS.profile) & (not 'G.SETTINGS.profile[G.PROFILES]'.all_unlocked) & {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0, 'minh': 0.7}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'minw': 3, 'maxw': 4, 'minh': 0.6, 'padding': 0.2, 'r': 0.1, 'hover': True, 'colour': G.C.ORANGE, 'func': 'can_unlock_all', 'button': 'unlock_all', 'shadow': True, 'focus_args': {'nav': 'wide'}}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(b_unlock_all), 'scale': 0.3, 'colour': G.C.UI.TEXT_LIGHT}}}}}} if (_profile == G.SETTINGS.profile) & (not 'G.SETTINGS.profile[G.PROFILES]'.all_unlocked) & {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0, 'minh': 0.7}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'minw': 3, 'maxw': 4, 'minh': 0.6, 'padding': 0.2, 'r': 0.1, 'hover': True, 'colour': G.C.ORANGE, 'func': 'can_unlock_all', 'button': 'unlock_all', 'shadow': True, 'focus_args': {'nav': 'wide'}}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(b_unlock_all), 'scale': 0.3, 'colour': G.C.UI.TEXT_LIGHT}}}}}} else {'n': G.UIT.R, 'config': {'align': 'cm', 'minw': 3, 'maxw': 4, 'minh': 0.7}, 'nodes': {1: '_profile[G.PROFILES]'.all_unlocked & ((not G.F_NO_ACHIEVEMENTS) & {'n': G.UIT.T, 'config': {'text': localize(), 'scale': 0.3, 'colour': G.C.UI.TEXT_LIGHT}} if (not G.F_NO_ACHIEVEMENTS) & {'n': G.UIT.T, 'config': {'text': localize(), 'scale': 0.3, 'colour': G.C.UI.TEXT_LIGHT}} else 'None') if '_profile[G.PROFILES]'.all_unlocked & ((not G.F_NO_ACHIEVEMENTS) & {'n': G.UIT.T, 'config': {'text': localize(), 'scale': 0.3, 'colour': G.C.UI.TEXT_LIGHT}} if (not G.F_NO_ACHIEVEMENTS) & {'n': G.UIT.T, 'config': {'text': localize(), 'scale': 0.3, 'colour': G.C.UI.TEXT_LIGHT}} else 'None') else 'None'}}}}}}}}, 3: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0}, 'nodes': {1: {'n': G.UIT.T, 'config': {'id': 'warning_text', 'text': localize(ph_click_confirm), 'scale': 0.4, 'colour': G.C.CLEAR}}}}}}
    return t
def stake_description(_stake):
    _stake_center = '_stake[G.P_CENTER_POOLS.Stake]'
    ret_nodes = {}
    if _stake_center:localize()
    desc_t = {}
    for kv in ipairs(ret_nodes):
        '#desc_t + 1[desc_t]' = {'n': G.UIT.R, 'config': {'align': 'cm', 'maxw': 5.3}, 'nodes': v}
    return {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0.05, 'r': 0.1, 'colour': G.C.L_BLACK}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(), 'scale': 0.35, 'colour': G.C.WHITE}}}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.03, 'colour': G.C.WHITE, 'r': 0.1, 'minh': 1, 'minw': 5.5}, 'nodes': desc_t}}}
def stake_option(_type):
    middle = {'n': G.UIT.R, 'config': {'align': 'cm', 'minh': 1.7, 'minw': 7.3}, 'nodes': {1: {'n': G.UIT.O, 'config': {'id': 'None', 'func': 'RUN_SETUP_check_stake2', 'object': Moveable()}}}}
    max_stake = get_deck_win_stake()
    if 'G.SETTINGS.profile[G.PROFILES]'.all_unlocked:
        max_stake = 8
    stake_options = {}
    for i in range(1, math.min(), ):
        'i[stake_options]' = i
    return {'n': G.UIT.ROOT, 'config': {'align': 'tm', 'colour': G.C.CLEAR, 'minh': 2.03, 'minw': 8.3}, 'nodes': {1: (_type == 'Continue') & middle if (_type == 'Continue') & middle else create_option_cycle()}}
def viewed_stake_option():
    G.viewed_stake = G.viewed_stake if G.viewed_stake else 1
    max_stake = get_deck_win_stake()
    if 'G.SETTINGS.profile[G.PROFILES]'.all_unlocked:
        max_stake = 8
    G.viewed_stake = math.min()
    if _type != 'Continue':
        'G.SETTINGS.profile[G.PROFILES]'.MEMORY.stake = G.viewed_stake
    stake_sprite = get_stake_sprite()
    return {'n': G.UIT.ROOT, 'config': {'align': 'cm', 'colour': G.C.BLACK, 'r': 0.1}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(k_stake), 'scale': 0.4, 'colour': G.C.L_BLACK, 'vert': True}}}}, 2: {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0.1}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0}, 'nodes': {1: {'n': G.UIT.O, 'config': {'colour': G.C.BLUE, 'object': stake_sprite, 'hover': True, 'can_collide': False}}}}, 2: G.UIDEF.stake_description()}}}}
def challenge_list(from_game_over):
    G.CHALLENGE_PAGE_SIZE = 10
    challenge_pages = {}
    for i in range(1, math.ceil(), ):table.insert(challenge_pages)G.E_MANAGER.add_event()
    _ch_comp = _ch_tot = (0, len(G.CHALLENGES))
    for kv in ipairs():
        if v.id & "v.id or ''[G.PROFILES[G.SETTINGS.profile].challenge_progress.completed]":
            _ch_comp = _ch_comp + 1
    t = create_UIBox_generic_options()
    return t
def challenge_list_page(_page):
    snapped = False
    challenge_list = {}
    for kv in ipairs():
        if (k > G.CHALLENGE_PAGE_SIZE * (_page if _page else 0)) & (k <= G.CHALLENGE_PAGE_SIZE * ((_page if _page else 0) + 1)):
            if G.CONTROLLER.focused.target & (G.CONTROLLER.focused.target.config.id == 'challenge_page'):
                snapped = True
            challenge_completed = "v.id or ''[G.PROFILES[G.SETTINGS.profile].challenge_progress.completed]"
            challenge_unlocked = 'G.SETTINGS.profile[G.PROFILES]'.challenges_unlocked & ('G.SETTINGS.profile[G.PROFILES]'.challenges_unlocked >= k)
            '#challenge_list + 1[challenge_list]' = {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cl', 'minw': 0.8}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': k + '', 'scale': 0.4, 'colour': G.C.WHITE}}}}, 2: UIBox_button(), 3: {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0.05, 'minw': 0.6}, 'nodes': {1: {'n': G.UIT.C, 'config': {'minh': 0.4, 'minw': 0.4, 'emboss': 0.05, 'r': 0.1, 'colour': challenge_completed & G.C.GREEN if challenge_completed & G.C.GREEN else G.C.BLACK}, 'nodes': {1: challenge_completed & {'n': G.UIT.O, 'config': {'object': Sprite(0, 0, 0.4, 0.4, "icons"[G.ASSET_ATLAS])}} if challenge_completed & {'n': G.UIT.O, 'config': {'object': Sprite(0, 0, 0.4, 0.4, "icons"[G.ASSET_ATLAS])}} else 'None'}}}}}}
            snapped = True
    return {'n': G.UIT.ROOT, 'config': {'align': 'cm', 'padding': 0.1, 'colour': G.C.CLEAR}, 'nodes': challenge_list}
def challenge_description(_id, daily, is_row):
    challenge = '_id[G.CHALLENGES]'
    if not challenge:
        return {'n': G.UIT.ROOT, 'config': {'align': 'cm', 'colour': G.C.BLACK, 'minh': 8.82, 'minw': 11.5, 'r': 0.1}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(ph_select_challenge), 'scale': 0.3, 'colour': G.C.UI.TEXT_LIGHT}}}}
    joker_size = 0.6
    jokers = CardArea(0, 0)
    if challenge.jokers:
        for kv in ipairs():
            card = Card(0, 0)
            if v.edition:card.set_edition()
            if v.eternal:card.set_eternal(True)
            if v.pinned:
                card.pinned = Truejokers.emplace(card)
    joker_col = {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0.05, 'colour': G.C.L_BLACK, 'r': 0.1, 'maxh': 1.8}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(k_jokers_cap), 'scale': 0.5, 'colour': G.C.UI.TEXT_LIGHT, 'vert': True, 'shadow': True}}, 2: {'n': G.UIT.C, 'config': {'align': 'cm', 'minh': 0.6 * G.CARD_H, 'minw': 5, 'r': 0.1, 'colour': G.C.UI.TRANSPARENT_DARK}, 'nodes': {1: jokers & {'n': G.UIT.O, 'config': {'object': jokers}} if jokers & {'n': G.UIT.O, 'config': {'object': jokers}} else {'n': G.UIT.T, 'config': {'text': localize(k_none), 'scale': 0.5, 'colour': G.C.UI.TEXT_LIGHT}}}}}}
    consumeables = CardArea(0, 0)
    if challenge.consumeables:
        for kv in ipairs():
            card = Card(0, 0)
            if v.edition:card.set_edition()
            if v.eternal:card.set_eternal(True)consumeables.emplace(card)
    consumable_col = {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0.05, 'colour': G.C.L_BLACK, 'r': 0.1, 'maxh': 1.8}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(k_cap_consumables), 'scale': 0.3, 'colour': G.C.UI.TEXT_LIGHT, 'vert': True, 'shadow': True}}, 2: {'n': G.UIT.C, 'config': {'align': 'cm', 'minh': 0.6 * G.CARD_H, 'r': 0.1, 'colour': G.C.UI.TRANSPARENT_DARK}, 'nodes': {1: consumeables & {'n': G.UIT.O, 'config': {'object': consumeables}} if consumeables & {'n': G.UIT.O, 'config': {'object': consumeables}} else {'n': G.UIT.T, 'config': {'text': localize(k_none), 'scale': 0.5, 'colour': G.C.UI.TEXT_LIGHT}}}}}}
    vouchers = CardArea(0, 0)
    if challenge.vouchers:
        for kv in ipairs():
            card = Card(0, 0)
            if v.edition:card.set_edition()
            if v.eternal:card.set_eternal(True)vouchers.emplace(card)
    voucher_col = {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0.05, 'colour': G.C.L_BLACK, 'r': 0.1, 'maxh': 1.8}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(k_vouchers_cap), 'scale': 0.33, 'colour': G.C.UI.TEXT_LIGHT, 'vert': True, 'shadow': True}}, 2: {'n': G.UIT.C, 'config': {'align': 'cm', 'minh': 0.6 * G.CARD_H, 'r': 0.1, 'colour': G.C.UI.TRANSPARENT_DARK}, 'nodes': {1: vouchers & {'n': G.UIT.O, 'config': {'object': vouchers}} if vouchers & {'n': G.UIT.O, 'config': {'object': vouchers}} else {'n': G.UIT.T, 'config': {'text': localize(k_none), 'scale': 0.5, 'colour': G.C.UI.TEXT_LIGHT}}}}}}
    return {'n': is_row & G.UIT.R if is_row & G.UIT.R else G.UIT.ROOT, 'config': {'align': 'cm', 'r': 0.1, 'colour': G.C.BLACK}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.1}, 'nodes': {1: joker_col, 2: consumable_col, 3: voucher_col}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0}, 'nodes': {1: create_tabs()}}, 3: (not is_row) & {'n': G.UIT.R, 'config': {'align': 'cm', 'minh': 0.9}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.1, 'minh': 0.7, 'minw': 9, 'r': 0.1, 'hover': True, 'colour': G.C.BLUE, 'button': 'start_challenge_run', 'shadow': True, 'id': _id}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(b_play_cap), 'scale': 0.5, 'colour': G.C.UI.TEXT_LIGHT, 'func': 'set_button_pip', 'focus_args': {'button': 'x', 'set_button_pip': True}}}}}}} if (not is_row) & {'n': G.UIT.R, 'config': {'align': 'cm', 'minh': 0.9}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.1, 'minh': 0.7, 'minw': 9, 'r': 0.1, 'hover': True, 'colour': G.C.BLUE, 'button': 'start_challenge_run', 'shadow': True, 'id': _id}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(b_play_cap), 'scale': 0.5, 'colour': G.C.UI.TEXT_LIGHT, 'func': 'set_button_pip', 'focus_args': {'button': 'x', 'set_button_pip': True}}}}}}} else 'None'}}
def challenge_description_tab(args):
    args = args if args else {}
    if args._tab == 'Rules':
        challenge = 'args._id[G.CHALLENGES]'
        start_rules = {}
        modded_starts = 'None'
        game_rules = {}
        starting_params = get_starting_params()
        base_modifiers = {'dollars': {'value': starting_params.dollars, 'order': 6}, 'discards': {'value': starting_params.discards, 'order': 2}, 'hands': {'value': starting_params.hands, 'order': 1}, 'reroll_cost': {'value': starting_params.reroll_cost, 'order': 7}, 'joker_slots': {'value': starting_params.joker_slots, 'order': 4}, 'consumable_slots': {'value': starting_params.consumable_slots, 'order': 5}, 'hand_size': {'value': starting_params.hand_size, 'order': 3}}
        bonus_mods = 100
        if challenge.rules:
            if challenge.rules.modifiers:
                for kv in ipairs():
                    'v.id[base_modifiers]' = {'value': v.value, 'order': 'v.id[base_modifiers]' & 'v.id[base_modifiers]'.order if 'v.id[base_modifiers]' & 'v.id[base_modifiers]'.order else bonus_mods, 'custom': True, 'old_val': 'v.id[base_modifiers]'.value}
                    bonus_mods = bonus_mods + 1
        nu_base_modifiers = {}
        for kv in pairs(base_modifiers):
            v.key = k
            '#nu_base_modifiers + 1[nu_base_modifiers]' = vtable.sort(nu_base_modifiers)
        for kv in ipairs(nu_base_modifiers):
            if v.old_val:
                modded_starts = modded_starts if modded_starts else {}
                '#modded_starts + 1[modded_starts]' = {'n': G.UIT.R, 'config': {'align': 'cl', 'maxw': 3.5}, 'nodes': localize()}
            else:
                '#start_rules + 1[start_rules]' = {'n': G.UIT.R, 'config': {'align': 'cl', 'maxw': 3.5}, 'nodes': localize()}
        if modded_starts:
            start_rules = {1: modded_starts & {'n': G.UIT.R, 'config': {'align': 'cl', 'padding': 0.05}, 'nodes': modded_starts} if modded_starts & {'n': G.UIT.R, 'config': {'align': 'cl', 'padding': 0.05}, 'nodes': modded_starts} else 'None', 2: {'n': G.UIT.R, 'config': {'align': 'cl', 'padding': 0.05, 'colour': G.C.GREY}, 'nodes': {}}, 3: {'n': G.UIT.R, 'config': {'align': 'cl', 'padding': 0.05}, 'nodes': start_rules}}
        if challenge.rules:
            if challenge.rules.custom:
                for kv in ipairs():
                    '#game_rules + 1[game_rules]' = {'n': G.UIT.R, 'config': {'align': 'cl'}, 'nodes': localize()}
        if (not '1[start_rules]') & (not modded_starts):
            '#start_rules + 1[start_rules]' = {'n': G.UIT.R, 'config': {'align': 'cl'}, 'nodes': localize()}
        if not '1[game_rules]':
            '#game_rules + 1[game_rules]' = {'n': G.UIT.R, 'config': {'align': 'cl'}, 'nodes': localize()}
        starting_rule_list = {'n': G.UIT.C, 'config': {'align': 'cm', 'minw': 3, 'r': 0.1, 'colour': G.C.BLUE}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.08, 'minh': 0.6}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(k_game_modifiers), 'scale': 0.4, 'colour': G.C.UI.TEXT_LIGHT, 'shadow': True}}}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm', 'minh': 4.1, 'minw': 4.2, 'padding': 0.05, 'r': 0.1, 'colour': G.C.WHITE}, 'nodes': start_rules}}}
        override_rule_list = {'n': G.UIT.C, 'config': {'align': 'cm', 'minw': 3, 'r': 0.1, 'colour': G.C.BLUE}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.08, 'minh': 0.6}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(k_custom_rules), 'scale': 0.4, 'colour': G.C.UI.TEXT_LIGHT, 'shadow': True}}}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm', 'minh': 4.1, 'minw': 6.8, 'maxw': 6.7, 'padding': 0.05, 'r': 0.1, 'colour': G.C.WHITE}, 'nodes': game_rules}}}
        return {'n': G.UIT.ROOT, 'config': {'align': 'cm', 'padding': 0.05, 'colour': G.C.CLEAR}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0.1, 'colour': G.C.L_BLACK, 'r': 0.1, 'minw': 3}, 'nodes': {1: override_rule_list, 2: starting_rule_list}}}}
    elif args._tab == 'Restrictions':
        challenge = 'args._id[G.CHALLENGES]'
        banned_cards = banned_tags = banned_other = ({}, {}, {})
        if challenge.restrictions:
            if challenge.restrictions.banned_cards:
                row_cards = {}
                n_rows = math.max(1)
                max_width = 1
                for kv in ipairs():
                    _row = math.floor()
                    '_row[row_cards]' = '_row[row_cards]' if '_row[row_cards]' else {}
                    '#row_cards[_row] + 1[row_cards[_row]]' = v
                    if len('_row[row_cards]' > max_width):
                        max_width = len('_row[row_cards]')
                card_size = math.max(0.3)
                for _row_card in ipairs(row_cards):
                    banned_card_area = CardArea(0, 0, 6.7)table.insert(banned_cards)
                    for kv in ipairs(row_card):
                        card = Card(0, 0)banned_card_area.emplace(card)
            if challenge.restrictions.banned_tags:
                tag_tab = {}
                for kv in pairs():
                    '#tag_tab + 1[tag_tab]' = 'v.id[G.P_TAGS]'table.sort(tag_tab)
                for kv in ipairs(tag_tab):
                    temp_tag = Tag()
                    temp_tag_ui = temp_tag.generate_UI()table.insert(banned_tags)
            if challenge.restrictions.banned_other:
                other_tab = {}
                for kv in pairs():
                    if v.type == 'blind':
                        '#other_tab + 1[other_tab]' = 'v.id[G.P_BLINDS]'table.sort(other_tab)
                for kv in ipairs(other_tab):
                    temp_blind = AnimatedSprite(0, 0, 1, 1, 'blind_chips'[G.ANIMATION_ATLAS])temp_blind.define_draw_steps()
                    temp_blind.float = True
                    temp_blind.states.hover.can = True
                    temp_blind.states.drag.can = False
                    temp_blind.states.collide.can = True
                    temp_blind.config = {'blind': v, 'force_focus': True}
                    temp_blind.hover = lambda: 
                    if not G.CONTROLLER.dragging.target if not G.CONTROLLER.dragging.target else G.CONTROLLER.using_touch:
                        if (not temp_blind.hovering) & temp_blind.states.visible:
                            temp_blind.hovering = True
                            temp_blind.hover_tilt = 3temp_blind.juice_up(0.05, 0.02)play_sound(chips1)
                            temp_blind.config.h_popup = create_UIBox_blind_popup(v, True)
                            temp_blind.config.h_popup_config = {'align': 'cl', 'offset': {'x': -0.1, 'y': 0}, 'parent': temp_blind}Node.hover(temp_blind)
                    temp_blind.stop_hover = lambda: 
                    temp_blind.hovering = False';'Node.stop_hover(temp_blind)';'
                    temp_blind.hover_tilt = 0table.insert(banned_other)
        if not '1[banned_cards]':
            '#banned_cards + 1[banned_cards]' = {'n': G.UIT.R, 'config': {'align': 'cl'}, 'nodes': localize()}
        if not '1[banned_tags]':
            '#banned_tags + 1[banned_tags]' = {'n': G.UIT.R, 'config': {'align': 'cl'}, 'nodes': localize()}
        if not '1[banned_other]':
            '#banned_other + 1[banned_other]' = {'n': G.UIT.R, 'config': {'align': 'cl'}, 'nodes': localize()}
        banned_cards = {'n': G.UIT.C, 'config': {'align': 'cm', 'r': 0.1, 'colour': G.C.RED}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.08, 'minh': 0.6}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(k_banned_cards), 'scale': 0.4, 'colour': G.C.UI.TEXT_LIGHT, 'shadow': True}}}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm', 'minh': 4.1, 'minw': 7.33, 'padding': 0.05, 'r': 0.1, 'colour': G.C.WHITE}, 'nodes': banned_cards}}}
        banned_tags = {'n': G.UIT.C, 'config': {'align': 'cm', 'r': 0.1, 'colour': G.C.RED}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.08, 'minh': 0.6, 'maxw': 1.48}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(k_banned_tags), 'scale': 0.3, 'colour': G.C.UI.TEXT_LIGHT, 'shadow': True}}}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm', 'minh': 4.1, 'minw': 1.48, 'padding': 0.05, 'r': 0.1, 'colour': G.C.WHITE}, 'nodes': banned_tags}}}
        banned_other = {'n': G.UIT.C, 'config': {'align': 'cm', 'r': 0.1, 'colour': G.C.RED}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.08, 'minh': 0.6, 'maxw': 1.84}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(k_other), 'scale': 0.4, 'colour': G.C.UI.TEXT_LIGHT, 'shadow': True}}}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm', 'minh': 4.1, 'minw': 2, 'padding': 0.05, 'r': 0.1, 'colour': G.C.WHITE}, 'nodes': banned_other}}}
        return {'n': G.UIT.ROOT, 'config': {'align': 'cm', 'padding': 0.05, 'colour': G.C.CLEAR}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0.1, 'colour': G.C.L_BLACK, 'r': 0.1}, 'nodes': {1: banned_cards, 2: banned_tags, 3: banned_other}}}}
    elif args._tab == 'Deck':
        challenge = 'args._id[G.CHALLENGES]'
        deck_tables = {}
        SUITS = {'S': {}, 'H': {}, 'C': {}, 'D': {}}
        suit_map = {1: 'S', 2: 'H', 3: 'C', 4: 'D'}
        card_protos = 'None'
        _de = 'None'
        if challenge:
            _de = challenge.deck
        if _de & _de.cards:
            card_protos = _de.cards
        if not card_protos:
            card_protos = {}
            for kv in pairs():
                _r = _s = (string.sub(k, 3, 3), string.sub(k, 1, 1))
                keep = _e = _d = _g = (True, 'None', 'None', 'None')
                if _de:
                    if _de.yes_ranks & (not '_r[_de.yes_ranks]'):
                        keep = False
                    if _de.no_ranks & '_r[_de.no_ranks]':
                        keep = False
                    if _de.yes_suits & (not '_s[_de.yes_suits]'):
                        keep = False
                    if _de.no_suits & '_s[_de.no_suits]':
                        keep = False
                    if _de.enhancement:
                        _e = _de.enhancement
                    if _de.edition:
                        _d = _de.edition
                    if _de.seal:
                        _g = _de.seal
                if keep:
                    '#card_protos + 1[card_protos]' = {'s': _s, 'r': _r, 'e': _e, 'd': _d, 'g': _g}
        for kv in ipairs(card_protos):
            _card = Card(0, 0)
            if v.d:_card.set_edition()
            if v.g:_card.set_seal()
            '#SUITS[v.s] + 1[SUITS[v.s]]' = _card
        for j in range(1, 4, ):
            if '1[SUITS[suit_map[j]]]':table.sort(suit_map[j][SUITS])
                view_deck = CardArea(0, 0)table.insert(deck_tables)
                for i in range(1, len('suit_map[j][SUITS]'), ):
                    if 'i[SUITS[suit_map[j]]]':view_deck.emplace(i[SUITS[suit_map[j]]])
        return {'n': G.UIT.ROOT, 'config': {'align': 'cm', 'padding': 0, 'colour': G.C.BLACK, 'r': 0.1, 'minw': 11.4, 'minh': 4.2}, 'nodes': deck_tables}
def run_setup_option(type):
    if not G.SAVED_GAME:
        G.SAVED_GAME = get_compressed()
        if G.SAVED_GAME != 'None':
            G.SAVED_GAME = STR_UNPACK()
    G.SETTINGS.current_setup = type
    G.GAME.viewed_back = Back()
    'G.SETTINGS.profile[G.PROFILES]'.MEMORY.stake = 'G.SETTINGS.profile[G.PROFILES]'.MEMORY.stake if 'G.SETTINGS.profile[G.PROFILES]'.MEMORY.stake else 1
    if type == 'Continue':
        G.viewed_stake = 1
        if G.SAVED_GAME != 'None':
            saved_game = G.SAVED_GAME
            viewed_deck = 'b_red'
            for kv in pairs():
                if v.name == saved_game.BACK.name:
                    viewed_deck = kG.GAME.viewed_back.change_to(viewed_deck[G.P_CENTERS])
            G.viewed_stake = saved_game.GAME.stake if saved_game.GAME.stake else 1
    if type == 'New Run':
        if G.OVERLAY_MENU:
            seed_toggle = G.OVERLAY_MENU.get_UIE_by_ID(run_setup_seed)
            if seed_toggle:
                seed_toggle.states.visible = True
        G.viewed_stake = 'G.SETTINGS.profile[G.PROFILES]'.MEMORY.stake if 'G.SETTINGS.profile[G.PROFILES]'.MEMORY.stake else 1G.FUNCS.change_stake()
    else:
        G.run_setup_seed = 'None'
        if G.OVERLAY_MENU:
            seed_toggle = G.OVERLAY_MENU.get_UIE_by_ID(run_setup_seed)
            if seed_toggle:
                seed_toggle.states.visible = False
    area = CardArea()
    for i in range(1, 10, ):
        card = Card()
        card.sprite_facing = 'back'
        card.facing = 'back'area.emplace(card)
        if i == 10:
            G.sticker_card = card';'
            card.sticker = get_deck_win_sticker()
    ordered_names = viewed_deck = ({}, 1)
    for kv in ipairs():
        '#ordered_names + 1[ordered_names]' = v.name
        if v.name == G.GAME.viewed_back.name:
            viewed_deck = k
    lwidth = rwidth = (1.4, 1.8)
    type_colour = G.C.BLUE
    scale = 0.39
    G.setup_seed = ''
    t = {'n': G.UIT.ROOT, 'config': {'align': 'cm', 'colour': G.C.CLEAR, 'minh': 6.6, 'minw': 6}, 'nodes': {1: (type == 'Continue') & {'n': G.UIT.R, 'config': {'align': 'tm', 'minh': 3.8, 'padding': 0.15}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'minh': 3.3, 'minw': 6.8}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'colour': G.C.BLACK, 'padding': 0.15, 'r': 0.1, 'emboss': 0.05}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'shadow': False}, 'nodes': {1: {'n': G.UIT.O, 'config': {'object': area}}}}}}, 2: {'n': G.UIT.C, 'config': {'align': 'cm', 'minw': 4, 'maxw': 4, 'minh': 1.7, 'r': 0.1, 'colour': G.C.L_BLACK, 'padding': 0.1}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'r': 0.1, 'minw': 4, 'maxw': 4, 'minh': 0.6}, 'nodes': {1: {'n': G.UIT.O, 'config': {'id': 'None', 'func': 'RUN_SETUP_check_back_name', 'object': Moveable()}}}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm', 'colour': G.C.WHITE, 'padding': 0.03, 'minh': 1.75, 'r': 0.1}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'minw': lwidth, 'maxw': lwidth}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(k_round), 'colour': G.C.UI.TEXT_DARK, 'scale': scale * 0.8}}}}, 2: {'n': G.UIT.C, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': ': ', 'colour': G.C.UI.TEXT_DARK, 'scale': scale * 0.8}}}}, 3: {'n': G.UIT.C, 'config': {'align': 'cl', 'minw': rwidth, 'maxw': lwidth}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': tostring(), 'colour': G.C.RED, 'scale': 0.8 * scale}}}}}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'minw': lwidth, 'maxw': lwidth}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(k_ante), 'colour': G.C.UI.TEXT_DARK, 'scale': scale * 0.8}}}}, 2: {'n': G.UIT.C, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': ': ', 'colour': G.C.UI.TEXT_DARK, 'scale': scale * 0.8}}}}, 3: {'n': G.UIT.C, 'config': {'align': 'cl', 'minw': rwidth, 'maxw': lwidth}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': tostring(), 'colour': G.C.BLUE, 'scale': 0.8 * scale}}}}}}, 3: {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'minw': lwidth, 'maxw': lwidth}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(k_money), 'colour': G.C.UI.TEXT_DARK, 'scale': scale * 0.8}}}}, 2: {'n': G.UIT.C, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': ': ', 'colour': G.C.UI.TEXT_DARK, 'scale': scale * 0.8}}}}, 3: {'n': G.UIT.C, 'config': {'align': 'cl', 'minw': rwidth, 'maxw': lwidth}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize($) + tostring(), 'colour': G.C.ORANGE, 'scale': 0.8 * scale}}}}}}, 4: {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'minw': lwidth, 'maxw': lwidth}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(k_best_hand), 'colour': G.C.UI.TEXT_DARK, 'scale': scale * 0.8}}}}, 2: {'n': G.UIT.C, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': ': ', 'colour': G.C.UI.TEXT_DARK, 'scale': scale * 0.8}}}}, 3: {'n': G.UIT.C, 'config': {'align': 'cl', 'minw': rwidth, 'maxw': lwidth}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': number_format(), 'colour': G.C.RED, 'scale': scale_number()}}}}}}, 5: saved_game.GAME.seeded & {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'minw': lwidth, 'maxw': lwidth}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(k_seed), 'colour': G.C.UI.TEXT_DARK, 'scale': scale * 0.8}}}}, 2: {'n': G.UIT.C, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': ': ', 'colour': G.C.UI.TEXT_DARK, 'scale': scale * 0.8}}}}, 3: {'n': G.UIT.C, 'config': {'align': 'cl', 'minw': rwidth, 'maxw': lwidth}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': tostring(), 'colour': G.C.RED, 'scale': 0.8 * scale}}}}}} if saved_game.GAME.seeded & {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'minw': lwidth, 'maxw': lwidth}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(k_seed), 'colour': G.C.UI.TEXT_DARK, 'scale': scale * 0.8}}}}, 2: {'n': G.UIT.C, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': ': ', 'colour': G.C.UI.TEXT_DARK, 'scale': scale * 0.8}}}}, 3: {'n': G.UIT.C, 'config': {'align': 'cl', 'minw': rwidth, 'maxw': lwidth}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': tostring(), 'colour': G.C.RED, 'scale': 0.8 * scale}}}}}} else 'None'}}}}, 3: {'n': G.UIT.C, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.O, 'config': {'id': G.GAME.viewed_back.name, 'func': 'RUN_SETUP_check_back_stake_column', 'object': UIBox()}}}}}}}}}} if (type == 'Continue') & {'n': G.UIT.R, 'config': {'align': 'tm', 'minh': 3.8, 'padding': 0.15}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'minh': 3.3, 'minw': 6.8}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'colour': G.C.BLACK, 'padding': 0.15, 'r': 0.1, 'emboss': 0.05}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'shadow': False}, 'nodes': {1: {'n': G.UIT.O, 'config': {'object': area}}}}}}, 2: {'n': G.UIT.C, 'config': {'align': 'cm', 'minw': 4, 'maxw': 4, 'minh': 1.7, 'r': 0.1, 'colour': G.C.L_BLACK, 'padding': 0.1}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'r': 0.1, 'minw': 4, 'maxw': 4, 'minh': 0.6}, 'nodes': {1: {'n': G.UIT.O, 'config': {'id': 'None', 'func': 'RUN_SETUP_check_back_name', 'object': Moveable()}}}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm', 'colour': G.C.WHITE, 'padding': 0.03, 'minh': 1.75, 'r': 0.1}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'minw': lwidth, 'maxw': lwidth}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(k_round), 'colour': G.C.UI.TEXT_DARK, 'scale': scale * 0.8}}}}, 2: {'n': G.UIT.C, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': ': ', 'colour': G.C.UI.TEXT_DARK, 'scale': scale * 0.8}}}}, 3: {'n': G.UIT.C, 'config': {'align': 'cl', 'minw': rwidth, 'maxw': lwidth}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': tostring(), 'colour': G.C.RED, 'scale': 0.8 * scale}}}}}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'minw': lwidth, 'maxw': lwidth}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(k_ante), 'colour': G.C.UI.TEXT_DARK, 'scale': scale * 0.8}}}}, 2: {'n': G.UIT.C, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': ': ', 'colour': G.C.UI.TEXT_DARK, 'scale': scale * 0.8}}}}, 3: {'n': G.UIT.C, 'config': {'align': 'cl', 'minw': rwidth, 'maxw': lwidth}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': tostring(), 'colour': G.C.BLUE, 'scale': 0.8 * scale}}}}}}, 3: {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'minw': lwidth, 'maxw': lwidth}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(k_money), 'colour': G.C.UI.TEXT_DARK, 'scale': scale * 0.8}}}}, 2: {'n': G.UIT.C, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': ': ', 'colour': G.C.UI.TEXT_DARK, 'scale': scale * 0.8}}}}, 3: {'n': G.UIT.C, 'config': {'align': 'cl', 'minw': rwidth, 'maxw': lwidth}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize($) + tostring(), 'colour': G.C.ORANGE, 'scale': 0.8 * scale}}}}}}, 4: {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'minw': lwidth, 'maxw': lwidth}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(k_best_hand), 'colour': G.C.UI.TEXT_DARK, 'scale': scale * 0.8}}}}, 2: {'n': G.UIT.C, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': ': ', 'colour': G.C.UI.TEXT_DARK, 'scale': scale * 0.8}}}}, 3: {'n': G.UIT.C, 'config': {'align': 'cl', 'minw': rwidth, 'maxw': lwidth}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': number_format(), 'colour': G.C.RED, 'scale': scale_number()}}}}}}, 5: saved_game.GAME.seeded & {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'minw': lwidth, 'maxw': lwidth}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(k_seed), 'colour': G.C.UI.TEXT_DARK, 'scale': scale * 0.8}}}}, 2: {'n': G.UIT.C, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': ': ', 'colour': G.C.UI.TEXT_DARK, 'scale': scale * 0.8}}}}, 3: {'n': G.UIT.C, 'config': {'align': 'cl', 'minw': rwidth, 'maxw': lwidth}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': tostring(), 'colour': G.C.RED, 'scale': 0.8 * scale}}}}}} if saved_game.GAME.seeded & {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'minw': lwidth, 'maxw': lwidth}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(k_seed), 'colour': G.C.UI.TEXT_DARK, 'scale': scale * 0.8}}}}, 2: {'n': G.UIT.C, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': ': ', 'colour': G.C.UI.TEXT_DARK, 'scale': scale * 0.8}}}}, 3: {'n': G.UIT.C, 'config': {'align': 'cl', 'minw': rwidth, 'maxw': lwidth}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': tostring(), 'colour': G.C.RED, 'scale': 0.8 * scale}}}}}} else 'None'}}}}, 3: {'n': G.UIT.C, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.O, 'config': {'id': G.GAME.viewed_back.name, 'func': 'RUN_SETUP_check_back_stake_column', 'object': UIBox()}}}}}}}}}} else {'n': G.UIT.R, 'config': {'align': 'cm', 'minh': 3.8}, 'nodes': {1: create_option_cycle()}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: (type == 'Continue') & {'n': G.UIT.R, 'config': {'align': 'cm', 'minh': 2.2, 'minw': 5}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'minh': 0.17}, 'nodes': {}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.O, 'config': {'id': 'None', 'func': 'RUN_SETUP_check_stake', 'insta_func': True, 'object': Moveable()}}}}}} if (type == 'Continue') & {'n': G.UIT.R, 'config': {'align': 'cm', 'minh': 2.2, 'minw': 5}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'minh': 0.17}, 'nodes': {}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.O, 'config': {'id': 'None', 'func': 'RUN_SETUP_check_stake', 'insta_func': True, 'object': Moveable()}}}}}} else {'n': G.UIT.R, 'config': {'align': 'cm', 'minh': 2.2, 'minw': 6.8}, 'nodes': {1: {'n': G.UIT.O, 'config': {'id': 'None', 'func': 'RUN_SETUP_check_stake', 'insta_func': True, 'object': Moveable()}}}}}}, 3: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.05, 'minh': 0.9}, 'nodes': {1: {'n': G.UIT.O, 'config': {'align': 'cm', 'func': 'toggle_seeded_run', 'object': Moveable()}, 'nodes': {}}}}, 4: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'minw': 2.4, 'id': 'run_setup_seed'}, 'nodes': {1: (type == 'New Run') & create_toggle() if (type == 'New Run') & create_toggle() else 'None'}}, 2: {'n': G.UIT.C, 'config': {'align': 'cm', 'minw': 5, 'minh': 0.8, 'padding': 0.2, 'r': 0.1, 'hover': True, 'colour': G.C.BLUE, 'button': 'start_setup_run', 'shadow': True, 'func': 'can_start_run'}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(b_play_cap), 'scale': 0.8, 'colour': G.C.UI.TEXT_LIGHT, 'func': 'set_button_pip', 'focus_args': {'button': 'x', 'set_button_pip': True}}}}}}}, 3: {'n': G.UIT.C, 'config': {'align': 'cm', 'minw': 2.5}, 'nodes': {}}}}}}
    return t
def create_button_binding_pip(args):
    button_sprite_map = {'a': G.F_SWAP_AB_PIPS & 1 if G.F_SWAP_AB_PIPS & 1 else 0, 'b': G.F_SWAP_AB_PIPS & 0 if G.F_SWAP_AB_PIPS & 0 else 1, 'x': 2, 'y': 3, 'leftshoulder': 4, 'rightshoulder': 5, 'triggerleft': 6, 'triggerright': 7, 'start': 8, 'back': 9, 'dpadup': 10, 'dpadright': 11, 'dpaddown': 12, 'dpadleft': 13, 'left': 14, 'right': 15, 'leftstick': 16, 'rightstick': 17, 'guide': 19}
    BUTTON_SPRITE = Sprite(0, 0)
    return {'n': G.UIT.ROOT, 'config': {'align': 'cm', 'colour': G.C.CLEAR}, 'nodes': {1: {'n': G.UIT.O, 'config': {'object': BUTTON_SPRITE}}}}
def create_UIBox_profile_button():
    letters = {}
    if G.F_DISP_USERNAME:
        for _c in utf8.chars():
            _char = c
            leng = "'all1'[G.LANGUAGES]".font.FONT.hasGlyphs(c)
            '#letters + 1[letters]' = {'n': G.UIT.T, 'config': {'lang': "leng and 'all1' or 'all2'[G.LANGUAGES]", 'text': _char, 'scale': 0.3, 'colour': mix_colours(), 'shadow': True}}
    if not 'G.SETTINGS.profile[G.PROFILES]'.name:
        'G.SETTINGS.profile[G.PROFILES]'.name = 'P' + G.SETTINGS.profile
    return {'n': G.UIT.ROOT, 'config': {'align': 'cm', 'colour': G.C.CLEAR}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.2, 'r': 0.1, 'emboss': 0.1, 'colour': G.C.L_BLACK}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(k_profile), 'scale': 0.4, 'colour': G.C.UI.TEXT_LIGHT, 'shadow': True}}}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0.15, 'minw': 2, 'minh': 0.8, 'maxw': 2, 'r': 0.1, 'hover': True, 'colour': mix_colours(), 'button': 'profile_select', 'shadow': True}, 'nodes': {1: {'n': G.UIT.T, 'config': {'ref_table': 'G.SETTINGS.profile[G.PROFILES]', 'ref_value': 'name', 'scale': 0.4, 'colour': G.C.UI.TEXT_LIGHT, 'shadow': True}}}}}}}}, 2: G.F_DISP_USERNAME & {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(k_playing_as), 'scale': 0.3, 'colour': G.C.UI.TEXT_LIGHT, 'shadow': True}}}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm', 'minh': 0.12}, 'nodes': {}}, 3: {'n': G.UIT.R, 'config': {'align': 'cm', 'maxw': 2}, 'nodes': letters}}} if G.F_DISP_USERNAME & {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': localize(k_playing_as), 'scale': 0.3, 'colour': G.C.UI.TEXT_LIGHT, 'shadow': True}}}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm', 'minh': 0.12}, 'nodes': {}}, 3: {'n': G.UIT.R, 'config': {'align': 'cm', 'maxw': 2}, 'nodes': letters}}} else 'None'}}
def create_UIBox_main_menu_buttons():
    text_scale = 0.45
    language = 'None'
    if not G.F_ENGLISH_ONLY:
        language = Sprite(0, 0, 0.6, 0.6, "icons"[G.ASSET_ATLAS])
        language.states.drag.can = False
    discord = 'None'
    twitter = 'None'
    if G.F_DISCORD:
        discord = Sprite(0, 0, 0.6, 0.6, "icons"[G.ASSET_ATLAS])
        discord.states.drag.can = False
        twitter = Sprite(0, 0, 0.6, 0.6, "icons"[G.ASSET_ATLAS])
        twitter.states.drag.can = False
    quit_func = 'quit'
    t = {'n': G.UIT.ROOT, 'config': {'align': 'cm', 'colour': G.C.CLEAR}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'bm'}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.2, 'r': 0.1, 'emboss': 0.1, 'colour': G.C.L_BLACK, 'mid': True}, 'nodes': {1: UIBox_button(), 2: {'n': G.UIT.C, 'config': {'align': 'cm'}, 'nodes': {1: UIBox_button(), 2: G.F_QUIT_BUTTON & {'n': G.UIT.C, 'config': {'align': 'cm', 'minw': 0.2}, 'nodes': {}} if G.F_QUIT_BUTTON & {'n': G.UIT.C, 'config': {'align': 'cm', 'minw': 0.2}, 'nodes': {}} else 'None', 3: G.F_QUIT_BUTTON & UIBox_button() if G.F_QUIT_BUTTON & UIBox_button() else 'None'}}, 3: UIBox_button()}}}}, 2: {'n': G.UIT.C, 'config': {'align': 'br', 'minw': 3.2, 'padding': 0.1}, 'nodes': {1: G.F_DISCORD & {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.2}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0.1, 'r': 0.1, 'hover': True, 'colour': mix_colours(), 'button': 'go_to_discord', 'shadow': True}, 'nodes': {1: {'n': G.UIT.O, 'config': {'object': discord}}}}, 2: {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0.1, 'r': 0.1, 'hover': True, 'colour': G.C.BLACK, 'button': 'go_to_twitter', 'shadow': True}, 'nodes': {1: {'n': G.UIT.O, 'config': {'object': twitter}}}}}} if G.F_DISCORD & {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.2}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0.1, 'r': 0.1, 'hover': True, 'colour': mix_colours(), 'button': 'go_to_discord', 'shadow': True}, 'nodes': {1: {'n': G.UIT.O, 'config': {'object': discord}}}}, 2: {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0.1, 'r': 0.1, 'hover': True, 'colour': G.C.BLACK, 'button': 'go_to_twitter', 'shadow': True}, 'nodes': {1: {'n': G.UIT.O, 'config': {'object': twitter}}}}}} else 'None', 2: (not G.F_ENGLISH_ONLY) & {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.2, 'r': 0.1, 'emboss': 0.1, 'colour': G.C.L_BLACK}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.15, 'minw': 1, 'r': 0.1, 'hover': True, 'colour': mix_colours(), 'button': 'language_selection', 'shadow': True}, 'nodes': {1: {'n': G.UIT.O, 'config': {'object': language}}, 2: {'n': G.UIT.T, 'config': {'text': G.LANG.label, 'scale': 0.4, 'colour': G.C.UI.TEXT_LIGHT, 'shadow': True}}}}}} if (not G.F_ENGLISH_ONLY) & {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.2, 'r': 0.1, 'emboss': 0.1, 'colour': G.C.L_BLACK}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.15, 'minw': 1, 'r': 0.1, 'hover': True, 'colour': mix_colours(), 'button': 'language_selection', 'shadow': True}, 'nodes': {1: {'n': G.UIT.O, 'config': {'object': language}}, 2: {'n': G.UIT.T, 'config': {'text': G.LANG.label, 'scale': 0.4, 'colour': G.C.UI.TEXT_LIGHT, 'shadow': True}}}}}} else 'None'}}}}
    return t
def create_UIBox_main_menu_competittion_name():
    G.SETTINGS.COMP.name = ''
    t = {'n': G.UIT.ROOT, 'config': {'align': 'cm', 'colour': G.C.CLEAR}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': 0.2, 'r': 0.1, 'emboss': 0.1, 'colour': G.C.L_BLACK, 'mid': True}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: create_text_input()}}, 2: UIBox_button()}}}}
    return t
def language_selector():
    rows = {}
    langs = {}
    for kv in pairs():
        if not v.omit:
            '#langs + 1[langs]' = vtable.sort(langs)
    _row = {}
    for kv in ipairs(langs):
        if not G.F_HIDE_BETA_LANGS if not G.F_HIDE_BETA_LANGS else not v.beta:
            '#_row + 1[_row]' = {'n': G.UIT.C, 'config': {'align': 'cm', 'func': 'beta_lang_alert', 'padding': 0.05, 'r': 0.1, 'minh': 0.7, 'minw': 4.5, 'button': v.beta & 'warn_lang' if v.beta & 'warn_lang' else 'change_lang', 'ref_table': v, 'colour': v.beta & G.C.RED if v.beta & G.C.RED else G.C.BLUE, 'hover': True, 'shadow': True, 'focus_args': {'snap_to': k == 1}}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': v.label, 'lang': v, 'scale': 0.45, 'colour': G.C.UI.TEXT_LIGHT, 'shadow': True}}}}}}
        if '3[_row]' if '3[_row]' else k == len(langs):
            '#rows + 1[rows]' = {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.1}, 'nodes': _row}
            _row = {}
    discord = 'None'
    discord = Sprite(0, 0, 0.6, 0.6, "icons"[G.ASSET_ATLAS])
    discord.states.drag.can = False
    t = create_UIBox_generic_options()
    return t
def create_UIBox_highlight(rect):
    t = {'n': G.UIT.ROOT, 'config': {'align': 'cm', 'minh': rect.T.h + 0.1, 'minw': rect.T.w + 0.15, 'r': 0.15, 'colour': G.C.DARK_EDITION}, 'nodes': {}}
    return t
def create_UIBox_generic_options(args):
    args = args if args else {}
    back_func = args.back_func if args.back_func else 'exit_overlay_menu'
    contents = args.contents if args.contents else {'n': G.UIT.T, 'config': {'text': 'EMPTY', 'colour': G.C.UI.RED, 'scale': 0.4}}
    if args.infotip:G.E_MANAGER.add_event()
    return {'n': G.UIT.ROOT, 'config': {'align': 'cm', 'minw': G.ROOM.T.w * 5, 'minh': G.ROOM.T.h * 5, 'padding': 0.1, 'r': 0.1, 'colour': args.bg_colour if args.bg_colour else {1: '1[G.C.GREY]', 2: '2[G.C.GREY]', 3: '3[G.C.GREY]', 4: 0.7}}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'minh': 1, 'r': 0.3, 'padding': 0.07, 'minw': 1, 'colour': args.outline_colour if args.outline_colour else G.C.JOKER_GREY, 'emboss': 0.1}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'minh': 1, 'r': 0.2, 'padding': 0.2, 'minw': 1, 'colour': args.colour if args.colour else G.C.L_BLACK}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': args.padding if args.padding else 0.2, 'minw': args.minw if args.minw else 7}, 'nodes': contents}, 2: (not args.no_back) & {'n': G.UIT.R, 'config': {'id': args.back_id if args.back_id else 'overlay_menu_back_button', 'align': 'cm', 'minw': 2.5, 'button_delay': args.back_delay, 'padding': 0.1, 'r': 0.1, 'hover': True, 'colour': args.back_colour if args.back_colour else G.C.ORANGE, 'button': back_func, 'shadow': True, 'focus_args': {'nav': 'wide', 'button': 'b', 'snap_to': args.snap_back}}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0, 'no_fill': True}, 'nodes': {1: {'n': G.UIT.T, 'config': {'id': args.back_id if args.back_id else 'None', 'text': args.back_label if args.back_label else localize(b_back), 'scale': 0.5, 'colour': G.C.UI.TEXT_LIGHT, 'shadow': True, 'func': (not args.no_pip) & 'set_button_pip' if (not args.no_pip) & 'set_button_pip' else 'None', 'focus_args': (not args.no_pip) & {'button': args.back_button if args.back_button else 'b'} if (not args.no_pip) & {'button': args.back_button if args.back_button else 'b'} else 'None'}}}}}} if (not args.no_back) & {'n': G.UIT.R, 'config': {'id': args.back_id if args.back_id else 'overlay_menu_back_button', 'align': 'cm', 'minw': 2.5, 'button_delay': args.back_delay, 'padding': 0.1, 'r': 0.1, 'hover': True, 'colour': args.back_colour if args.back_colour else G.C.ORANGE, 'button': back_func, 'shadow': True, 'focus_args': {'nav': 'wide', 'button': 'b', 'snap_to': args.snap_back}}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0, 'no_fill': True}, 'nodes': {1: {'n': G.UIT.T, 'config': {'id': args.back_id if args.back_id else 'None', 'text': args.back_label if args.back_label else localize(b_back), 'scale': 0.5, 'colour': G.C.UI.TEXT_LIGHT, 'shadow': True, 'func': (not args.no_pip) & 'set_button_pip' if (not args.no_pip) & 'set_button_pip' else 'None', 'focus_args': (not args.no_pip) & {'button': args.back_button if args.back_button else 'b'} if (not args.no_pip) & {'button': args.back_button if args.back_button else 'b'} else 'None'}}}}}} else 'None'}}}}, 2: {'n': G.UIT.R, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.O, 'config': {'id': 'overlay_menu_infotip', 'object': Moveable()}}}}}}
def UIBox_dyn_container(inner_table, horizontal, colour_override, background_override, flipped, padding):
    return {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.03, 'colour': G.C.UI.TRANSPARENT_DARK, 'r': 0.1}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.05, 'colour': colour_override if colour_override else G.C.DYN_UI.MAIN, 'r': 0.1}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': horizontal & 'cl' if horizontal & 'cl' else flipped & 'bm' if flipped & 'bm' else 'tm', 'colour': background_override if background_override else G.C.DYN_UI.BOSS_DARK, 'minw': horizontal & 100 if horizontal & 100 else 0, 'minh': horizontal & 0 if horizontal & 0 else 30, 'r': 0.1, 'padding': padding if padding else 0.08}, 'nodes': inner_table}}}}}
def simple_text_container(_loc, args):
    if not _loc:
        return 'None'
    args = args if args else {}
    container = {}
    loc_result = localize(_loc)
    if loc_result & (type(loc_result) == 'table'):
        for kv in ipairs(loc_result):
            '#container + 1[container]' = {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': v, 'scale': args.scale if args.scale else 0.35, 'colour': args.colour if args.colour else G.C.UI.TEXT_DARK, 'shadow': args.shadow}}}}
        return {'n': args.col & G.UIT.C if args.col & G.UIT.C else G.UIT.R, 'config': {'align': 'cm', 'padding': args.padding if args.padding else 0.03}, 'nodes': container}
def UIBox_button(args):
    args = args if args else {}
    args.button = args.button if args.button else 'exit_overlay_menu'
    args.func = args.func if args.func else 'None'
    args.colour = args.colour if args.colour else G.C.RED
    args.choice = args.choice if args.choice else 'None'
    args.chosen = args.chosen if args.chosen else 'None'
    args.label = args.label if args.label else {1: 'LABEL'}
    args.minw = args.minw if args.minw else 2.7
    args.maxw = args.maxw if args.maxw else args.minw - 0.2
    if args.minw < args.maxw:
        args.maxw = args.minw - 0.2
    args.minh = args.minh if args.minh else 0.9
    args.scale = args.scale if args.scale else 0.5
    args.focus_args = args.focus_args if args.focus_args else 'None'
    args.text_colour = args.text_colour if args.text_colour else G.C.UI.TEXT_LIGHT
    but_UIT = (args.col == True) & G.UIT.C if (args.col == True) & G.UIT.C else G.UIT.R
    but_UI_label = {}
    button_pip = 'None'
    for kv in ipairs():
        if k == len(args.label & args.focus_args & args.focus_args.set_button_pip):
            button_pip = 'set_button_pip'table.insert(but_UI_label)
    if args.count:table.insert(but_UI_label)
    return {'n': but_UIT, 'config': {'align': 'cm'}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'cm', 'padding': args.padding if args.padding else 0, 'r': 0.1, 'hover': True, 'colour': args.colour, 'one_press': args.one_press, 'button': (args.button != 'nil') & args.button if (args.button != 'nil') & args.button else 'None', 'choice': args.choice, 'chosen': args.chosen, 'focus_args': args.focus_args, 'minh': args.minh - 0.3 * (args.count & 1 if args.count & 1 else 0), 'shadow': True, 'func': args.func, 'id': args.id, 'back_func': args.back_func, 'ref_table': args.ref_table, 'mid': args.mid}, 'nodes': but_UI_label}}}