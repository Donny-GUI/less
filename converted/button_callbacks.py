G.FUNCS.tut_next = lambda e: 
if G.OVERLAY_TUTORIAL:G.OVERLAY_TUTORIAL.Jimbo.remove_button()G.OVERLAY_TUTORIAL.Jimbo.remove_speech_bubble()
    G.OVERLAY_TUTORIAL.step_complete = False
    G.OVERLAY_TUTORIAL.step = G.OVERLAY_TUTORIAL.step + 1
G.FUNCS.blueprint_compat = lambda e: 
if e.config.ref_table.ability.blueprint_compat != e.config.ref_table.ability.blueprint_compat_check:
    if e.config.ref_table.ability.blueprint_compat == 'compatible':
        e.config.colour = mix_colours()
    elif e.config.ref_table.ability.blueprint_compat == 'incompatible':
        e.config.colour = mix_colours()
    e.config.ref_table.ability.blueprint_compat_ui = ' ' + localize() + ' '
    e.config.ref_table.ability.blueprint_compat_check = e.config.ref_table.ability.blueprint_compat
G.FUNCS.sort_hand_suit = lambda e: G.hand.sort(suit desc)play_sound(paper1)
G.FUNCS.sort_hand_value = lambda e: G.hand.sort(desc)play_sound(paper1)
G.FUNCS.can_buy = lambda e: 
if (e.config.ref_table.cost > G.GAME.dollars - G.GAME.bankrupt_at) & (e.config.ref_table.cost > 0):
    e.config.colour = G.C.UI.BACKGROUND_INACTIVE
    e.config.button = 'None'
else:
    e.config.colour = G.C.ORANGE
    e.config.button = 'buy_from_shop'
if e.config.ref_parent & e.config.ref_parent.children.buy_and_use:
    if e.config.ref_parent.children.buy_and_use.states.visible:
        e.UIBox.alignment.offset.y = -0.6
    else:
        e.UIBox.alignment.offset.y = 0
G.FUNCS.can_buy_and_use = lambda e: 
if (e.config.ref_table.cost > G.GAME.dollars - G.GAME.bankrupt_at) & (e.config.ref_table.cost > 0) if (e.config.ref_table.cost > G.GAME.dollars - G.GAME.bankrupt_at) & (e.config.ref_table.cost > 0) else not e.config.ref_table.can_use_consumeable():
    e.UIBox.states.visible = False
    e.config.colour = G.C.UI.BACKGROUND_INACTIVE
    e.config.button = 'None'
else:
    if e.config.ref_table.highlighted:
        e.UIBox.states.visible = True
    e.config.colour = G.C.SECONDARY_SET.Voucher
    e.config.button = 'buy_from_shop'
G.FUNCS.can_redeem = lambda e: 
if e.config.ref_table.cost > G.GAME.dollars - G.GAME.bankrupt_at:
    e.config.colour = G.C.UI.BACKGROUND_INACTIVE
    e.config.button = 'None'
else:
    e.config.colour = G.C.GREEN
    e.config.button = 'use_card'
G.FUNCS.can_open = lambda e: 
if (e.config.ref_table.cost > 0) & (e.config.ref_table.cost > G.GAME.dollars - G.GAME.bankrupt_at):
    e.config.colour = G.C.UI.BACKGROUND_INACTIVE
    e.config.button = 'None'
else:
    e.config.colour = G.C.GREEN
    e.config.button = 'use_card'
G.FUNCS.HUD_blind_visible = lambda e: 
if G.GAME.blind & ((G.GAME.blind.name != '') & G.GAME.blind.blind_set):
    G.GAME.blind.states.visible = True
elif G.GAME.blind:
    G.GAME.blind.states.visible = False
G.FUNCS.HUD_blind_debuff = lambda e: 
if G.GAME.blind & G.GAME.blind.loc_debuff_text & (G.GAME.blind.loc_debuff_text != ''):
    if e.parent.config.minh == 0 if e.parent.config.minh == 0 else e.config.prev_loc != G.GAME.blind.loc_debuff_text:
        e.parent.config.minh = 0.35
        e.config.scale = 0.36
        if 'e.config.ref_value[G.GAME.blind.loc_debuff_lines]' == '':
            e.config.scale = 0.0';'
            e.parent.config.minh = 0.001
        e.config.prev_loc = G.GAME.blind.loc_debuff_texte.UIBox.recalculate(True)
elif e.parent.config.minh > 0:
    e.parent.config.minh = 0
    e.config.scale = 0e.UIBox.recalculate(True)
G.FUNCS.HUD_blind_debuff_prefix = lambda e: 
if G.GAME.blind & (G.GAME.blind.name == 'The Wheel') & (not G.GAME.blind.disabled) if G.GAME.blind & (G.GAME.blind.name == 'The Wheel') & (not G.GAME.blind.disabled) else e.config.id == 'bl_wheel':
    e.config.ref_table.val = '' + G.GAME.probabilities.normal
    e.config.scale = 0.32
else:
    e.config.ref_table.val = ''
    e.config.scale = 0
G.FUNCS.HUD_blind_reward = lambda e: 
if G.GAME.modifiers.no_blind_reward & (G.GAME.blind & 'G.GAME.blind:get_type()[G.GAME.modifiers.no_blind_reward]'):
    if e.config.minh > 0.44:
        e.config.minh = 0.4
        '1[e.children]'.config.text = localize(k_no_reward)e.UIBox.recalculate(True)
elif e.config.minh < 0.45:
    e.config.minh = 0.45
    '1[e.children]'.config.text = localize(k_reward) + ': '
    '2[e.children]'.states.visible = Truee.UIBox.recalculate(True)
G.FUNCS.can_continue = lambda e: 
if e.config.func:
    _can_continue = 'None'
    savefile = love.filesystem.getInfo()
    if savefile == 'None':
        e.config.colour = G.C.UI.BACKGROUND_INACTIVE
        e.config.button = 'None'
    else:
        if not G.SAVED_GAME:
            G.SAVED_GAME = get_compressed()
            if G.SAVED_GAME != 'None':
                G.SAVED_GAME = STR_UNPACK()
        if not G.SAVED_GAME.VERSION if not G.SAVED_GAME.VERSION else G.SAVED_GAME.VERSION < '0.9.2':
            e.config.colour = G.C.UI.BACKGROUND_INACTIVE
            e.config.button = 'None'
        else:
            _can_continue = True
    e.config.func = 'None'
    return _can_continue
G.FUNCS.can_load_profile = lambda e: 
if G.SETTINGS.profile == G.focused_profile:
    e.config.colour = G.C.UI.BACKGROUND_INACTIVE
    e.config.button = 'None'
else:
    e.config.colour = G.C.BLUE
    e.config.button = 'load_profile'
G.FUNCS.load_profile = lambda delete_prof_data: 
G.SAVED_GAME = 'None'G.E_MANAGER.clear_queue()G.FUNCS.wipe_on()G.E_MANAGER.add_event()G.E_MANAGER.add_event()G.FUNCS.wipe_off()
G.FUNCS.can_delete_profile = lambda e: 
G.CHECK_PROFILE_DATA = G.CHECK_PROFILE_DATA if G.CHECK_PROFILE_DATA else love.filesystem.getInfo()
if not G.CHECK_PROFILE_DATA if not G.CHECK_PROFILE_DATA else e.config.disable_button:
    G.CHECK_PROFILE_DATA = False
    e.config.colour = G.C.UI.BACKGROUND_INACTIVE
    e.config.button = 'None'
else:
    e.config.colour = G.C.RED
    e.config.button = 'delete_profile'
G.FUNCS.delete_profile = lambda e: 
warning_text = e.UIBox.get_UIE_by_ID(warning_text)
if warning_text.config.colour != G.C.WHITE:warning_text.juice_up()
    warning_text.config.colour = G.C.WHITE
    warning_text.config.shadow = True
    e.config.disable_button = TrueG.E_MANAGER.add_event()G.E_MANAGER.add_event()play_sound(tarot2, 1, 0.4)
else:love.filesystem.remove()love.filesystem.remove()love.filesystem.remove()love.filesystem.remove()love.filesystem.remove()
    G.SAVED_GAME = 'None'
    G.DISCOVER_TALLIES = 'None'
    G.PROGRESS = 'None'
    'G.focused_profile[G.PROFILES]' = {}
    if G.focused_profile == G.SETTINGS.profile:G.FUNCS.load_profile(True)
    else:
        tab_but = G.OVERLAY_MENU.get_UIE_by_ID()G.FUNCS.change_tab(tab_but)
G.FUNCS.can_unlock_all = lambda e: 
if 'G.SETTINGS.profile[G.PROFILES]'.all_unlocked if 'G.SETTINGS.profile[G.PROFILES]'.all_unlocked else e.config.disable_button:
    e.config.colour = G.C.UI.BACKGROUND_INACTIVE
    e.config.button = 'None'
else:
    e.config.colour = G.C.GREY
    e.config.button = 'unlock_all'
G.FUNCS.unlock_all = lambda e: 
_infotip_object = G.OVERLAY_MENU.get_UIE_by_ID(overlay_menu_infotip)
if (not _infotip_object.config.set) & (not G.F_NO_ACHIEVEMENTS):_infotip_object.config.object.remove()
    _infotip_object.config.object = UIBox()_infotip_object.config.object.UIRoot.juice_up()
    _infotip_object.config.set = True
    e.config.disable_button = TrueG.E_MANAGER.add_event()G.E_MANAGER.add_event()play_sound(tarot2, 1, 0.4)
else:
    'G.SETTINGS.profile[G.PROFILES]'.all_unlocked = True
    for kv in pairs():
        if (not v.demo) & (not v.wip):
            v.alerted = True
            v.discovered = True
            v.unlocked = True
    for kv in pairs():
        if (not v.demo) & (not v.wip):
            v.alerted = True
            v.discovered = True
            v.unlocked = True
    for kv in pairs():
        if (not v.demo) & (not v.wip):
            v.alerted = True
            v.discovered = True
            v.unlocked = Trueset_profile_progress()set_discover_tallies()G.save_progress()
    G.FILE_HANDLER.force = True
    tab_but = G.OVERLAY_MENU.get_UIE_by_ID()G.FUNCS.change_tab(tab_but)
G.FUNCS.high_score_alert = lambda e: 
if e.config.id & (not e.children.alert):
    if 'e.config.id[G.GAME.round_scores]' & 'e.config.id[G.GAME.round_scores]'.high_score:
        e.children.alert = UIBox()
        e.children.alert.states.collide.can = False
G.FUNCS.beta_lang_alert = lambda e: 
if not e.children.alert:
    if e.config.ref_table & e.config.ref_table.beta:
        e.children.alert = UIBox()
        e.children.alert.states.collide.can = False
G.FUNCS.set_button_pip = lambda e: 
if G.CONTROLLER.HID.controller & e.config.focus_args & (not e.children.button_pip):
    e.children.button_pip = UIBox()
    e.children.button_pip.states.collide.can = False
if (not G.CONTROLLER.HID.controller) & e.children.button_pip:e.children.button_pip.remove()
    e.children.button_pip = 'None'
