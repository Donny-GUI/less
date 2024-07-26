def set_screen_positions():
    if G.STAGE == G.STAGES.RUN:
        G.hand.T.x = G.TILE_W - G.hand.T.w - 2.85
        G.hand.T.y = G.TILE_H - G.hand.T.h
        G.play.T.x = G.hand.T.x + (G.hand.T.w - G.play.T.w) / 2
        G.play.T.y = G.hand.T.y - 3.6
        G.jokers.T.x = G.hand.T.x - 0.1
        G.jokers.T.y = 0
        G.consumeables.T.x = G.jokers.T.x + G.jokers.T.w + 0.2
        G.consumeables.T.y = 0
        G.deck.T.x = G.TILE_W - G.deck.T.w - 0.5
        G.deck.T.y = G.TILE_H - G.deck.T.h
        G.discard.T.x = G.jokers.T.x + G.jokers.T.w / 2 + 0.3 + 15
        G.discard.T.y = 4.2G.hand.hard_set_VT()G.play.hard_set_VT()G.jokers.hard_set_VT()G.consumeables.hard_set_VT()G.deck.hard_set_VT()G.discard.hard_set_VT()
    if G.STAGE == G.STAGES.MAIN_MENU:
        if G.STATE == G.STATES.DEMO_CTA:
            G.title_top.T.x = G.TILE_W / 2 - G.title_top.T.w / 2
            G.title_top.T.y = G.TILE_H / 2 - G.title_top.T.h / 2 - 2
        else:
            G.title_top.T.x = G.TILE_W / 2 - G.title_top.T.w / 2
            G.title_top.T.y = G.TILE_H / 2 - G.title_top.T.h / 2 - (G.debug_splash_size_toggle & 2 if G.debug_splash_size_toggle & 2 else 1.2)G.title_top.hard_set_VT()
def ease_chips(mod):G.E_MANAGER.add_event()
def ease_dollars(mod, instant):

    def _mod(mod):
        dollar_UI = G.HUD.get_UIE_by_ID(dollar_text_UI)
        mod = mod if mod else 0
        text = '+' + localize($)
        col = G.C.MONEY
        if mod < 0:
            text = '-' + localize($)
            col = G.C.RED
        else:inc_career_stat(c_dollars_earned, mod)
        G.GAME.dollars = G.GAME.dollars + modcheck_and_set_high_score(most_money)check_for_unlock()dollar_UI.config.object.update()G.HUD.recalculate()attention_text()play_sound(coin1)
    if instant:_mod(mod)
    else:G.E_MANAGER.add_event()
def ease_discard(mod, instant, silent):
    _mod = lambda mod: 
    if math.abs() == 0:
        return False
    discard_UI = G.HUD.get_UIE_by_ID(discard_UI_count)
    mod = mod if mod else 0
    mod = math.max()
    text = '+'
    col = G.C.GREEN
    if mod < 0:
        text = ''
        col = G.C.RED
    G.GAME.current_round.discards_left = G.GAME.current_round.discards_left + moddiscard_UI.config.object.update()G.HUD.recalculate()attention_text()
    if not silent:play_sound(chips2)
    if instant:_mod(mod)
    else:G.E_MANAGER.add_event()
def ease_hands_played(mod, instant):
    _mod = lambda mod: 
    hand_UI = G.HUD.get_UIE_by_ID(hand_UI_count)
    mod = mod if mod else 0
    text = '+'
    col = G.C.GREEN
    if mod < 0:
        text = ''
        col = G.C.RED
    G.GAME.current_round.hands_left = G.GAME.current_round.hands_left + modhand_UI.config.object.update()G.HUD.recalculate()attention_text()play_sound(chips2)
    if instant:_mod(mod)
    else:G.E_MANAGER.add_event()
def ease_ante(mod):G.E_MANAGER.add_event()
def ease_round(mod):G.E_MANAGER.add_event()
def ease_value(ref_table, ref_value, mod, floored, timer_type, not_blockable, delay, ease_type):
    mod = mod if mod else 0G.E_MANAGER.add_event()
def ease_background_colour(args):
    for kv in pairs():
        if args.new_colour & ((k == 'C' if k == 'C' else k == 'L') if (k == 'C' if k == 'C' else k == 'L') else k == 'D'):
            if args.special_colour & args.tertiary_colour:
                col_key = ((k == 'L') & 'new_colour' if (k == 'L') & 'new_colour' else (k == 'C') & 'special_colour') if ((k == 'L') & 'new_colour' if (k == 'L') & 'new_colour' else (k == 'C') & 'special_colour') else (k == 'D') & 'tertiary_colour'ease_value(v, 1)ease_value(v, 2)ease_value(v, 3)
            else:
                brightness = ((k == 'L') & 1.3 if (k == 'L') & 1.3 else (k == 'D') & (args.special_colour & 0.4 if args.special_colour & 0.4 else 0.7)) if ((k == 'L') & 1.3 if (k == 'L') & 1.3 else (k == 'D') & (args.special_colour & 0.4 if args.special_colour & 0.4 else 0.7)) else 0.9
                if (k == 'C') & args.special_colour:ease_value(v, 1)ease_value(v, 2)ease_value(v, 3)
                else:ease_value(v, 1)ease_value(v, 2)ease_value(v, 3)
    if args.contrast:ease_value()
def ease_colour(old_colour, new_colour, delay):ease_value(old_colour, 1)ease_value(old_colour, 2)ease_value(old_colour, 3)ease_value(old_colour, 4)
def ease_background_colour_blind(state, blind_override):
    blindname = (blind_override if blind_override else G.GAME.blind & (G.GAME.blind.name != '') & G.GAME.blind.name) if (blind_override if blind_override else G.GAME.blind & (G.GAME.blind.name != '') & G.GAME.blind.name) else 'Small Blind'
    blindname = (blindname == '') & 'Small Blind' if (blindname == '') & 'Small Blind' else blindname
    if state == G.STATES.SHOP:ease_colour()
    elif state == G.STATES.TAROT_PACK:ease_colour()
    elif state == G.STATES.SPECTRAL_PACK:ease_colour()
    elif state == G.STATES.STANDARD_PACK:ease_colour()
    elif state == G.STATES.BUFFOON_PACK:ease_colour()
    elif state == G.STATES.PLANET_PACK:ease_colour()
    elif G.GAME.blind:G.GAME.blind.change_colour()
    if state == G.STATES.TAROT_PACK:ease_background_colour()
    elif state == G.STATES.SPECTRAL_PACK:ease_background_colour()
    elif state == G.STATES.STANDARD_PACK:ease_background_colour()
    elif state == G.STATES.BUFFOON_PACK:ease_background_colour()
    elif state == G.STATES.PLANET_PACK:ease_background_colour()
    elif G.GAME.won:ease_background_colour()
    elif (blindname == 'Small Blind' if blindname == 'Small Blind' else blindname == 'Big Blind') if (blindname == 'Small Blind' if blindname == 'Small Blind' else blindname == 'Big Blind') else blindname == '':ease_background_colour()
    else:
        boss_col = G.C.BLACK
        for kv in pairs():
            if v.name == blindname:
                if v.boss.showdown:ease_background_colour()
                    return False
                boss_col = v.boss_colour if v.boss_colour else G.C.BLACKease_background_colour()
def delay(time, queue):G.E_MANAGER.add_event()
def add_joker(joker, edition, silent, eternal):
    _area = G.P_CENTERS[joker[G.P_CENTERS]'.consumeable & G.consumeables if 'joker].consumeable & G.consumeables else G.jokers
    _T = _area & _area.T if _area & _area.T else {'x': G.ROOM.T.w / 2 - G.CARD_W / 2, 'y': G.ROOM.T.h / 2 - G.CARD_H / 2}
    card = Card()card.start_materialize(None, silent)
    if _area:card.add_to_deck()
    if edition:card.set_edition()
    if eternal:card.set_eternal(True)
    if _area & (card.ability.set == 'Joker'):_area.emplace(card)
    elif G.consumeables:G.consumeables.emplace(card)
    card.created_on_pause = 'None'
    return card
def draw_card(from, to, percent, dir, sort, card, delay, mute, stay_flipped, vol, discarded_only):
    percent = percent if percent else 50
    delay = delay if delay else 0.1
    if dir == 'down':
        percent = 1 - percent
    sort = sort if sort else False
    drawn = 'None'G.E_MANAGER.add_event()
def highlight_card(card, percent, dir):
    percent = percent if percent else 0.5
    highlight = True
    if dir == 'down':
        percent = 1 - percent
        highlight = FalseG.E_MANAGER.add_event()
def play_area_status_text(text, silent, delay):
    delay = delay if delay else 0.6G.E_MANAGER.add_event()
def level_up_hand(card, hand, instant, amount):
    amount = amount if amount else 1
    G.GAME.hands[hand].level = math.max(0)
    G.GAME.hands[hand].mult = math.max()
    G.GAME.hands[hand].chips = math.max()
    if not instant:G.E_MANAGER.add_event()update_hand_text()G.E_MANAGER.add_event()update_hand_text()G.E_MANAGER.add_event()update_hand_text()delay(1.3)G.E_MANAGER.add_event()
def update_hand_text(config, vals):G.E_MANAGER.add_event()
def eval_card(card, context):
    context = context if context else {}
    ret = {}
    if context.repetition_only:
        seals = card.calculate_seal(context)
        if seals:
            ret.seals = seals
        return ret
    if context.cardarea == G.play:
        chips = card.get_chip_bonus()
        if chips > 0:
            ret.chips = chips
        mult = card.get_chip_mult()
        if mult > 0:
            ret.mult = mult
        x_mult = card.get_chip_x_mult(context)
        if x_mult > 0:
            ret.x_mult = x_mult
        p_dollars = card.get_p_dollars()
        if p_dollars > 0:
            ret.p_dollars = p_dollars
        jokers = card.calculate_joker(context)
        if jokers:
            ret.jokers = jokers
        edition = card.get_edition(context)
        if edition:
            ret.edition = edition
    if context.cardarea == G.hand:
        h_mult = card.get_chip_h_mult()
        if h_mult > 0:
            ret.h_mult = h_mult
        h_x_mult = card.get_chip_h_x_mult()
        if h_x_mult > 0:
            ret.x_mult = h_x_mult
        jokers = card.calculate_joker(context)
        if jokers:
            ret.jokers = jokers
    if context.cardarea == G.jokers if context.cardarea == G.jokers else context.card == G.consumeables:
        jokers = 'None'
        if context.edition:
            jokers = card.get_edition(context)
        elif context.other_joker:
            jokers = context.other_joker.calculate_joker(context)
        else:
            jokers = card.calculate_joker(context)
        if jokers:
            ret.jokers = jokers
    return ret
