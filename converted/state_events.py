def win_game():
    if (not G.GAME.seeded) & (not G.GAME.challenge):set_joker_win()set_deck_win()check_and_set_high_score(win_streak)check_and_set_high_score(current_streak)check_for_unlock()check_for_unlock()check_for_unlock()check_for_unlock()check_for_unlock()check_for_unlock()inc_career_stat(c_wins, 1)set_profile_progress()
    if G.GAME.challenge:
        'G.GAME.challenge[G.PROFILES[G.SETTINGS.profile].challenge_progress.completed]' = Trueset_challenge_unlock()check_for_unlock()G.save_settings()G.E_MANAGER.add_event()
    if (not G.GAME.seeded) & (not G.GAME.challenge):
        'G.SETTINGS.profile[G.PROFILES]'.stake = math.max()G.save_progress()
    G.FILE_HANDLER.force = TrueG.E_MANAGER.add_event()
def end_round():G.E_MANAGER.add_event()
def new_round():
    G.RESET_JIGGLES = 'None'delay(0.4)G.E_MANAGER.add_event()
G.FUNCS.draw_from_deck_to_hand = lambda e: 
if (not (G.STATE == G.STATES.TAROT_PACK if G.STATE == G.STATES.TAROT_PACK else G.STATE == G.STATES.SPECTRAL_PACK)) & (G.hand.config.card_limit <= 0) & len(G.hand.cards == 0):
    G.STATE = G.STATES.GAME_OVER';'
    G.STATE_COMPLETE = False
    return True
hand_space = e if e else math.min()
if (G.GAME.blind.name == 'The Serpent') & (not G.GAME.blind.disabled) & (G.GAME.current_round.hands_played > 0 if G.GAME.current_round.hands_played > 0 else G.GAME.current_round.discards_used > 0):
    hand_space = math.min()delay(0.3)
for i in range(1, hand_space, ):
    if G.STATE == G.STATES.TAROT_PACK if G.STATE == G.STATES.TAROT_PACK else G.STATE == G.STATES.SPECTRAL_PACK:draw_card()
    else:draw_card()
G.FUNCS.discard_cards_from_highlighted = lambda ehook: stop_use()
G.CONTROLLER.interrupt.focus = TrueG.CONTROLLER.save_cardarea_focus(hand)
for kv in ipairs():
    v.ability.forced_selection = 'None'
if G.CONTROLLER.focused.target & (G.CONTROLLER.focused.target.area == G.hand):
    G.card_area_focus_reset = {'area': G.hand, 'rank': G.CONTROLLER.focused.target.rank}
highlighted_count = math.min()
if highlighted_count > 0:update_hand_text()table.sort()inc_career_stat(c_cards_discarded, highlighted_count)
    for j in range(1, len(G.jokers.cards), ):'j[G.jokers.cards]'.calculate_joker()
    cards = {}
    destroyed_cards = {}
    for i in range(1, highlighted_count, ):'i[G.hand.highlighted]'.calculate_seal()
        removed = False
        for j in range(1, len(G.jokers.cards), ):
            eval = 'None'
            eval = 'j[G.jokers.cards]'.calculate_joker()
            if eval:
                if eval.remove:
                    removed = Truecard_eval_status_text(j[G.jokers.cards], jokers, None, 1, None, eval)table.insert(cards, i[G.hand.highlighted])
        if removed:
            '#destroyed_cards + 1[destroyed_cards]' = 'i[G.hand.highlighted]'
            if 'i[G.hand.highlighted]'.ability.name == 'Glass Card':'i[G.hand.highlighted]'.shatter()
            else:'i[G.hand.highlighted]'.start_dissolve()
        else:
            'i[G.hand.highlighted]'.ability.discarded = Truedraw_card()
    if '1[destroyed_cards]':
        for j in range(1, len(G.jokers.cards), ):eval_card(j[G.jokers.cards])
    G.GAME.round_scores.cards_discarded.amt = G.GAME.round_scores.cards_discarded.amt + len(cards)check_for_unlock()
    if not hook:
        if G.GAME.modifiers.discard_cost:ease_dollars()ease_discard()
        G.GAME.current_round.discards_used = G.GAME.current_round.discards_used + 1
        G.STATE = G.STATES.DRAW_TO_HANDG.E_MANAGER.add_event()