G.FUNCS.flash = lambda e: 
if G.CONTROLLER.text_input_hook:
    if (math.floor() % 2) == 1:
        '4[e.config.colour]' = 0
    else:
        '4[e.config.colour]' = 1
    if e.config.w != 0.1:
        e.config.w = 0.1';'e.UIBox.recalculate(True)
else:
    '4[e.config.colour]' = 0
    if e.config.w != 0:
        e.config.w = 0';'e.UIBox.recalculate(True)
G.FUNCS.pip_dynatext = lambda e: 
if 'pip_' + tostring() == e.config.id:
    if e.config.pip_state != 1:
        e.config.colour = e.config.pipcol1
        e.config.pip_state = 1
elif e.config.pip_state != 2:
    e.config.colour = e.config.pipcol2
    e.config.pip_state = 2
def toggle_button(e):
    'e.config.ref_table.ref_value[e.config.ref_table.ref_table]' = not 'e.config.ref_table.ref_value[e.config.ref_table.ref_table]'
    if e.config.toggle_callback:e.config.toggle_callback(e.config.ref_table.ref_value[e.config.ref_table.ref_table])
def toggle(e):
    if (not 'e.config.ref_table.ref_value[e.config.ref_table.ref_table]') & e.config.toggle_active:
        e.config.toggle_active = 'None'
        e.config.colour = e.config.ref_table.inactive_colour
        '1[e.children]'.states.visible = False
        '1[e.children]'.config.object.states.visible = False
    elif 'e.config.ref_table.ref_value[e.config.ref_table.ref_table]' & (not e.config.toggle_active):
        e.config.toggle_active = True
        e.config.colour = e.config.ref_table.active_colour
        '1[e.children]'.states.visible = True
        '1[e.children]'.config.object.states.visible = True
def slider(e):
    c = '1[e.children]'
    e.states.drag.can = True
    c.states.drag.can = True
    if G.CONTROLLER & G.CONTROLLER.dragging.target & (G.CONTROLLER.dragging.target == e if G.CONTROLLER.dragging.target == e else G.CONTROLLER.dragging.target == c):
        rt = c.config.ref_table
        'rt.ref_value[rt.ref_table]' = math.min()
        rt.text = string.format()
        c.T.w = ('rt.ref_value[rt.ref_table]' - rt.min) / (rt.max - rt.min) * rt.w
        c.config.w = c.T.w
        if rt.callback:'rt.callback[G.FUNCS]'(rt)
def slider_descreet(e, per):
    c = '1[e.children]'
    e.states.drag.can = True
    c.states.drag.can = True
    if per:
        rt = c.config.ref_table
        'rt.ref_value[rt.ref_table]' = math.min()
        rt.text = string.format()
        c.T.w = ('rt.ref_value[rt.ref_table]' - rt.min) / (rt.max - rt.min) * rt.w
        c.config.w = c.T.w
G.FUNCS.option_cycle = lambda e: 
from_val = 'e.config.ref_table.current_option[e.config.ref_table.options]'
from_key = e.config.ref_table.current_option
old_pip = e.UIBox.get_UIE_by_ID()
cycle_main = e.UIBox.get_UIE_by_ID(cycle_main)
if cycle_main & cycle_main.config.h_popup:cycle_main.stop_hover()G.E_MANAGER.add_event()
if e.config.ref_value == 'l':
    e.config.ref_table.current_option = e.config.ref_table.current_option - 1
    if e.config.ref_table.current_option <= 0:
        e.config.ref_table.current_option = len(e.config.ref_table.options)
else:
    e.config.ref_table.current_option = e.config.ref_table.current_option + 1
    if e.config.ref_table.current_option > len(e.config.ref_table.options):
        e.config.ref_table.current_option = 1
to_val = 'e.config.ref_table.current_option[e.config.ref_table.options]'
to_key = e.config.ref_table.current_option
e.config.ref_table.current_option_val = 'e.config.ref_table.current_option[e.config.ref_table.options]'
new_pip = e.UIBox.get_UIE_by_ID()
if old_pip:
    old_pip.config.colour = G.C.BLACK
if new_pip:
    new_pip.config.colour = G.C.WHITE
if e.config.ref_table.opt_callback:'e.config.ref_table.opt_callback[G.FUNCS]'()
G.FUNCS.test_framework_cycle_callback = lambda args: 
args = args if args else {}
if args.cycle_config & args.cycle_config.ref_table & args.cycle_config.ref_value:
    'args.cycle_config.ref_value[args.cycle_config.ref_table]' = args.to_val
G.FUNCS.your_collection_joker_page = lambda args: 
if not args if not args else not args.cycle_config:
    return False
for j in range(1, len(G.your_collection), ):
    for i in range(len('j[G.your_collection]'.cards), 1, -1):
        c = 'j[G.your_collection]'.remove_card(i[G.your_collection[j].cards])c.remove()
        c = 'None'
for i in range(1, 5, ):
    for j in range(1, len(G.your_collection), ):
        center = 'i + j - 1 * 5 + 5 * #G.your_collection * args.cycle_config.current_option - 1[G.P_CENTER_POOLS["Joker"]]'
        if not center:
            break
        card = Card()
        card.sticker = get_joker_win_sticker(center)'j[G.your_collection]'.emplace(card)INIT_COLLECTION_CARD_ALERTS()
G.FUNCS.your_collection_tarot_page = lambda args: 
if not args if not args else not args.cycle_config:
    return False
for j in range(1, len(G.your_collection), ):
    for i in range(len('j[G.your_collection]'.cards), 1, -1):
        c = 'j[G.your_collection]'.remove_card(i[G.your_collection[j].cards])c.remove()
        c = 'None'
for j in range(1, len(G.your_collection), ):
    for i in range(1, 4 + j, ):
        center = 'i + j - 1 * 5 + 11 * args.cycle_config.current_option - 1[G.P_CENTER_POOLS["Tarot"]]'
        if not center:
            break
        card = Card()card.start_materialize(None)'j[G.your_collection]'.emplace(card)INIT_COLLECTION_CARD_ALERTS()
G.FUNCS.your_collection_spectral_page = lambda args: 
if not args if not args else not args.cycle_config:
    return False
for j in range(1, len(G.your_collection), ):
    for i in range(len('j[G.your_collection]'.cards), 1, -1):
        c = 'j[G.your_collection]'.remove_card(i[G.your_collection[j].cards])c.remove()
        c = 'None'
for j in range(1, len(G.your_collection), ):
    for i in range(1, 3 + j, ):
        center = 'i + j - 1 * 4 + 9 * args.cycle_config.current_option - 1[G.P_CENTER_POOLS["Spectral"]]'
        if not center:
            break
        card = Card()card.start_materialize(None)'j[G.your_collection]'.emplace(card)INIT_COLLECTION_CARD_ALERTS()
G.FUNCS.your_collection_booster_page = lambda args: 
if not args if not args else not args.cycle_config:
    return False
for j in range(1, len(G.your_collection), ):
    for i in range(len('j[G.your_collection]'.cards), 1, -1):
        c = 'j[G.your_collection]'.remove_card(i[G.your_collection[j].cards])c.remove()
        c = 'None'
for j in range(1, len(G.your_collection), ):
    for i in range(1, 4, ):
        center = 'i + j - 1 * 4 + 8 * args.cycle_config.current_option - 1[G.P_CENTER_POOLS["Booster"]]'
        if not center:
            break
        card = Card()card.start_materialize(None)'j[G.your_collection]'.emplace(card)INIT_COLLECTION_CARD_ALERTS()
G.FUNCS.your_collection_voucher_page = lambda args: 
if not args if not args else not args.cycle_config:
    return False
for j in range(1, len(G.your_collection), ):
    for i in range(len('j[G.your_collection]'.cards), 1, -1):
        c = 'j[G.your_collection]'.remove_card(i[G.your_collection[j].cards])c.remove()
        c = 'None'
for i in range(1, 4, ):
    for j in range(1, len(G.your_collection), ):
        center = 'i + j - 1 * 4 + 8 * args.cycle_config.current_option - 1[G.P_CENTER_POOLS["Voucher"]]'
        if not center:
            break
        card = Card()card.start_materialize(None)'j[G.your_collection]'.emplace(card)INIT_COLLECTION_CARD_ALERTS()
G.FUNCS.change_selected_back = lambda args: G.GAME.selected_back.change_to(args.to_key[G.P_CENTER_POOLS.Back])
G.FUNCS.change_viewed_back = lambda args: 
G.viewed_stake = G.viewed_stake if G.viewed_stake else 1G.GAME.viewed_back.change_to(args.to_key[G.P_CENTER_POOLS.Back])
if G.sticker_card:
    G.sticker_card.sticker = get_deck_win_sticker()
max_stake = get_deck_win_stake() if get_deck_win_stake() else 0
G.viewed_stake = math.min()
'G.SETTINGS.profile[G.PROFILES]'.MEMORY.deck = args.to_val
G.FUNCS.change_stake = lambda args: 
G.viewed_stake = args.to_key
'G.SETTINGS.profile[G.PROFILES]'.MEMORY.stake = args.to_key
G.FUNCS.change_vsync = lambda args: 
G.SETTINGS.QUEUED_CHANGE.vsync = ((G.SETTINGS.WINDOW.vsync == 0) & (args.to_key == 1) & 1 if (G.SETTINGS.WINDOW.vsync == 0) & (args.to_key == 1) & 1 else (G.SETTINGS.WINDOW.vsync == 1) & (args.to_key == 2) & 0) if ((G.SETTINGS.WINDOW.vsync == 0) & (args.to_key == 1) & 1 if (G.SETTINGS.WINDOW.vsync == 0) & (args.to_key == 1) & 1 else (G.SETTINGS.WINDOW.vsync == 1) & (args.to_key == 2) & 0) else 'None'
G.FUNCS.change_screen_resolution = lambda args: 
curr_disp = G.SETTINGS.WINDOW.selected_display
to_resolution = 'args.to_key[G.SETTINGS.WINDOW.DISPLAYS[curr_disp].screen_resolutions.values]'
G.SETTINGS.QUEUED_CHANGE.screenres = {'w': to_resolution.w, 'h': to_resolution.h}
G.FUNCS.change_screenmode = lambda args: 
G.ARGS.screenmode_vals = G.ARGS.screenmode_vals if G.ARGS.screenmode_vals else {1: 'Windowed', 2: 'Fullscreen', 3: 'Borderless'}
G.SETTINGS.QUEUED_CHANGE.screenmode = 'args.to_key[G.ARGS.screenmode_vals]'G.FUNCS.change_window_cycle_UI()
G.FUNCS.change_display = lambda args: 
G.SETTINGS.QUEUED_CHANGE.selected_display = args.to_keyG.FUNCS.change_window_cycle_UI()
G.FUNCS.change_window_cycle_UI = lambda: 
if G.OVERLAY_MENU:
    swap_node = G.OVERLAY_MENU.get_UIE_by_ID(resolution_cycle)
    if swap_node:
        focused_display = focused_screenmode = (G.SETTINGS.QUEUED_CHANGE.selected_display if G.SETTINGS.QUEUED_CHANGE.selected_display else G.SETTINGS.WINDOW.selected_display, G.SETTINGS.QUEUED_CHANGE.screenmode if G.SETTINGS.QUEUED_CHANGE.screenmode else G.SETTINGS.WINDOW.screenmode)
        res_option = GET_DISPLAYINFO(focused_screenmode, focused_display)'1[swap_node.children]'.remove()
        '1[swap_node.children]' = 'None'swap_node.UIBox.add_child()