def set_alerts():
    if G.REFRESH_ALERTS:
        G.REFRESH_ALERTS = 'None'
        alert_joker = alert_voucher = alert_tarot = alert_planet = alert_spectral = alert_blind = alert_edition = alert_tag = alert_seal = alert_booster = (False, False, False, False, False, False, False, False, False, False)
        for kv in pairs():
            if v.discovered & (not v.alerted):
                if v.set == 'Voucher':
                    alert_voucher = True
                if v.set == 'Tarot':
                    alert_tarot = True
                if v.set == 'Planet':
                    alert_planet = True
                if v.set == 'Spectral':
                    alert_spectral = True
                if v.set == 'Joker':
                    alert_joker = True
                if v.set == 'Edition':
                    alert_edition = True
                if v.set == 'Booster':
                    alert_booster = True
        for kv in pairs():
            if v.discovered & (not v.alerted):
                alert_blind = True
        for kv in pairs():
            if v.discovered & (not v.alerted):
                alert_tag = True
        for kv in pairs():
            if v.discovered & (not v.alerted):
                alert_seal = True
        alert_any = (((((((alert_voucher if alert_voucher else alert_joker) if (alert_voucher if alert_voucher else alert_joker) else alert_tarot) if ((alert_voucher if alert_voucher else alert_joker) if (alert_voucher if alert_voucher else alert_joker) else alert_tarot) else alert_planet) if (((alert_voucher if alert_voucher else alert_joker) if (alert_voucher if alert_voucher else alert_joker) else alert_tarot) if ((alert_voucher if alert_voucher else alert_joker) if (alert_voucher if alert_voucher else alert_joker) else alert_tarot) else alert_planet) else alert_spectral) if ((((alert_voucher if alert_voucher else alert_joker) if (alert_voucher if alert_voucher else alert_joker) else alert_tarot) if ((alert_voucher if alert_voucher else alert_joker) if (alert_voucher if alert_voucher else alert_joker) else alert_tarot) else alert_planet) if (((alert_voucher if alert_voucher else alert_joker) if (alert_voucher if alert_voucher else alert_joker) else alert_tarot) if ((alert_voucher if alert_voucher else alert_joker) if (alert_voucher if alert_voucher else alert_joker) else alert_tarot) else alert_planet) else alert_spectral) else alert_blind) if (((((alert_voucher if alert_voucher else alert_joker) if (alert_voucher if alert_voucher else alert_joker) else alert_tarot) if ((alert_voucher if alert_voucher else alert_joker) if (alert_voucher if alert_voucher else alert_joker) else alert_tarot) else alert_planet) if (((alert_voucher if alert_voucher else alert_joker) if (alert_voucher if alert_voucher else alert_joker) else alert_tarot) if ((alert_voucher if alert_voucher else alert_joker) if (alert_voucher if alert_voucher else alert_joker) else alert_tarot) else alert_planet) else alert_spectral) if ((((alert_voucher if alert_voucher else alert_joker) if (alert_voucher if alert_voucher else alert_joker) else alert_tarot) if ((alert_voucher if alert_voucher else alert_joker) if (alert_voucher if alert_voucher else alert_joker) else alert_tarot) else alert_planet) if (((alert_voucher if alert_voucher else alert_joker) if (alert_voucher if alert_voucher else alert_joker) else alert_tarot) if ((alert_voucher if alert_voucher else alert_joker) if (alert_voucher if alert_voucher else alert_joker) else alert_tarot) else alert_planet) else alert_spectral) else alert_blind) else alert_edition) if ((((((alert_voucher if alert_voucher else alert_joker) if (alert_voucher if alert_voucher else alert_joker) else alert_tarot) if ((alert_voucher if alert_voucher else alert_joker) if (alert_voucher if alert_voucher else alert_joker) else alert_tarot) else alert_planet) if (((alert_voucher if alert_voucher else alert_joker) if (alert_voucher if alert_voucher else alert_joker) else alert_tarot) if ((alert_voucher if alert_voucher else alert_joker) if (alert_voucher if alert_voucher else alert_joker) else alert_tarot) else alert_planet) else alert_spectral) if ((((alert_voucher if alert_voucher else alert_joker) if (alert_voucher if alert_voucher else alert_joker) else alert_tarot) if ((alert_voucher if alert_voucher else alert_joker) if (alert_voucher if alert_voucher else alert_joker) else alert_tarot) else alert_planet) if (((alert_voucher if alert_voucher else alert_joker) if (alert_voucher if alert_voucher else alert_joker) else alert_tarot) if ((alert_voucher if alert_voucher else alert_joker) if (alert_voucher if alert_voucher else alert_joker) else alert_tarot) else alert_planet) else alert_spectral) else alert_blind) if (((((alert_voucher if alert_voucher else alert_joker) if (alert_voucher if alert_voucher else alert_joker) else alert_tarot) if ((alert_voucher if alert_voucher else alert_joker) if (alert_voucher if alert_voucher else alert_joker) else alert_tarot) else alert_planet) if (((alert_voucher if alert_voucher else alert_joker) if (alert_voucher if alert_voucher else alert_joker) else alert_tarot) if ((alert_voucher if alert_voucher else alert_joker) if (alert_voucher if alert_voucher else alert_joker) else alert_tarot) else alert_planet) else alert_spectral) if ((((alert_voucher if alert_voucher else alert_joker) if (alert_voucher if alert_voucher else alert_joker) else alert_tarot) if ((alert_voucher if alert_voucher else alert_joker) if (alert_voucher if alert_voucher else alert_joker) else alert_tarot) else alert_planet) if (((alert_voucher if alert_voucher else alert_joker) if (alert_voucher if alert_voucher else alert_joker) else alert_tarot) if ((alert_voucher if alert_voucher else alert_joker) if (alert_voucher if alert_voucher else alert_joker) else alert_tarot) else alert_planet) else alert_spectral) else alert_blind) else alert_edition) else alert_seal) if (((((((alert_voucher if alert_voucher else alert_joker) if (alert_voucher if alert_voucher else alert_joker) else alert_tarot) if ((alert_voucher if alert_voucher else alert_joker) if (alert_voucher if alert_voucher else alert_joker) else alert_tarot) else alert_planet) if (((alert_voucher if alert_voucher else alert_joker) if (alert_voucher if alert_voucher else alert_joker) else alert_tarot) if ((alert_voucher if alert_voucher else alert_joker) if (alert_voucher if alert_voucher else alert_joker) else alert_tarot) else alert_planet) else alert_spectral) if ((((alert_voucher if alert_voucher else alert_joker) if (alert_voucher if alert_voucher else alert_joker) else alert_tarot) if ((alert_voucher if alert_voucher else alert_joker) if (alert_voucher if alert_voucher else alert_joker) else alert_tarot) else alert_planet) if (((alert_voucher if alert_voucher else alert_joker) if (alert_voucher if alert_voucher else alert_joker) else alert_tarot) if ((alert_voucher if alert_voucher else alert_joker) if (alert_voucher if alert_voucher else alert_joker) else alert_tarot) else alert_planet) else alert_spectral) else alert_blind) if (((((alert_voucher if alert_voucher else alert_joker) if (alert_voucher if alert_voucher else alert_joker) else alert_tarot) if ((alert_voucher if alert_voucher else alert_joker) if (alert_voucher if alert_voucher else alert_joker) else alert_tarot) else alert_planet) if (((alert_voucher if alert_voucher else alert_joker) if (alert_voucher if alert_voucher else alert_joker) else alert_tarot) if ((alert_voucher if alert_voucher else alert_joker) if (alert_voucher if alert_voucher else alert_joker) else alert_tarot) else alert_planet) else alert_spectral) if ((((alert_voucher if alert_voucher else alert_joker) if (alert_voucher if alert_voucher else alert_joker) else alert_tarot) if ((alert_voucher if alert_voucher else alert_joker) if (alert_voucher if alert_voucher else alert_joker) else alert_tarot) else alert_planet) if (((alert_voucher if alert_voucher else alert_joker) if (alert_voucher if alert_voucher else alert_joker) else alert_tarot) if ((alert_voucher if alert_voucher else alert_joker) if (alert_voucher if alert_voucher else alert_joker) else alert_tarot) else alert_planet) else alert_spectral) else alert_blind) else alert_edition) if ((((((alert_voucher if alert_voucher else alert_joker) if (alert_voucher if alert_voucher else alert_joker) else alert_tarot) if ((alert_voucher if alert_voucher else alert_joker) if (alert_voucher if alert_voucher else alert_joker) else alert_tarot) else alert_planet) if (((alert_voucher if alert_voucher else alert_joker) if (alert_voucher if alert_voucher else alert_joker) else alert_tarot) if ((alert_voucher if alert_voucher else alert_joker) if (alert_voucher if alert_voucher else alert_joker) else alert_tarot) else alert_planet) else alert_spectral) if ((((alert_voucher if alert_voucher else alert_joker) if (alert_voucher if alert_voucher else alert_joker) else alert_tarot) if ((alert_voucher if alert_voucher else alert_joker) if (alert_voucher if alert_voucher else alert_joker) else alert_tarot) else alert_planet) if (((alert_voucher if alert_voucher else alert_joker) if (alert_voucher if alert_voucher else alert_joker) else alert_tarot) if ((alert_voucher if alert_voucher else alert_joker) if (alert_voucher if alert_voucher else alert_joker) else alert_tarot) else alert_planet) else alert_spectral) else alert_blind) if (((((alert_voucher if alert_voucher else alert_joker) if (alert_voucher if alert_voucher else alert_joker) else alert_tarot) if ((alert_voucher if alert_voucher else alert_joker) if (alert_voucher if alert_voucher else alert_joker) else alert_tarot) else alert_planet) if (((alert_voucher if alert_voucher else alert_joker) if (alert_voucher if alert_voucher else alert_joker) else alert_tarot) if ((alert_voucher if alert_voucher else alert_joker) if (alert_voucher if alert_voucher else alert_joker) else alert_tarot) else alert_planet) else alert_spectral) if ((((alert_voucher if alert_voucher else alert_joker) if (alert_voucher if alert_voucher else alert_joker) else alert_tarot) if ((alert_voucher if alert_voucher else alert_joker) if (alert_voucher if alert_voucher else alert_joker) else alert_tarot) else alert_planet) if (((alert_voucher if alert_voucher else alert_joker) if (alert_voucher if alert_voucher else alert_joker) else alert_tarot) if ((alert_voucher if alert_voucher else alert_joker) if (alert_voucher if alert_voucher else alert_joker) else alert_tarot) else alert_planet) else alert_spectral) else alert_blind) else alert_edition) else alert_seal) else alert_tag
        G.ARGS.set_alerts_alertables = G.ARGS.set_alerts_alertables if G.ARGS.set_alerts_alertables else {1: {'id': 'your_collection', 'alert_uibox_name': 'your_collection_alert'}, 2: {'id': 'your_collection_jokers', 'alert_uibox_name': 'your_collection_jokers_alert'}, 3: {'id': 'your_collection_tarots', 'alert_uibox_name': 'your_collection_tarots_alert'}, 4: {'id': 'your_collection_planets', 'alert_uibox_name': 'your_collection_planets_alert'}, 5: {'id': 'your_collection_spectrals', 'alert_uibox_name': 'your_collection_spectrals_alert'}, 6: {'id': 'your_collection_vouchers', 'alert_uibox_name': 'your_collection_vouchers_alert'}, 7: {'id': 'your_collection_editions', 'alert_uibox_name': 'your_collection_editions_alert'}, 8: {'id': 'your_collection_blinds', 'alert_uibox_name': 'your_collection_blinds_alert'}, 9: {'id': 'your_collection_tags', 'alert_uibox_name': 'your_collection_tags_alert'}, 10: {'id': 'your_collection_seals', 'alert_uibox_name': 'your_collection_seals_alert'}, 11: {'id': 'your_collection_boosters', 'alert_uibox_name': 'your_collection_boosters_alert'}}
        G.ARGS.set_alerts_alertables[1].should_alert = alert_any
        G.ARGS.set_alerts_alertables[1].should_alert = alert_joker
        G.ARGS.set_alerts_alertables[1].should_alert = alert_tarot
        G.ARGS.set_alerts_alertables[1].should_alert = alert_planet
        G.ARGS.set_alerts_alertables[1].should_alert = alert_spectral
        G.ARGS.set_alerts_alertables[1].should_alert = alert_voucher
        G.ARGS.set_alerts_alertables[1].should_alert = alert_edition
        G.ARGS.set_alerts_alertables[1].should_alert = alert_blind
        G.ARGS.set_alerts_alertables[1].should_alert = alert_tag
        G.ARGS.set_alerts_alertables[1].should_alert = alert_seal
        G.ARGS.set_alerts_alertables[1].should_alert = alert_booster
        for kv in ipairs():
            if G.OVERLAY_MENU & G.OVERLAY_MENU.get_UIE_by_ID():
                if v.should_alert:
                    if not G.ARGS.set_alerts_alertables[1]:
                        G.ARGS.set_alerts_alertables[1] = UIBox()
                        G.ARGS.set_alerts_alertables[1].states.collide.can = False
                elif G.ARGS.set_alerts_alertables[1].remove()
                    G.ARGS.set_alerts_alertables[1] = 'None'
            elif G.ARGS.set_alerts_alertables[1].remove()
                G.ARGS.set_alerts_alertables[1] = 'None'
        if G.MAIN_MENU_UI:
            if alert_any:
                if not G.collection_alert:
                    G.collection_alert = UIBox()
                    G.collection_alert.states.collide.can = False
            elif G.collection_alert:G.collection_alert.remove()
                G.collection_alert = 'None'
        elif G.collection_alert:G.collection_alert.remove()
            G.collection_alert = 'None'
def set_main_menu_UI():
    G.MAIN_MENU_UI = UIBox()
    G.MAIN_MENU_UI.alignment.offset.y = 0G.MAIN_MENU_UI.align_to_major()G.E_MANAGER.add_event()G.CONTROLLER.snap_to()
def card_eval_status_text(card, eval_type, amt, percent, dir, extra):
    percent = percent if percent else 0.9 + 0.2 * math.random()
    if dir == 'down':
        percent = 1 - percent
    if extra & extra.focus:
        card = extra.focus
    text = ''
    sound = 'None'
    volume = 1
    card_aligned = 'bm'
    y_off = 0.15 * G.CARD_H
    if card.area == G.jokers if card.area == G.jokers else card.area == G.consumeables:
        y_off = 0.05 * card.T.h
    elif card.area == G.hand:
        y_off = -0.05 * G.CARD_H
        card_aligned = 'tm'
    elif card.area == G.play:
        y_off = -0.05 * G.CARD_H
        card_aligned = 'tm'
    elif card.jimbo:
        y_off = -0.05 * G.CARD_H
        card_aligned = 'tm'
    config = {}
    delay = 0.65
    colour = (config.colour if config.colour else extra & extra.colour) if (config.colour if config.colour else extra & extra.colour) else G.C.FILTER
    extrafunc = 'None'
    if eval_type == 'debuff':
        sound = 'cancel'
        amt = 1
        colour = G.C.RED
        config.scale = 0.6
        text = localize(k_debuffed)
    elif eval_type == 'chips':
        sound = 'chips1'
        amt = amt
        colour = G.C.CHIPS
        text = localize()
        delay = 0.6
    elif eval_type == 'mult':
        sound = 'multhit1'
        amt = amt
        text = localize()
        colour = G.C.MULT
        config.type = 'fade'
        config.scale = 0.7
    elif eval_type == 'x_mult' if eval_type == 'x_mult' else eval_type == 'h_x_mult':
        sound = 'multhit2'
        volume = 0.7
        amt = amt
        text = localize()
        colour = G.C.XMULT
        config.type = 'fade'
        config.scale = 0.7
    elif eval_type == 'h_mult':
        sound = 'multhit1'
        amt = amt
        text = localize()
        colour = G.C.MULT
        config.type = 'fade'
        config.scale = 0.7
    elif eval_type == 'dollars':
        sound = 'coin3'
        amt = amt
        text = (amt < -0.01 & '-' if amt < -0.01 & '-' else '') + localize($) + tostring()
        colour = amt < -0.01 & G.C.RED if amt < -0.01 & G.C.RED else G.C.MONEY
    elif eval_type == 'swap':
        sound = 'generic1'
        amt = amt
        text = localize(k_swapped_ex)
        colour = G.C.PURPLE
    elif eval_type == 'extra' if eval_type == 'extra' else eval_type == 'jokers':
        sound = ((extra.edition & 'foil2' if extra.edition & 'foil2' else extra.mult_mod & 'multhit1') if (extra.edition & 'foil2' if extra.edition & 'foil2' else extra.mult_mod & 'multhit1') else extra.Xmult_mod & 'multhit2') if ((extra.edition & 'foil2' if extra.edition & 'foil2' else extra.mult_mod & 'multhit1') if (extra.edition & 'foil2' if extra.edition & 'foil2' else extra.mult_mod & 'multhit1') else extra.Xmult_mod & 'multhit2') else 'generic1'
        if extra.edition:
            colour = G.C.DARK_EDITION
        volume = (extra.edition & 0.3 if extra.edition & 0.3 else (sound == 'multhit2') & 0.7) if (extra.edition & 0.3 if extra.edition & 0.3 else (sound == 'multhit2') & 0.7) else 1
        delay = extra.delay if extra.delay else 0.75
        amt = 1
        text = extra.message if extra.message else text
        if (not extra.edition) & (extra.mult_mod if extra.mult_mod else extra.Xmult_mod):
            colour = G.C.MULT
        if extra.chip_mod:
            config.type = 'fall'
            colour = G.C.CHIPS
            config.scale = 0.7
        elif extra.swap:
            config.type = 'fall'
            colour = G.C.PURPLE
            config.scale = 0.7
        else:
            config.type = 'fall'
            config.scale = 0.7
    delay = delay * 1.25
    if amt > 0 if amt > 0 else amt < 0:
        if extra & extra.instant:
            if extrafunc:extrafunc()attention_text()play_sound(sound)
            if not extra if not extra else not extra.no_juice:card.juice_up(0.6, 0.1)
                G.ROOM.jiggle = G.ROOM.jiggle + 0.7
        else:G.E_MANAGER.add_event()
    if extra & extra.playing_cards_created:playing_card_joker_effects()
def add_round_eval_row(config):
    config = config if config else {}
    width = G.round_eval.T.w - 0.51
    num_dollars = config.dollars if config.dollars else 1
    scale = 0.9
    if config.name != 'bottom':
        if config.name != 'blind1':
            if not G.round_eval.divider_added:G.E_MANAGER.add_event()delay(0.6)
                G.round_eval.divider_added = True
        else:delay(0.2)delay(0.2)G.E_MANAGER.add_event()
        dollar_row = 0
        if num_dollars > 60:
            dollar_string = localize($) + num_dollarsG.E_MANAGER.add_event()
        else:
            for i in range(1, num_dollars if num_dollars else 1, ):G.E_MANAGER.add_event()
    else:delay(0.4)G.E_MANAGER.add_event()