G.FUNCS.play_cards_from_highlighted = lambda e: 
if G.play & '1[G.play.cards]':
    return Falsestop_use()
G.GAME.blind.triggered = False
G.CONTROLLER.interrupt.focus = TrueG.CONTROLLER.save_cardarea_focus(hand)
for kv in ipairs():
    v.ability.forced_selection = 'None'table.sort()G.E_MANAGER.add_event()inc_career_stat(c_cards_played)inc_career_stat(c_hands_played, 1)ease_hands_played()delay(0.4)
for i in range(1, len(G.hand.highlighted), ):
    if 'i[G.hand.highlighted]'.is_face():inc_career_stat(c_face_cards_played, 1)
    'i[G.hand.highlighted]'.base.times_played = 'i[G.hand.highlighted]'.base.times_played + 1
    'i[G.hand.highlighted]'.ability.played_this_ante = True
    G.GAME.round_scores.cards_played.amt = G.GAME.round_scores.cards_played.amt + 1draw_card()check_for_unlock()
if G.GAME.blind.press_play():G.E_MANAGER.add_event()delay(0.4)G.E_MANAGER.add_event()
G.FUNCS.get_poker_hand_info = lambda _cards: 
poker_hands = evaluate_poker_hand(_cards)
scoring_hand = {}
text = disp_text = loc_disp_text = ('NULL', 'NULL', 'NULL')
if next("Flush Five"[poker_hands]):
    text = 'Flush Five'';'
    scoring_hand = '1[poker_hands["Flush Five"]]'
elif next("Flush House"[poker_hands]):
    text = 'Flush House'';'
    scoring_hand = '1[poker_hands["Flush House"]]'
elif next("Five of a Kind"[poker_hands]):
    text = 'Five of a Kind'';'
    scoring_hand = '1[poker_hands["Five of a Kind"]]'
elif next("Straight Flush"[poker_hands]):
    text = 'Straight Flush'';'
    scoring_hand = '1[poker_hands["Straight Flush"]]'
elif next("Four of a Kind"[poker_hands]):
    text = 'Four of a Kind'';'
    scoring_hand = '1[poker_hands["Four of a Kind"]]'
elif next("Full House"[poker_hands]):
    text = 'Full House'';'
    scoring_hand = '1[poker_hands["Full House"]]'
elif next("Flush"[poker_hands]):
    text = 'Flush'';'
    scoring_hand = '1[poker_hands["Flush"]]'
elif next("Straight"[poker_hands]):
    text = 'Straight'';'
    scoring_hand = '1[poker_hands["Straight"]]'
elif next("Three of a Kind"[poker_hands]):
    text = 'Three of a Kind'';'
    scoring_hand = '1[poker_hands["Three of a Kind"]]'
elif next("Two Pair"[poker_hands]):
    text = 'Two Pair'';'
    scoring_hand = '1[poker_hands["Two Pair"]]'
elif next("Pair"[poker_hands]):
    text = 'Pair'';'
    scoring_hand = '1[poker_hands["Pair"]]'
elif next("High Card"[poker_hands]):
    text = 'High Card'';'
    scoring_hand = '1[poker_hands["High Card"]]'
disp_text = text
if text == 'Straight Flush':
    min = 10
    for j in range(1, len(scoring_hand), ):
        if 'j[scoring_hand]'.get_id() < min:
            min = 'j[scoring_hand]'.get_id()
    if min >= 10:
        disp_text = 'Royal Flush'
loc_disp_text = localize(disp_text, poker_hands)
return textloc_disp_textpoker_handsscoring_handdisp_text
G.FUNCS.evaluate_play = lambda e: 
text = disp_text = poker_hands = scoring_hand = non_loc_disp_text = G.FUNCS.get_poker_hand_info()
'text[G.GAME.hands]'.played = 'text[G.GAME.hands]'.played + 1
'text[G.GAME.hands]'.played_this_round = 'text[G.GAME.hands]'.played_this_round + 1
G.GAME.last_hand_played = textset_hand_usage(text)
'text[G.GAME.hands]'.visible = True
pures = {}
for i in range(1, len(G.play.cards), ):
    if next():
        'i[scoring_hand]' = 'i[G.play.cards]'
    elif 'i[G.play.cards]'.ability.effect == 'Stone Card':
        inside = False
        for j in range(1, len(scoring_hand), ):
            if 'j[scoring_hand]' == 'i[G.play.cards]':
                inside = True
        if not inside:table.insert(pures, i[G.play.cards])