G.FUNCS.change_gamespeed = lambda args: 
G.SETTINGS.GAMESPEED = args.to_val
G.FUNCS.change_play_discard_position = lambda args: 
G.SETTINGS.play_button_pos = args.to_key
if G.buttons:G.buttons.remove()
    G.buttons = UIBox()
G.FUNCS.change_shadows = lambda args: 
G.SETTINGS.GRAPHICS.shadows = (args.to_key == 1) & 'On' if (args.to_key == 1) & 'On' else 'Off'G.save_settings()
G.FUNCS.change_pixel_smoothing = lambda args: 
G.SETTINGS.GRAPHICS.texture_scaling = args.to_keyG.set_render_settings()G.save_settings()
G.FUNCS.change_crt_bloom = lambda args: 
G.SETTINGS.GRAPHICS.bloom = args.to_keyG.save_settings()
G.FUNCS.key_button = lambda e: 
args = e.config.ref_table
if args.key:G.CONTROLLER.key_press_update()
G.FUNCS.text_input = lambda e: 
args = e.config.ref_table
if G.CONTROLLER.text_input_hook == e:
    e.parent.parent.config.colour = args.hooked_colour
    args.current_prompt_text = ''
    args.current_position_text = args.position_text
else:
    e.parent.parent.config.colour = args.colour
    args.current_prompt_text = ('args.text.ref_value[args.text.ref_table]' == '') & args.prompt_text if ('args.text.ref_value[args.text.ref_table]' == '') & args.prompt_text else ''
    args.current_position_text = ''
OSkeyboard_e = e.parent.parent.parent
if (G.CONTROLLER.text_input_hook == e) & G.CONTROLLER.HID.controller:
    if not OSkeyboard_e.children.controller_keyboard:
        OSkeyboard_e.children.controller_keyboard = UIBox()
        G.CONTROLLER.screen_keyboard = OSkeyboard_e.children.controller_keyboardG.CONTROLLER.mod_cursor_context_layer(1)
elif OSkeyboard_e.children.controller_keyboard:OSkeyboard_e.children.controller_keyboard.remove()
    OSkeyboard_e.children.controller_keyboard = 'None'
    G.CONTROLLER.screen_keyboard = 'None'G.CONTROLLER.mod_cursor_context_layer()
G.FUNCS.paste_seed = lambda e: 
G.CONTROLLER.text_input_hook = "1[e.UIBox:get_UIE_by_ID('text_input').children[1].children]"
for i in range(1, 8, ):G.FUNCS.text_input_key()
for i in range(1, 8, ):G.FUNCS.text_input_key()
clipboard = (G.F_LOCAL_CLIPBOARD & G.CLIPBOARD if G.F_LOCAL_CLIPBOARD & G.CLIPBOARD else love.system.getClipboardText()) if (G.F_LOCAL_CLIPBOARD & G.CLIPBOARD if G.F_LOCAL_CLIPBOARD & G.CLIPBOARD else love.system.getClipboardText()) else ''
for i in range(1, len(clipboard), ):
    c = clipboard.sub(i, i)G.FUNCS.text_input_key()G.FUNCS.text_input_key()
G.FUNCS.select_text_input = lambda e: 
G.CONTROLLER.text_input_hook = '1[e.children[1].children]'TRANSPOSE_TEXT_INPUT(0)e.UIBox.recalculate(True)
G.FUNCS.text_input_key = lambda args: 
args = args if args else {}
if args.key == '[' if args.key == '[' else args.key == ']':
    return False
if args.key == '0':
    args.key = 'o'
hook_config = G.CONTROLLER.text_input_hook.config.ref_table
hook_config.orig_colour = hook_config.orig_colour if hook_config.orig_colour else copy_table()
args.key = args.key if args.key else '%'
args.caps = (args.caps if args.caps else G.CONTROLLER.capslock) if (args.caps if args.caps else G.CONTROLLER.capslock) else hook_config.all_caps
keymap = {'space': ' ', 'backspace': 'BACKSPACE', 'delete': 'DELETE', 'return': 'RETURN', 'right': 'RIGHT', 'left': 'LEFT'}
hook = G.CONTROLLER.text_input_hook
corpus = '123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' + (hook.config.ref_table.extended_corpus & ' 0!$&()<>?:{}+-=,.[]_' if hook.config.ref_table.extended_corpus & ' 0!$&()<>?:{}+-=,.[]_' else '')
if hook.config.ref_table.extended_corpus:
    lower_ext = "1234567890-=;\\',./"
    upper_ext = '!@#$%^&*()_+:"<>?'
    if string.find(lower_ext) & args.caps:
        args.key = string.sub()
text = hook_config.text
args.key = 'args.key[keymap]' if 'args.key[keymap]' else args.caps & string.upper() if args.caps & string.upper() else args.keyTRANSPOSE_TEXT_INPUT(0)
if (string.len(text.ref_value[text.ref_table]) > 0) & (args.key == 'BACKSPACE'):MODIFY_TEXT_INPUT()TRANSPOSE_TEXT_INPUT()
elif (string.len(text.ref_value[text.ref_table]) > 0) & (args.key == 'DELETE'):MODIFY_TEXT_INPUT()TRANSPOSE_TEXT_INPUT(0)
elif args.key == 'RETURN':
    if hook.config.ref_table.callback:hook.config.ref_table.callback()
    hook.parent.parent.config.colour = hook_config.colour
    temp_colour = copy_table()
    '1[hook_config.colour]' = '1[G.C.WHITE]'
    '2[hook_config.colour]' = '2[G.C.WHITE]'
    '3[hook_config.colour]' = '3[G.C.WHITE]'ease_colour()
    G.CONTROLLER.text_input_hook = 'None'
elif args.key == 'LEFT':TRANSPOSE_TEXT_INPUT()
elif args.key == 'RIGHT':TRANSPOSE_TEXT_INPUT(1)
elif (hook_config.max_length > string.len(text.ref_value[text.ref_table])) & (string.len() == 1) & string.find(corpus):MODIFY_TEXT_INPUT()TRANSPOSE_TEXT_INPUT(1)
def GET_TEXT_FROM_INPUT():
    new_text = ''
    hook = G.CONTROLLER.text_input_hook
    for i in range(1, len(hook.children), ):
        if 'i[hook.children]'.config & ('i[hook.children]'.config.id.sub(1, 7) == 'letter_') & ('i[hook.children]'.config.text != ''):
            new_text = new_text + 'i[hook.children]'.config.text
    return new_text
def MODIFY_TEXT_INPUT(args):
    args = args if args else {}
    if args.delete & (args.pos > 0):
        if args.pos >= len(args.text_table.letters):
            'args.pos[args.text_table.letters]' = ''
        else:
            'args.pos[args.text_table.letters]' = 'args.pos + 1[args.text_table.letters]'MODIFY_TEXT_INPUT()
        return False
    swapped_letter = 'args.pos[args.text_table.letters]'
    'args.pos[args.text_table.letters]' = args.letter
    if swapped_letter & (swapped_letter != ''):MODIFY_TEXT_INPUT()
def TRANSPOSE_TEXT_INPUT(amount):
    position_child = 'None'
    hook = G.CONTROLLER.text_input_hook
    text = G.CONTROLLER.text_input_hook.config.ref_table.text
    for i in range(1, len(hook.children), ):
        if 'i[hook.children]'.config:
            if 'i[hook.children]'.config.id == 'position':
                position_child = i';'
                break
    dir = amount / math.abs(amount) if amount / math.abs(amount) else 0
    while amount != 0:
        if position_child + dir < 1 if position_child + dir < 1 else position_child + dir >= len(hook.children):
            break
        real_letter = ('position_child + dir[hook.children]'.config.id.sub(1, 7) == 'letter_') & ('position_child + dir[hook.children]'.config.text != '')SWAP()
        if real_letter:
            amount = amount - dir
        position_child = position_child + dir
    else:
    text.current_position = math.min()hook.UIBox.recalculate(True)
    'text.ref_value[text.ref_table]' = GET_TEXT_FROM_INPUT()
G.FUNCS.can_apply_window_changes = lambda e: 
can_apply = False
if G.SETTINGS.QUEUED_CHANGE:
    if G.SETTINGS.QUEUED_CHANGE.screenmode & (G.SETTINGS.QUEUED_CHANGE.screenmode != G.SETTINGS.WINDOW.screenmode):
        can_apply = True
    elif G.SETTINGS.QUEUED_CHANGE.screenres:
        can_apply = True
    elif G.SETTINGS.QUEUED_CHANGE.vsync:
        can_apply = True
    elif G.SETTINGS.QUEUED_CHANGE.selected_display & (G.SETTINGS.QUEUED_CHANGE.selected_display != G.SETTINGS.WINDOW.selected_display):
        can_apply = True
if can_apply:
    e.config.button = 'apply_window_changes'
    e.config.colour = G.C.RED
else:
    e.config.button = 'None'
    e.config.colour = G.C.UI.BACKGROUND_INACTIVE