def change_shop_size(mod):
    if not G.GAME.shop:
        return False
    G.GAME.shop.joker_max = G.GAME.shop.joker_max + mod
    if G.shop_jokers & G.shop_jokers.cards:
        if mod < 0:
            for i in range(len(G.shop_jokers.cards), G.GAME.shop.joker_max + 1, -1):
                if G.shop_jokers.cards[i[G.shop_jokers.cards]':'i].remove()
        G.shop_jokers.config.card_limit = G.GAME.shop.joker_max
        G.shop_jokers.T.w = G.GAME.shop.joker_max * 1.01 * G.CARD_WG.shop.recalculate()
        if mod > 0:
            for i in range(1, G.GAME.shop.joker_max - len(G.shop_jokers.cards), ):G.shop_jokers.emplace()
def juice_card(card):G.E_MANAGER.add_event()
def update_canvas_juice(dt):
    G.JIGGLE_VIBRATION = G.ROOM.jiggle if G.ROOM.jiggle else 0
    if not G.SETTINGS.screenshake if not G.SETTINGS.screenshake else type() != 'number':
        G.SETTINGS.screenshake = G.SETTINGS.reduced_motion & 0 if G.SETTINGS.reduced_motion & 0 else 50
    shake_amt = (G.SETTINGS.reduced_motion & 0 if G.SETTINGS.reduced_motion & 0 else 1) * math.max(0) / 100
    G.ARGS.eased_cursor_pos = G.ARGS.eased_cursor_pos if G.ARGS.eased_cursor_pos else {'x': G.CURSOR.T.x, 'y': G.CURSOR.T.y, 'sx': G.CONTROLLER.cursor_position.x, 'sy': G.CONTROLLER.cursor_position.y}
    G.ARGS.eased_cursor_pos.x = G.ARGS.eased_cursor_pos.x * (1 - 3 * dt) + 3 * dt * (shake_amt * G.CURSOR.T.x + (1 - shake_amt) * G.ROOM.T.w / 2)
    G.ARGS.eased_cursor_pos.y = G.ARGS.eased_cursor_pos.y * (1 - 3 * dt) + 3 * dt * (shake_amt * G.CURSOR.T.y + (1 - shake_amt) * G.ROOM.T.h / 2)
    G.ARGS.eased_cursor_pos.sx = G.ARGS.eased_cursor_pos.sx * (1 - 3 * dt) + 3 * dt * (shake_amt * G.CONTROLLER.cursor_position.x + (1 - shake_amt) * G.WINDOWTRANS.real_window_w / 2)
    G.ARGS.eased_cursor_pos.sy = G.ARGS.eased_cursor_pos.sy * (1 - 3 * dt) + 3 * dt * (shake_amt * G.CONTROLLER.cursor_position.y + (1 - shake_amt) * G.WINDOWTRANS.real_window_h / 2)
    shake_amt = (G.SETTINGS.reduced_motion & 0 if G.SETTINGS.reduced_motion & 0 else 1) * G.SETTINGS.screenshake / 100 * 3
    if shake_amt < 0.05:
        shake_amt = 0
    G.ROOM.jiggle = (G.ROOM.jiggle if G.ROOM.jiggle else 0) * (1 - 5 * dt) * ((shake_amt > 0.05) & 1 if (shake_amt > 0.05) & 1 else 0)
    G.ROOM.T.r = (0.001 * math.sin() + 0.002 * G.ROOM.jiggle * math.sin()) * shake_amt
    G.ROOM.T.x = G.ROOM_ORIG.x + shake_amt * (0.015 * math.sin() + 0.01 * (G.ROOM.jiggle * shake_amt) * math.sin() + (G.ARGS.eased_cursor_pos.x - 0.5 * (G.ROOM.T.w + G.ROOM_ORIG.x)) * 0.01)
    G.ROOM.T.y = G.ROOM_ORIG.y + shake_amt * (0.015 * math.sin() + 0.01 * (G.ROOM.jiggle * shake_amt) * math.sin() + (G.ARGS.eased_cursor_pos.y - 0.5 * (G.ROOM.T.h + G.ROOM_ORIG.y)) * 0.01)
    G.JIGGLE_VIBRATION = G.JIGGLE_VIBRATION * (1 - 5 * dt)
    G.CURR_VIBRATION = G.CURR_VIBRATION if G.CURR_VIBRATION else 0
    G.CURR_VIBRATION = math.min(1)
    G.VIBRATION = 0
    G.CURR_VIBRATION = (1 - 15 * dt) * G.CURR_VIBRATION
    if not G.SETTINGS.rumble:
        G.CURR_VIBRATION = 0
    if G.CONTROLLER.GAMEPAD.object & G.F_RUMBLE:G.CONTROLLER.GAMEPAD.object.setVibration()