for i in range(1, len(pures), ):table.insert(scoring_hand, i[pures])table.sort(scoring_hand)delay(0.2)
for i in range(1, len(scoring_hand), ):highlight_card(i[scoring_hand])
percent = 0.3
percent_delta = 0.08
if G.GAME.current_round.current_hand.handname != disp_text:delay(0.3)update_hand_text()
if not G.GAME.blind.debuff_hand():
    mult = mod_mult()
    hand_chips = mod_chips()check_for_unlock()delay(0.4)
    if G.GAME.first_used_hand_level & (G.GAME.first_used_hand_level > 0):level_up_hand(1[G.deck.cards], text, None)
        G.GAME.first_used_hand_level = 'None'
    hand_text_set = False
    for i in range(1, len(G.jokers.cards), ):
        effects = eval_card(i[G.jokers.cards])
        if effects.jokers:card_eval_status_text(i[G.jokers.cards], jokers, None, percent, None)
            percent = percent + percent_delta
            if effects.jokers.level_up:level_up_hand(i[G.jokers.cards], text)
    mult = mod_mult()
    hand_chips = mod_chips()
    modded = False
    mult = hand_chips = modded = G.GAME.blind.modify_hand()
    mult = hand_chips = (mod_mult(mult), mod_chips(hand_chips))
    if modded:update_hand_text()
    for i in range(1, len(scoring_hand), ):
        if 'i[scoring_hand]'.ability.effect != 'Stone Card':
            'scoring_hand[i].base.value[G.GAME.cards_played]'.total = 'scoring_hand[i].base.value[G.GAME.cards_played]'.total + 1
            'scoring_hand[i].base.suit[G.GAME.cards_played[scoring_hand[i].base.value].suits]' = True
        if 'i[scoring_hand]'.debuff:
            G.GAME.blind.triggered = TrueG.E_MANAGER.add_event()card_eval_status_text(i[scoring_hand], debuff)
        else:
            reps = {1: 1}
            eval = eval_card(i[scoring_hand])
            if next(eval):
                for h in range(1, eval.seals.repetitions, ):
                    '#reps + 1[reps]' = eval
            for j in range(1, len(G.jokers.cards), ):
                eval = eval_card(j[G.jokers.cards])
                if next(eval) & eval.jokers:
                    for h in range(1, eval.jokers.repetitions, ):
                        '#reps + 1[reps]' = eval
            for j in range(1, len(reps), ):
                percent = percent + percent_delta
                if 'j[reps]' != 1:card_eval_status_text()
                effects = {1: eval_card(i[scoring_hand])}
                for k in range(1, len(G.jokers.cards), ):
                    eval = 'k[G.jokers.cards]'.calculate_joker()
                    if eval:table.insert(effects, eval)
                'i[scoring_hand]'.lucky_trigger = 'None'
                for ii in range(1, len(effects), ):
                    if 'ii[effects]'.chips:
                        if 'ii[effects]'.card:juice_card()
                        hand_chips = mod_chips()update_hand_text()card_eval_status_text(i[scoring_hand], chips)
                    if 'ii[effects]'.mult:
                        if 'ii[effects]'.card:juice_card()
                        mult = mod_mult()update_hand_text()card_eval_status_text(i[scoring_hand], mult)
                    if 'ii[effects]'.p_dollars:
                        if 'ii[effects]'.card:juice_card()ease_dollars()card_eval_status_text(i[scoring_hand], dollars)
                    if 'ii[effects]'.dollars:
                        if 'ii[effects]'.card:juice_card()ease_dollars()card_eval_status_text(i[scoring_hand], dollars)
                    if 'ii[effects]'.extra:
                        if 'ii[effects]'.card:juice_card()
                        extras = {'mult': False, 'hand_chips': False}
                        if 'ii[effects]'.extra.mult_mod:
                            mult = mod_mult()';'
                            extras.mult = True
                        if 'ii[effects]'.extra.chip_mod:
                            hand_chips = mod_chips()';'
                            extras.hand_chips = True
                        if 'ii[effects]'.extra.swap:
                            old_mult = mult
                            mult = mod_mult(hand_chips)
                            hand_chips = mod_chips(old_mult)
                            extras.hand_chips = True';'
                            extras.mult = True
                        if 'ii[effects]'.extra.func:'ii[effects]'.extra.func()update_hand_text()card_eval_status_text(i[scoring_hand], extra, None, percent, None)
                    if 'ii[effects]'.x_mult:
                        if 'ii[effects]'.card:juice_card()
                        mult = mod_mult()update_hand_text()card_eval_status_text(i[scoring_hand], x_mult)
                    if 'ii[effects]'.edition:
                        hand_chips = mod_chips()
                        mult = mult + ('ii[effects]'.edition.mult_mod if 'ii[effects]'.edition.mult_mod else 0)
                        mult = mod_mult()update_hand_text()card_eval_status_text(i[scoring_hand], extra, None, percent, None)delay(0.3)
    mod_percent = False
    for i in range(1, len(G.hand.cards), ):
        if mod_percent:
            percent = percent + percent_delta
        mod_percent = False
        reps = {1: 1}
        j = 1
        while j <= len(reps):
            if 'j[reps]' != 1:card_eval_status_text()
                percent = percent + percent_delta
            effects = {1: eval_card(i[G.hand.cards])}
            for k in range(1, len(G.jokers.cards), ):
                eval = 'k[G.jokers.cards]'.calculate_joker()
                if eval:
                    mod_percent = Truetable.insert(effects, eval)
            if 'j[reps]' == 1:
                eval = eval_card(i[G.hand.cards])
                if next(eval) & (next(1[effects]) if next(1[effects]) else len(effects > 1)):
                    for h in range(1, eval.seals.repetitions, ):
                        '#reps + 1[reps]' = eval
                for j in range(1, len(G.jokers.cards), ):
                    eval = eval_card(j[G.jokers.cards])
                    if next(eval):
                        for h in range(1, eval.jokers.repetitions, ):
                            '#reps + 1[reps]' = eval
            for ii in range(1, len(effects), ):
                if 'ii[effects]'.card:
                    mod_percent = TrueG.E_MANAGER.add_event()
                if 'ii[effects]'.dollars:ease_dollars()card_eval_status_text(i[G.hand.cards], dollars)
                if 'ii[effects]'.h_mult:
                    mod_percent = True
                    mult = mod_mult()update_hand_text()card_eval_status_text(i[G.hand.cards], h_mult)
                if 'ii[effects]'.x_mult:
                    mod_percent = True
                    mult = mod_mult()update_hand_text()card_eval_status_text(i[G.hand.cards], x_mult)
                if 'ii[effects]'.message:
                    mod_percent = Trueupdate_hand_text()card_eval_status_text(i[G.hand.cards], extra, None, percent, None, ii[effects])
            j = j + 1
        else:
    percent = percent + percent_delta
    for i in range(1, len(G.jokers.cards + len(G.consumeables.cards)), ):
        _card = 'i[G.jokers.cards]' if 'i[G.jokers.cards]' else 'i - #G.jokers.cards[G.consumeables.cards]'
        edition_effects = eval_card(_card)
        if edition_effects.jokers:
            edition_effects.jokers.edition = True
            if edition_effects.jokers.chip_mod:
                hand_chips = mod_chips()update_hand_text()card_eval_status_text(_card, jokers, None, percent, None)
            if edition_effects.jokers.mult_mod:
                mult = mod_mult()update_hand_text()card_eval_status_text(_card, jokers, None, percent, None)
            percent = percent + percent_delta
        effects = eval_card(_card)
        if effects.jokers:
            extras = {'mult': False, 'hand_chips': False}
            if effects.jokers.mult_mod:
                mult = mod_mult()';'
                extras.mult = True
            if effects.jokers.chip_mod:
                hand_chips = mod_chips()';'
                extras.hand_chips = True
            if effects.jokers.Xmult_mod:
                mult = mod_mult()';'
                extras.mult = Trueupdate_hand_text()card_eval_status_text(_card, jokers, None, percent, None)
            percent = percent + percent_delta
        for _v in ipairs():
            effect = v.calculate_joker()
            if effect:
                extras = {'mult': False, 'hand_chips': False}
                if effect.mult_mod:
                    mult = mod_mult()';'
                    extras.mult = True
                if effect.chip_mod:
                    hand_chips = mod_chips()';'
                    extras.hand_chips = True
                if effect.Xmult_mod:
                    mult = mod_mult()';'
                    extras.mult = True
                if extras.mult if extras.mult else extras.hand_chips:update_hand_text()
                if extras.mult if extras.mult else extras.hand_chips:card_eval_status_text(v, jokers, None, percent, None, effect)
                percent = percent + percent_delta
        if edition_effects.jokers:
            if edition_effects.jokers.x_mult_mod:
                mult = mod_mult()update_hand_text()card_eval_status_text(_card, jokers, None, percent, None)
            percent = percent + percent_delta
    nu_chip = nu_mult = G.GAME.selected_back.trigger_effect()
    mult = mod_mult()
    hand_chips = mod_chips()
    cards_destroyed = {}
    for i in range(1, len(scoring_hand), ):
        destroyed = 'None'highlight_card(i[scoring_hand])
        for j in range(1, len(G.jokers.cards), ):
            destroyed = 'j[G.jokers.cards]'.calculate_joker()
            if destroyed:
                break
        if ('i[scoring_hand]'.ability.name == 'Glass Card') & (not 'i[scoring_hand]'.debuff) & pseudorandom(glass) < G.GAME.probabilities.normal / 'i[scoring_hand]'.ability.extra:
            destroyed = True
        if destroyed:
            if 'i[scoring_hand]'.ability.name == 'Glass Card':
                'i[scoring_hand]'.shattered = True
            else:
                'i[scoring_hand]'.destroyed = True
            '#cards_destroyed + 1[cards_destroyed]' = 'i[scoring_hand]'
    for j in range(1, len(G.jokers.cards), ):eval_card(j[G.jokers.cards])
    glass_shattered = {}
    for kv in ipairs(cards_destroyed):
        if v.shattered:
            '#glass_shattered + 1[glass_shattered]' = vcheck_for_unlock()
    for i in range(1, len(cards_destroyed), ):G.E_MANAGER.add_event()