G.FUNCS.apply_window_changes = lambda _initial: 
G.SETTINGS.WINDOW.screenmode = (G.SETTINGS.QUEUED_CHANGE & G.SETTINGS.QUEUED_CHANGE.screenmode if G.SETTINGS.QUEUED_CHANGE & G.SETTINGS.QUEUED_CHANGE.screenmode else G.SETTINGS.WINDOW.screenmode) if (G.SETTINGS.QUEUED_CHANGE & G.SETTINGS.QUEUED_CHANGE.screenmode if G.SETTINGS.QUEUED_CHANGE & G.SETTINGS.QUEUED_CHANGE.screenmode else G.SETTINGS.WINDOW.screenmode) else 'Windowed'
G.SETTINGS.WINDOW.selected_display = (G.SETTINGS.QUEUED_CHANGE & G.SETTINGS.QUEUED_CHANGE.selected_display if G.SETTINGS.QUEUED_CHANGE & G.SETTINGS.QUEUED_CHANGE.selected_display else G.SETTINGS.WINDOW.selected_display) if (G.SETTINGS.QUEUED_CHANGE & G.SETTINGS.QUEUED_CHANGE.selected_display if G.SETTINGS.QUEUED_CHANGE & G.SETTINGS.QUEUED_CHANGE.selected_display else G.SETTINGS.WINDOW.selected_display) else 1
'G.SETTINGS.WINDOW.selected_display[G.SETTINGS.WINDOW.DISPLAYS]'.screen_res = {'w': (G.SETTINGS.QUEUED_CHANGE & G.SETTINGS.QUEUED_CHANGE.screenres & G.SETTINGS.QUEUED_CHANGE.screenres.w if G.SETTINGS.QUEUED_CHANGE & G.SETTINGS.QUEUED_CHANGE.screenres & G.SETTINGS.QUEUED_CHANGE.screenres.w else G.SETTINGS.screen_res & G.SETTINGS.screen_res.w) if (G.SETTINGS.QUEUED_CHANGE & G.SETTINGS.QUEUED_CHANGE.screenres & G.SETTINGS.QUEUED_CHANGE.screenres.w if G.SETTINGS.QUEUED_CHANGE & G.SETTINGS.QUEUED_CHANGE.screenres & G.SETTINGS.QUEUED_CHANGE.screenres.w else G.SETTINGS.screen_res & G.SETTINGS.screen_res.w) else love.graphics.getWidth(), 'h': (G.SETTINGS.QUEUED_CHANGE & G.SETTINGS.QUEUED_CHANGE.screenres & G.SETTINGS.QUEUED_CHANGE.screenres.h if G.SETTINGS.QUEUED_CHANGE & G.SETTINGS.QUEUED_CHANGE.screenres & G.SETTINGS.QUEUED_CHANGE.screenres.h else G.SETTINGS.screen_res & G.SETTINGS.screen_res.h) if (G.SETTINGS.QUEUED_CHANGE & G.SETTINGS.QUEUED_CHANGE.screenres & G.SETTINGS.QUEUED_CHANGE.screenres.h if G.SETTINGS.QUEUED_CHANGE & G.SETTINGS.QUEUED_CHANGE.screenres & G.SETTINGS.QUEUED_CHANGE.screenres.h else G.SETTINGS.screen_res & G.SETTINGS.screen_res.h) else love.graphics.getHeight()}
G.SETTINGS.WINDOW.vsync = (G.SETTINGS.QUEUED_CHANGE & G.SETTINGS.QUEUED_CHANGE.vsync if G.SETTINGS.QUEUED_CHANGE & G.SETTINGS.QUEUED_CHANGE.vsync else G.SETTINGS.WINDOW.vsync) if (G.SETTINGS.QUEUED_CHANGE & G.SETTINGS.QUEUED_CHANGE.vsync if G.SETTINGS.QUEUED_CHANGE & G.SETTINGS.QUEUED_CHANGE.vsync else G.SETTINGS.WINDOW.vsync) else 1love.window.updateMode()
G.SETTINGS.QUEUED_CHANGE = {}
if _initial != True:love.resize()G.save_settings()
if G.OVERLAY_MENU:
    tab_but = G.OVERLAY_MENU.get_UIE_by_ID(tab_but_Video)G.FUNCS.change_tab(tab_but)
def INIT_COLLECTION_CARD_ALERTS():
    for j in range(1, len(G.your_collection), ):
        for _v in ipairs():v.update_alert()
G.FUNCS.RUN_SETUP_check_back = lambda e: 
if G.GAME.viewed_back.name != e.config.id:e.config.object.remove()
    e.config.object = UIBox()
    e.config.id = G.GAME.viewed_back.name
G.FUNCS.RUN_SETUP_check_back_name = lambda e: 
if e.config.object & (G.GAME.viewed_back.name != e.config.id):e.config.object.remove()
    e.config.object = UIBox()
    e.config.id = G.GAME.viewed_back.name
G.FUNCS.RUN_SETUP_check_stake = lambda e: 
if G.GAME.viewed_back.name != e.config.id:e.config.object.remove()
    e.config.object = UIBox()
    e.config.id = G.GAME.viewed_back.name
G.FUNCS.RUN_SETUP_check_stake2 = lambda e: 
if G.viewed_stake != e.config.id:e.config.object.remove()
    e.config.object = UIBox()
    e.config.id = G.viewed_stake
G.FUNCS.RUN_SETUP_check_back_stake_column = lambda e: 
if G.GAME.viewed_back.name != e.config.id:e.config.object.remove()
    e.config.object = UIBox()
    e.config.id = G.GAME.viewed_back.name
G.FUNCS.RUN_SETUP_check_back_stake_highlight = lambda e: 
if (G.viewed_stake == e.config.id) & e.config.outline < 0.1:
    e.config.outline = 0.8
elif (G.viewed_stake != e.config.id) & (e.config.outline > 0.1):
    e.config.outline = 0
G.FUNCS.change_tab = lambda e: 
if not e:
    return False
_infotip_object = G.OVERLAY_MENU.get_UIE_by_ID(overlay_menu_infotip)
if _infotip_object & _infotip_object.config.object:_infotip_object.config.object.remove()
    _infotip_object.config.object = Moveable()
tab_contents = e.UIBox.get_UIE_by_ID(tab_contents)tab_contents.config.object.remove()
tab_contents.config.object = UIBox()tab_contents.UIBox.recalculate()
G.FUNCS.overlay_menu = lambda args: 
if not args:
    return False
if G.OVERLAY_MENU:G.OVERLAY_MENU.remove()
G.CONTROLLER.locks.frame_set = True
G.CONTROLLER.locks.frame = True
G.CONTROLLER.cursor_down.target = 'None'G.CONTROLLER.mod_cursor_context_layer()
args.config = args.config if args.config else {}
args.config = {'align': args.config.align if args.config.align else 'cm', 'offset': args.config.offset if args.config.offset else {'x': 0, 'y': 10}, 'major': args.config.major if args.config.major else G.ROOM_ATTACH, 'bond': 'Weak', 'no_esc': args.config.no_esc}
G.OVERLAY_MENU = True
G.OVERLAY_MENU = UIBox()
G.OVERLAY_MENU.alignment.offset.y = 0
G.ROOM.jiggle = G.ROOM.jiggle + 1G.OVERLAY_MENU.align_to_major()
G.FUNCS.exit_overlay_menu = lambda: 
if not G.OVERLAY_MENU:
    return False
G.CONTROLLER.locks.frame_set = True
G.CONTROLLER.locks.frame = TrueG.CONTROLLER.mod_cursor_context_layer()G.OVERLAY_MENU.remove()
G.OVERLAY_MENU = 'None'
G.VIEWING_DECK = 'None'
G.SETTINGS.paused = FalseG.save_settings()
G.FUNCS.continue_unlock = lambda: G.FUNCS.exit_overlay_menu()G.CONTROLLER.mod_cursor_context_layer()G.E_MANAGER.update(0, True)
G.FUNCS.test_framework = lambda options: 
G.SETTINGS.paused = TrueG.FUNCS.overlay_menu()
G.FUNCS.options = lambda e: 
G.SETTINGS.paused = TrueG.FUNCS.overlay_menu()
G.FUNCS.current_hands = lambda esimple: 
G.SETTINGS.paused = TrueG.FUNCS.overlay_menu()
G.FUNCS.run_info = lambda e: 
G.SETTINGS.paused = TrueG.FUNCS.overlay_menu()
G.FUNCS.deck_info = lambda e: 
G.SETTINGS.paused = True
if G.deck_preview:G.deck_preview.remove()
    G.deck_preview = 'None'G.FUNCS.overlay_menu()
G.FUNCS.settings = lambda einstant: 
G.SETTINGS.paused = TrueG.FUNCS.overlay_menu()
G.FUNCS.show_credits = lambda e: 
G.SETTINGS.paused = TrueG.FUNCS.overlay_menu()
G.FUNCS.language_selection = lambda e: 
G.SETTINGS.paused = TrueG.FUNCS.overlay_menu()
G.FUNCS.your_collection = lambda e: 
G.SETTINGS.paused = TrueG.FUNCS.overlay_menu()
G.FUNCS.your_collection_blinds = lambda e: 
G.SETTINGS.paused = TrueG.FUNCS.overlay_menu()
G.FUNCS.your_collection_jokers = lambda e: 
G.SETTINGS.paused = TrueG.FUNCS.overlay_menu()
G.FUNCS.your_collection_tarots = lambda e: 
G.SETTINGS.paused = TrueG.FUNCS.overlay_menu()
G.FUNCS.your_collection_planets = lambda e: 
G.SETTINGS.paused = TrueG.FUNCS.overlay_menu()
G.FUNCS.your_collection_spectrals = lambda e: 
G.SETTINGS.paused = TrueG.FUNCS.overlay_menu()
G.FUNCS.your_collection_vouchers = lambda e: 
G.SETTINGS.paused = TrueG.FUNCS.overlay_menu()
G.FUNCS.your_collection_enhancements_exit_overlay_menu = lambda e: 
G.SETTINGS.paused = TrueG.FUNCS.overlay_menu()
G.FUNCS.your_collection_enhancements = lambda e: 
G.SETTINGS.paused = TrueG.FUNCS.overlay_menu()
G.FUNCS.your_collection_decks = lambda e: 
G.SETTINGS.paused = TrueG.FUNCS.overlay_menu()
G.FUNCS.your_collection_editions = lambda e: 
G.SETTINGS.paused = TrueG.FUNCS.overlay_menu()
G.FUNCS.your_collection_tags = lambda e: 
G.SETTINGS.paused = TrueG.FUNCS.overlay_menu()
G.FUNCS.your_collection_seals = lambda e: 
G.SETTINGS.paused = TrueG.FUNCS.overlay_menu()
G.FUNCS.your_collection_boosters = lambda e: 
G.SETTINGS.paused = TrueG.FUNCS.overlay_menu()
G.FUNCS.challenge_list = lambda e: 
G.SETTINGS.paused = TrueG.FUNCS.overlay_menu()
if e.config.id == 'from_game_over':
    G.OVERLAY_MENU.config.no_esc = True
G.FUNCS.high_scores = lambda e: 
G.SETTINGS.paused = TrueG.FUNCS.overlay_menu()
G.FUNCS.usage = lambda e: 
G.SETTINGS.paused = TrueG.FUNCS.overlay_menu()
G.FUNCS.setup_run = lambda e: 
G.SETTINGS.paused = TrueG.FUNCS.overlay_menu()
if e.config.id == 'from_game_over' if e.config.id == 'from_game_over' else e.config.id == 'from_game_won':
    G.OVERLAY_MENU.config.no_esc = True
G.FUNCS.wait_for_high_scores = lambda e: 
if G.ARGS.HIGH_SCORE_RESPONSE:e.config.object.remove()
    e.config.object = UIBox()
    G.ARGS.HIGH_SCORE_RESPONSE = 'None'
G.FUNCS.notify_then_setup_run = lambda e: G.OVERLAY_MENU.remove()
G.OVERLAY_MENU = 'None'G.E_MANAGER.add_event()G.E_MANAGER.add_event()
G.FUNCS.change_challenge_description = lambda e: 
if G.OVERLAY_MENU:
    desc_area = G.OVERLAY_MENU.get_UIE_by_ID(challenge_area)
    if desc_area & (desc_area.config.oid != e.config.id):
        if desc_area.config.old_chosen:
            desc_area.config.old_chosen.config.chosen = 'None'
        e.config.chosen = 'vert'
        if desc_area.config.object:desc_area.config.object.remove()
        desc_area.config.object = UIBox()
        desc_area.config.oid = e.config.id
        desc_area.config.old_chosen = e
G.FUNCS.change_challenge_list_page = lambda args: 
if not args if not args else not args.cycle_config:
    return False