def juice_card_until(card, eval_func, first, delay):G.E_MANAGER.add_event()
def check_for_unlock(args):
    if not next(args):
        return False
    if G.GAME.seeded:
        return False
    if args.type == 'win_challenge':unlock_achievement(rule_bender)
        _c = True
        for kv in pairs():
            if not G.SETTINGS.profile].challenge_progress.completed[v.id[G.PROFILES]:
                _c = False
        if _c:unlock_achievement(rule_breaker)
    if G.GAME.challenge:
        return False
    if args.type == 'career_stat':
        if (args.statname == G.SETTINGS.profile].challenge_progress.completed[v.id[G.PROFILES] >= 2500):unlock_achievement(card_player)
        if (args.statname == G.SETTINGS.profile].challenge_progress.completed[v.id[G.PROFILES] >= 2500):unlock_achievement(card_discarder)
    if args.type == 'ante_up':
        if args.ante >= 4:unlock_achievement(ante_up)
        if args.ante >= 8:unlock_achievement(ante_upper)
    if args.type == 'win':unlock_achievement(heads_up)
        if G.GAME.round <= 12:unlock_achievement(speedrunner)
        if G.GAME.round_scores.times_rerolled.amt <= 0:unlock_achievement(you_get_what_you_get)
    if args.type == 'win_stake':
        highest_win = lowest_win = get_deck_win_stake(None)
        if highest_win >= 2:unlock_achievement(low_stakes)
        if highest_win >= 4:unlock_achievement(mid_stakes)
        if highest_win >= 8:unlock_achievement(high_stakes)
        if G.PROGRESS & (G.PROGRESS.deck_stakes.tally / G.PROGRESS.deck_stakes.of >= 1):unlock_achievement(completionist_plus)
        if G.PROGRESS & (G.PROGRESS.joker_stickers.tally / G.PROGRESS.joker_stickers.of >= 1):unlock_achievement(completionist_plus_plus)
    if args.type == 'money':
        if G.GAME.dollars >= 400:unlock_achievement(nest_egg)
    if args.type == 'hand':
        if (args.handname == 'Flush') & args.scoring_hand:
            _w = 0
            for kv in ipairs():
                if v.ability.name == 'Wild Card':
                    _w = _w + 1
            if _w == len(args.scoring_hand):unlock_achievement(flushed)
        if args.disp_text == 'Royal Flush':unlock_achievement(royale)
    if args.type == 'shatter':
        if len(args.shattered >= 2):unlock_achievement(shattered)
    if args.type == 'run_redeem':
        _v = 0
        _v = _v - (G.GAME.starting_voucher_count if G.GAME.starting_voucher_count else 0)
        for kv in pairs():
            _v = _v + 1
        if (_v >= 5) & (G.GAME.round_resets.ante <= 4):unlock_achievement(roi)
    if args.type == 'upgrade_hand':
        if args.level >= 10:unlock_achievement(retrograde)
    if args.type == 'chip_score':
        if args.chips >= 10000:unlock_achievement(_10k)
        if args.chips >= 1000000:unlock_achievement(_1000k)
        if args.chips >= 100000000:unlock_achievement(_100000k)
    if args.type == 'modify_deck':
        if G.deck & (G.deck.config.card_limit <= 20):unlock_achievement(tiny_hands)
        if G.deck & (G.deck.config.card_limit >= 80):unlock_achievement(big_hands)
    if args.type == 'spawn_legendary':unlock_achievement(legendary)
    if args.type == 'discover_amount':
        if G.DISCOVER_TALLIES.vouchers.tally / G.DISCOVER_TALLIES.vouchers.of >= 1:unlock_achievement(extreme_couponer)
        if G.DISCOVER_TALLIES.spectrals.tally / G.DISCOVER_TALLIES.spectrals.of >= 1:unlock_achievement(clairvoyance)
        if G.DISCOVER_TALLIES.tarots.tally / G.DISCOVER_TALLIES.tarots.of >= 1:unlock_achievement(cartomancy)
        if G.DISCOVER_TALLIES.planets.tally / G.DISCOVER_TALLIES.planets.of >= 1:unlock_achievement(astronomy)
        if G.DISCOVER_TALLIES.total.tally / G.DISCOVER_TALLIES.total.of >= 1:unlock_achievement(completionist)
    i = 1
    while i <= len(G.P_LOCKED):
        ret = False
        card = G.SETTINGS.profile].challenge_progress.completed[v.id[G.PROFILES]
        if (not card.unlocked) & card.unlock_condition & (args.type == 'career_stat'):
            if (args.statname == card.unlock_condition.type) & (G.SETTINGS.profile].challenge_progress.completed[v.id[G.PROFILES] >= card.unlock_condition.extra):
                ret = Trueunlock_card(card)
        if (not card.unlocked) & card.unlock_condition & (card.unlock_condition.type == args.type):
            if (args.type == 'hand') & (args.handname == card.unlock_condition.extra):
                ret = Trueunlock_card(card)
            if (args.type == 'min_hand_size') & G.hand & (G.hand.config.card_limit <= card.unlock_condition.extra):
                ret = Trueunlock_card(card)
            if (args.type == G.SETTINGS.profile].challenge_progress.completed[v.id[G.PROFILES].career_stats.c_round_interest_cap_streak):
                ret = Trueunlock_card(card)
            if args.type == 'run_card_replays':
                for kv in ipairs():
                    if v.base.times_played >= card.unlock_condition.extra:
                        ret = Trueunlock_card(card)
                        break
            if args.type == 'play_all_hearts':
                played = True
                for kv in ipairs():
                    if (v.ability.name != 'Stone Card') & (v.base.suit == 'Hearts'):
                        played = False
                for kv in ipairs():
                    if (v.ability.name != 'Stone Card') & (v.base.suit == 'Hearts'):
                        played = False
                if played:
                    ret = Trueunlock_card(card)
            if args.type == 'run_redeem':
                vouchers_redeemed = 0
                for kv in pairs():
                    vouchers_redeemed = vouchers_redeemed + 1
                if vouchers_redeemed >= card.unlock_condition.extra:
                    ret = Trueunlock_card(card)
            if args.type == 'have_edition':
                shiny_jokers = 0
                for kv in ipairs():
                    if v.edition:
                        shiny_jokers = shiny_jokers + 1
                if shiny_jokers >= card.unlock_condition.extra:
                    ret = Trueunlock_card(card)
            if args.type == 'double_gold':
                ret = Trueunlock_card(card)
            if args.type == 'continue_game':
                ret = Trueunlock_card(card)
            if args.type == 'blank_redeems':
                if "'v_blank'[G.PROFILES[G.SETTINGS.profile].voucher_usage]" & ("'v_blank'[G.PROFILES[G.SETTINGS.profile].voucher_usage]".count >= card.unlock_condition.extra):unlock_card(card)
            if args.type == 'modify_deck':
                if card.unlock_condition.extra & card.unlock_condition.extra.suit:
                    count = 0
                    for _v in pairs():
                        if v.base.suit == card.unlock_condition.extra.suit:
                            count = count + 1
                    if count >= card.unlock_condition.extra.count:
                        ret = Trueunlock_card(card)
                if card.unlock_condition.extra & card.unlock_condition.extra.enhancement:
                    count = 0
                    for _v in pairs():
                        if v.ability.name == card.unlock_condition.extra.enhancement:
                            count = count + 1
                    if count >= card.unlock_condition.extra.count:
                        ret = Trueunlock_card(card)
                if card.unlock_condition.extra & card.unlock_condition.extra.tally:
                    count = 0
                    for _v in pairs():
                        if v.ability.set == 'Enhanced':
                            count = count + 1
                    if count >= card.unlock_condition.extra.count:
                        ret = Trueunlock_card(card)
            if args.type == 'discover_amount':
                if card.unlock_condition.amount:
                    if card.unlock_condition.amount <= args.amount:
                        ret = Trueunlock_card(card)
                if card.unlock_condition.tarot_count:
                    if card.unlock_condition.tarot_count <= args.tarot_count:
                        ret = Trueunlock_card(card)
                if card.unlock_condition.planet_count:
                    if card.unlock_condition.planet_count <= args.planet_count:
                        ret = Trueunlock_card(card)
            if args.type == 'win_deck':
                if card.unlock_condition.deck:
                    if get_deck_win_stake() > 0:
                        ret = Trueunlock_card(card)
            if args.type == 'win_stake':
                if card.unlock_condition.stake:
                    if get_deck_win_stake() >= card.unlock_condition.stake:
                        ret = Trueunlock_card(card)
            if args.type == 'discover_planets':
                count = 0
                for kv in pairs():
                    if (v.set == 'Planet') & v.discovered:
                        count = count + 1
                if count >= 9:
                    ret = Trueunlock_card(card)
            if args.type == 'blind_discoveries':
                discovered_blinds = 0
                for kv in pairs():
                    if v.discovered:
                        discovered_blinds = discovered_blinds + 1
                if discovered_blinds >= card.unlock_condition.extra:
                    ret = Trueunlock_card(card)
            if (args.type == 'modify_jokers') & G.jokers:
                if card.unlock_condition.extra.count:
                    count = 0
                    for _v in pairs():
                        if (v.ability.set == 'Joker') & v.edition & v.edition.polychrome & card.unlock_condition.extra.polychrome:
                            count = count + 1
                    if count >= card.unlock_condition.extra.count:
                        ret = Trueunlock_card(card)
            if args.type == 'money':
                if card.unlock_condition.extra <= G.GAME.dollars:
                    ret = Trueunlock_card(card)
            if args.type == 'round_win':
                if card.name == 'Matador':
                    if (G.GAME.current_round.hands_played == 1) & (G.GAME.current_round.discards_left == G.GAME.round_resets.discards) & (G.GAME.blind.get_type() == 'Boss'):
                        ret = Trueunlock_card(card)
                if card.name == 'Troubadour':
                    if G.SETTINGS.profile].challenge_progress.completed[v.id[G.PROFILES].career_stats.c_single_hand_round_streak >= card.unlock_condition.extra:
                        ret = Trueunlock_card(card)
                if card.name == 'Hanging Chad':
                    if (G.GAME.last_hand_played == card.unlock_condition.extra) & (G.GAME.blind.get_type() == 'Boss'):
                        ret = Trueunlock_card(card)
            if args.type == 'ante_up':
                if card.unlock_condition.ante:
                    if args.ante == card.unlock_condition.ante:
                        ret = Trueunlock_card(card)
            if args.type == 'hand_contents':
                if card.name == 'Seeing Double':
                    tally = 0
                    for j in range(1, len(args.cards), ):
                        if (G.SETTINGS.profile].challenge_progress.completed[v.id[G.PROFILES].is_suit(Clubs):
                            tally = tally + 1
                    if tally >= 4:
                        ret = Trueunlock_card(card)
                if card.name == 'Golden Ticket':
                    tally = 0
                    for j in range(1, len(args.cards), ):
                        if G.SETTINGS.profile].challenge_progress.completed[v.id[G.PROFILES].ability.name == 'Gold Card':
                            tally = tally + 1
                    if tally >= 5:
                        ret = Trueunlock_card(card)
            if args.type == 'discard_custom':
                if card.name == 'Hit the Road':
                    tally = 0
                    for j in range(1, len(args.cards), ):
                        if G.SETTINGS.profile].challenge_progress.completed[v.id[G.PROFILES].get_id() == 11:
                            tally = tally + 1
                    if tally >= 5:
                        ret = Trueunlock_card(card)
                if card.name == 'Brainstorm':
                    eval = evaluate_poker_hand()
                    if next('Straight Flush'[eval]):
                        min = 10
                        for j in range(1, len(args.cards), ):
                            if G.SETTINGS.profile].challenge_progress.completed[v.id[G.PROFILES].get_id() < min:
                                min = G.SETTINGS.profile].challenge_progress.completed[v.id[G.PROFILES].get_id()
                        if min == 10:
                            ret = Trueunlock_card(card)
            if (args.type == G.SETTINGS.profile].challenge_progress.completed[v.id[G.PROFILES].played == 0):
                ret = Trueunlock_card(card)
            if args.type == 'win_custom':
                if (card.name == 'Invisible Joker') & (G.GAME.max_jokers <= 4):
                    ret = Trueunlock_card(card)
                if card.name == 'Blueprint':
                    ret = Trueunlock_card(card)
            if args.type == 'win':
                if card.unlock_condition.n_rounds >= G.GAME.round:
                    ret = Trueunlock_card(card)
            if args.type == 'chip_score':
                if card.unlock_condition.chips <= args.chips:
                    ret = TrueG.E_MANAGER.add_event()
        if ret == True:table.remove()
        else:
            i = i + 1
    else:
def unlock_card(card):
    if card.unlocked == False:
        if G.GAME.seeded if G.GAME.seeded else G.GAME.challenge:
            return False
        if card.unlocked if card.unlocked else card.wip:
            return FalseG.save_notify(card)
        card.unlocked = True
        if card.set == 'Back':discover_card(card)table.sort("Back"[G.P_CENTER_POOLS])G.save_progress()
        G.FILE_HANDLER.force = Truenotify_alert()
def fetch_achievements():
    G.ACHIEVEMENTS = G.ACHIEVEMENTS if G.ACHIEVEMENTS else {'ante_up': {'order': 1, 'tier': 3, 'earned': False, 'steamid': 'BAL_01'}, 'ante_upper': {'order': 2, 'tier': 3, 'earned': False, 'steamid': 'BAL_02'}, 'heads_up': {'order': 3, 'tier': 2, 'earned': False, 'steamid': 'BAL_03'}, 'low_stakes': {'order': 4, 'tier': 2, 'earned': False, 'steamid': 'BAL_04'}, 'mid_stakes': {'order': 5, 'tier': 2, 'earned': False, 'steamid': 'BAL_05'}, 'high_stakes': {'order': 6, 'tier': 2, 'earned': False, 'steamid': 'BAL_06'}, 'card_player': {'order': 7, 'tier': 3, 'earned': False, 'steamid': 'BAL_07'}, 'card_discarder': {'order': 8, 'tier': 3, 'earned': False, 'steamid': 'BAL_08'}, 'nest_egg': {'order': 9, 'tier': 2, 'earned': False, 'steamid': 'BAL_09'}, 'flushed': {'order': 10, 'tier': 3, 'earned': False, 'steamid': 'BAL_10'}, 'speedrunner': {'order': 11, 'tier': 2, 'earned': False, 'steamid': 'BAL_11'}, 'roi': {'order': 12, 'tier': 3, 'earned': False, 'steamid': 'BAL_12'}, 'shattered': {'order': 13, 'tier': 3, 'earned': False, 'steamid': 'BAL_13'}, 'royale': {'order': 14, 'tier': 3, 'earned': False, 'steamid': 'BAL_14'}, 'retrograde': {'order': 15, 'tier': 2, 'earned': False, 'steamid': 'BAL_15'}, '_10k': {'order': 16, 'tier': 3, 'earned': False, 'steamid': 'BAL_16'}, '_1000k': {'order': 17, 'tier': 2, 'earned': False, 'steamid': 'BAL_17'}, '_100000k': {'order': 18, 'tier': 1, 'earned': False, 'steamid': 'BAL_18'}, 'tiny_hands': {'order': 19, 'tier': 2, 'earned': False, 'steamid': 'BAL_19'}, 'big_hands': {'order': 20, 'tier': 2, 'earned': False, 'steamid': 'BAL_20'}, 'you_get_what_you_get': {'order': 21, 'tier': 3, 'earned': False, 'steamid': 'BAL_21'}, 'rule_bender': {'order': 22, 'tier': 3, 'earned': False, 'steamid': 'BAL_22'}, 'rule_breaker': {'order': 23, 'tier': 1, 'earned': False, 'steamid': 'BAL_23'}, 'legendary': {'order': 24, 'tier': 3, 'earned': False, 'steamid': 'BAL_24'}, 'astronomy': {'order': 25, 'tier': 3, 'earned': False, 'steamid': 'BAL_25'}, 'cartomancy': {'order': 26, 'tier': 3, 'earned': False, 'steamid': 'BAL_26'}, 'clairvoyance': {'order': 27, 'tier': 2, 'earned': False, 'steamid': 'BAL_27'}, 'extreme_couponer': {'order': 28, 'tier': 1, 'earned': False, 'steamid': 'BAL_28'}, 'completionist': {'order': 29, 'tier': 1, 'earned': False, 'steamid': 'BAL_29'}, 'completionist_plus': {'order': 30, 'tier': 1, 'earned': False, 'steamid': 'BAL_30'}, 'completionist_plus_plus': {'order': 31, 'tier': 1, 'earned': False, 'steamid': 'BAL_31'}}
    if G.F_NO_ACHIEVEMENTS:
        return False
    if not G.STEAM:
        G.SETTINGS.ACHIEVEMENTS_EARNED = G.SETTINGS.ACHIEVEMENTS_EARNED if G.SETTINGS.ACHIEVEMENTS_EARNED else {}
        for kv in pairs():
            if G.ACHIEVEMENTS[k]:
                G.ACHIEVEMENTS[k].earned = True
    if G.STEAM & (not G.STEAM.initial_fetch):
        for kv in pairs():
            achievement_name = v.steamid
            success = achieved = G.STEAM.userStats.getAchievement(achievement_name)
            if success:
                v.earned = not not achieved
        G.STEAM.initial_fetch = True
def unlock_achievement(achievement_name):
    if G.PROFILES[G.SETTINGS.profile].all_unlocked:
        return FalseG.E_MANAGER.add_event()
def notify_alert(_achievement, _type):
    _type = _type if _type else 'achievement'G.E_MANAGER.add_event()G.E_MANAGER.add_event()G.E_MANAGER.add_event()G.E_MANAGER.add_event()G.E_MANAGER.add_event()
def inc_steam_stat(stat_name):
    if not G.STEAM:
        return False
    success = current_stat = G.STEAM.userStats.getStatInt(stat_name)
    if success:G.STEAM.userStats.setStatInt(stat_name)
        G.STEAM.send_control.update_queued = True
def unlock_notify():
    _UN = get_compressed()
    if _UN:
        for key in string.gmatch():create_unlock_overlay(key)love.filesystem.remove()
def create_unlock_overlay(key):
    if G.P_CENTERS[key]:G.E_MANAGER.add_event()
def discover_card(card):
    if G.GAME.seeded if G.GAME.seeded else G.GAME.challenge:
        return False
    card = card if card else {}
    if card.discovered if card.discovered else card.wip:
        return False
    if card & (not card.discovered):
        card.alert = True
        G.GAME.round_scores.new_collection.amt = G.GAME.round_scores.new_collection.amt + 1
    card.discovered = Trueset_discover_tallies()G.E_MANAGER.add_event()
def get_deck_from_name(_name):
    for kv in pairs():
        if v.name == _name:
            return v
def get_next_voucher_key(_from_tag):
    _pool = _pool_key = get_current_pool(Voucher)
    if _from_tag:
        _pool_key = 'Voucher_fromtag'
    center = pseudorandom_element(_pool)
    it = 1
    while center == 'UNAVAILABLE':
        it = it + 1
        center = pseudorandom_element(_pool)
    else:
    return center
def get_next_tag_key(append):
    if G.FORCE_TAG:
        return G.FORCE_TAG
    _pool = _pool_key = get_current_pool(Tag, None, None, append)
    _tag = pseudorandom_element(_pool)
    it = 1
    while _tag == 'UNAVAILABLE':
        it = it + 1
        _tag = pseudorandom_element(_pool)
    else:
    return _tag
def create_playing_card(card_init, area, skip_materialize, silent, colours):
    card_init = card_init if card_init else {}
    card_init.front = card_init.front if card_init.front else pseudorandom_element()
    card_init.center = card_init.center if card_init.center else G.P_CENTERS.c_base
    G.playing_card = G.playing_card & G.playing_card + 1 if G.playing_card & G.playing_card + 1 else 1
    _area = area if area else G.hand
    card = Card()table.insert()
    card.playing_card = G.playing_card
    if area:area.emplace(card)
    if not skip_materialize:card.start_materialize(colours, silent)
    return card
def get_pack(_key, _type):
    if (not G.GAME.first_shop_buffoon) & (not "'p_buffoon_normal_1'[G.GAME.banned_keys]"):
        G.GAME.first_shop_buffoon = True
        return "'p_buffoon_normal_'..math.random(1, 2)[G.P_CENTERS]"
    cume = it = center = (0, 0, 'None')
    for kv in ipairs('Booster'[G.P_CENTER_POOLS]):
        if (not _type if not _type else _type == v.kind) & (not G.GAME.banned_keys[v.key]):
            cume = cume + (v.weight if v.weight else 1)
    poll = pseudorandom() * cume
    for kv in ipairs('Booster'[G.P_CENTER_POOLS]):
        if not G.GAME.banned_keys[v.key]:
            if not _type if not _type else _type == v.kind:
                it = it + (v.weight if v.weight else 1)
            if (it >= poll) & (it - (v.weight if v.weight else 1) <= poll):
                center = v';'
                break
    return center
def get_current_pool(_type, _rarity, _legendary, _append):
    G.ARGS.TEMP_POOL = EMPTY()
    _pool = _starting_pool = _pool_key = _pool_size = (G.ARGS.TEMP_POOL, 'None', '', 0)
    if _type == 'Joker':
        rarity = _rarity if _rarity else pseudorandom()
        rarity = ((_legendary & 4 if _legendary & 4 else (rarity > 0.95) & 3) if (_legendary & 4 if _legendary & 4 else (rarity > 0.95) & 3) else (rarity > 0.7) & 2) if ((_legendary & 4 if _legendary & 4 else (rarity > 0.95) & 3) if (_legendary & 4 if _legendary & 4 else (rarity > 0.95) & 3) else (rarity > 0.7) & 2) else 1
        _starting_pool = _pool_key = (G.P_JOKER_RARITY_POOLS[rarity], 'Joker' + rarity + ((not _legendary) & _append if (not _legendary) & _append else ''))
    else:
        _starting_pool = _pool_key = (G.P_JOKER_RARITY_POOLS[rarity], _type + (_append if _append else ''))
    for kv in ipairs(_starting_pool):
        add = 'None'
        if _type == 'Enhanced':
            add = True
        elif _type == 'Demo':
            if v.pos & v.config:
                add = True
        elif _type == 'Tag':
            if (not v.requires if not v.requires else G.P_JOKER_RARITY_POOLS[rarity].discovered) & (not v.min_ante if not v.min_ante else v.min_ante <= G.GAME.round_resets.ante):
                add = True
        elif (not G.P_JOKER_RARITY_POOLS[rarity] & (not next())) & (v.unlocked != False if v.unlocked != False else v.rarity == 4):
            if v.set == 'Voucher':
                if not G.P_JOKER_RARITY_POOLS[rarity]:
                    include = True
                    if v.requires:
                        for kkvv in pairs():
                            if not G.P_JOKER_RARITY_POOLS[rarity]:
                                include = False
                    if G.shop_vouchers & G.shop_vouchers.cards:
                        for kkvv in ipairs():
                            if vv.config.center.key == v.key:
                                include = False
                    if include:
                        add = True
            elif v.set == 'Planet':
                if not v.config.softlock if not v.config.softlock else G.P_JOKER_RARITY_POOLS[rarity].played > 0:
                    add = True
            elif v.enhancement_gate:
                add = 'None'
                for kkvv in pairs():
                    if vv.config.center.key == v.enhancement_gate:
                        add = True
            else:
                add = True
            if v.name == 'Black Hole' if v.name == 'Black Hole' else v.name == 'The Soul':
                add = False
        if v.no_pool_flag & G.P_JOKER_RARITY_POOLS[rarity]:
            add = 'None'
        if v.yes_pool_flag & (not G.P_JOKER_RARITY_POOLS[rarity]):
            add = 'None'
        if add & (not G.P_JOKER_RARITY_POOLS[rarity]):
            G.P_JOKER_RARITY_POOLS[rarity] = v.key
            _pool_size = _pool_size + 1
        else:
            G.P_JOKER_RARITY_POOLS[rarity] = 'UNAVAILABLE'
    if _pool_size == 0:
        _pool = EMPTY()
        if _type == 'Tarot' if _type == 'Tarot' else _type == 'Tarot_Planet':
            G.P_JOKER_RARITY_POOLS[rarity] = 'c_strength'
        elif _type == 'Planet':
            G.P_JOKER_RARITY_POOLS[rarity] = 'c_pluto'
        elif _type == 'Spectral':
            G.P_JOKER_RARITY_POOLS[rarity] = 'c_incantation'
        elif _type == 'Joker':
            G.P_JOKER_RARITY_POOLS[rarity] = 'j_joker'
        elif _type == 'Demo':
            G.P_JOKER_RARITY_POOLS[rarity] = 'j_joker'
        elif _type == 'Voucher':
            G.P_JOKER_RARITY_POOLS[rarity] = 'v_blank'
        elif _type == 'Tag':
            G.P_JOKER_RARITY_POOLS[rarity] = 'tag_handy'
        else:
            G.P_JOKER_RARITY_POOLS[rarity] = 'j_joker'
    return _pool_pool_key + ((not _legendary) & G.GAME.round_resets.ante if (not _legendary) & G.GAME.round_resets.ante else '')
def poll_edition(_key, _mod, _no_neg, _guaranteed):
    _mod = _mod if _mod else 1
    edition_poll = pseudorandom()
    if _guaranteed:
        if (edition_poll > 1 - 0.003 * 25) & (not _no_neg):
            return {'negative': True}
        elif edition_poll > 1 - 0.006 * 25:
            return {'polychrome': True}
        elif edition_poll > 1 - 0.02 * 25:
            return {'holo': True}
        elif edition_poll > 1 - 0.04 * 25:
            return {'foil': True}
    elif (edition_poll > 1 - 0.003 * _mod) & (not _no_neg):
        return {'negative': True}
    elif edition_poll > 1 - 0.006 * G.GAME.edition_rate * _mod:
        return {'polychrome': True}
    elif edition_poll > 1 - 0.02 * G.GAME.edition_rate * _mod:
        return {'holo': True}
    elif edition_poll > 1 - 0.04 * G.GAME.edition_rate * _mod:
        return {'foil': True}
    return 'None'
def create_card(_type, area, legendary, _rarity, skip_materialize, soulable, forced_key, key_append):
    area = area if area else G.jokers
    center = G.P_CENTERS.b_red
    if (not forced_key) & soulable & (not "'c_soul'[G.GAME.banned_keys]"):
        if ((_type == 'Tarot' if _type == 'Tarot' else _type == 'Spectral') if (_type == 'Tarot' if _type == 'Tarot' else _type == 'Spectral') else _type == 'Tarot_Planet') & (not "'c_soul'[G.GAME.used_jokers]" & (not next())):
            if pseudorandom() > 0.997:
                forced_key = 'c_soul'
        if (_type == 'Planet' if _type == 'Planet' else _type == 'Spectral') & (not "'c_black_hole'[G.GAME.used_jokers]" & (not next())):
            if pseudorandom() > 0.997:
                forced_key = 'c_black_hole'
    if _type == 'Base':
        forced_key = 'c_base'
    if forced_key & (not G.GAME.banned_keys[forced_key]):
        center = G.GAME.banned_keys[forced_key]
        _type = (center.set != 'Default') & center.set if (center.set != 'Default') & center.set else _type
    else:
        _pool = _pool_key = get_current_pool(_type, _rarity, legendary, key_append)
        center = pseudorandom_element(_pool)
        it = 1
        while center == 'UNAVAILABLE':
            it = it + 1
            center = pseudorandom_element(_pool)
        else:
        center = G.GAME.banned_keys[forced_key]
    front = (_type == 'Base' if _type == 'Base' else _type == 'Enhanced') & pseudorandom_element() if (_type == 'Base' if _type == 'Base' else _type == 'Enhanced') & pseudorandom_element() else 'None'
    card = Card()
    if card.ability.consumeable & (not skip_materialize):card.start_materialize()
    if _type == 'Joker':
        if G.GAME.modifiers.all_eternal:card.set_eternal(True)
        if area == G.shop_jokers if area == G.shop_jokers else area == G.pack_cards:
            eternal_perishable_poll = pseudorandom()
            if G.GAME.modifiers.enable_eternals_in_shop & (eternal_perishable_poll > 0.7):card.set_eternal(True)
            elif G.GAME.modifiers.enable_perishables_in_shop & ((eternal_perishable_poll > 0.4) & (eternal_perishable_poll <= 0.7)):card.set_perishable(True)
            if G.GAME.modifiers.enable_rentals_in_shop & (pseudorandom() > 0.7):card.set_rental(True)
        edition = poll_edition()card.set_edition(edition)check_for_unlock()
    return card
def copy_card(other, new_card, card_scale, playing_card, strip_edition):
    new_card = new_card if new_card else Card()new_card.set_ability()
    new_card.ability.type = other.ability.typenew_card.set_base()
    for kv in pairs():
        if type(v) == 'table':
            new_card.ability[k] = copy_table(v)
        else:
            new_card.ability[k] = v
    if not strip_edition:new_card.set_edition()check_for_unlock()new_card.set_seal()
    if other.params:
        new_card.params = other.params
        new_card.params.playing_card = playing_card
    new_card.debuff = other.debuff
    new_card.pinned = other.pinned
    return new_card
def tutorial_info(args):
    overlay_colour = {1: 0.32, 2: 0.36, 3: 0.41, 4: 0}ease_value(overlay_colour, 4, 0.6, None, REAL, True, 0.4)
    G.OVERLAY_TUTORIAL = G.OVERLAY_TUTORIAL if G.OVERLAY_TUTORIAL else UIBox()
    G.OVERLAY_TUTORIAL.step = G.OVERLAY_TUTORIAL.step if G.OVERLAY_TUTORIAL.step else 1
    G.OVERLAY_TUTORIAL.step_complete = False
    row_dollars_chips = G.HUD.get_UIE_by_ID(row_dollars_chips)
    align = args.align if args.align else 'tm'
    step = args.step if args.step else 1
    attach = args.attach if args.attach else {'major': row_dollars_chips, 'type': 'tm', 'offset': {'x': 0, 'y': -0.5}}
    pos = args.pos if args.pos else {'x': attach.major.T.x + attach.major.T.w / 2, 'y': attach.major.T.y + attach.major.T.h / 2}
    button = args.button if args.button else {'button': localize(b_next), 'func': 'tut_next'}
    args.highlight = args.highlight if args.highlight else {}G.E_MANAGER.add_event()
    return step + 1
def calculate_reroll_cost(skip_increment):
    if G.GAME.current_round.free_rerolls < 0:
        G.GAME.current_round.free_rerolls = 0
    if G.GAME.current_round.free_rerolls > 0:
        G.GAME.current_round.reroll_cost = 0';'
        return False
    G.GAME.current_round.reroll_cost_increase = G.GAME.current_round.reroll_cost_increase if G.GAME.current_round.reroll_cost_increase else 0
    if not skip_increment:
        G.GAME.current_round.reroll_cost_increase = G.GAME.current_round.reroll_cost_increase + 1
    G.GAME.current_round.reroll_cost = (G.GAME.round_resets.temp_reroll_cost if G.GAME.round_resets.temp_reroll_cost else G.GAME.round_resets.reroll_cost) + G.GAME.current_round.reroll_cost_increase
def reset_idol_card():
    G.GAME.current_round.idol_card.rank = 'Ace'
    G.GAME.current_round.idol_card.suit = 'Spades'
    valid_idol_cards = {}
    for kv in ipairs():
        if v.ability.effect != 'Stone Card':
            valid_idol_cards[#valid_idol_cards + 1] = v
    if valid_idol_cards[#valid_idol_cards + 1]:
        idol_card = pseudorandom_element(valid_idol_cards)
        G.GAME.current_round.idol_card.rank = idol_card.base.value
        G.GAME.current_round.idol_card.suit = idol_card.base.suit
        G.GAME.current_round.idol_card.id = idol_card.base.id
def reset_mail_rank():
    G.GAME.current_round.mail_card.rank = 'Ace'
    valid_mail_cards = {}
    for kv in ipairs():
        if v.ability.effect != 'Stone Card':
            valid_mail_cards[#valid_mail_cards + 1] = v
    if valid_mail_cards[#valid_mail_cards + 1]:
        mail_card = pseudorandom_element(valid_mail_cards)
        G.GAME.current_round.mail_card.rank = mail_card.base.value
        G.GAME.current_round.mail_card.id = mail_card.base.id
def reset_ancient_card():
    ancient_suits = {}
    for kv in ipairs():
        if v != G.GAME.current_round.ancient_card.suit:
            ancient_suits[#ancient_suits + 1] = v
    ancient_card = pseudorandom_element(ancient_suits)
    G.GAME.current_round.ancient_card.suit = ancient_card
def reset_castle_card():
    G.GAME.current_round.castle_card.suit = 'Spades'
    valid_castle_cards = {}
    for kv in ipairs():
        if v.ability.effect != 'Stone Card':
            valid_castle_cards[#valid_castle_cards + 1] = v
    if valid_castle_cards[#valid_castle_cards + 1]:
        castle_card = pseudorandom_element(valid_castle_cards)
        G.GAME.current_round.castle_card.suit = castle_card.base.suit
def reset_blinds():
    G.GAME.round_resets.blind_states = G.GAME.round_resets.blind_states if G.GAME.round_resets.blind_states else {'Small': 'Select', 'Big': 'Upcoming', 'Boss': 'Upcoming'}
    if G.GAME.round_resets.blind_states.Boss == 'Defeated':
        G.GAME.round_resets.blind_states.Small = 'Upcoming'
        G.GAME.round_resets.blind_states.Big = 'Upcoming'
        G.GAME.round_resets.blind_states.Boss = 'Upcoming'
        G.GAME.blind_on_deck = 'Small'
        G.GAME.round_resets.blind_choices.Boss = get_new_boss()
        G.GAME.round_resets.boss_rerolled = False
def get_new_boss():
    G.GAME.perscribed_bosses = G.GAME.perscribed_bosses if G.GAME.perscribed_bosses else {}
    if G.GAME.perscribed_bosses & G.GAME.perscribed_bosses[G.GAME.round_resets.ante]:
        ret_boss = G.GAME.perscribed_bosses[G.GAME.round_resets.ante]
        G.GAME.perscribed_bosses[G.GAME.round_resets.ante] = 'None'
        G.GAME.perscribed_bosses[G.GAME.round_resets.ante] + 1
        return ret_boss
    if G.FORCE_BOSS:
        return G.FORCE_BOSS
    eligible_bosses = {}
    for kv in pairs():
        if not v.boss:
        elif (not v.boss.showdown) & ((v.boss.min <= math.max(1)) & ((math.max(1) % G.GAME.win_ante) != 0 if (math.max(1) % G.GAME.win_ante) != 0 else G.GAME.round_resets.ante < 2)):
            G.GAME.perscribed_bosses[G.GAME.round_resets.ante] = True
        elif v.boss.showdown & ((G.GAME.round_resets.ante % G.GAME.win_ante) == 0) & (G.GAME.round_resets.ante >= 2):
            G.GAME.perscribed_bosses[G.GAME.round_resets.ante] = True
    for kv in pairs():
        if G.GAME.perscribed_bosses[G.GAME.round_resets.ante]:
            G.GAME.perscribed_bosses[G.GAME.round_resets.ante] = 'None'
    min_use = 100
    for kv in pairs():
        if G.GAME.perscribed_bosses[G.GAME.round_resets.ante]:
            G.GAME.perscribed_bosses[G.GAME.round_resets.ante] = v
            if G.GAME.perscribed_bosses[G.GAME.round_resets.ante] <= min_use:
                min_use = G.GAME.perscribed_bosses[G.GAME.round_resets.ante]
    for kv in pairs(eligible_bosses):
        if G.GAME.perscribed_bosses[G.GAME.round_resets.ante]:
            if G.GAME.perscribed_bosses[G.GAME.round_resets.ante] > min_use:
                G.GAME.perscribed_bosses[G.GAME.round_resets.ante] = 'None'
    _ = boss = pseudorandom_element(eligible_bosses)
    G.GAME.perscribed_bosses[G.GAME.round_resets.ante] + 1
    return boss
def get_type_colour(_c, card):
    return (((((((_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK if (_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK else (_c.unlocked != False) & ((_c.set == G.C.SECONDARY_SET[Joker' if _c.set == 'Joker' else _c.consumeable) if (_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) else _c.set == 'Voucher') & (not _c.discoveredand) & (not ((_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area if (_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area else not _c.area)) & G.C.JOKER_GREY) if ((_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK if (_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK else (_c.unlocked != False) & ((_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) if (_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) else _c.set == 'Voucher') & (not _c.discoveredand) & (not ((_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area if (_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area else not _c.area)) & G.C.JOKER_GREY) else card & card.debuff & mix_colours()) if (((_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK if (_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK else (_c.unlocked != False) & ((_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) if (_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) else _c.set == 'Voucher') & (not _c.discoveredand) & (not ((_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area if (_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area else not _c.area)) & G.C.JOKER_GREY) if ((_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK if (_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK else (_c.unlocked != False) & ((_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) if (_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) else _c.set == 'Voucher') & (not _c.discoveredand) & (not ((_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area if (_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area else not _c.area)) & G.C.JOKER_GREY) else card & card.debuff & mix_colours()) else (_c.set == 'Joker') & '_c.rarity[G.C.RARITY]') if ((((_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK if (_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK else (_c.unlocked != False) & ((_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) if (_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) else _c.set == 'Voucher') & (not _c.discoveredand) & (not ((_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area if (_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area else not _c.area)) & G.C.JOKER_GREY) if ((_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK if (_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK else (_c.unlocked != False) & ((_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) if (_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) else _c.set == 'Voucher') & (not _c.discoveredand) & (not ((_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area if (_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area else not _c.area)) & G.C.JOKER_GREY) else card & card.debuff & mix_colours()) if (((_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK if (_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK else (_c.unlocked != False) & ((_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) if (_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) else _c.set == 'Voucher') & (not _c.discoveredand) & (not ((_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area if (_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area else not _c.area)) & G.C.JOKER_GREY) if ((_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK if (_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK else (_c.unlocked != False) & ((_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) if (_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) else _c.set == 'Voucher') & (not _c.discoveredand) & (not ((_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area if (_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area else not _c.area)) & G.C.JOKER_GREY) else card & card.debuff & mix_colours()) else (_c.set == 'Joker') & '_c.rarity[G.C.RARITY]') else (_c.set == 'Edition') & G.C.DARK_EDITION) if (((((_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK if (_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK else (_c.unlocked != False) & ((_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) if (_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) else _c.set == 'Voucher') & (not _c.discoveredand) & (not ((_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area if (_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area else not _c.area)) & G.C.JOKER_GREY) if ((_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK if (_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK else (_c.unlocked != False) & ((_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) if (_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) else _c.set == 'Voucher') & (not _c.discoveredand) & (not ((_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area if (_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area else not _c.area)) & G.C.JOKER_GREY) else card & card.debuff & mix_colours()) if (((_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK if (_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK else (_c.unlocked != False) & ((_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) if (_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) else _c.set == 'Voucher') & (not _c.discoveredand) & (not ((_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area if (_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area else not _c.area)) & G.C.JOKER_GREY) if ((_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK if (_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK else (_c.unlocked != False) & ((_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) if (_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) else _c.set == 'Voucher') & (not _c.discoveredand) & (not ((_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area if (_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area else not _c.area)) & G.C.JOKER_GREY) else card & card.debuff & mix_colours()) else (_c.set == 'Joker') & '_c.rarity[G.C.RARITY]') if ((((_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK if (_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK else (_c.unlocked != False) & ((_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) if (_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) else _c.set == 'Voucher') & (not _c.discoveredand) & (not ((_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area if (_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area else not _c.area)) & G.C.JOKER_GREY) if ((_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK if (_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK else (_c.unlocked != False) & ((_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) if (_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) else _c.set == 'Voucher') & (not _c.discoveredand) & (not ((_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area if (_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area else not _c.area)) & G.C.JOKER_GREY) else card & card.debuff & mix_colours()) if (((_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK if (_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK else (_c.unlocked != False) & ((_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) if (_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) else _c.set == 'Voucher') & (not _c.discoveredand) & (not ((_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area if (_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area else not _c.area)) & G.C.JOKER_GREY) if ((_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK if (_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK else (_c.unlocked != False) & ((_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) if (_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) else _c.set == 'Voucher') & (not _c.discoveredand) & (not ((_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area if (_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area else not _c.area)) & G.C.JOKER_GREY) else card & card.debuff & mix_colours()) else (_c.set == 'Joker') & '_c.rarity[G.C.RARITY]') else (_c.set == 'Edition') & G.C.DARK_EDITION) else (_c.set == 'Booster') & G.C.BOOSTER) if ((((((_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK if (_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK else (_c.unlocked != False) & ((_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) if (_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) else _c.set == 'Voucher') & (not _c.discoveredand) & (not ((_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area if (_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area else not _c.area)) & G.C.JOKER_GREY) if ((_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK if (_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK else (_c.unlocked != False) & ((_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) if (_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) else _c.set == 'Voucher') & (not _c.discoveredand) & (not ((_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area if (_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area else not _c.area)) & G.C.JOKER_GREY) else card & card.debuff & mix_colours()) if (((_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK if (_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK else (_c.unlocked != False) & ((_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) if (_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) else _c.set == 'Voucher') & (not _c.discoveredand) & (not ((_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area if (_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area else not _c.area)) & G.C.JOKER_GREY) if ((_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK if (_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK else (_c.unlocked != False) & ((_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) if (_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) else _c.set == 'Voucher') & (not _c.discoveredand) & (not ((_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area if (_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area else not _c.area)) & G.C.JOKER_GREY) else card & card.debuff & mix_colours()) else (_c.set == 'Joker') & '_c.rarity[G.C.RARITY]') if ((((_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK if (_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK else (_c.unlocked != False) & ((_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) if (_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) else _c.set == 'Voucher') & (not _c.discoveredand) & (not ((_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area if (_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area else not _c.area)) & G.C.JOKER_GREY) if ((_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK if (_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK else (_c.unlocked != False) & ((_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) if (_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) else _c.set == 'Voucher') & (not _c.discoveredand) & (not ((_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area if (_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area else not _c.area)) & G.C.JOKER_GREY) else card & card.debuff & mix_colours()) if (((_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK if (_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK else (_c.unlocked != False) & ((_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) if (_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) else _c.set == 'Voucher') & (not _c.discoveredand) & (not ((_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area if (_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area else not _c.area)) & G.C.JOKER_GREY) if ((_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK if (_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK else (_c.unlocked != False) & ((_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) if (_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) else _c.set == 'Voucher') & (not _c.discoveredand) & (not ((_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area if (_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area else not _c.area)) & G.C.JOKER_GREY) else card & card.debuff & mix_colours()) else (_c.set == 'Joker') & '_c.rarity[G.C.RARITY]') else (_c.set == 'Edition') & G.C.DARK_EDITION) if (((((_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK if (_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK else (_c.unlocked != False) & ((_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) if (_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) else _c.set == 'Voucher') & (not _c.discoveredand) & (not ((_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area if (_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area else not _c.area)) & G.C.JOKER_GREY) if ((_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK if (_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK else (_c.unlocked != False) & ((_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) if (_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) else _c.set == 'Voucher') & (not _c.discoveredand) & (not ((_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area if (_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area else not _c.area)) & G.C.JOKER_GREY) else card & card.debuff & mix_colours()) if (((_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK if (_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK else (_c.unlocked != False) & ((_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) if (_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) else _c.set == 'Voucher') & (not _c.discoveredand) & (not ((_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area if (_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area else not _c.area)) & G.C.JOKER_GREY) if ((_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK if (_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK else (_c.unlocked != False) & ((_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) if (_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) else _c.set == 'Voucher') & (not _c.discoveredand) & (not ((_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area if (_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area else not _c.area)) & G.C.JOKER_GREY) else card & card.debuff & mix_colours()) else (_c.set == 'Joker') & '_c.rarity[G.C.RARITY]') if ((((_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK if (_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK else (_c.unlocked != False) & ((_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) if (_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) else _c.set == 'Voucher') & (not _c.discoveredand) & (not ((_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area if (_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area else not _c.area)) & G.C.JOKER_GREY) if ((_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK if (_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK else (_c.unlocked != False) & ((_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) if (_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) else _c.set == 'Voucher') & (not _c.discoveredand) & (not ((_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area if (_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area else not _c.area)) & G.C.JOKER_GREY) else card & card.debuff & mix_colours()) if (((_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK if (_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK else (_c.unlocked != False) & ((_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) if (_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) else _c.set == 'Voucher') & (not _c.discoveredand) & (not ((_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area if (_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area else not _c.area)) & G.C.JOKER_GREY) if ((_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK if (_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK else (_c.unlocked != False) & ((_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) if (_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) else _c.set == 'Voucher') & (not _c.discoveredand) & (not ((_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area if (_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area else not _c.area)) & G.C.JOKER_GREY) else card & card.debuff & mix_colours()) else (_c.set == 'Joker') & '_c.rarity[G.C.RARITY]') else (_c.set == 'Edition') & G.C.DARK_EDITION) else (_c.set == 'Booster') & G.C.BOOSTER) else '_c.set[G.C.SECONDARY_SET]') if (((((((_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK if (_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK else (_c.unlocked != False) & ((_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) if (_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) else _c.set == 'Voucher') & (not _c.discoveredand) & (not ((_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area if (_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area else not _c.area)) & G.C.JOKER_GREY) if ((_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK if (_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK else (_c.unlocked != False) & ((_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) if (_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) else _c.set == 'Voucher') & (not _c.discoveredand) & (not ((_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area if (_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area else not _c.area)) & G.C.JOKER_GREY) else card & card.debuff & mix_colours()) if (((_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK if (_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK else (_c.unlocked != False) & ((_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) if (_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) else _c.set == 'Voucher') & (not _c.discoveredand) & (not ((_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area if (_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area else not _c.area)) & G.C.JOKER_GREY) if ((_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK if (_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK else (_c.unlocked != False) & ((_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) if (_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) else _c.set == 'Voucher') & (not _c.discoveredand) & (not ((_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area if (_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area else not _c.area)) & G.C.JOKER_GREY) else card & card.debuff & mix_colours()) else (_c.set == 'Joker') & '_c.rarity[G.C.RARITY]') if ((((_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK if (_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK else (_c.unlocked != False) & ((_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) if (_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) else _c.set == 'Voucher') & (not _c.discoveredand) & (not ((_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area if (_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area else not _c.area)) & G.C.JOKER_GREY) if ((_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK if (_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK else (_c.unlocked != False) & ((_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) if (_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) else _c.set == 'Voucher') & (not _c.discoveredand) & (not ((_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area if (_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area else not _c.area)) & G.C.JOKER_GREY) else card & card.debuff & mix_colours()) if (((_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK if (_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK else (_c.unlocked != False) & ((_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) if (_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) else _c.set == 'Voucher') & (not _c.discoveredand) & (not ((_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area if (_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area else not _c.area)) & G.C.JOKER_GREY) if ((_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK if (_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK else (_c.unlocked != False) & ((_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) if (_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) else _c.set == 'Voucher') & (not _c.discoveredand) & (not ((_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area if (_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area else not _c.area)) & G.C.JOKER_GREY) else card & card.debuff & mix_colours()) else (_c.set == 'Joker') & '_c.rarity[G.C.RARITY]') else (_c.set == 'Edition') & G.C.DARK_EDITION) if (((((_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK if (_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK else (_c.unlocked != False) & ((_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) if (_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) else _c.set == 'Voucher') & (not _c.discoveredand) & (not ((_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area if (_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area else not _c.area)) & G.C.JOKER_GREY) if ((_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK if (_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK else (_c.unlocked != False) & ((_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) if (_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) else _c.set == 'Voucher') & (not _c.discoveredand) & (not ((_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area if (_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area else not _c.area)) & G.C.JOKER_GREY) else card & card.debuff & mix_colours()) if (((_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK if (_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK else (_c.unlocked != False) & ((_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) if (_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) else _c.set == 'Voucher') & (not _c.discoveredand) & (not ((_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area if (_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area else not _c.area)) & G.C.JOKER_GREY) if ((_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK if (_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK else (_c.unlocked != False) & ((_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) if (_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) else _c.set == 'Voucher') & (not _c.discoveredand) & (not ((_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area if (_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area else not _c.area)) & G.C.JOKER_GREY) else card & card.debuff & mix_colours()) else (_c.set == 'Joker') & '_c.rarity[G.C.RARITY]') if ((((_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK if (_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK else (_c.unlocked != False) & ((_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) if (_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) else _c.set == 'Voucher') & (not _c.discoveredand) & (not ((_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area if (_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area else not _c.area)) & G.C.JOKER_GREY) if ((_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK if (_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK else (_c.unlocked != False) & ((_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) if (_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) else _c.set == 'Voucher') & (not _c.discoveredand) & (not ((_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area if (_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area else not _c.area)) & G.C.JOKER_GREY) else card & card.debuff & mix_colours()) if (((_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK if (_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK else (_c.unlocked != False) & ((_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) if (_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) else _c.set == 'Voucher') & (not _c.discoveredand) & (not ((_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area if (_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area else not _c.area)) & G.C.JOKER_GREY) if ((_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK if (_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK else (_c.unlocked != False) & ((_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) if (_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) else _c.set == 'Voucher') & (not _c.discoveredand) & (not ((_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area if (_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area else not _c.area)) & G.C.JOKER_GREY) else card & card.debuff & mix_colours()) else (_c.set == 'Joker') & '_c.rarity[G.C.RARITY]') else (_c.set == 'Edition') & G.C.DARK_EDITION) else (_c.set == 'Booster') & G.C.BOOSTER) if ((((((_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK if (_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK else (_c.unlocked != False) & ((_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) if (_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) else _c.set == 'Voucher') & (not _c.discoveredand) & (not ((_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area if (_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area else not _c.area)) & G.C.JOKER_GREY) if ((_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK if (_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK else (_c.unlocked != False) & ((_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) if (_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) else _c.set == 'Voucher') & (not _c.discoveredand) & (not ((_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area if (_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area else not _c.area)) & G.C.JOKER_GREY) else card & card.debuff & mix_colours()) if (((_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK if (_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK else (_c.unlocked != False) & ((_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) if (_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) else _c.set == 'Voucher') & (not _c.discoveredand) & (not ((_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area if (_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area else not _c.area)) & G.C.JOKER_GREY) if ((_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK if (_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK else (_c.unlocked != False) & ((_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) if (_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) else _c.set == 'Voucher') & (not _c.discoveredand) & (not ((_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area if (_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area else not _c.area)) & G.C.JOKER_GREY) else card & card.debuff & mix_colours()) else (_c.set == 'Joker') & '_c.rarity[G.C.RARITY]') if ((((_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK if (_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK else (_c.unlocked != False) & ((_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) if (_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) else _c.set == 'Voucher') & (not _c.discoveredand) & (not ((_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area if (_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area else not _c.area)) & G.C.JOKER_GREY) if ((_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK if (_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK else (_c.unlocked != False) & ((_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) if (_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) else _c.set == 'Voucher') & (not _c.discoveredand) & (not ((_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area if (_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area else not _c.area)) & G.C.JOKER_GREY) else card & card.debuff & mix_colours()) if (((_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK if (_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK else (_c.unlocked != False) & ((_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) if (_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) else _c.set == 'Voucher') & (not _c.discoveredand) & (not ((_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area if (_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area else not _c.area)) & G.C.JOKER_GREY) if ((_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK if (_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK else (_c.unlocked != False) & ((_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) if (_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) else _c.set == 'Voucher') & (not _c.discoveredand) & (not ((_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area if (_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area else not _c.area)) & G.C.JOKER_GREY) else card & card.debuff & mix_colours()) else (_c.set == 'Joker') & '_c.rarity[G.C.RARITY]') else (_c.set == 'Edition') & G.C.DARK_EDITION) if (((((_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK if (_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK else (_c.unlocked != False) & ((_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) if (_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) else _c.set == 'Voucher') & (not _c.discoveredand) & (not ((_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area if (_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area else not _c.area)) & G.C.JOKER_GREY) if ((_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK if (_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK else (_c.unlocked != False) & ((_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) if (_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) else _c.set == 'Voucher') & (not _c.discoveredand) & (not ((_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area if (_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area else not _c.area)) & G.C.JOKER_GREY) else card & card.debuff & mix_colours()) if (((_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK if (_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK else (_c.unlocked != False) & ((_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) if (_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) else _c.set == 'Voucher') & (not _c.discoveredand) & (not ((_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area if (_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area else not _c.area)) & G.C.JOKER_GREY) if ((_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK if (_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK else (_c.unlocked != False) & ((_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) if (_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) else _c.set == 'Voucher') & (not _c.discoveredand) & (not ((_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area if (_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area else not _c.area)) & G.C.JOKER_GREY) else card & card.debuff & mix_colours()) else (_c.set == 'Joker') & '_c.rarity[G.C.RARITY]') if ((((_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK if (_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK else (_c.unlocked != False) & ((_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) if (_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) else _c.set == 'Voucher') & (not _c.discoveredand) & (not ((_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area if (_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area else not _c.area)) & G.C.JOKER_GREY) if ((_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK if (_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK else (_c.unlocked != False) & ((_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) if (_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) else _c.set == 'Voucher') & (not _c.discoveredand) & (not ((_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area if (_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area else not _c.area)) & G.C.JOKER_GREY) else card & card.debuff & mix_colours()) if (((_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK if (_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK else (_c.unlocked != False) & ((_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) if (_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) else _c.set == 'Voucher') & (not _c.discoveredand) & (not ((_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area if (_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area else not _c.area)) & G.C.JOKER_GREY) if ((_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK if (_c.unlocked == False) & (not card & card.bypass_lock) & G.C.BLACK else (_c.unlocked != False) & ((_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) if (_c.set == 'Joker' if _c.set == 'Joker' else _c.consumeable) else _c.set == 'Voucher') & (not _c.discoveredand) & (not ((_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area if (_c.area != G.jokers) & (_c.area != G.consumeables) & _c.area else not _c.area)) & G.C.JOKER_GREY) else card & card.debuff & mix_colours()) else (_c.set == 'Joker') & '_c.rarity[G.C.RARITY]') else (_c.set == 'Edition') & G.C.DARK_EDITION) else (_c.set == 'Booster') & G.C.BOOSTER) else '_c.set]) else {1: 0, 2: 1, 3: 1, 4: 1}
def generate_card_ui(_c, full_UI_table, specific_vars, card_type, badges, hide_desc, main_start, main_end):
    first_pass = 'None'
    if not full_UI_table:
        first_pass = True
        full_UI_table = {'main': {}, 'info': {}, 'type': {}, 'name': 'None', 'badges': badges if badges else {}}
    desc_nodes = (not full_UI_table.name) & full_UI_table.main if (not full_UI_table.name) & full_UI_table.main else full_UI_table.info
    name_override = 'None'
    info_queue = {}
    if full_UI_table.name:
        full_UI_table.info[#full_UI_table.info + 1] = {}
        desc_nodes = full_UI_table.info[#full_UI_table.info + 1]
    if not full_UI_table.name:
        if specific_vars & specific_vars.no_name:
            full_UI_table.name = True
        elif card_type == 'Locked':
            full_UI_table.name = localize()
        elif card_type == 'Undiscovered':
            full_UI_table.name = localize()
        elif specific_vars & (card_type == 'Default' if card_type == 'Default' else card_type == 'Enhanced'):
            if _c.name == 'Stone Card':
                full_UI_table.name = True
            if specific_vars.playing_card & (_c.name != 'Stone Card'):
                full_UI_table.name = {}localize()
                full_UI_table.name = full_UI_table.info[#full_UI_table.info + 1]
        elif card_type == 'Booster':
        else:
            full_UI_table.name = localize()
        full_UI_table.card_type = card_type if card_type else _c.set
    loc_vars = {}
    if main_start:
        full_UI_table.info[#full_UI_table.info + 1] = main_start
    if _c.set == 'Other':localize()
    elif card_type == 'Locked':
        if _c.wip:localize()
        elif _c.demo & specific_vars:localize()
        elif _c.demo:localize()
        else:
            if _c.name == 'Golden Ticket':
            elif _c.name == 'Mr. Bones':
                loc_vars = {1: _c.unlock_condition.extra, 2: full_UI_table.info[#full_UI_table.info + 1].career_stats.c_losses}
            elif _c.name == 'Acrobat':
                loc_vars = {1: _c.unlock_condition.extra, 2: full_UI_table.info[#full_UI_table.info + 1].career_stats.c_hands_played}
            elif _c.name == 'Sock and Buskin':
                loc_vars = {1: _c.unlock_condition.extra, 2: full_UI_table.info[#full_UI_table.info + 1].career_stats.c_face_cards_played}
            elif _c.name == 'Swashbuckler':
                loc_vars = {1: _c.unlock_condition.extra, 2: full_UI_table.info[#full_UI_table.info + 1].career_stats.c_jokers_sold}
            elif _c.name == 'Troubadour':
                loc_vars = {1: _c.unlock_condition.extra}
            elif _c.name == 'Certificate':
            elif _c.name == 'Smeared Joker':
                loc_vars = {1: _c.unlock_condition.extra.count, 2: localize()}
            elif _c.name == 'Throwback':
            elif _c.name == 'Hanging Chad':
                loc_vars = {1: localize()}
            elif _c.name == 'Rough Gem':
                loc_vars = {1: _c.unlock_condition.extra.count, 2: localize()}
            elif _c.name == 'Bloodstone':
                loc_vars = {1: _c.unlock_condition.extra.count, 2: localize()}
            elif _c.name == 'Arrowhead':
                loc_vars = {1: _c.unlock_condition.extra.count, 2: localize()}
            elif _c.name == 'Onyx Agate':
                loc_vars = {1: _c.unlock_condition.extra.count, 2: localize()}
            elif _c.name == 'Glass Joker':
                loc_vars = {1: _c.unlock_condition.extra.count, 2: localize()}
            elif _c.name == 'Showman':
                loc_vars = {1: _c.unlock_condition.ante}
            elif _c.name == 'Flower Pot':
                loc_vars = {1: _c.unlock_condition.ante}
            elif _c.name == 'Blueprint':
            elif _c.name == 'Wee Joker':
                loc_vars = {1: _c.unlock_condition.n_rounds}
            elif _c.name == 'Merry Andy':
                loc_vars = {1: _c.unlock_condition.n_rounds}
            elif _c.name == 'Oops! All 6s':
                loc_vars = {1: number_format()}
            elif _c.name == 'The Idol':
                loc_vars = {1: number_format()}
            elif _c.name == 'Seeing Double':
                loc_vars = {1: localize(ph_4_7_of_clubs)}
            elif _c.name == 'Matador':
            elif _c.name == 'Hit the Road':
            elif _c.name == 'The Duo':
                loc_vars = {1: localize()}
            elif _c.name == 'The Trio':
                loc_vars = {1: localize()}
            elif _c.name == 'The Family':
                loc_vars = {1: localize()}
            elif _c.name == 'The Order':
                loc_vars = {1: localize()}
            elif _c.name == 'The Tribe':
                loc_vars = {1: localize()}
            elif _c.name == 'Stuntman':
                loc_vars = {1: number_format()}
            elif _c.name == 'Invisible Joker':
            elif _c.name == 'Brainstorm':
            elif _c.name == 'Satellite':
                loc_vars = {1: _c.unlock_condition.extra}
            elif _c.name == 'Shoot the Moon':
            elif _c.name == "Driver's License":
                loc_vars = {1: _c.unlock_condition.extra.count}
            elif _c.name == 'Cartomancer':
                loc_vars = {1: _c.unlock_condition.tarot_count}
            elif _c.name == 'Astronomer':
            elif _c.name == 'Burnt Joker':
                loc_vars = {1: _c.unlock_condition.extra, 2: full_UI_table.info[#full_UI_table.info + 1].career_stats.c_cards_sold}
            elif _c.name == 'Bootstraps':
                loc_vars = {1: _c.unlock_condition.extra.count}
            elif _c.name == 'Overstock Plus':
                loc_vars = {1: _c.unlock_condition.extra, 2: full_UI_table.info[#full_UI_table.info + 1].career_stats.c_shop_dollars_spent}
            elif _c.name == 'Liquidation':
                loc_vars = {1: _c.unlock_condition.extra}
            elif _c.name == 'Tarot Tycoon':
                loc_vars = {1: _c.unlock_condition.extra, 2: full_UI_table.info[#full_UI_table.info + 1].career_stats.c_tarots_bought}
            elif _c.name == 'Planet Tycoon':
                loc_vars = {1: _c.unlock_condition.extra, 2: full_UI_table.info[#full_UI_table.info + 1].career_stats.c_planets_bought}
            elif _c.name == 'Glow Up':
                loc_vars = {1: _c.unlock_condition.extra}
            elif _c.name == 'Reroll Glut':
                loc_vars = {1: _c.unlock_condition.extra, 2: full_UI_table.info[#full_UI_table.info + 1].career_stats.c_shop_rerolls}
            elif _c.name == 'Omen Globe':
                loc_vars = {1: _c.unlock_condition.extra, 2: full_UI_table.info[#full_UI_table.info + 1].career_stats.c_tarot_reading_used}
            elif _c.name == 'Observatory':
                loc_vars = {1: _c.unlock_condition.extra, 2: full_UI_table.info[#full_UI_table.info + 1].career_stats.c_planetarium_used}
            elif _c.name == 'Nacho Tong':
                loc_vars = {1: _c.unlock_condition.extra, 2: full_UI_table.info[#full_UI_table.info + 1].career_stats.c_cards_played}
            elif _c.name == 'Recyclomancy':
                loc_vars = {1: _c.unlock_condition.extra, 2: full_UI_table.info[#full_UI_table.info + 1].career_stats.c_cards_discarded}
            elif _c.name == 'Money Tree':
                loc_vars = {1: _c.unlock_condition.extra, 2: full_UI_table.info[#full_UI_table.info + 1].career_stats.c_round_interest_cap_streak}
            elif _c.name == 'Antimatter':
                loc_vars = {1: _c.unlock_condition.extra, 2: full_UI_table.info[#full_UI_table.info + 1].voucher_usage.v_blank.count else 0}
            elif _c.name == 'Illusion':
                loc_vars = {1: _c.unlock_condition.extra, 2: full_UI_table.info[#full_UI_table.info + 1].career_stats.c_playing_cards_bought}
            elif _c.name == 'Petroglyph':
                loc_vars = {1: _c.unlock_condition.extra}
            elif _c.name == 'Retcon':
                loc_vars = {1: _c.unlock_condition.extra}
            elif _c.name == 'Palette':
                loc_vars = {1: _c.unlock_condition.extra}
            if _c.rarity & (_c.rarity == 4) & specific_vars & (not specific_vars.not_hidden):localize()
            else:localize()
    elif hide_desc:localize()
    elif specific_vars & specific_vars.debuffed:localize()
    elif _c.set == 'Joker':
        if _c.name == 'Stone Joker' if _c.name == 'Stone Joker' else _c.name == 'Marble Joker':
            full_UI_table.info[#full_UI_table.info + 1] = G.P_CENTERS.m_stone
        elif _c.name == 'Steel Joker':
            full_UI_table.info[#full_UI_table.info + 1] = G.P_CENTERS.m_steel
        elif _c.name == 'Glass Joker':
            full_UI_table.info[#full_UI_table.info + 1] = G.P_CENTERS.m_glass
        elif _c.name == 'Golden Ticket':
            full_UI_table.info[#full_UI_table.info + 1] = G.P_CENTERS.m_gold
        elif _c.name == 'Lucky Cat':
            full_UI_table.info[#full_UI_table.info + 1] = G.P_CENTERS.m_lucky
        elif _c.name == 'Midas Mask':
            full_UI_table.info[#full_UI_table.info + 1] = G.P_CENTERS.m_gold
        elif _c.name == 'Invisible Joker':
            if G.jokers & G.jokers.cards:
                for kv in ipairs():
                    if v.edition & v.edition.negative & G.localization.descriptions.Other.remove_negative:
                        main_end = {}localize()
                        main_end = full_UI_table.info[#full_UI_table.info + 1]
                        break
        elif _c.name == 'Diet Cola':
            full_UI_table.info[#full_UI_table.info + 1] = {'key': 'tag_double', 'set': 'Tag'}
        elif _c.name == 'Perkeo':
            full_UI_table.info[#full_UI_table.info + 1] = {'key': 'e_negative_consumable', 'set': 'Edition', 'config': {'extra': 1}}
        if specific_vars & specific_vars.pinned:
            full_UI_table.info[#full_UI_table.info + 1] = {'key': 'pinned_left', 'set': 'Other'}
        if specific_vars & specific_vars.sticker:
            full_UI_table.info[#full_UI_table.info + 1] = {'key': string.lower() + '_sticker', 'set': 'Other'}localize()
    elif _c.set == 'Tag':
        if _c.name == 'Negative Tag':
            full_UI_table.info[#full_UI_table.info + 1] = G.P_CENTERS.e_negative
        elif _c.name == 'Foil Tag':
            full_UI_table.info[#full_UI_table.info + 1] = G.P_CENTERS.e_foil
        elif _c.name == 'Holographic Tag':
            full_UI_table.info[#full_UI_table.info + 1] = G.P_CENTERS.e_holo
        elif _c.name == 'Polychrome Tag':
            full_UI_table.info[#full_UI_table.info + 1] = G.P_CENTERS.e_polychrome
        elif _c.name == 'Charm Tag':
            full_UI_table.info[#full_UI_table.info + 1] = G.P_CENTERS.p_arcana_mega_1
        elif _c.name == 'Meteor Tag':
            full_UI_table.info[#full_UI_table.info + 1] = G.P_CENTERS.p_celestial_mega_1
        elif _c.name == 'Ethereal Tag':
            full_UI_table.info[#full_UI_table.info + 1] = G.P_CENTERS.p_spectral_normal_1
        elif _c.name == 'Standard Tag':
            full_UI_table.info[#full_UI_table.info + 1] = G.P_CENTERS.p_standard_mega_1
        elif _c.name == 'Buffoon Tag':
            full_UI_table.info[#full_UI_table.info + 1] = G.P_CENTERS.p_buffoon_mega_1localize()
    elif _c.set == 'Voucher':
        if _c.name == 'Overstock' if _c.name == 'Overstock' else _c.name == 'Overstock Plus':
        elif _c.name == 'Tarot Merchant' if _c.name == 'Tarot Merchant' else _c.name == 'Tarot Tycoon':
            loc_vars = {1: _c.config.extra_disp}
        elif _c.name == 'Planet Merchant' if _c.name == 'Planet Merchant' else _c.name == 'Planet Tycoon':
            loc_vars = {1: _c.config.extra_disp}
        elif _c.name == 'Hone' if _c.name == 'Hone' else _c.name == 'Glow Up':
            loc_vars = {1: _c.config.extra}
        elif _c.name == 'Reroll Surplus' if _c.name == 'Reroll Surplus' else _c.name == 'Reroll Glut':
            loc_vars = {1: _c.config.extra}
        elif _c.name == 'Grabber' if _c.name == 'Grabber' else _c.name == 'Nacho Tong':
            loc_vars = {1: _c.config.extra}
        elif _c.name == 'Wasteful' if _c.name == 'Wasteful' else _c.name == 'Recyclomancy':
            loc_vars = {1: _c.config.extra}
        elif _c.name == 'Seed Money' if _c.name == 'Seed Money' else _c.name == 'Money Tree':
            loc_vars = {1: _c.config.extra / 5}
        elif _c.name == 'Blank' if _c.name == 'Blank' else _c.name == 'Antimatter':
        elif _c.name == 'Hieroglyph' if _c.name == 'Hieroglyph' else _c.name == 'Petroglyph':
            loc_vars = {1: _c.config.extra}
        elif _c.name == "Director's Cut" if _c.name == "Director's Cut" else _c.name == 'Retcon':
            loc_vars = {1: _c.config.extra}
        elif _c.name == 'Paint Brush' if _c.name == 'Paint Brush' else _c.name == 'Palette':
            loc_vars = {1: _c.config.extra}
        elif _c.name == 'Telescope' if _c.name == 'Telescope' else _c.name == 'Observatory':
            loc_vars = {1: _c.config.extra}
        elif _c.name == 'Clearance Sale' if _c.name == 'Clearance Sale' else _c.name == 'Liquidation':
            loc_vars = {1: _c.config.extra}localize()
    elif _c.set == 'Edition':
        loc_vars = {1: _c.config.extra}localize()
    elif (_c.set == 'Default') & specific_vars:
        if specific_vars.nominal_chips:localize()
        if specific_vars.bonus_chips:localize()
    elif _c.set == 'Enhanced':
        if specific_vars & (_c.name != 'Stone Card') & specific_vars.nominal_chips:localize()
        if _c.effect == 'Mult Card':
            loc_vars = {1: _c.config.mult}
        elif _c.effect == 'Wild Card':
        elif _c.effect == 'Glass Card':
            loc_vars = {1: _c.config.Xmult, 2: G.GAME.probabilities.normal, 3: _c.config.extra}
        elif _c.effect == 'Steel Card':
            loc_vars = {1: _c.config.h_x_mult}
        elif _c.effect == 'Stone Card':
            loc_vars = {1: specific_vars & specific_vars.bonus_chips if specific_vars & specific_vars.bonus_chips else _c.config.bonus}
        elif _c.effect == 'Gold Card':
            loc_vars = {1: _c.config.h_dollars}
        elif _c.effect == 'Lucky Card':
            loc_vars = {1: G.GAME.probabilities.normal, 2: _c.config.mult, 3: 5, 4: _c.config.p_dollars, 5: 15}localize()
        if (_c.name != 'Stone Card') & (specific_vars & specific_vars.bonus_chips if specific_vars & specific_vars.bonus_chips else _c.config.bonus):localize()
    elif _c.set == 'Booster':
        desc_override = 'p_arcana_normal'
        if _c.name == 'Arcana Pack':
            desc_override = 'p_arcana_normal'';'
            loc_vars = {1: _c.config.choose, 2: _c.config.extra}
        elif _c.name == 'Jumbo Arcana Pack':
            desc_override = 'p_arcana_jumbo'';'
            loc_vars = {1: _c.config.choose, 2: _c.config.extra}
        elif _c.name == 'Mega Arcana Pack':
            desc_override = 'p_arcana_mega'';'
            loc_vars = {1: _c.config.choose, 2: _c.config.extra}
        elif _c.name == 'Celestial Pack':
            desc_override = 'p_celestial_normal'';'
            loc_vars = {1: _c.config.choose, 2: _c.config.extra}
        elif _c.name == 'Jumbo Celestial Pack':
            desc_override = 'p_celestial_jumbo'';'
            loc_vars = {1: _c.config.choose, 2: _c.config.extra}
        elif _c.name == 'Mega Celestial Pack':
            desc_override = 'p_celestial_mega'';'
            loc_vars = {1: _c.config.choose, 2: _c.config.extra}
        elif _c.name == 'Spectral Pack':
            desc_override = 'p_spectral_normal'';'
            loc_vars = {1: _c.config.choose, 2: _c.config.extra}
        elif _c.name == 'Jumbo Spectral Pack':
            desc_override = 'p_spectral_jumbo'';'
            loc_vars = {1: _c.config.choose, 2: _c.config.extra}
        elif _c.name == 'Mega Spectral Pack':
            desc_override = 'p_spectral_mega'';'
            loc_vars = {1: _c.config.choose, 2: _c.config.extra}
        elif _c.name == 'Standard Pack':
            desc_override = 'p_standard_normal'';'
            loc_vars = {1: _c.config.choose, 2: _c.config.extra}
        elif _c.name == 'Jumbo Standard Pack':
            desc_override = 'p_standard_jumbo'';'
            loc_vars = {1: _c.config.choose, 2: _c.config.extra}
        elif _c.name == 'Mega Standard Pack':
            desc_override = 'p_standard_mega'';'
            loc_vars = {1: _c.config.choose, 2: _c.config.extra}
        elif _c.name == 'Buffoon Pack':
            desc_override = 'p_buffoon_normal'';'
            loc_vars = {1: _c.config.choose, 2: _c.config.extra}
        elif _c.name == 'Jumbo Buffoon Pack':
            desc_override = 'p_buffoon_jumbo'';'
            loc_vars = {1: _c.config.choose, 2: _c.config.extra}
        elif _c.name == 'Mega Buffoon Pack':
            desc_override = 'p_buffoon_mega'';'
            loc_vars = {1: _c.config.choose, 2: _c.config.extra}
        name_override = desc_override
        if not full_UI_table.name:
            full_UI_table.name = localize()localize()
    elif _c.set == 'Spectral':
        if (_c.name == 'Familiar' if _c.name == 'Familiar' else _c.name == 'Grim') if (_c.name == 'Familiar' if _c.name == 'Familiar' else _c.name == 'Grim') else _c.name == 'Incantation':
            loc_vars = {1: _c.config.extra}
        elif _c.name == 'Immolate':
            loc_vars = {1: _c.config.extra.destroy, 2: _c.config.extra.dollars}
        elif _c.name == 'Hex':
            full_UI_table.info[#full_UI_table.info + 1] = G.P_CENTERS.e_polychrome
        elif _c.name == 'Talisman':
            full_UI_table.info[#full_UI_table.info + 1] = {'key': 'gold_seal', 'set': 'Other'}
        elif _c.name == 'Deja Vu':
            full_UI_table.info[#full_UI_table.info + 1] = {'key': 'red_seal', 'set': 'Other'}
        elif _c.name == 'Trance':
            full_UI_table.info[#full_UI_table.info + 1] = {'key': 'blue_seal', 'set': 'Other'}
        elif _c.name == 'Medium':
            full_UI_table.info[#full_UI_table.info + 1] = {'key': 'purple_seal', 'set': 'Other'}
        elif _c.name == 'Ankh':
            if G.jokers & G.jokers.cards:
                for kv in ipairs():
                    if v.edition & v.edition.negative & G.localization.descriptions.Other.remove_negative:
                        full_UI_table.info[#full_UI_table.info + 1] = G.P_CENTERS.e_negative
                        main_end = {}localize()
                        main_end = full_UI_table.info[#full_UI_table.info + 1]
                        break
        elif _c.name == 'Cryptid':
            loc_vars = {1: _c.config.extra}
        if _c.name == 'Ectoplasm':
            full_UI_table.info[#full_UI_table.info + 1] = G.P_CENTERS.e_negative';'
            loc_vars = {1: G.GAME.ecto_minus if G.GAME.ecto_minus else 1}
        if _c.name == 'Aura':
            full_UI_table.info[#full_UI_table.info + 1] = G.P_CENTERS.e_foil
            full_UI_table.info[#full_UI_table.info + 1] = G.P_CENTERS.e_holo
            full_UI_table.info[#full_UI_table.info + 1] = G.P_CENTERS.e_polychromelocalize()
    elif _c.set == 'Planet':
        loc_vars = {1: full_UI_table.info[#full_UI_table.info + 1]}}localize()
    elif _c.set == 'Tarot':
        if _c.name == 'The Fool':
            fool_c = G.GAME.last_tarot_planet & full_UI_table.info[#full_UI_table.info + 1] else 'None'
            last_tarot_planet = fool_c & localize() if fool_c & localize() else localize(k_none)
            colour = (not fool_c if not fool_c else fool_c.name == 'The Fool') & G.C.RED if (not fool_c if not fool_c else fool_c.name == 'The Fool') & G.C.RED else G.C.GREEN
            main_end = {1: {'n': G.UIT.C, 'config': {'align': 'bm', 'padding': 0.02}, 'nodes': {1: {'n': G.UIT.C, 'config': {'align': 'm', 'colour': colour, 'r': 0.05, 'padding': 0.05}, 'nodes': {1: {'n': G.UIT.T, 'config': {'text': ' ' + last_tarot_planet + ' ', 'colour': G.C.UI.TEXT_LIGHT, 'scale': 0.3, 'shadow': True}}}}}}}
            loc_vars = {1: last_tarot_planet}
            if not (not fool_c if not fool_c else fool_c.name == 'The Fool'):
                full_UI_table.info[#full_UI_table.info + 1] = fool_c
        elif _c.name == 'The Magician':
            loc_vars = {1: _c.config.max_highlighted, 2: localize()}';'
            full_UI_table.info[#full_UI_table.info + 1]
        elif _c.name == 'The High Priestess':
            loc_vars = {1: _c.config.planets}
        elif _c.name == 'The Empress':
            loc_vars = {1: _c.config.max_highlighted, 2: localize()}';'
            full_UI_table.info[#full_UI_table.info + 1]
        elif _c.name == 'The Emperor':
            loc_vars = {1: _c.config.tarots}
        elif _c.name == 'The Hierophant':
            loc_vars = {1: _c.config.max_highlighted, 2: localize()}';'
            full_UI_table.info[#full_UI_table.info + 1]
        elif _c.name == 'The Lovers':
            loc_vars = {1: _c.config.max_highlighted, 2: localize()}';'
            full_UI_table.info[#full_UI_table.info + 1]
        elif _c.name == 'The Chariot':
            loc_vars = {1: _c.config.max_highlighted, 2: localize()}';'
            full_UI_table.info[#full_UI_table.info + 1]
        elif _c.name == 'Justice':
            loc_vars = {1: _c.config.max_highlighted, 2: localize()}';'
            full_UI_table.info[#full_UI_table.info + 1]
        elif _c.name == 'The Hermit':
            loc_vars = {1: _c.config.extra}
        elif _c.name == 'The Wheel of Fortune':
            loc_vars = {1: G.GAME.probabilities.normal, 2: _c.config.extra}';'
            full_UI_table.info[#full_UI_table.info + 1] = G.P_CENTERS.e_foil';'
            full_UI_table.info[#full_UI_table.info + 1] = G.P_CENTERS.e_holo';'
            full_UI_table.info[#full_UI_table.info + 1] = G.P_CENTERS.e_polychrome';'
        elif _c.name == 'Strength':
            loc_vars = {1: _c.config.max_highlighted}
        elif _c.name == 'The Hanged Man':
            loc_vars = {1: _c.config.max_highlighted}
        elif _c.name == 'Death':
            loc_vars = {1: _c.config.max_highlighted}
        elif _c.name == 'Temperance':
            _money = 0
            if G.jokers:
                for i in range(1, len(G.jokers.cards), ):
                    if full_UI_table.info[#full_UI_table.info + 1].ability.set == 'Joker':
                        _money = _money + full_UI_table.info[#full_UI_table.info + 1].sell_cost
            loc_vars = {1: _c.config.extra, 2: math.min()}
        elif _c.name == 'The Devil':
            loc_vars = {1: _c.config.max_highlighted, 2: localize()}';'
            full_UI_table.info[#full_UI_table.info + 1]
        elif _c.name == 'The Tower':
            loc_vars = {1: _c.config.max_highlighted, 2: localize()}';'
            full_UI_table.info[#full_UI_table.info + 1]
        elif _c.name == 'The Star':
            loc_vars = {1: _c.config.max_highlighted, 2: localize(), full_UI_table.info[#full_UI_table.info + 1]}}
        elif _c.name == 'The Moon':
            loc_vars = {1: _c.config.max_highlighted, 2: localize(), full_UI_table.info[#full_UI_table.info + 1]}}
        elif _c.name == 'The Sun':
            loc_vars = {1: _c.config.max_highlighted, 2: localize(), full_UI_table.info[#full_UI_table.info + 1]}}
        elif _c.name == 'Judgement':
        elif _c.name == 'The World':
            loc_vars = {1: _c.config.max_highlighted, 2: localize(), full_UI_table.info[#full_UI_table.info + 1]}}localize()
    if main_end:
        full_UI_table.info[#full_UI_table.info + 1] = main_end
    if not specific_vars & (not specific_vars.sticker) & (card_type == 'Default' if card_type == 'Default' else card_type == 'Enhanced'):
        if (desc_nodes == full_UI_table.main) & (not full_UI_table.name):localize()
            if not full_UI_table.name:
                full_UI_table.name = {}
        elif desc_nodes != full_UI_table.main:
            desc_nodes.name = localize()
    if first_pass & (not _c.set == 'Edition') & badges:
        for kv in ipairs(badges):
            if v == 'foil':
                full_UI_table.info[#full_UI_table.info + 1] = "'e_foil'[G.P_CENTERS]"
            if v == 'holographic':
                full_UI_table.info[#full_UI_table.info + 1] = "'e_holo'[G.P_CENTERS]"
            if v == 'polychrome':
                full_UI_table.info[#full_UI_table.info + 1] = "'e_polychrome'[G.P_CENTERS]"
            if v == 'negative':
                full_UI_table.info[#full_UI_table.info + 1] = "'e_negative'[G.P_CENTERS]"
            if v == 'negative_consumable':
                full_UI_table.info[#full_UI_table.info + 1] = {'key': 'e_negative_consumable', 'set': 'Edition', 'config': {'extra': 1}}
            if v == 'gold_seal':
                full_UI_table.info[#full_UI_table.info + 1] = {'key': 'gold_seal', 'set': 'Other'}
            if v == 'blue_seal':
                full_UI_table.info[#full_UI_table.info + 1] = {'key': 'blue_seal', 'set': 'Other'}
            if v == 'red_seal':
                full_UI_table.info[#full_UI_table.info + 1] = {'key': 'red_seal', 'set': 'Other'}
            if v == 'purple_seal':
                full_UI_table.info[#full_UI_table.info + 1] = {'key': 'purple_seal', 'set': 'Other'}
            if v == 'eternal':
                full_UI_table.info[#full_UI_table.info + 1] = {'key': 'eternal', 'set': 'Other'}
            if v == 'perishable':
                full_UI_table.info[#full_UI_table.info + 1] = {'key': 'perishable', 'set': 'Other', 'vars': {1: G.GAME.perishable_rounds if G.GAME.perishable_rounds else 1, 2: specific_vars.perish_tally if specific_vars.perish_tally else G.GAME.perishable_rounds}}
            if v == 'rental':
                full_UI_table.info[#full_UI_table.info + 1] = {'key': 'rental', 'set': 'Other', 'vars': {1: G.GAME.rental_rate if G.GAME.rental_rate else 1}}
            if v == 'pinned_left':
                full_UI_table.info[#full_UI_table.info + 1] = {'key': 'pinned_left', 'set': 'Other'}
    for _v in ipairs(info_queue):generate_card_ui(v, full_UI_table)
    return full_UI_table