else:
    mult = mod_mult(0)
    hand_chips = mod_chips(0)G.E_MANAGER.add_event()play_area_status_text(Not Allowed!)
    for i in range(1, len(G.jokers.cards), ):
        effects = eval_card(i[G.jokers.cards])
        if effects.jokers:card_eval_status_text(i[G.jokers.cards], jokers, None, percent, None)
            percent = percent + percent_deltaG.E_MANAGER.add_event()check_and_set_high_score(hand)check_for_unlock()
if hand_chips * mult > 0:delay(0.8)G.E_MANAGER.add_event()G.E_MANAGER.add_event()G.E_MANAGER.add_event()G.E_MANAGER.add_event()delay(0.3)
for i in range(1, len(G.jokers.cards), ):
    effects = eval_card(i[G.jokers.cards])
    if effects.jokers:card_eval_status_text(i[G.jokers.cards], jokers, None, percent, None)
        percent = percent + percent_deltaG.E_MANAGER.add_event()
G.FUNCS.draw_from_play_to_discard = lambda e: 
play_count = len(G.play.cards)
it = 1
for kv in ipairs():
    if (not v.shattered) & (not v.destroyed):draw_card()
        it = it + 1
G.FUNCS.draw_from_play_to_hand = lambda cards: 
gold_count = len(cards)
for i in range(1, gold_count, ):
    if (not 'i[cards]'.shattered) & (not 'i[cards]'.destroyed):draw_card()