if G.OVERLAY_MENU:
    ch_list = G.OVERLAY_MENU.get_UIE_by_ID(challenge_list)
    if ch_list:
        if ch_list.config.object:ch_list.config.object.remove()
        ch_list.config.object = UIBox()G.FUNCS.change_challenge_description()
G.FUNCS.deck_view_challenge = lambda e: G.FUNCS.overlay_menu()
G.FUNCS.profile_select = lambda e: 
G.SETTINGS.paused = True
G.focused_profile = G.SETTINGS.profile
for i in range(1, 3, ):
    if (i != G.focused_profile) & love.filesystem.getInfo():G.load_profile(i)G.load_profile()G.FUNCS.overlay_menu()
G.FUNCS.quit = lambda e: love.event.quit()
G.FUNCS.quit_cta = lambda e: 
G.SETTINGS.paused = True
G.SETTINGS.DEMO.quit_CTA_shown = TrueG.save_progress()G.FUNCS.overlay_menu()
Jimbo = 'None'
if not G.jimboed:
    G.jimboed = TrueG.E_MANAGER.add_event()
G.FUNCS.demo_survey = lambda e: love.system.openURL(https://forms.gle/WX26BHq1AwwV5xyH9)
G.FUNCS.louisf_insta = lambda e: love.system.openURL(https://www.instagram.com/louisfsoundtracks/)
G.FUNCS.wishlist_steam = lambda e: love.system.openURL(https://store.steampowered.com/app/2379780/Balatro/#game_area_purchase)
G.FUNCS.go_to_playbalatro = lambda e: love.system.openURL(https://www.playbalatro.com)
G.FUNCS.go_to_discord = lambda e: love.system.openURL(https://discord.gg/balatro)
G.FUNCS.go_to_discord_loc = lambda e: love.system.openURL(https://discord.com/channels/1116389027176787968/1207803392978853898)
G.FUNCS.loc_survey = lambda e: love.system.openURL(https://forms.gle/pL5tMh1oXLmv8czz9)
G.FUNCS.go_to_twitter = lambda e: love.system.openURL(https://twitter.com/LocalThunk)
G.FUNCS.unlock_this = lambda e: unlock_achievement()
G.FUNCS.reset_achievements = lambda e: 
G.ACHIEVEMENTS = 'None'
G.SETTINGS.ACHIEVEMENTS_EARNED = {}G.save_progress()G.FUNCS.exit_overlay_menu()
G.FUNCS.warn_lang = lambda e: 
_infotip_object = G.OVERLAY_MENU.get_UIE_by_ID(overlay_menu_infotip)
if (_infotip_object.config.set != e.config.ref_table.label) & (not G.F_NO_ACHIEVEMENTS):_infotip_object.config.object.remove()
    _infotip_object.config.object = UIBox()_infotip_object.config.object.UIRoot.juice_up()
    _infotip_object.config.set = e.config.ref_table.label
    e.config.disable_button = TrueG.E_MANAGER.add_event()G.E_MANAGER.add_event()
    e.config.button = 'change_lang'play_sound(tarot2, 1, 0.4)
G.FUNCS.change_lang = lambda e: 
lang = e.config.ref_table
if not lang if not lang else lang == G.LANG:G.FUNCS.exit_overlay_menu()
else:
    G.SETTINGS.language = lang.keyG.set_language()G.E_MANAGER.clear_queue()G.FUNCS.wipe_on()G.E_MANAGER.add_event()G.FUNCS.wipe_off()
G.FUNCS.copy_seed = lambda e: 
if G.F_LOCAL_CLIPBOARD:
    G.CLIPBOARD = G.GAME.pseudorandom.seed
else:love.system.setClipboardText()
G.FUNCS.start_setup_run = lambda e: 
if G.OVERLAY_MENU:G.FUNCS.exit_overlay_menu()
if G.SETTINGS.current_setup == 'New Run':
    if not G.GAME if not G.GAME else (not G.GAME.won) & (not G.GAME.seeded):
        if G.SAVED_GAME != 'None':
            if not G.SAVED_GAME.GAME.won:
                'G.SETTINGS.profile[G.PROFILES]'.high_scores.current_streak.amt = 0G.save_settings()
    _seed = (G.run_setup_seed & G.setup_seed if G.run_setup_seed & G.setup_seed else G.forced_seed) if (G.run_setup_seed & G.setup_seed if G.run_setup_seed & G.setup_seed else G.forced_seed) else 'None'
    _challenge = G.challenge_tab if G.challenge_tab else 'None'
    _stake = (G.forced_stake if G.forced_stake else 'G.SETTINGS.profile[G.PROFILES]'.MEMORY.stake) if (G.forced_stake if G.forced_stake else 'G.SETTINGS.profile[G.PROFILES]'.MEMORY.stake) else 1G.FUNCS.start_run(e)
elif G.SETTINGS.current_setup == 'Continue':
    if G.SAVED_GAME != 'None':G.FUNCS.start_run(None)
G.FUNCS.start_challenge_run = lambda e: 
if G.OVERLAY_MENU:G.FUNCS.exit_overlay_menu()G.FUNCS.start_run(e)
def toggle_seeded_run(e):
    if e.config.object & (not G.run_setup_seed):e.config.object.remove()
        e.config.object = 'None'
    elif (not e.config.object) & G.run_setup_seed:
        e.config.object = UIBox()e.config.object.recalculate()
G.FUNCS.start_tutorial = lambda e: 
if G.OVERLAY_MENU:G.FUNCS.exit_overlay_menu()
G.SETTINGS.tutorial_progress = {'forced_shop': {1: 'j_joker', 2: 'c_empress'}, 'forced_voucher': 'v_grabber', 'forced_tags': {1: 'tag_handy', 2: 'tag_garbage'}, 'hold_parts': {}, 'completed_parts': {}}
G.SETTINGS.tutorial_complete = FalseG.FUNCS.start_run(e)
G.FUNCS.chip_UI_set = lambda e: 
new_chips_text = number_format()
if G.GAME.chips_text != new_chips_text:
    e.config.scale = math.min(0.8)
    G.GAME.chips_text = new_chips_text
G.FUNCS.blind_chip_UI_scale = lambda e: 
if G.GAME.blind & G.GAME.blind.chips:
    e.config.scale = scale_number()
def scale_number(number, scale, max):
    G.E_SWITCH_POINT = G.E_SWITCH_POINT if G.E_SWITCH_POINT else 100000000000
    if not number if not number else type(number) != 'number':
        return scale
    if not max:
        max = 10000
    if number >= G.E_SWITCH_POINT:
        scale = scale * math.floor() / math.floor()
    elif number >= max:
        scale = scale * math.floor() / math.floor()
    return scale
G.FUNCS.hand_mult_UI_set = lambda e: 
new_mult_text = number_format()
if new_mult_text != G.GAME.current_round.current_hand.mult_text:
    G.GAME.current_round.current_hand.mult_text = new_mult_text
    e.config.object.scale = scale_number()e.config.object.update_text()
    if not G.TAROT_INTERRUPT_PULSE:G.FUNCS.text_super_juice(e)
G.FUNCS.hand_chip_UI_set = lambda e: 
new_chip_text = number_format()
if new_chip_text != G.GAME.current_round.current_hand.chip_text:
    G.GAME.current_round.current_hand.chip_text = new_chip_text
    e.config.object.scale = scale_number()e.config.object.update_text()
    if not G.TAROT_INTERRUPT_PULSE:G.FUNCS.text_super_juice(e)
G.FUNCS.hand_chip_total_UI_set = lambda e: 
if G.GAME.current_round.current_hand.chip_total < 1:
    G.GAME.current_round.current_hand.chip_total_text = ''
else:
    new_chip_total_text = number_format()
    if new_chip_total_text != G.GAME.current_round.current_hand.chip_total_text:
        e.config.object.scale = scale_number()
        G.GAME.current_round.current_hand.chip_total_text = new_chip_total_text
        if not G.ARGS.hand_chip_total_UI_set if not G.ARGS.hand_chip_total_UI_set else G.ARGS.hand_chip_total_UI_set < G.GAME.current_round.current_hand.chip_total:G.FUNCS.text_super_juice(e)
        G.ARGS.hand_chip_total_UI_set = G.GAME.current_round.current_hand.chip_total
def text_super_juice(e, _amount):e.config.object.set_quiver()e.config.object.pulse()e.config.object.update_text()e.config.object.align_letters()e.update_object()
G.FUNCS.flame_handler = lambda e: 
G.C.UI_CHIPLICK = G.C.UI_CHIPLICK if G.C.UI_CHIPLICK else {1: 1, 2: 1, 3: 1, 4: 1}
G.C.UI_MULTLICK = G.C.UI_MULTLICK if G.C.UI_MULTLICK else {1: 1, 2: 1, 3: 1, 4: 1}
for i in range(1, 3, ):
    'i[G.C.UI_CHIPLICK]' = math.min()
    'i[G.C.UI_MULTLICK]' = math.min()
G.ARGS.flame_handler = G.ARGS.flame_handler if G.ARGS.flame_handler else {'chips': {'id': 'flame_chips', 'arg_tab': 'chip_flames', 'colour': G.C.UI_CHIPS, 'accent': G.C.UI_CHIPLICK}, 'mult': {'id': 'flame_mult', 'arg_tab': 'mult_flames', 'colour': G.C.UI_MULT, 'accent': G.C.UI_MULTLICK}}
for kv in pairs():
    if e.config.id == v.id:
        if not e.config.object.is(Sprite) if not e.config.object.is(Sprite) else e.config.object.ID != v.ID:e.config.object.remove()
            e.config.object = Sprite(0, 0, 2.5, 2.5, "ui_1"[G.ASSET_ATLAS])
            v.ID = e.config.object.ID
            'v.arg_tab[G.ARGS]' = {'intensity': 0, 'real_intensity': 0, 'intensity_vel': 0, 'colour_1': v.colour, 'colour_2': v.accent, 'timer': G.TIMERS.REAL}e.config.object.set_alignment()e.config.object.define_draw_steps()e.config.object.get_pos_pixel()
        _F = 'v.arg_tab[G.ARGS]'
        exptime = math.exp()
        if (G.ARGS.score_intensity.earned_score >= G.ARGS.score_intensity.required_score) & (G.ARGS.score_intensity.required_score > 0):
            _F.intensity = (G.pack_cards & (not G.pack_cards.REMOVED) if G.pack_cards & (not G.pack_cards.REMOVED) else G.TAROT_INTERRUPT) & 0 if (G.pack_cards & (not G.pack_cards.REMOVED) if G.pack_cards & (not G.pack_cards.REMOVED) else G.TAROT_INTERRUPT) & 0 else math.max(0.0)
        else:
            _F.intensity = 0
        _F.timer = _F.timer + G.real_dt * (1 + _F.intensity * 0.2)
        if _F.intensity_vel < 0:
            _F.intensity_vel = _F.intensity_vel * (1 - 10 * G.real_dt)
        _F.intensity_vel = (1 - exptime) * (_F.intensity - _F.real_intensity) * G.real_dt * 25 + exptime * _F.intensity_vel
        _F.real_intensity = math.max(0)
        _F.change = (_F.change if _F.change else 0) * (1 - 4.0 * G.real_dt) + 4.0 * G.real_dt * (_F.real_intensity < _F.intensity - 0.0 & 1 if _F.real_intensity < _F.intensity - 0.0 & 1 else 0) * _F.real_intensity
G.FUNCS.hand_text_UI_set = lambda e: 
if G.GAME.current_round.current_hand.handname != G.GAME.current_round.current_hand.handname_text:
    G.GAME.current_round.current_hand.handname_text = G.GAME.current_round.current_hand.handname
    if G.GAME.current_round.current_hand.handname.len() >= 13:
        e.config.object.scale = 12 * 0.56 / G.GAME.current_round.current_hand.handname.len()
    else:
        e.config.object.scale = 2.4 / math.sqrt()e.config.object.update_text()
G.FUNCS.can_play = lambda e: 
if len((G.hand.highlighted <= 0 if G.hand.highlighted <= 0 else G.GAME.blind.block_play) if (G.hand.highlighted <= 0 if G.hand.highlighted <= 0 else G.GAME.blind.block_play) else len(G.hand.highlighted > 5)):
    e.config.colour = G.C.UI.BACKGROUND_INACTIVE
    e.config.button = 'None'
else:
    e.config.colour = G.C.BLUE
    e.config.button = 'play_cards_from_highlighted'
G.FUNCS.can_start_run = lambda e: 
if not G.GAME.viewed_back.effect.center.unlocked:
    e.config.colour = G.C.UI.BACKGROUND_INACTIVE
    e.config.button = 'None'
else:
    e.config.colour = G.C.BLUE
    e.config.button = 'start_setup_run'
G.FUNCS.visible_blind = lambda e: 
if next():
    e.states.visible = True
else:
    e.states.visible = False
G.FUNCS.can_reroll = lambda e: 
if G.GAME.dollars - G.GAME.bankrupt_at - G.GAME.current_round.reroll_cost < 0 & (G.GAME.current_round.reroll_cost != 0):
    e.config.colour = G.C.UI.BACKGROUND_INACTIVE
    e.config.button = 'None'
else:
    e.config.colour = G.C.GREEN
    e.config.button = 'reroll_shop'
G.FUNCS.can_discard = lambda e: 
if G.GAME.current_round.discards_left <= 0 if G.GAME.current_round.discards_left <= 0 else len(G.hand.highlighted <= 0):
    e.config.colour = G.C.UI.BACKGROUND_INACTIVE
    e.config.button = 'None'
else:
    e.config.colour = G.C.RED
    e.config.button = 'discard_cards_from_highlighted'
G.FUNCS.can_use_consumeable = lambda e: 
if e.config.ref_table.can_use_consumeable():
    e.config.colour = G.C.RED
    e.config.button = 'use_card'
else:
    e.config.colour = G.C.UI.BACKGROUND_INACTIVE
    e.config.button = 'None'
G.FUNCS.can_select_card = lambda e: 
if (e.config.ref_table.ability.set != 'Joker' if e.config.ref_table.ability.set != 'Joker' else e.config.ref_table.edition & e.config.ref_table.edition.negative) if (e.config.ref_table.ability.set != 'Joker' if e.config.ref_table.ability.set != 'Joker' else e.config.ref_table.edition & e.config.ref_table.edition.negative) else len(G.jokers.cards < G.jokers.config.card_limit):
    e.config.colour = G.C.GREEN
    e.config.button = 'use_card'
else:
    e.config.colour = G.C.UI.BACKGROUND_INACTIVE
    e.config.button = 'None'
G.FUNCS.can_sell_card = lambda e: 
if e.config.ref_table.can_sell_card():
    e.config.colour = G.C.GREEN
    e.config.button = 'sell_card'
else:
    e.config.colour = G.C.UI.BACKGROUND_INACTIVE
    e.config.button = 'None'
G.FUNCS.can_skip_booster = lambda e: 
if G.pack_cards & '1[G.pack_cards.cards]' & (((G.STATE == G.STATES.PLANET_PACK if G.STATE == G.STATES.PLANET_PACK else G.STATE == G.STATES.STANDARD_PACK) if (G.STATE == G.STATES.PLANET_PACK if G.STATE == G.STATES.PLANET_PACK else G.STATE == G.STATES.STANDARD_PACK) else G.STATE == G.STATES.BUFFOON_PACK) if ((G.STATE == G.STATES.PLANET_PACK if G.STATE == G.STATES.PLANET_PACK else G.STATE == G.STATES.STANDARD_PACK) if (G.STATE == G.STATES.PLANET_PACK if G.STATE == G.STATES.PLANET_PACK else G.STATE == G.STATES.STANDARD_PACK) else G.STATE == G.STATES.BUFFOON_PACK) else G.hand & ('1[G.hand.cards]' if '1[G.hand.cards]' else G.hand.config.card_limit <= 0)):
    e.config.colour = G.C.GREY
    e.config.button = 'skip_booster'
else:
    e.config.colour = G.C.UI.BACKGROUND_INACTIVE
    e.config.button = 'None'
G.FUNCS.show_infotip = lambda e: 
if e.config.ref_table:
    e.children.info = UIBox()e.children.info.align_to_major()
    e.config.ref_table = 'None'
G.FUNCS.use_card = lambda emutenosave: 
e.config.button = 'None'
card = e.config.ref_table
area = card.area
prev_state = G.STATE
dont_dissolve = 'None'
delay_fac = 1
if card.check_use():G.E_MANAGER.add_event()
    return False
if (card.ability.set == 'Booster') & (not nosave) & (G.STATE == G.STATES.SHOP):save_with_action()
G.TAROT_INTERRUPT = G.STATE
if card.ability.set == 'Booster':
    G.GAME.PACK_INTERRUPT = G.STATE
G.STATE = (((((G.STATE == G.STATES.TAROT_PACK) & G.STATES.TAROT_PACK if (G.STATE == G.STATES.TAROT_PACK) & G.STATES.TAROT_PACK else (G.STATE == G.STATES.PLANET_PACK) & G.STATES.PLANET_PACK) if ((G.STATE == G.STATES.TAROT_PACK) & G.STATES.TAROT_PACK if (G.STATE == G.STATES.TAROT_PACK) & G.STATES.TAROT_PACK else (G.STATE == G.STATES.PLANET_PACK) & G.STATES.PLANET_PACK) else (G.STATE == G.STATES.SPECTRAL_PACK) & G.STATES.SPECTRAL_PACK) if (((G.STATE == G.STATES.TAROT_PACK) & G.STATES.TAROT_PACK if (G.STATE == G.STATES.TAROT_PACK) & G.STATES.TAROT_PACK else (G.STATE == G.STATES.PLANET_PACK) & G.STATES.PLANET_PACK) if ((G.STATE == G.STATES.TAROT_PACK) & G.STATES.TAROT_PACK if (G.STATE == G.STATES.TAROT_PACK) & G.STATES.TAROT_PACK else (G.STATE == G.STATES.PLANET_PACK) & G.STATES.PLANET_PACK) else (G.STATE == G.STATES.SPECTRAL_PACK) & G.STATES.SPECTRAL_PACK) else (G.STATE == G.STATES.STANDARD_PACK) & G.STATES.STANDARD_PACK) if ((((G.STATE == G.STATES.TAROT_PACK) & G.STATES.TAROT_PACK if (G.STATE == G.STATES.TAROT_PACK) & G.STATES.TAROT_PACK else (G.STATE == G.STATES.PLANET_PACK) & G.STATES.PLANET_PACK) if ((G.STATE == G.STATES.TAROT_PACK) & G.STATES.TAROT_PACK if (G.STATE == G.STATES.TAROT_PACK) & G.STATES.TAROT_PACK else (G.STATE == G.STATES.PLANET_PACK) & G.STATES.PLANET_PACK) else (G.STATE == G.STATES.SPECTRAL_PACK) & G.STATES.SPECTRAL_PACK) if (((G.STATE == G.STATES.TAROT_PACK) & G.STATES.TAROT_PACK if (G.STATE == G.STATES.TAROT_PACK) & G.STATES.TAROT_PACK else (G.STATE == G.STATES.PLANET_PACK) & G.STATES.PLANET_PACK) if ((G.STATE == G.STATES.TAROT_PACK) & G.STATES.TAROT_PACK if (G.STATE == G.STATES.TAROT_PACK) & G.STATES.TAROT_PACK else (G.STATE == G.STATES.PLANET_PACK) & G.STATES.PLANET_PACK) else (G.STATE == G.STATES.SPECTRAL_PACK) & G.STATES.SPECTRAL_PACK) else (G.STATE == G.STATES.STANDARD_PACK) & G.STATES.STANDARD_PACK) else (G.STATE == G.STATES.BUFFOON_PACK) & G.STATES.BUFFOON_PACK) if (((((G.STATE == G.STATES.TAROT_PACK) & G.STATES.TAROT_PACK if (G.STATE == G.STATES.TAROT_PACK) & G.STATES.TAROT_PACK else (G.STATE == G.STATES.PLANET_PACK) & G.STATES.PLANET_PACK) if ((G.STATE == G.STATES.TAROT_PACK) & G.STATES.TAROT_PACK if (G.STATE == G.STATES.TAROT_PACK) & G.STATES.TAROT_PACK else (G.STATE == G.STATES.PLANET_PACK) & G.STATES.PLANET_PACK) else (G.STATE == G.STATES.SPECTRAL_PACK) & G.STATES.SPECTRAL_PACK) if (((G.STATE == G.STATES.TAROT_PACK) & G.STATES.TAROT_PACK if (G.STATE == G.STATES.TAROT_PACK) & G.STATES.TAROT_PACK else (G.STATE == G.STATES.PLANET_PACK) & G.STATES.PLANET_PACK) if ((G.STATE == G.STATES.TAROT_PACK) & G.STATES.TAROT_PACK if (G.STATE == G.STATES.TAROT_PACK) & G.STATES.TAROT_PACK else (G.STATE == G.STATES.PLANET_PACK) & G.STATES.PLANET_PACK) else (G.STATE == G.STATES.SPECTRAL_PACK) & G.STATES.SPECTRAL_PACK) else (G.STATE == G.STATES.STANDARD_PACK) & G.STATES.STANDARD_PACK) if ((((G.STATE == G.STATES.TAROT_PACK) & G.STATES.TAROT_PACK if (G.STATE == G.STATES.TAROT_PACK) & G.STATES.TAROT_PACK else (G.STATE == G.STATES.PLANET_PACK) & G.STATES.PLANET_PACK) if ((G.STATE == G.STATES.TAROT_PACK) & G.STATES.TAROT_PACK if (G.STATE == G.STATES.TAROT_PACK) & G.STATES.TAROT_PACK else (G.STATE == G.STATES.PLANET_PACK) & G.STATES.PLANET_PACK) else (G.STATE == G.STATES.SPECTRAL_PACK) & G.STATES.SPECTRAL_PACK) if (((G.STATE == G.STATES.TAROT_PACK) & G.STATES.TAROT_PACK if (G.STATE == G.STATES.TAROT_PACK) & G.STATES.TAROT_PACK else (G.STATE == G.STATES.PLANET_PACK) & G.STATES.PLANET_PACK) if ((G.STATE == G.STATES.TAROT_PACK) & G.STATES.TAROT_PACK if (G.STATE == G.STATES.TAROT_PACK) & G.STATES.TAROT_PACK else (G.STATE == G.STATES.PLANET_PACK) & G.STATES.PLANET_PACK) else (G.STATE == G.STATES.SPECTRAL_PACK) & G.STATES.SPECTRAL_PACK) else (G.STATE == G.STATES.STANDARD_PACK) & G.STATES.STANDARD_PACK) else (G.STATE == G.STATES.BUFFOON_PACK) & G.STATES.BUFFOON_PACK) else G.STATES.PLAY_TAROT
G.CONTROLLER.locks.use = True
if G.booster_pack & (not G.booster_pack.alignment.offset.py) & (card.ability.consumeable if card.ability.consumeable else not G.GAME.pack_choices & (G.GAME.pack_choices > 1)):
    G.booster_pack.alignment.offset.py = G.booster_pack.alignment.offset.y
    G.booster_pack.alignment.offset.y = G.ROOM.T.y + 29
if G.shop & (not G.shop.alignment.offset.py):
    G.shop.alignment.offset.py = G.shop.alignment.offset.y
    G.shop.alignment.offset.y = G.ROOM.T.y + 29
if G.blind_select & (not G.blind_select.alignment.offset.py):
    G.blind_select.alignment.offset.py = G.blind_select.alignment.offset.y
    G.blind_select.alignment.offset.y = G.ROOM.T.y + 39
if G.round_eval & (not G.round_eval.alignment.offset.py):
    G.round_eval.alignment.offset.py = G.round_eval.alignment.offset.y
    G.round_eval.alignment.offset.y = G.ROOM.T.y + 29
if card.children.use_button:card.children.use_button.remove()';'
    card.children.use_button = 'None'
if card.children.sell_button:card.children.sell_button.remove()';'
    card.children.sell_button = 'None'
if card.children.price:card.children.price.remove()';'
    card.children.price = 'None'
if card.area:card.area.remove_card(card)
if card.ability.consumeable:
    if (G.STATE == G.STATES.TAROT_PACK if G.STATE == G.STATES.TAROT_PACK else G.STATE == G.STATES.PLANET_PACK) if (G.STATE == G.STATES.TAROT_PACK if G.STATE == G.STATES.TAROT_PACK else G.STATE == G.STATES.PLANET_PACK) else G.STATE == G.STATES.SPECTRAL_PACK:
        card.T.x = G.hand.T.x + G.hand.T.w / 2 - card.T.w / 2
        card.T.y = G.hand.T.y + G.hand.T.h / 2 - card.T.h / 2 - 0.5discover_card()
    else:draw_card()delay(0.2)e.config.ref_table.use_consumeable(area)
    for i in range(1, len(G.jokers.cards), ):'i[G.jokers.cards]'.calculate_joker()
elif card.ability.set == 'Enhanced' if card.ability.set == 'Enhanced' else card.ability.set == 'Default':
    G.playing_card = G.playing_card & G.playing_card + 1 if G.playing_card & G.playing_card + 1 else 1G.deck.emplace(card)play_sound(card1, 0.8, 0.6)play_sound(generic1)
    card.playing_card = G.playing_cardplaying_card_joker_effects()card.add_to_deck()table.insert()
    dont_dissolve = True
    delay_fac = 0.2
elif card.ability.set == 'Joker':card.add_to_deck()G.jokers.emplace(card)play_sound(card1, 0.8, 0.6)play_sound(generic1)
    dont_dissolve = True
    delay_fac = 0.2
elif card.ability.set == 'Booster':delay(0.1)
    if card.ability.booster_pos:
        'card.ability.booster_pos[G.GAME.current_round.used_packs]' = 'USED'draw_card()
    if not card.from_tag:
        G.GAME.round_scores.cards_purchased.amt = G.GAME.round_scores.cards_purchased.amt + 1e.config.ref_table.open()
elif card.ability.set == 'Voucher':delay(0.1)draw_card()
    G.GAME.round_scores.cards_purchased.amt = G.GAME.round_scores.cards_purchased.amt + 1e.config.ref_table.redeem()
if card.ability.set == 'Booster':
    G.CONTROLLER.locks.use = False
    G.TAROT_INTERRUPT = 'None'
else:G.E_MANAGER.add_event()
G.FUNCS.sell_card = lambda e: 
card = e.config.ref_tablecard.sell_card()
for i in range(1, len(G.jokers.cards), ):
    if 'i[G.jokers.cards]' != card:'i[G.jokers.cards]'.calculate_joker()
G.FUNCS.can_confirm_contest_name = lambda e: 
if G.SETTINGS.COMP & (G.SETTINGS.COMP.name != ''):
    e.config.colour = G.C.UI.BACKGROUND_INACTIVE
    e.config.button = 'None'
else:
    e.config.colour = G.C.PALE_GREEN
    e.config.button = 'confirm_contest_name'
G.FUNCS.confirm_contest_name = lambda e: 
G.SETTINGS.COMP.submission_name = True
if G.MAIN_MENU_UI:G.MAIN_MENU_UI.remove()
if G.PROFILE_BUTTON:G.PROFILE_BUTTON.remove()set_main_menu_UI()G.save_progress()
G.FILE_HANDLER.force = True
G.FUNCS.change_contest_name = lambda e: 
G.SETTINGS.COMP.name = ''
if G.MAIN_MENU_UI:G.MAIN_MENU_UI.remove()
if G.PROFILE_BUTTON:G.PROFILE_BUTTON.remove()set_main_menu_UI()
G.FUNCS.skip_tutorial_section = lambda e: 
G.OVERLAY_TUTORIAL.skip_steps = True
if G.OVERLAY_TUTORIAL.Jimbo:G.OVERLAY_TUTORIAL.Jimbo.remove()
if G.OVERLAY_TUTORIAL.content:G.OVERLAY_TUTORIAL.content.remove()G.OVERLAY_TUTORIAL.remove()
G.OVERLAY_TUTORIAL = 'None'G.E_MANAGER.clear_queue(tutorial)
if G.SETTINGS.tutorial_progress.section == 'small_blind':
    "'small_blind'[G.SETTINGS.tutorial_progress.completed_parts]" = True
elif G.SETTINGS.tutorial_progress.section == 'big_blind':
    "'big_blind'[G.SETTINGS.tutorial_progress.completed_parts]" = True
    G.SETTINGS.tutorial_progress.forced_tags = 'None'
elif G.SETTINGS.tutorial_progress.section == 'second_hand':
    "'second_hand'[G.SETTINGS.tutorial_progress.completed_parts]" = True
    "'second_hand'[G.SETTINGS.tutorial_progress.hold_parts]" = True
elif G.SETTINGS.tutorial_progress.section == 'first_hand':
    "'first_hand'[G.SETTINGS.tutorial_progress.completed_parts]" = True
    "'first_hand_2'[G.SETTINGS.tutorial_progress.completed_parts]" = True
    "'first_hand_3'[G.SETTINGS.tutorial_progress.completed_parts]" = True
    "'first_hand_4'[G.SETTINGS.tutorial_progress.completed_parts]" = True
    "'first_hand_section'[G.SETTINGS.tutorial_progress.completed_parts]" = True
elif G.SETTINGS.tutorial_progress.section == 'shop':
    "'shop_1'[G.SETTINGS.tutorial_progress.completed_parts]" = True
    G.SETTINGS.tutorial_progress.forced_voucher = 'None'
G.FUNCS.shop_voucher_empty = lambda e: 
if G.shop_vouchers & G.shop_vouchers.cards & ('1[G.shop_vouchers.cards]' if '1[G.shop_vouchers.cards]' else G.GAME.current_round.voucher):
    e.states.visible = False
elif G.SETTINGS.language != 'en-us':
    e.states.visible = False
else:
    e.states.visible = True
G.FUNCS.check_for_buy_space = lambda card: 
if (card.ability.set != 'Voucher') & (card.ability.set != 'Enhanced') & (card.ability.set != 'Default') & (not (card.ability.set == 'Joker') & len(G.jokers.cards < G.jokers.config.card_limit + (card.edition & card.edition.negative & 1 if card.edition & card.edition.negative & 1 else 0))) & (not card.ability.consumeable & len(G.consumeables.cards < G.consumeables.config.card_limit + (card.edition & card.edition.negative & 1 if card.edition & card.edition.negative & 1 else 0))):alert_no_space(card)
    return False
return True
G.FUNCS.buy_from_shop = lambda e: 
c1 = e.config.ref_table
if c1 & c1.is(Card):
    if e.config.id != 'buy_and_use':
        if not G.FUNCS.check_for_buy_space(c1):
            e.disable_button = 'None'
            return FalseG.E_MANAGER.add_event()
G.FUNCS.toggle_shop = lambda e: stop_use()
G.CONTROLLER.locks.toggle_shop = True
if G.shop:
    for i in range(1, len(G.jokers.cards), ):'i[G.jokers.cards]'.calculate_joker()G.E_MANAGER.add_event()G.E_MANAGER.add_event()
G.FUNCS.select_blind = lambda e: stop_use()
if G.blind_select:
    G.GAME.facing_blind = True
    G.blind_prompt_box.get_UIE_by_ID(prompt_dynatext1).config.object.pop_delay = 0G.blind_prompt_box.get_UIE_by_ID(prompt_dynatext1).config.object.pop_out(5)
    G.blind_prompt_box.get_UIE_by_ID(prompt_dynatext2).config.object.pop_delay = 0G.blind_prompt_box.get_UIE_by_ID(prompt_dynatext2).config.object.pop_out(5)G.E_MANAGER.add_event()G.E_MANAGER.add_event()G.E_MANAGER.add_event()
G.FUNCS.skip_booster = lambda e: 
for i in range(1, len(G.jokers.cards), ):'i[G.jokers.cards]'.calculate_joker()G.FUNCS.end_consumeable(e)
G.FUNCS.end_consumeable = lambda edelayfac: 
delayfac = delayfac if delayfac else 1stop_use()
if G.booster_pack:
    if G.booster_pack_sparkles:G.booster_pack_sparkles.fade()
    if G.booster_pack_stars:G.booster_pack_stars.fade()
    if G.booster_pack_meteors:G.booster_pack_meteors.fade()
    G.booster_pack.alignment.offset.y = G.ROOM.T.y + 9G.E_MANAGER.add_event()G.E_MANAGER.add_event()delay()G.E_MANAGER.add_event()
G.FUNCS.blind_choice_handler = lambda e: 
if (not e.config.ref_table.run_info) & G.blind_select & G.blind_select.VT.y < 10 & e.config.id & 'string.lower(e.config.id)[G.blind_select_opts]':
    if e.UIBox.role.xy_bond != 'Weak':e.UIBox.set_role()
    if (e.config.ref_table.deck != 'on') & (e.config.id == G.GAME.blind_on_deck) if (e.config.ref_table.deck != 'on') & (e.config.id == G.GAME.blind_on_deck) else (e.config.ref_table.deck != 'off') & (e.config.id != G.GAME.blind_on_deck):
        _blind_choice = 'string.lower(e.config.id)[G.blind_select_opts]'
        _top_button = e.UIBox.get_UIE_by_ID(select_blind_button)
        _border = '1[e.UIBox.UIRoot.children[1].children]'
        _tag = e.UIBox.get_UIE_by_ID()
        _tag_container = e.UIBox.get_UIE_by_ID(tag_container)
        if _tag_container & (not G.SETTINGS.tutorial_complete) & (not "'shop_1'[G.SETTINGS.tutorial_progress.completed_parts]"):
            _tag_container.states.visible = False
        elif _tag_container:
            _tag_container.states.visible = True
        if e.config.id == G.GAME.blind_on_deck:
            e.config.ref_table.deck = 'on'
            e.config.draw_after = False
            e.config.colour = G.C.CLEAR
            _border.parent.config.outline = 2
            _border.parent.config.outline_colour = G.C.UI.TRANSPARENT_DARK
            _border.config.outline_colour = _border.config.outline & _border.config.outline_colour if _border.config.outline & _border.config.outline_colour else get_blind_main_colour()
            _border.config.outline = 1.5
            _blind_choice.alignment.offset.y = -0.9
            if _tag & _tag_container:
                '2[_tag_container.children]'.config.draw_after = False
                '2[_tag_container.children]'.config.colour = G.C.BLACK
                '2[_tag.children]'.config.button = 'skip_blind'
                _tag.config.outline_colour = adjust_alpha()
                '2[_tag.children]'.config.hover = True
                '2[_tag.children]'.config.colour = G.C.RED
                '1[_tag.children[2].children]'.config.colour = G.C.UI.TEXT_LIGHT
                _sprite = _tag.config.ref_table
                _sprite.config.force_focus = 'None'
            if _top_button:G.E_MANAGER.add_event()
                _top_button.config.button = 'select_blind'
                _top_button.config.colour = G.C.FILTER
                _top_button.config.hover = True
                '1[_top_button.children]'.config.colour = G.C.WHITE
        elif e.config.id != G.GAME.blind_on_deck:
            e.config.ref_table.deck = 'off'
            e.config.draw_after = True
            e.config.colour = adjust_alpha()
            _border.parent.config.outline = 'None'
            _border.parent.config.outline_colour = 'None'
            _border.config.outline_colour = 'None'
            _border.config.outline = 'None'
            _blind_choice.alignment.offset.y = -0.2
            if _tag & _tag_container:
                if 'e.config.id[G.GAME.round_resets.blind_states]' == 'Skipped' if 'e.config.id[G.GAME.round_resets.blind_states]' == 'Skipped' else 'e.config.id[G.GAME.round_resets.blind_states]' == 'Defeated':'2[_tag_container.children]'.set_role()'2[_tag_container.children]'.align(0, 10)'1[_tag_container.children]'.set_role()'1[_tag_container.children]'.align(0, 10)
                if 'e.config.id[G.GAME.round_resets.blind_states]' == 'Skipped':
                    _blind_choice.children.alert = UIBox()
                '2[_tag.children]'.config.button = 'None'
                _tag.config.outline_colour = G.C.UI.BACKGROUND_INACTIVE
                '2[_tag.children]'.config.hover = False
                '2[_tag.children]'.config.colour = G.C.UI.BACKGROUND_INACTIVE
                '1[_tag.children[2].children]'.config.colour = G.C.UI.TEXT_INACTIVE
                _sprite = _tag.config.ref_table
                _sprite.config.force_focus = True
            if _top_button:
                _top_button.config.colour = G.C.UI.BACKGROUND_INACTIVE
                _top_button.config.button = 'None'
                _top_button.config.hover = False
                '1[_top_button.children]'.config.colour = G.C.UI.TEXT_INACTIVE
G.FUNCS.hover_tag_proxy = lambda e: 
if not e.parent if not e.parent else not e.parent.states:
    return False
if (e.states.hover.is if e.states.hover.is else e.parent.states.hover.is) & (e.created_on_pause == G.SETTINGS.paused) & (not e.parent.children.alert):
    _sprite = e.config.ref_table.get_uibox_table()
    e.parent.children.alert = UIBox()_sprite.juice_up(0.05, 0.02)play_sound(paper1)play_sound(tarot2)
    e.parent.children.alert.states.collide.can = False
elif e.parent.children.alert & ((not e.states.collide.is) & (not e.parent.states.collide.is) if (not e.states.collide.is) & (not e.parent.states.collide.is) else e.created_on_pause != G.SETTINGS.paused):e.parent.children.alert.remove()
    e.parent.children.alert = 'None'
G.FUNCS.skip_blind = lambda e: stop_use()
G.CONTROLLER.locks.skip_blind = TrueG.E_MANAGER.add_event()
_tag = e.UIBox.get_UIE_by_ID(tag_container)
G.GAME.skips = (G.GAME.skips if G.GAME.skips else 0) + 1
if _tag:add_tag()
    skipped = skip_to = (G.GAME.blind_on_deck if G.GAME.blind_on_deck else 'Small', ((G.GAME.blind_on_deck == 'Small') & 'Big' if (G.GAME.blind_on_deck == 'Small') & 'Big' else (G.GAME.blind_on_deck == 'Big') & 'Boss') if ((G.GAME.blind_on_deck == 'Small') & 'Big' if (G.GAME.blind_on_deck == 'Small') & 'Big' else (G.GAME.blind_on_deck == 'Big') & 'Boss') else 'Boss')
    'skipped[G.GAME.round_resets.blind_states]' = 'Skipped'
    'skip_to[G.GAME.round_resets.blind_states]' = 'Select'
    G.GAME.blind_on_deck = skip_toplay_sound(generic1)G.E_MANAGER.add_event()
G.FUNCS.reroll_boss_button = lambda e: 
if (G.GAME.dollars - G.GAME.bankrupt_at - 10 >= 0) & ('"v_retcon"[G.GAME.used_vouchers]' if '"v_retcon"[G.GAME.used_vouchers]' else '"v_directors_cut"[G.GAME.used_vouchers]' & (not G.GAME.round_resets.boss_rerolled)):
    e.config.colour = G.C.RED
    e.config.button = 'reroll_boss'
    '1[e.children[1].children]'.config.shadow = True
    if '2[e.children]':
        '1[e.children[2].children]'.config.shadow = True
else:
    e.config.colour = G.C.UI.BACKGROUND_INACTIVE
    e.config.button = 'None'
    '1[e.children[1].children]'.config.shadow = False
    if '2[e.children]':
        '1[e.children[2].children]'.config.shadow = False
G.FUNCS.reroll_boss = lambda e: stop_use()
G.GAME.round_resets.boss_rerolled = True
if not G.from_boss_tag:ease_dollars()
G.from_boss_tag = 'None'
G.CONTROLLER.locks.boss_reroll = TrueG.E_MANAGER.add_event()G.E_MANAGER.add_event()
G.FUNCS.reroll_shop = lambda e: stop_use()
G.CONTROLLER.locks.shop_reroll = True
if G.CONTROLLER.save_cardarea_focus(shop_jokers):
    G.CONTROLLER.interrupt.focus = True
if G.GAME.current_round.reroll_cost > 0:inc_career_stat(c_shop_dollars_spent)inc_career_stat(c_shop_rerolls, 1)ease_dollars()G.E_MANAGER.add_event()G.E_MANAGER.add_event()G.E_MANAGER.add_event()
G.FUNCS.cash_out = lambda e: stop_use()
if G.round_eval:
    e.config.button = 'None'
    G.round_eval.alignment.offset.y = G.ROOM.T.y + 15
    G.round_eval.alignment.offset.x = 0G.deck.shuffle()G.deck.hard_set_T()delay(0.3)G.E_MANAGER.add_event()ease_dollars()G.E_MANAGER.add_event()play_sound(coin7)
    G.VIBRATION = G.VIBRATION + 1ease_chips(0)
if G.GAME.round_resets.blind_states.Boss == 'Defeated':
    G.GAME.round_resets.blind_ante = G.GAME.round_resets.ante
    G.GAME.round_resets.blind_tags.Small = get_next_tag_key()
    G.GAME.round_resets.blind_tags.Big = get_next_tag_key()reset_blinds()delay(0.6)
G.FUNCS.start_run = lambda eargs: 
G.SETTINGS.paused = True
if e & (e.config.id == 'restart_button'):
    G.GAME.viewed_back = 'None'G.E_MANAGER.clear_queue()G.FUNCS.wipe_on()G.E_MANAGER.add_event()G.E_MANAGER.add_event()G.FUNCS.wipe_off()
G.FUNCS.go_to_menu = lambda e: 
G.SETTINGS.paused = TrueG.E_MANAGER.clear_queue()G.FUNCS.wipe_on()G.E_MANAGER.add_event()G.E_MANAGER.add_event()G.FUNCS.wipe_off()
G.FUNCS.go_to_demo_cta = lambda e: 
G.SETTINGS.paused = TrueG.E_MANAGER.clear_queue(None)play_sound(explosion_buildup1, None, 0.3)play_sound(whoosh1, 0.7, 0.8)play_sound(introPad1, 0.704, 0.8)
G.video_organ = 0.6G.FUNCS.wipe_on(None, True, None)G.E_MANAGER.add_event()G.E_MANAGER.add_event()G.FUNCS.wipe_off()
G.FUNCS.show_main_cta = lambda e: 
if e:
    if (e.config.id == 'lose_cta') & (not G.SETTINGS.DEMO.lose_CTA_shown):
        G.SETTINGS.DEMO.lose_CTA_shown = True
    if (e.config.id == 'win_cta') & (not G.SETTINGS.DEMO.win_CTA_shown):
        G.SETTINGS.DEMO.win_CTA_shown = TrueG.save_progress()
G.SETTINGS.paused = True
G.normal_music_speed = TrueG.FUNCS.overlay_menu()
G.FUNCS.wipe_on = lambda messageno_cardtimefacalt_colour: 
timefac = timefac if timefac else 1
if G.screenwipe:
    return False
G.CONTROLLER.locks.wipe = True
G.STAGE_OBJECT_INTERRUPT = True
colours = {'black': HEX(4f6367FF), 'white': {1: 1, 2: 1, 3: 1, 4: 1}}
if not no_card:
    G.screenwipecard = Card(1, 1)
    G.screenwipecard.sprite_facing = 'back'
    G.screenwipecard.facing = 'back'
    G.screenwipecard.states.hover.can = FalseG.screenwipecard.juice_up(0.5, 1)
message_t = 'None'
if message:
    message_t = {}
    for kv in ipairs(message):table.insert(message_t)
G.screenwipe = UIBox()
G.screenwipe.colours = colours
G.screenwipe.children.particles = Particles(0, 0, 0, 0)
G.STAGE_OBJECT_INTERRUPT = 'None'
G.screenwipe.alignment.offset.y = 0
if message:
    for kv in ipairs():'1[v.children]'.config.object.pulse()G.E_MANAGER.add_event()
G.FUNCS.wipe_off = lambda: G.E_MANAGER.add_event()G.E_MANAGER.add_event()G.E_MANAGER.add_event()G.E_MANAGER.add_event()