G.FUNCS.draw_from_discard_to_deck = lambda e: G.E_MANAGER.add_event()
G.FUNCS.draw_from_hand_to_deck = lambda e: 
hand_count = len(G.hand.cards)
for i in range(1, hand_count, ):draw_card()
G.FUNCS.draw_from_hand_to_discard = lambda e: 
hand_count = len(G.hand.cards)
for i in range(1, hand_count, ):draw_card()
G.FUNCS.evaluate_round = lambda: 
pitch = 0.95
dollars = 0
if G.GAME.chips - G.GAME.blind.chips >= 0:add_round_eval_row()
    pitch = pitch + 0.06
    dollars = dollars + G.GAME.blind.dollars
else:add_round_eval_row()
    pitch = pitch + 0.06G.E_MANAGER.add_event()delay(0.2)G.E_MANAGER.add_event()G.GAME.selected_back.trigger_effect()
if (G.GAME.current_round.hands_left > 0) & (not G.GAME.modifiers.no_extra_hand_money):add_round_eval_row()
    pitch = pitch + 0.06
    dollars = dollars + G.GAME.current_round.hands_left * (G.GAME.modifiers.money_per_hand if G.GAME.modifiers.money_per_hand else 1)
if (G.GAME.current_round.discards_left > 0) & G.GAME.modifiers.money_per_discard:add_round_eval_row()
    pitch = pitch + 0.06
    dollars = dollars + G.GAME.current_round.discards_left * G.GAME.modifiers.money_per_discard
for i in range(1, len(G.jokers.cards), ):
    ret = 'i[G.jokers.cards]'.calculate_dollar_bonus()
    if ret:add_round_eval_row()
        pitch = pitch + 0.06
        dollars = dollars + ret
for i in range(1, len(G.GAME.tags), ):
    ret = 'i[G.GAME.tags]'.apply_to_run()
    if ret:add_round_eval_row()
        pitch = pitch + 0.06
        dollars = dollars + ret.dollars
if (G.GAME.dollars >= 5) & (not G.GAME.modifiers.no_interest):add_round_eval_row()
    pitch = pitch + 0.06
    if (not G.GAME.seeded) & (not G.GAME.challenge):
        if G.GAME.interest_amount * math.min() == G.GAME.interest_amount * G.GAME.interest_cap / 5:
            'G.SETTINGS.profile[G.PROFILES]'.career_stats.c_round_interest_cap_streak = 'G.SETTINGS.profile[G.PROFILES]'.career_stats.c_round_interest_cap_streak + 1
        else:
            'G.SETTINGS.profile[G.PROFILES]'.career_stats.c_round_interest_cap_streak = 0check_for_unlock()
    dollars = dollars + G.GAME.interest_amount * math.min()
pitch = pitch + 0.06add_round_eval_row()
G.FUNCS.tutorial_controller = lambda: 
if G.F_SKIP_TUTORIAL:
    G.SETTINGS.tutorial_complete = True
    G.SETTINGS.tutorial_progress = 'None'
    return False
G.SETTINGS.tutorial_progress = G.SETTINGS.tutorial_progress if G.SETTINGS.tutorial_progress else {'forced_shop': {1: 'j_joker', 2: 'c_empress'}, 'forced_voucher': 'v_grabber', 'forced_tags': {1: 'tag_handy', 2: 'tag_garbage'}, 'hold_parts': {}, 'completed_parts': {}}
if (not G.SETTINGS.paused) & (not G.SETTINGS.tutorial_complete):
    if (G.STATE == G.STATES.BLIND_SELECT) & G.blind_select & (not "'small_blind'[G.SETTINGS.tutorial_progress.completed_parts]"):
        G.SETTINGS.tutorial_progress.section = 'small_blind'G.FUNCS.tutorial_part(small_blind)
        "'small_blind'[G.SETTINGS.tutorial_progress.completed_parts]" = TrueG.save_progress()
    if (G.STATE == G.STATES.BLIND_SELECT) & G.blind_select & (not "'big_blind'[G.SETTINGS.tutorial_progress.completed_parts]") & (G.GAME.round > 0):
        G.SETTINGS.tutorial_progress.section = 'big_blind'G.FUNCS.tutorial_part(big_blind)
        "'big_blind'[G.SETTINGS.tutorial_progress.completed_parts]" = True
        G.SETTINGS.tutorial_progress.forced_tags = 'None'G.save_progress()
    if (G.STATE == G.STATES.SELECTING_HAND) & (not "'second_hand'[G.SETTINGS.tutorial_progress.completed_parts]") & "'big_blind'[G.SETTINGS.tutorial_progress.hold_parts]":
        G.SETTINGS.tutorial_progress.section = 'second_hand'G.FUNCS.tutorial_part(second_hand)
        "'second_hand'[G.SETTINGS.tutorial_progress.completed_parts]" = TrueG.save_progress()
    if "'second_hand'[G.SETTINGS.tutorial_progress.hold_parts]":
        G.SETTINGS.tutorial_complete = True
    if not "'first_hand_section'[G.SETTINGS.tutorial_progress.completed_parts]":
        if (G.STATE == G.STATES.SELECTING_HAND) & (not "'first_hand'[G.SETTINGS.tutorial_progress.completed_parts]"):
            G.SETTINGS.tutorial_progress.section = 'first_hand'G.FUNCS.tutorial_part(first_hand)
            "'first_hand'[G.SETTINGS.tutorial_progress.completed_parts]" = TrueG.save_progress()
        if (G.STATE == G.STATES.SELECTING_HAND) & (not "'first_hand_2'[G.SETTINGS.tutorial_progress.completed_parts]") & "'first_hand'[G.SETTINGS.tutorial_progress.hold_parts]":G.FUNCS.tutorial_part(first_hand_2)
            "'first_hand_2'[G.SETTINGS.tutorial_progress.completed_parts]" = TrueG.save_progress()
        if (G.STATE == G.STATES.SELECTING_HAND) & (not "'first_hand_3'[G.SETTINGS.tutorial_progress.completed_parts]") & "'first_hand_2'[G.SETTINGS.tutorial_progress.hold_parts]":G.FUNCS.tutorial_part(first_hand_3)
            "'first_hand_3'[G.SETTINGS.tutorial_progress.completed_parts]" = TrueG.save_progress()
        if (G.STATE == G.STATES.SELECTING_HAND) & (not "'first_hand_4'[G.SETTINGS.tutorial_progress.completed_parts]") & "'first_hand_3'[G.SETTINGS.tutorial_progress.hold_parts]":G.FUNCS.tutorial_part(first_hand_4)
            "'first_hand_4'[G.SETTINGS.tutorial_progress.completed_parts]" = True
            "'first_hand_section'[G.SETTINGS.tutorial_progress.completed_parts]" = TrueG.save_progress()
    if (G.STATE == G.STATES.SHOP) & G.shop & G.shop.VT.y < 5 & (not "'shop_1'[G.SETTINGS.tutorial_progress.completed_parts]"):
        G.SETTINGS.tutorial_progress.section = 'shop'G.FUNCS.tutorial_part(shop_1)
        "'shop_1'[G.SETTINGS.tutorial_progress.completed_parts]" = True
        G.SETTINGS.tutorial_progress.forced_voucher = 'None'G.save_progress()
G.FUNCS.tutorial_part = lambda _part: 
step = 1
G.SETTINGS.paused = True
if _part == 'small_blind':
    step = tutorial_info()
    step = tutorial_info()
    step = tutorial_info()
    step = tutorial_info()
elif _part == 'big_blind':
    step = tutorial_info()
    step = tutorial_info()
    step = tutorial_info()
    step = tutorial_info()
    step = tutorial_info()
elif _part == 'first_hand':
    step = tutorial_info()
    step = tutorial_info()
    step = tutorial_info()
elif _part == 'first_hand_2':
    step = tutorial_info()
    step = tutorial_info()
elif _part == 'first_hand_3':
    step = tutorial_info()
elif _part == 'first_hand_4':
    step = tutorial_info()
    step = tutorial_info()
elif _part == 'second_hand':
    step = tutorial_info()
    empress = "1[find_joker('The Empress')]"
    if empress:
        step = tutorial_info()
        step = tutorial_info()
elif _part == 'shop_1':
    step = tutorial_info()
    step = tutorial_info()
    step = tutorial_info()
    step = tutorial_info()
    step = tutorial_info()
    step = tutorial_info()
    step = tutorial_info()
    step = tutorial_info()
    step = tutorial_info()
    step = tutorial_info()
    step = tutorial_info()
    step = tutorial_info()G.E_MANAGER.add_event()
G.SETTINGS.paused = False