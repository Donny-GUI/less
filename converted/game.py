class Game(object):

    def __init__(self):
        G = selfself.set_globals()

    def start_up(self):
        settings = get_compressed(settings.jkr)
        settings_ver = 'None'
        if settings:
            settings_file = STR_UNPACK(settings)
            if (G.VERSION >= '1.0.0') & (love.system.getOS() == 'NOPE') & (not settings_file.version if not settings_file.version else settings_file.version < '1.0.0'):
                for i in range(1, 3, ):love.filesystem.remove()love.filesystem.remove()love.filesystem.remove()love.filesystem.remove()love.filesystem.remove()
                for kv in pairs(settings_file):
                    'k[self.SETTINGS]' = v
                self.SETTINGS.profile = 1
                self.SETTINGS.tutorial_progress = 'None'
            else:
                if G.VERSION < '1.0.0':
                    settings_ver = settings_file.version
                for kv in pairs(settings_file):
                    'k[self.SETTINGS]' = v
        self.SETTINGS.version = settings_ver if settings_ver else G.VERSION
        self.SETTINGS.paused = 'None'
        new_colour_proto = '"SO_"..self.SETTINGS.colourblind_option and 2 or 1[self.C]'
        self.C.SUITS.Hearts = new_colour_proto.Hearts
        self.C.SUITS.Diamonds = new_colour_proto.Diamonds
        self.C.SUITS.Spades = new_colour_proto.Spades
        self.C.SUITS.Clubs = new_colour_proto.Clubsboot_timer(start, settings, 0.1)
        if self.SETTINGS.GRAPHICS.texture_scaling:
            self.SETTINGS.GRAPHICS.texture_scaling = (self.SETTINGS.GRAPHICS.texture_scaling > 1) & 2 if (self.SETTINGS.GRAPHICS.texture_scaling > 1) & 2 else 1
        if self.SETTINGS.DEMO & (not self.F_CTA):
            self.SETTINGS.DEMO = {'total_uptime': 0, 'timed_CTA_shown': True, 'win_CTA_shown': True, 'quit_CTA_shown': True}
        SOURCES = {}
        sound_files = love.filesystem.getDirectoryItems(resources/sounds)
        for _filename in ipairs(sound_files):
            extension = string.sub(filename)
            if extension == '.ogg':
                sound_code = string.sub(filename, 1)
                'sound_code[SOURCES]' = {}
        self.SETTINGS.language = self.SETTINGS.language if self.SETTINGS.language else 'en-us'boot_timer(settings, window init, 0.2)self.init_window()
        if G.F_SOUND_THREAD:boot_timer(window init, soundmanager2)
            self.SOUND_MANAGER = {'thread': love.thread.newThread(engine/sound_manager.lua), 'channel': love.thread.getChannel(sound_request), 'load_channel': love.thread.getChannel(load_channel)}self.SOUND_MANAGER.thread.start(1)
            sound_loaded = prev_file = (False, 'none')
            while (not sound_loaded) & False:
                request = self.SOUND_MANAGER.load_channel.pop()
                if request:
                    if request == 'finished':
                        sound_loaded = True
                    else:boot_timer(request, prev_file)
                        prev_file = requestlove.timer.sleep(0.001)
            else:boot_timer(soundmanager2, savemanager, 0.22)boot_timer(window init, savemanager)
        G.SAVE_MANAGER = {'thread': love.thread.newThread(engine/save_manager.lua), 'channel': love.thread.getChannel(save_request)}G.SAVE_MANAGER.thread.start(2)boot_timer(savemanager, shaders, 0.4)
        G.HTTP_MANAGER = {'thread': love.thread.newThread(engine/http_manager.lua), 'out_channel': love.thread.getChannel(http_request), 'in_channel': love.thread.getChannel(http_response)}
        if G.F_HTTP_SCORES:G.HTTP_MANAGER.thread.start()
        self.SHADERS = {}
        shader_files = love.filesystem.getDirectoryItems(resources/shaders)
        for kfilename in ipairs(shader_files):
            extension = string.sub(filename)
            if extension == '.fs':
                shader_name = string.sub(filename, 1)
                'shader_name[self.SHADERS]' = love.graphics.newShader()boot_timer(shaders, controllers, 0.7)
        self.CONTROLLER = Controller()love.joystick.loadGamepadMappings(resources/gamecontrollerdb.txt)
        if self.F_RUMBLE:
            joysticks = love.joystick.getJoysticks()
            if joysticks:
                if '1[joysticks]':self.CONTROLLER.set_gamepad()boot_timer(controllers, localization, 0.8)
        if self.SETTINGS.GRAPHICS.texture_scaling:
            self.SETTINGS.GRAPHICS.texture_scaling = (self.SETTINGS.GRAPHICS.texture_scaling > 1) & 2 if (self.SETTINGS.GRAPHICS.texture_scaling > 1) & 2 else 1self.load_profile()
        self.SETTINGS.QUEUED_CHANGE = {}
        self.SETTINGS.music_control = {'desired_track': '', 'current_track': '', 'lerp': 1}self.set_render_settings()self.set_language()self.init_item_prototypes()boot_timer(protos, shared sprites, 0.9)
        self.shared_debuff = Sprite(0, 0)
        self.shared_soul = Sprite(0, 0)
        self.shared_undiscovered_joker = Sprite(0, 0)
        self.shared_undiscovered_tarot = Sprite(0, 0)
        self.shared_sticker_eternal = Sprite(0, 0)
        self.shared_sticker_perishable = Sprite(0, 0)
        self.shared_sticker_rental = Sprite(0, 0)
        self.shared_stickers = {'White': Sprite(0, 0), 'Red': Sprite(0, 0), 'Green': Sprite(0, 0), 'Black': Sprite(0, 0), 'Blue': Sprite(0, 0), 'Purple': Sprite(0, 0), 'Orange': Sprite(0, 0), 'Gold': Sprite(0, 0)}
        self.shared_seals = {'Gold': Sprite(0, 0), 'Purple': Sprite(0, 0), 'Red': Sprite(0, 0), 'Blue': Sprite(0, 0)}
        self.sticker_map = {1: 'White', 2: 'Red', 3: 'Green', 4: 'Black', 5: 'Blue', 6: 'Purple', 7: 'Orange', 8: 'Gold'}boot_timer(shared sprites, prep stage, 0.95)
        G.STAGE_OBJECT_INTERRUPT = True
        self.CURSOR = Sprite(0, 0, 0.3, 0.3, 'gamepad_ui'[self.ASSET_ATLAS])
        self.CURSOR.states.collide.can = False
        G.STAGE_OBJECT_INTERRUPT = False
        self.E_MANAGER = EventManager()
        self.SPEEDFACTOR = 1set_profile_progress()boot_timer(prep stage, splash prep, 1)self.splash_screen()boot_timer(splash prep, end, 1)

    def init_item_prototypes(self):
        self.P_SEALS = {'Gold': {'order': 1, 'discovered': True, 'set': 'Seal'}, 'Red': {'order': 2, 'discovered': True, 'set': 'Seal'}, 'Blue': {'order': 3, 'discovered': True, 'set': 'Seal'}, 'Purple': {'order': 4, 'discovered': True, 'set': 'Seal'}}
        self.P_TAGS = {'tag_uncommon': {'name': 'Uncommon Tag', 'set': 'Tag', 'discovered': True, 'min_ante': 'None', 'order': 1, 'config': {'type': 'store_joker_create'}, 'pos': {'x': 0, 'y': 0}}, 'tag_rare': {'name': 'Rare Tag', 'set': 'Tag', 'discovered': True, 'min_ante': 'None', 'order': 2, 'config': {'type': 'store_joker_create', 'odds': 3}, 'requires': 'j_blueprint', 'pos': {'x': 1, 'y': 0}}, 'tag_negative': {'name': 'Negative Tag', 'set': 'Tag', 'discovered': True, 'min_ante': 2, 'order': 3, 'config': {'type': 'store_joker_modify', 'edition': 'negative', 'odds': 5}, 'requires': 'e_negative', 'pos': {'x': 2, 'y': 0}}, 'tag_foil': {'name': 'Foil Tag', 'set': 'Tag', 'discovered': True, 'min_ante': 'None', 'order': 4, 'config': {'type': 'store_joker_modify', 'edition': 'foil', 'odds': 2}, 'requires': 'e_foil', 'pos': {'x': 3, 'y': 0}}, 'tag_holo': {'name': 'Holographic Tag', 'set': 'Tag', 'discovered': True, 'min_ante': 'None', 'order': 5, 'config': {'type': 'store_joker_modify', 'edition': 'holo', 'odds': 3}, 'requires': 'e_holo', 'pos': {'x': 0, 'y': 1}}, 'tag_polychrome': {'name': 'Polychrome Tag', 'set': 'Tag', 'discovered': True, 'min_ante': 'None', 'order': 6, 'config': {'type': 'store_joker_modify', 'edition': 'polychrome', 'odds': 4}, 'requires': 'e_polychrome', 'pos': {'x': 1, 'y': 1}}, 'tag_investment': {'name': 'Investment Tag', 'set': 'Tag', 'discovered': True, 'min_ante': 'None', 'order': 7, 'config': {'type': 'eval', 'dollars': 25}, 'pos': {'x': 2, 'y': 1}}, 'tag_voucher': {'name': 'Voucher Tag', 'set': 'Tag', 'discovered': True, 'min_ante': 'None', 'order': 8, 'config': {'type': 'voucher_add'}, 'pos': {'x': 3, 'y': 1}}, 'tag_boss': {'name': 'Boss Tag', 'set': 'Tag', 'discovered': True, 'min_ante': 'None', 'order': 9, 'config': {'type': 'new_blind_choice'}, 'pos': {'x': 0, 'y': 2}}, 'tag_standard': {'name': 'Standard Tag', 'set': 'Tag', 'discovered': True, 'min_ante': 2, 'order': 10, 'config': {'type': 'new_blind_choice'}, 'pos': {'x': 1, 'y': 2}}, 'tag_charm': {'name': 'Charm Tag', 'set': 'Tag', 'discovered': True, 'min_ante': 'None', 'order': 11, 'config': {'type': 'new_blind_choice'}, 'pos': {'x': 2, 'y': 2}}, 'tag_meteor': {'name': 'Meteor Tag', 'set': 'Tag', 'discovered': True, 'min_ante': 2, 'order': 12, 'config': {'type': 'new_blind_choice'}, 'pos': {'x': 3, 'y': 2}}, 'tag_buffoon': {'name': 'Buffoon Tag', 'set': 'Tag', 'discovered': True, 'min_ante': 2, 'order': 13, 'config': {'type': 'new_blind_choice'}, 'pos': {'x': 4, 'y': 2}}, 'tag_handy': {'name': 'Handy Tag', 'set': 'Tag', 'discovered': True, 'min_ante': 2, 'order': 14, 'config': {'type': 'immediate', 'dollars_per_hand': 1}, 'pos': {'x': 1, 'y': 3}}, 'tag_garbage': {'name': 'Garbage Tag', 'set': 'Tag', 'discovered': True, 'min_ante': 2, 'order': 15, 'config': {'type': 'immediate', 'dollars_per_discard': 1}, 'pos': {'x': 2, 'y': 3}}, 'tag_ethereal': {'name': 'Ethereal Tag', 'set': 'Tag', 'discovered': True, 'min_ante': 2, 'order': 16, 'config': {'type': 'new_blind_choice'}, 'pos': {'x': 3, 'y': 3}}, 'tag_coupon': {'name': 'Coupon Tag', 'set': 'Tag', 'discovered': True, 'min_ante': 'None', 'order': 17, 'config': {'type': 'shop_final_pass'}, 'pos': {'x': 4, 'y': 0}}, 'tag_double': {'name': 'Double Tag', 'set': 'Tag', 'discovered': True, 'min_ante': 'None', 'order': 18, 'config': {'type': 'tag_add'}, 'pos': {'x': 5, 'y': 0}}, 'tag_juggle': {'name': 'Juggle Tag', 'set': 'Tag', 'discovered': True, 'min_ante': 'None', 'order': 19, 'config': {'type': 'round_start_bonus', 'h_size': 3}, 'pos': {'x': 5, 'y': 1}}, 'tag_d_six': {'name': 'D6 Tag', 'set': 'Tag', 'discovered': True, 'min_ante': 'None', 'order': 20, 'config': {'type': 'shop_start'}, 'pos': {'x': 5, 'y': 3}}, 'tag_top_up': {'name': 'Top-up Tag', 'set': 'Tag', 'discovered': True, 'min_ante': 2, 'order': 21, 'config': {'type': 'immediate', 'spawn_jokers': 2}, 'pos': {'x': 4, 'y': 1}}, 'tag_skip': {'name': 'Skip Tag', 'set': 'Tag', 'discovered': True, 'min_ante': 'None', 'order': 22, 'config': {'type': 'immediate', 'skip_bonus': 5}, 'pos': {'x': 0, 'y': 3}}, 'tag_orbital': {'name': 'Orbital Tag', 'set': 'Tag', 'discovered': True, 'min_ante': 2, 'order': 23, 'config': {'type': 'immediate', 'levels': 3}, 'pos': {'x': 5, 'y': 2}}, 'tag_economy': {'name': 'Economy Tag', 'set': 'Tag', 'discovered': True, 'min_ante': 'None', 'order': 24, 'config': {'type': 'immediate', 'max': 40}, 'pos': {'x': 4, 'y': 3}}}
        self.tag_undiscovered = {'name': 'Not Discovered', 'order': 1, 'config': {'type': ''}, 'pos': {'x': 3, 'y': 4}}
        self.P_STAKES = {'stake_white': {'name': 'White Chip', 'unlocked': True, 'order': 1, 'pos': {'x': 0, 'y': 0}, 'stake_level': 1, 'set': 'Stake'}, 'stake_red': {'name': 'Red Chip', 'unlocked': False, 'order': 2, 'pos': {'x': 1, 'y': 0}, 'stake_level': 2, 'set': 'Stake'}, 'stake_green': {'name': 'Green Chip', 'unlocked': False, 'order': 3, 'pos': {'x': 2, 'y': 0}, 'stake_level': 3, 'set': 'Stake'}, 'stake_black': {'name': 'Black Chip', 'unlocked': False, 'order': 4, 'pos': {'x': 4, 'y': 0}, 'stake_level': 4, 'set': 'Stake'}, 'stake_blue': {'name': 'Blue Chip', 'unlocked': False, 'order': 5, 'pos': {'x': 3, 'y': 0}, 'stake_level': 5, 'set': 'Stake'}, 'stake_purple': {'name': 'Purple Chip', 'unlocked': False, 'order': 6, 'pos': {'x': 0, 'y': 1}, 'stake_level': 6, 'set': 'Stake'}, 'stake_orange': {'name': 'Orange Chip', 'unlocked': False, 'order': 7, 'pos': {'x': 1, 'y': 1}, 'stake_level': 7, 'set': 'Stake'}, 'stake_gold': {'name': 'Gold Chip', 'unlocked': False, 'order': 8, 'pos': {'x': 2, 'y': 1}, 'stake_level': 8, 'set': 'Stake'}}
        self.P_BLINDS = {'bl_small': {'name': 'Small Blind', 'defeated': False, 'order': 1, 'dollars': 3, 'mult': 1, 'vars': {}, 'debuff_text': '', 'debuff': {}, 'pos': {'x': 0, 'y': 0}}, 'bl_big': {'name': 'Big Blind', 'defeated': False, 'order': 2, 'dollars': 4, 'mult': 1.5, 'vars': {}, 'debuff_text': '', 'debuff': {}, 'pos': {'x': 0, 'y': 1}}, 'bl_ox': {'name': 'The Ox', 'defeated': False, 'order': 4, 'dollars': 5, 'mult': 2, 'vars': {1: localize(ph_most_played)}, 'debuff': {}, 'pos': {'x': 0, 'y': 2}, 'boss': {'min': 6, 'max': 10}, 'boss_colour': HEX(b95b08)}, 'bl_hook': {'name': 'The Hook', 'defeated': False, 'order': 3, 'dollars': 5, 'mult': 2, 'vars': {}, 'debuff': {}, 'pos': {'x': 0, 'y': 7}, 'boss': {'min': 1, 'max': 10}, 'boss_colour': HEX(a84024)}, 'bl_mouth': {'name': 'The Mouth', 'defeated': False, 'order': 17, 'dollars': 5, 'mult': 2, 'vars': {}, 'debuff': {}, 'pos': {'x': 0, 'y': 18}, 'boss': {'min': 2, 'max': 10}, 'boss_colour': HEX(ae718e)}, 'bl_fish': {'name': 'The Fish', 'defeated': False, 'order': 10, 'dollars': 5, 'mult': 2, 'vars': {}, 'debuff': {}, 'pos': {'x': 0, 'y': 5}, 'boss': {'min': 2, 'max': 10}, 'boss_colour': HEX(3e85bd)}, 'bl_club': {'name': 'The Club', 'defeated': False, 'order': 9, 'dollars': 5, 'mult': 2, 'vars': {}, 'debuff': {'suit': 'Clubs'}, 'pos': {'x': 0, 'y': 4}, 'boss': {'min': 1, 'max': 10}, 'boss_colour': HEX(b9cb92)}, 'bl_manacle': {'name': 'The Manacle', 'defeated': False, 'order': 15, 'dollars': 5, 'mult': 2, 'vars': {}, 'debuff': {}, 'pos': {'x': 0, 'y': 8}, 'boss': {'min': 1, 'max': 10}, 'boss_colour': HEX(575757)}, 'bl_tooth': {'name': 'The Tooth', 'defeated': False, 'order': 23, 'dollars': 5, 'mult': 2, 'vars': {}, 'debuff': {}, 'pos': {'x': 0, 'y': 22}, 'boss': {'min': 3, 'max': 10}, 'boss_colour': HEX(b52d2d)}, 'bl_wall': {'name': 'The Wall', 'defeated': False, 'order': 6, 'dollars': 5, 'mult': 4, 'vars': {}, 'debuff': {}, 'pos': {'x': 0, 'y': 9}, 'boss': {'min': 2, 'max': 10}, 'boss_colour': HEX(8a59a5)}, 'bl_house': {'name': 'The House', 'defeated': False, 'order': 5, 'dollars': 5, 'mult': 2, 'vars': {}, 'debuff': {}, 'pos': {'x': 0, 'y': 3}, 'boss': {'min': 2, 'max': 10}, 'boss_colour': HEX(5186a8)}, 'bl_mark': {'name': 'The Mark', 'defeated': False, 'order': 25, 'dollars': 5, 'mult': 2, 'vars': {}, 'debuff': {}, 'pos': {'x': 0, 'y': 23}, 'boss': {'min': 2, 'max': 10}, 'boss_colour': HEX(6a3847)}, 'bl_final_bell': {'name': 'Cerulean Bell', 'defeated': False, 'order': 30, 'dollars': 8, 'mult': 2, 'vars': {}, 'debuff': {}, 'pos': {'x': 0, 'y': 26}, 'boss': {'showdown': True, 'min': 10, 'max': 10}, 'boss_colour': HEX(009cfd)}, 'bl_wheel': {'name': 'The Wheel', 'defeated': False, 'order': 7, 'dollars': 5, 'mult': 2, 'vars': {}, 'debuff': {}, 'pos': {'x': 0, 'y': 10}, 'boss': {'min': 2, 'max': 10}, 'boss_colour': HEX(50bf7c)}, 'bl_arm': {'name': 'The Arm', 'defeated': False, 'order': 8, 'dollars': 5, 'mult': 2, 'vars': {}, 'debuff': {}, 'pos': {'x': 0, 'y': 11}, 'boss': {'min': 2, 'max': 10}, 'boss_colour': HEX(6865f3)}, 'bl_psychic': {'name': 'The Psychic', 'defeated': False, 'order': 11, 'dollars': 5, 'mult': 2, 'vars': {}, 'debuff': {'h_size_ge': 5}, 'pos': {'x': 0, 'y': 12}, 'boss': {'min': 1, 'max': 10}, 'boss_colour': HEX(efc03c)}, 'bl_goad': {'name': 'The Goad', 'defeated': False, 'order': 12, 'dollars': 5, 'mult': 2, 'vars': {}, 'debuff': {'suit': 'Spades'}, 'pos': {'x': 0, 'y': 13}, 'boss': {'min': 1, 'max': 10}, 'boss_colour': HEX(b95c96)}, 'bl_water': {'name': 'The Water', 'defeated': False, 'order': 13, 'dollars': 5, 'mult': 2, 'vars': {}, 'debuff': {}, 'pos': {'x': 0, 'y': 14}, 'boss': {'min': 2, 'max': 10}, 'boss_colour': HEX(c6e0eb)}, 'bl_eye': {'name': 'The Eye', 'defeated': False, 'order': 16, 'dollars': 5, 'mult': 2, 'vars': {}, 'debuff': {}, 'pos': {'x': 0, 'y': 17}, 'boss': {'min': 3, 'max': 10}, 'boss_colour': HEX(4b71e4)}, 'bl_plant': {'name': 'The Plant', 'defeated': False, 'order': 18, 'dollars': 5, 'mult': 2, 'vars': {}, 'debuff': {'is_face': 'face'}, 'pos': {'x': 0, 'y': 19}, 'boss': {'min': 4, 'max': 10}, 'boss_colour': HEX(709284)}, 'bl_needle': {'name': 'The Needle', 'defeated': False, 'order': 21, 'dollars': 5, 'mult': 1, 'vars': {}, 'debuff': {}, 'pos': {'x': 0, 'y': 20}, 'boss': {'min': 2, 'max': 10}, 'boss_colour': HEX(5c6e31)}, 'bl_head': {'name': 'The Head', 'defeated': False, 'order': 22, 'dollars': 5, 'mult': 2, 'vars': {}, 'debuff': {'suit': 'Hearts'}, 'pos': {'x': 0, 'y': 21}, 'boss': {'min': 1, 'max': 10}, 'boss_colour': HEX(ac9db4)}, 'bl_final_leaf': {'name': 'Verdant Leaf', 'defeated': False, 'order': 27, 'dollars': 8, 'mult': 2, 'vars': {}, 'debuff': {}, 'pos': {'x': 0, 'y': 28}, 'boss': {'showdown': True, 'min': 10, 'max': 10}, 'boss_colour': HEX(56a786)}, 'bl_final_vessel': {'name': 'Violet Vessel', 'defeated': False, 'order': 28, 'dollars': 8, 'mult': 6, 'vars': {}, 'debuff': {}, 'pos': {'x': 0, 'y': 29}, 'boss': {'showdown': True, 'min': 10, 'max': 10}, 'boss_colour': HEX(8a71e1)}, 'bl_window': {'name': 'The Window', 'defeated': False, 'order': 14, 'dollars': 5, 'mult': 2, 'vars': {}, 'debuff': {'suit': 'Diamonds'}, 'pos': {'x': 0, 'y': 6}, 'boss': {'min': 1, 'max': 10}, 'boss_colour': HEX(a9a295)}, 'bl_serpent': {'name': 'The Serpent', 'defeated': False, 'order': 19, 'dollars': 5, 'mult': 2, 'vars': {}, 'debuff': {}, 'pos': {'x': 0, 'y': 15}, 'boss': {'min': 5, 'max': 10}, 'boss_colour': HEX(439a4f)}, 'bl_pillar': {'name': 'The Pillar', 'defeated': False, 'order': 20, 'dollars': 5, 'mult': 2, 'vars': {}, 'debuff': {}, 'pos': {'x': 0, 'y': 16}, 'boss': {'min': 1, 'max': 10}, 'boss_colour': HEX(7e6752)}, 'bl_flint': {'name': 'The Flint', 'defeated': False, 'order': 24, 'dollars': 5, 'mult': 2, 'vars': {}, 'debuff': {}, 'pos': {'x': 0, 'y': 24}, 'boss': {'min': 2, 'max': 10}, 'boss_colour': HEX(e56a2f)}, 'bl_final_acorn': {'name': 'Amber Acorn', 'defeated': False, 'order': 26, 'dollars': 8, 'mult': 2, 'vars': {}, 'debuff': {}, 'pos': {'x': 0, 'y': 27}, 'boss': {'showdown': True, 'min': 10, 'max': 10}, 'boss_colour': HEX(fda200)}, 'bl_final_heart': {'name': 'Crimson Heart', 'defeated': False, 'order': 29, 'dollars': 8, 'mult': 2, 'vars': {}, 'debuff': {}, 'pos': {'x': 0, 'y': 25}, 'boss': {'showdown': True, 'min': 10, 'max': 10}, 'boss_colour': HEX(ac3232)}}
        self.b_undiscovered = {'name': 'Undiscovered', 'debuff_text': 'Defeat this blind to discover', 'pos': {'x': 0, 'y': 30}}
        self.P_CARDS = {'H_2': {'name': '2 of Hearts', 'value': '2', 'suit': 'Hearts', 'pos': {'x': 0, 'y': 0}}, 'H_3': {'name': '3 of Hearts', 'value': '3', 'suit': 'Hearts', 'pos': {'x': 1, 'y': 0}}, 'H_4': {'name': '4 of Hearts', 'value': '4', 'suit': 'Hearts', 'pos': {'x': 2, 'y': 0}}, 'H_5': {'name': '5 of Hearts', 'value': '5', 'suit': 'Hearts', 'pos': {'x': 3, 'y': 0}}, 'H_6': {'name': '6 of Hearts', 'value': '6', 'suit': 'Hearts', 'pos': {'x': 4, 'y': 0}}, 'H_7': {'name': '7 of Hearts', 'value': '7', 'suit': 'Hearts', 'pos': {'x': 5, 'y': 0}}, 'H_8': {'name': '8 of Hearts', 'value': '8', 'suit': 'Hearts', 'pos': {'x': 6, 'y': 0}}, 'H_9': {'name': '9 of Hearts', 'value': '9', 'suit': 'Hearts', 'pos': {'x': 7, 'y': 0}}, 'H_T': {'name': '10 of Hearts', 'value': '10', 'suit': 'Hearts', 'pos': {'x': 8, 'y': 0}}, 'H_J': {'name': 'Jack of Hearts', 'value': 'Jack', 'suit': 'Hearts', 'pos': {'x': 9, 'y': 0}}, 'H_Q': {'name': 'Queen of Hearts', 'value': 'Queen', 'suit': 'Hearts', 'pos': {'x': 10, 'y': 0}}, 'H_K': {'name': 'King of Hearts', 'value': 'King', 'suit': 'Hearts', 'pos': {'x': 11, 'y': 0}}, 'H_A': {'name': 'Ace of Hearts', 'value': 'Ace', 'suit': 'Hearts', 'pos': {'x': 12, 'y': 0}}, 'C_2': {'name': '2 of Clubs', 'value': '2', 'suit': 'Clubs', 'pos': {'x': 0, 'y': 1}}, 'C_3': {'name': '3 of Clubs', 'value': '3', 'suit': 'Clubs', 'pos': {'x': 1, 'y': 1}}, 'C_4': {'name': '4 of Clubs', 'value': '4', 'suit': 'Clubs', 'pos': {'x': 2, 'y': 1}}, 'C_5': {'name': '5 of Clubs', 'value': '5', 'suit': 'Clubs', 'pos': {'x': 3, 'y': 1}}, 'C_6': {'name': '6 of Clubs', 'value': '6', 'suit': 'Clubs', 'pos': {'x': 4, 'y': 1}}, 'C_7': {'name': '7 of Clubs', 'value': '7', 'suit': 'Clubs', 'pos': {'x': 5, 'y': 1}}, 'C_8': {'name': '8 of Clubs', 'value': '8', 'suit': 'Clubs', 'pos': {'x': 6, 'y': 1}}, 'C_9': {'name': '9 of Clubs', 'value': '9', 'suit': 'Clubs', 'pos': {'x': 7, 'y': 1}}, 'C_T': {'name': '10 of Clubs', 'value': '10', 'suit': 'Clubs', 'pos': {'x': 8, 'y': 1}}, 'C_J': {'name': 'Jack of Clubs', 'value': 'Jack', 'suit': 'Clubs', 'pos': {'x': 9, 'y': 1}}, 'C_Q': {'name': 'Queen of Clubs', 'value': 'Queen', 'suit': 'Clubs', 'pos': {'x': 10, 'y': 1}}, 'C_K': {'name': 'King of Clubs', 'value': 'King', 'suit': 'Clubs', 'pos': {'x': 11, 'y': 1}}, 'C_A': {'name': 'Ace of Clubs', 'value': 'Ace', 'suit': 'Clubs', 'pos': {'x': 12, 'y': 1}}, 'D_2': {'name': '2 of Diamonds', 'value': '2', 'suit': 'Diamonds', 'pos': {'x': 0, 'y': 2}}, 'D_3': {'name': '3 of Diamonds', 'value': '3', 'suit': 'Diamonds', 'pos': {'x': 1, 'y': 2}}, 'D_4': {'name': '4 of Diamonds', 'value': '4', 'suit': 'Diamonds', 'pos': {'x': 2, 'y': 2}}, 'D_5': {'name': '5 of Diamonds', 'value': '5', 'suit': 'Diamonds', 'pos': {'x': 3, 'y': 2}}, 'D_6': {'name': '6 of Diamonds', 'value': '6', 'suit': 'Diamonds', 'pos': {'x': 4, 'y': 2}}, 'D_7': {'name': '7 of Diamonds', 'value': '7', 'suit': 'Diamonds', 'pos': {'x': 5, 'y': 2}}, 'D_8': {'name': '8 of Diamonds', 'value': '8', 'suit': 'Diamonds', 'pos': {'x': 6, 'y': 2}}, 'D_9': {'name': '9 of Diamonds', 'value': '9', 'suit': 'Diamonds', 'pos': {'x': 7, 'y': 2}}, 'D_T': {'name': '10 of Diamonds', 'value': '10', 'suit': 'Diamonds', 'pos': {'x': 8, 'y': 2}}, 'D_J': {'name': 'Jack of Diamonds', 'value': 'Jack', 'suit': 'Diamonds', 'pos': {'x': 9, 'y': 2}}, 'D_Q': {'name': 'Queen of Diamonds', 'value': 'Queen', 'suit': 'Diamonds', 'pos': {'x': 10, 'y': 2}}, 'D_K': {'name': 'King of Diamonds', 'value': 'King', 'suit': 'Diamonds', 'pos': {'x': 11, 'y': 2}}, 'D_A': {'name': 'Ace of Diamonds', 'value': 'Ace', 'suit': 'Diamonds', 'pos': {'x': 12, 'y': 2}}, 'S_2': {'name': '2 of Spades', 'value': '2', 'suit': 'Spades', 'pos': {'x': 0, 'y': 3}}, 'S_3': {'name': '3 of Spades', 'value': '3', 'suit': 'Spades', 'pos': {'x': 1, 'y': 3}}, 'S_4': {'name': '4 of Spades', 'value': '4', 'suit': 'Spades', 'pos': {'x': 2, 'y': 3}}, 'S_5': {'name': '5 of Spades', 'value': '5', 'suit': 'Spades', 'pos': {'x': 3, 'y': 3}}, 'S_6': {'name': '6 of Spades', 'value': '6', 'suit': 'Spades', 'pos': {'x': 4, 'y': 3}}, 'S_7': {'name': '7 of Spades', 'value': '7', 'suit': 'Spades', 'pos': {'x': 5, 'y': 3}}, 'S_8': {'name': '8 of Spades', 'value': '8', 'suit': 'Spades', 'pos': {'x': 6, 'y': 3}}, 'S_9': {'name': '9 of Spades', 'value': '9', 'suit': 'Spades', 'pos': {'x': 7, 'y': 3}}, 'S_T': {'name': '10 of Spades', 'value': '10', 'suit': 'Spades', 'pos': {'x': 8, 'y': 3}}, 'S_J': {'name': 'Jack of Spades', 'value': 'Jack', 'suit': 'Spades', 'pos': {'x': 9, 'y': 3}}, 'S_Q': {'name': 'Queen of Spades', 'value': 'Queen', 'suit': 'Spades', 'pos': {'x': 10, 'y': 3}}, 'S_K': {'name': 'King of Spades', 'value': 'King', 'suit': 'Spades', 'pos': {'x': 11, 'y': 3}}, 'S_A': {'name': 'Ace of Spades', 'value': 'Ace', 'suit': 'Spades', 'pos': {'x': 12, 'y': 3}}}
        self.j_locked = {'unlocked': False, 'max': 1, 'name': 'Locked', 'pos': {'x': 8, 'y': 9}, 'set': 'Joker', 'cost_mult': 1.0, 'config': {}}
        self.v_locked = {'unlocked': False, 'max': 1, 'name': 'Locked', 'pos': {'x': 8, 'y': 3}, 'set': 'Voucher', 'cost_mult': 1.0, 'config': {}}
        self.c_locked = {'unlocked': False, 'max': 1, 'name': 'Locked', 'pos': {'x': 4, 'y': 2}, 'set': 'Tarot', 'cost_mult': 1.0, 'config': {}}
        self.j_undiscovered = {'unlocked': False, 'max': 1, 'name': 'Locked', 'pos': {'x': 9, 'y': 9}, 'set': 'Joker', 'cost_mult': 1.0, 'config': {}}
        self.t_undiscovered = {'unlocked': False, 'max': 1, 'name': 'Locked', 'pos': {'x': 6, 'y': 2}, 'set': 'Tarot', 'cost_mult': 1.0, 'config': {}}
        self.p_undiscovered = {'unlocked': False, 'max': 1, 'name': 'Locked', 'pos': {'x': 7, 'y': 2}, 'set': 'Planet', 'cost_mult': 1.0, 'config': {}}
        self.s_undiscovered = {'unlocked': False, 'max': 1, 'name': 'Locked', 'pos': {'x': 5, 'y': 2}, 'set': 'Spectral', 'cost_mult': 1.0, 'config': {}}
        self.v_undiscovered = {'unlocked': False, 'max': 1, 'name': 'Locked', 'pos': {'x': 8, 'y': 2}, 'set': 'Voucher', 'cost_mult': 1.0, 'config': {}}
        self.booster_undiscovered = {'unlocked': False, 'max': 1, 'name': 'Locked', 'pos': {'x': 0, 'y': 5}, 'set': 'Booster', 'cost_mult': 1.0, 'config': {}}
        self.P_CENTERS = {'c_base': {'max': 500, 'freq': 1, 'line': 'base', 'name': 'Default Base', 'pos': {'x': 1, 'y': 0}, 'set': 'Default', 'label': 'Base Card', 'effect': 'Base', 'cost_mult': 1.0, 'config': {}}, 'j_joker': {'order': 1, 'unlocked': True, 'start_alerted': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 1, 'cost': 2, 'name': 'Joker', 'pos': {'x': 0, 'y': 0}, 'set': 'Joker', 'effect': 'Mult', 'cost_mult': 1.0, 'config': {'mult': 4}}, 'j_greedy_joker': {'order': 2, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 1, 'cost': 5, 'name': 'Greedy Joker', 'pos': {'x': 6, 'y': 1}, 'set': 'Joker', 'effect': 'Suit Mult', 'cost_mult': 1.0, 'config': {'extra': {'s_mult': 3, 'suit': 'Diamonds'}}}, 'j_lusty_joker': {'order': 3, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 1, 'cost': 5, 'name': 'Lusty Joker', 'pos': {'x': 7, 'y': 1}, 'set': 'Joker', 'effect': 'Suit Mult', 'cost_mult': 1.0, 'config': {'extra': {'s_mult': 3, 'suit': 'Hearts'}}}, 'j_wrathful_joker': {'order': 4, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 1, 'cost': 5, 'name': 'Wrathful Joker', 'pos': {'x': 8, 'y': 1}, 'set': 'Joker', 'effect': 'Suit Mult', 'cost_mult': 1.0, 'config': {'extra': {'s_mult': 3, 'suit': 'Spades'}}}, 'j_gluttenous_joker': {'order': 5, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 1, 'cost': 5, 'name': 'Gluttonous Joker', 'pos': {'x': 9, 'y': 1}, 'set': 'Joker', 'effect': 'Suit Mult', 'cost_mult': 1.0, 'config': {'extra': {'s_mult': 3, 'suit': 'Clubs'}}}, 'j_jolly': {'order': 6, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 1, 'cost': 3, 'name': 'Jolly Joker', 'pos': {'x': 2, 'y': 0}, 'set': 'Joker', 'effect': 'Type Mult', 'cost_mult': 1.0, 'config': {'t_mult': 8, 'type': 'Pair'}}, 'j_zany': {'order': 7, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 1, 'cost': 4, 'name': 'Zany Joker', 'pos': {'x': 3, 'y': 0}, 'set': 'Joker', 'effect': 'Type Mult', 'cost_mult': 1.0, 'config': {'t_mult': 12, 'type': 'Three of a Kind'}}, 'j_mad': {'order': 8, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 1, 'cost': 4, 'name': 'Mad Joker', 'pos': {'x': 4, 'y': 0}, 'set': 'Joker', 'effect': 'Type Mult', 'cost_mult': 1.0, 'config': {'t_mult': 10, 'type': 'Two Pair'}}, 'j_crazy': {'order': 9, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 1, 'cost': 4, 'name': 'Crazy Joker', 'pos': {'x': 5, 'y': 0}, 'set': 'Joker', 'effect': 'Type Mult', 'cost_mult': 1.0, 'config': {'t_mult': 12, 'type': 'Straight'}}, 'j_droll': {'order': 10, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 1, 'cost': 4, 'name': 'Droll Joker', 'pos': {'x': 6, 'y': 0}, 'set': 'Joker', 'effect': 'Type Mult', 'cost_mult': 1.0, 'config': {'t_mult': 10, 'type': 'Flush'}}, 'j_sly': {'order': 11, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 1, 'cost': 3, 'name': 'Sly Joker', 'set': 'Joker', 'config': {'t_chips': 50, 'type': 'Pair'}, 'pos': {'x': 0, 'y': 14}}, 'j_wily': {'order': 12, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 1, 'cost': 4, 'name': 'Wily Joker', 'set': 'Joker', 'config': {'t_chips': 100, 'type': 'Three of a Kind'}, 'pos': {'x': 1, 'y': 14}}, 'j_clever': {'order': 13, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 1, 'cost': 4, 'name': 'Clever Joker', 'set': 'Joker', 'config': {'t_chips': 80, 'type': 'Two Pair'}, 'pos': {'x': 2, 'y': 14}}, 'j_devious': {'order': 14, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 1, 'cost': 4, 'name': 'Devious Joker', 'set': 'Joker', 'config': {'t_chips': 100, 'type': 'Straight'}, 'pos': {'x': 3, 'y': 14}}, 'j_crafty': {'order': 15, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 1, 'cost': 4, 'name': 'Crafty Joker', 'set': 'Joker', 'config': {'t_chips': 80, 'type': 'Flush'}, 'pos': {'x': 4, 'y': 14}}, 'j_half': {'order': 16, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 1, 'cost': 5, 'name': 'Half Joker', 'pos': {'x': 7, 'y': 0}, 'set': 'Joker', 'effect': 'Hand Size Mult', 'cost_mult': 1.0, 'config': {'extra': {'mult': 20, 'size': 3}}}, 'j_stencil': {'order': 17, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 2, 'cost': 8, 'name': 'Joker Stencil', 'pos': {'x': 2, 'y': 5}, 'set': 'Joker', 'effect': 'Hand Size Mult', 'cost_mult': 1.0, 'config': {}}, 'j_four_fingers': {'order': 18, 'unlocked': True, 'discovered': True, 'blueprint_compat': False, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 2, 'cost': 7, 'name': 'Four Fingers', 'pos': {'x': 6, 'y': 6}, 'set': 'Joker', 'effect': '', 'config': {}}, 'j_mime': {'order': 19, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 2, 'cost': 5, 'name': 'Mime', 'pos': {'x': 4, 'y': 1}, 'set': 'Joker', 'effect': 'Hand card double', 'cost_mult': 1.0, 'config': {'extra': 1}}, 'j_credit_card': {'order': 20, 'unlocked': True, 'discovered': True, 'blueprint_compat': False, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 1, 'cost': 1, 'name': 'Credit Card', 'pos': {'x': 5, 'y': 1}, 'set': 'Joker', 'effect': 'Credit', 'cost_mult': 1.0, 'config': {'extra': 20}}, 'j_ceremonial': {'order': 21, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': False, 'eternal_compat': True, 'rarity': 2, 'cost': 6, 'name': 'Ceremonial Dagger', 'pos': {'x': 5, 'y': 5}, 'set': 'Joker', 'effect': '', 'config': {'mult': 0}}, 'j_banner': {'order': 22, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 1, 'cost': 5, 'name': 'Banner', 'pos': {'x': 1, 'y': 2}, 'set': 'Joker', 'effect': 'Discard Chips', 'cost_mult': 1.0, 'config': {'extra': 30}}, 'j_mystic_summit': {'order': 23, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 1, 'cost': 5, 'name': 'Mystic Summit', 'pos': {'x': 2, 'y': 2}, 'set': 'Joker', 'effect': 'No Discard Mult', 'cost_mult': 1.0, 'config': {'extra': {'mult': 15, 'd_remaining': 0}}}, 'j_marble': {'order': 24, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 2, 'cost': 6, 'name': 'Marble Joker', 'pos': {'x': 3, 'y': 2}, 'set': 'Joker', 'effect': 'Stone card hands', 'cost_mult': 1.0, 'config': {'extra': 1}}, 'j_loyalty_card': {'order': 25, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 2, 'cost': 5, 'name': 'Loyalty Card', 'pos': {'x': 4, 'y': 2}, 'set': 'Joker', 'effect': '1 in 10 mult', 'cost_mult': 1.0, 'config': {'extra': {'Xmult': 4, 'every': 5, 'remaining': '5 remaining'}}}, 'j_8_ball': {'order': 26, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 1, 'cost': 5, 'name': '8 Ball', 'pos': {'x': 0, 'y': 5}, 'set': 'Joker', 'effect': 'Spawn Tarot', 'cost_mult': 1.0, 'config': {'extra': 4}}, 'j_misprint': {'order': 27, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 1, 'cost': 4, 'name': 'Misprint', 'pos': {'x': 6, 'y': 2}, 'set': 'Joker', 'effect': 'Random Mult', 'cost_mult': 1.0, 'config': {'extra': {'max': 23, 'min': 0}}}, 'j_dusk': {'order': 28, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 2, 'cost': 5, 'name': 'Dusk', 'pos': {'x': 4, 'y': 7}, 'set': 'Joker', 'effect': '', 'config': {'extra': 1}, 'unlock_condition': {'type': '', 'extra': '', 'hidden': True}}, 'j_raised_fist': {'order': 29, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 1, 'cost': 5, 'name': 'Raised Fist', 'pos': {'x': 8, 'y': 2}, 'set': 'Joker', 'effect': 'Socialized Mult', 'cost_mult': 1.0, 'config': {}}, 'j_chaos': {'order': 30, 'unlocked': True, 'discovered': True, 'blueprint_compat': False, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 1, 'cost': 4, 'name': 'Chaos the Clown', 'pos': {'x': 1, 'y': 0}, 'set': 'Joker', 'effect': 'Bonus Rerolls', 'cost_mult': 1.0, 'config': {'extra': 1}}, 'j_fibonacci': {'order': 31, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 2, 'cost': 8, 'name': 'Fibonacci', 'pos': {'x': 1, 'y': 5}, 'set': 'Joker', 'effect': 'Card Mult', 'cost_mult': 1.0, 'config': {'extra': 8}}, 'j_steel_joker': {'order': 32, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 2, 'cost': 7, 'name': 'Steel Joker', 'pos': {'x': 7, 'y': 2}, 'set': 'Joker', 'effect': 'Steel Card Buff', 'cost_mult': 1.0, 'config': {'extra': 0.2}, 'enhancement_gate': 'm_steel'}, 'j_scary_face': {'order': 33, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 1, 'cost': 4, 'name': 'Scary Face', 'pos': {'x': 2, 'y': 3}, 'set': 'Joker', 'effect': 'Scary Face Cards', 'cost_mult': 1.0, 'config': {'extra': 30}}, 'j_abstract': {'order': 34, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 1, 'cost': 4, 'name': 'Abstract Joker', 'pos': {'x': 3, 'y': 3}, 'set': 'Joker', 'effect': 'Joker Mult', 'cost_mult': 1.0, 'config': {'extra': 3}}, 'j_delayed_grat': {'order': 35, 'unlocked': True, 'discovered': True, 'blueprint_compat': False, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 1, 'cost': 4, 'name': 'Delayed Gratification', 'pos': {'x': 4, 'y': 3}, 'set': 'Joker', 'effect': 'Discard dollars', 'cost_mult': 1.0, 'config': {'extra': 2}}, 'j_hack': {'order': 36, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 2, 'cost': 6, 'name': 'Hack', 'pos': {'x': 5, 'y': 2}, 'set': 'Joker', 'effect': 'Low Card double', 'cost_mult': 1.0, 'config': {'extra': 1}}, 'j_pareidolia': {'order': 37, 'unlocked': True, 'discovered': True, 'blueprint_compat': False, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 2, 'cost': 5, 'name': 'Pareidolia', 'pos': {'x': 6, 'y': 3}, 'set': 'Joker', 'effect': 'All face cards', 'cost_mult': 1.0, 'config': {}}, 'j_gros_michel': {'order': 38, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': False, 'rarity': 1, 'cost': 5, 'name': 'Gros Michel', 'pos': {'x': 7, 'y': 6}, 'set': 'Joker', 'effect': '', 'config': {'extra': {'odds': 6, 'mult': 15}}, 'no_pool_flag': 'gros_michel_extinct'}, 'j_even_steven': {'order': 39, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 1, 'cost': 4, 'name': 'Even Steven', 'pos': {'x': 8, 'y': 3}, 'set': 'Joker', 'effect': 'Even Card Buff', 'cost_mult': 1.0, 'config': {'extra': 4}}, 'j_odd_todd': {'order': 40, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 1, 'cost': 4, 'name': 'Odd Todd', 'pos': {'x': 9, 'y': 3}, 'set': 'Joker', 'effect': 'Odd Card Buff', 'cost_mult': 1.0, 'config': {'extra': 31}}, 'j_scholar': {'order': 41, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 1, 'cost': 4, 'name': 'Scholar', 'pos': {'x': 0, 'y': 4}, 'set': 'Joker', 'effect': 'Ace Buff', 'cost_mult': 1.0, 'config': {'extra': {'mult': 4, 'chips': 20}}}, 'j_business': {'order': 42, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 1, 'cost': 4, 'name': 'Business Card', 'pos': {'x': 1, 'y': 4}, 'set': 'Joker', 'effect': 'Face Card dollar Chance', 'cost_mult': 1.0, 'config': {'extra': 2}}, 'j_supernova': {'order': 43, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 1, 'cost': 5, 'name': 'Supernova', 'pos': {'x': 2, 'y': 4}, 'set': 'Joker', 'effect': 'Hand played mult', 'cost_mult': 1.0, 'config': {'extra': 1}}, 'j_ride_the_bus': {'order': 44, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': False, 'eternal_compat': True, 'rarity': 1, 'cost': 6, 'name': 'Ride the Bus', 'pos': {'x': 1, 'y': 6}, 'set': 'Joker', 'effect': '', 'config': {'extra': 1}, 'unlock_condition': {'type': 'discard_custom'}}, 'j_space': {'order': 45, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 2, 'cost': 5, 'name': 'Space Joker', 'pos': {'x': 3, 'y': 5}, 'set': 'Joker', 'effect': 'Upgrade Hand chance', 'cost_mult': 1.0, 'config': {'extra': 4}}, 'j_egg': {'order': 46, 'unlocked': True, 'discovered': True, 'blueprint_compat': False, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 1, 'cost': 4, 'name': 'Egg', 'pos': {'x': 0, 'y': 10}, 'set': 'Joker', 'config': {'extra': 3}}, 'j_burglar': {'order': 47, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 2, 'cost': 6, 'name': 'Burglar', 'pos': {'x': 1, 'y': 10}, 'set': 'Joker', 'config': {'extra': 3}}, 'j_blackboard': {'order': 48, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 2, 'cost': 6, 'name': 'Blackboard', 'pos': {'x': 2, 'y': 10}, 'set': 'Joker', 'config': {'extra': 3}}, 'j_runner': {'order': 49, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': False, 'eternal_compat': True, 'rarity': 1, 'cost': 5, 'name': 'Runner', 'pos': {'x': 3, 'y': 10}, 'set': 'Joker', 'config': {'extra': {'chips': 0, 'chip_mod': 15}}}, 'j_ice_cream': {'order': 50, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': False, 'rarity': 1, 'cost': 5, 'name': 'Ice Cream', 'pos': {'x': 4, 'y': 10}, 'set': 'Joker', 'config': {'extra': {'chips': 100, 'chip_mod': 5}}}, 'j_dna': {'order': 51, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 3, 'cost': 8, 'name': 'DNA', 'pos': {'x': 5, 'y': 10}, 'set': 'Joker', 'config': {}}, 'j_splash': {'order': 52, 'unlocked': True, 'discovered': True, 'blueprint_compat': False, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 1, 'cost': 3, 'name': 'Splash', 'pos': {'x': 6, 'y': 10}, 'set': 'Joker', 'config': {}}, 'j_blue_joker': {'order': 53, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 1, 'cost': 5, 'name': 'Blue Joker', 'pos': {'x': 7, 'y': 10}, 'set': 'Joker', 'config': {'extra': 2}}, 'j_sixth_sense': {'order': 54, 'unlocked': True, 'discovered': True, 'blueprint_compat': False, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 2, 'cost': 6, 'name': 'Sixth Sense', 'pos': {'x': 8, 'y': 10}, 'set': 'Joker', 'config': {}}, 'j_constellation': {'order': 55, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': False, 'eternal_compat': True, 'rarity': 2, 'cost': 6, 'name': 'Constellation', 'pos': {'x': 9, 'y': 10}, 'set': 'Joker', 'config': {'extra': 0.1, 'Xmult': 1}}, 'j_hiker': {'order': 56, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 2, 'cost': 5, 'name': 'Hiker', 'pos': {'x': 0, 'y': 11}, 'set': 'Joker', 'config': {'extra': 5}}, 'j_faceless': {'order': 57, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 1, 'cost': 4, 'name': 'Faceless Joker', 'pos': {'x': 1, 'y': 11}, 'set': 'Joker', 'config': {'extra': {'dollars': 5, 'faces': 3}}}, 'j_green_joker': {'order': 58, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': False, 'eternal_compat': True, 'rarity': 1, 'cost': 4, 'name': 'Green Joker', 'pos': {'x': 2, 'y': 11}, 'set': 'Joker', 'config': {'extra': {'hand_add': 1, 'discard_sub': 1}}}, 'j_superposition': {'order': 59, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 1, 'cost': 4, 'name': 'Superposition', 'pos': {'x': 3, 'y': 11}, 'set': 'Joker', 'config': {}}, 'j_todo_list': {'order': 60, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 1, 'cost': 4, 'name': 'To Do List', 'pos': {'x': 4, 'y': 11}, 'set': 'Joker', 'config': {'extra': {'dollars': 4, 'poker_hand': 'High Card'}}}, 'j_cavendish': {'order': 61, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': False, 'rarity': 1, 'cost': 4, 'name': 'Cavendish', 'pos': {'x': 5, 'y': 11}, 'set': 'Joker', 'cost_mult': 1.0, 'config': {'extra': {'odds': 1000, 'Xmult': 3}}, 'yes_pool_flag': 'gros_michel_extinct'}, 'j_card_sharp': {'order': 62, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 2, 'cost': 6, 'name': 'Card Sharp', 'pos': {'x': 6, 'y': 11}, 'set': 'Joker', 'cost_mult': 1.0, 'config': {'extra': {'Xmult': 3}}}, 'j_red_card': {'order': 63, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': False, 'eternal_compat': True, 'rarity': 1, 'cost': 5, 'name': 'Red Card', 'pos': {'x': 7, 'y': 11}, 'set': 'Joker', 'cost_mult': 1.0, 'config': {'extra': 3}}, 'j_madness': {'order': 64, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': False, 'eternal_compat': True, 'rarity': 2, 'cost': 7, 'name': 'Madness', 'pos': {'x': 8, 'y': 11}, 'set': 'Joker', 'cost_mult': 1.0, 'config': {'extra': 0.5}}, 'j_square': {'order': 65, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': False, 'eternal_compat': True, 'rarity': 1, 'cost': 4, 'name': 'Square Joker', 'pos': {'x': 9, 'y': 11}, 'set': 'Joker', 'cost_mult': 1.0, 'config': {'extra': {'chips': 0, 'chip_mod': 4}}}, 'j_seance': {'order': 66, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 2, 'cost': 6, 'name': 'Seance', 'pos': {'x': 0, 'y': 12}, 'set': 'Joker', 'cost_mult': 1.0, 'config': {'extra': {'poker_hand': 'Straight Flush'}}}, 'j_riff_raff': {'order': 67, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 1, 'cost': 6, 'name': 'Riff-raff', 'pos': {'x': 1, 'y': 12}, 'set': 'Joker', 'cost_mult': 1.0, 'config': {'extra': 2}}, 'j_vampire': {'order': 68, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': False, 'eternal_compat': True, 'rarity': 2, 'cost': 7, 'name': 'Vampire', 'set': 'Joker', 'config': {'extra': 0.1, 'Xmult': 1}, 'pos': {'x': 2, 'y': 12}}, 'j_shortcut': {'order': 69, 'unlocked': True, 'discovered': True, 'blueprint_compat': False, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 2, 'cost': 7, 'name': 'Shortcut', 'set': 'Joker', 'config': {}, 'pos': {'x': 3, 'y': 12}}, 'j_hologram': {'order': 70, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': False, 'eternal_compat': True, 'rarity': 2, 'cost': 7, 'name': 'Hologram', 'set': 'Joker', 'config': {'extra': 0.25, 'Xmult': 1}, 'pos': {'x': 4, 'y': 12}, 'soul_pos': {'x': 2, 'y': 9}}, 'j_vagabond': {'order': 71, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 3, 'cost': 8, 'name': 'Vagabond', 'set': 'Joker', 'config': {'extra': 4}, 'pos': {'x': 5, 'y': 12}}, 'j_baron': {'order': 72, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 3, 'cost': 8, 'name': 'Baron', 'set': 'Joker', 'config': {'extra': 1.5}, 'pos': {'x': 6, 'y': 12}}, 'j_cloud_9': {'order': 73, 'unlocked': True, 'discovered': True, 'blueprint_compat': False, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 2, 'cost': 7, 'name': 'Cloud 9', 'set': 'Joker', 'config': {'extra': 1}, 'pos': {'x': 7, 'y': 12}}, 'j_rocket': {'order': 74, 'unlocked': True, 'discovered': True, 'blueprint_compat': False, 'perishable_compat': False, 'eternal_compat': True, 'rarity': 2, 'cost': 6, 'name': 'Rocket', 'set': 'Joker', 'config': {'extra': {'dollars': 1, 'increase': 2}}, 'pos': {'x': 8, 'y': 12}}, 'j_obelisk': {'order': 75, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': False, 'eternal_compat': True, 'rarity': 3, 'cost': 8, 'name': 'Obelisk', 'set': 'Joker', 'config': {'extra': 0.2, 'Xmult': 1}, 'pos': {'x': 9, 'y': 12}}, 'j_midas_mask': {'order': 76, 'unlocked': True, 'discovered': True, 'blueprint_compat': False, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 2, 'cost': 7, 'name': 'Midas Mask', 'set': 'Joker', 'config': {}, 'pos': {'x': 0, 'y': 13}}, 'j_luchador': {'order': 77, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': False, 'rarity': 2, 'cost': 5, 'name': 'Luchador', 'set': 'Joker', 'config': {}, 'pos': {'x': 1, 'y': 13}}, 'j_photograph': {'order': 78, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 1, 'cost': 5, 'name': 'Photograph', 'set': 'Joker', 'config': {'extra': 2}, 'pos': {'x': 2, 'y': 13}}, 'j_gift': {'order': 79, 'unlocked': True, 'discovered': True, 'blueprint_compat': False, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 2, 'cost': 6, 'name': 'Gift Card', 'set': 'Joker', 'config': {'extra': 1}, 'pos': {'x': 3, 'y': 13}}, 'j_turtle_bean': {'order': 80, 'unlocked': True, 'discovered': True, 'blueprint_compat': False, 'perishable_compat': True, 'eternal_compat': False, 'rarity': 2, 'cost': 6, 'name': 'Turtle Bean', 'set': 'Joker', 'config': {'extra': {'h_size': 5, 'h_mod': 1}}, 'pos': {'x': 4, 'y': 13}}, 'j_erosion': {'order': 81, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 2, 'cost': 6, 'name': 'Erosion', 'set': 'Joker', 'config': {'extra': 4}, 'pos': {'x': 5, 'y': 13}}, 'j_reserved_parking': {'order': 82, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 1, 'cost': 6, 'name': 'Reserved Parking', 'set': 'Joker', 'config': {'extra': {'odds': 2, 'dollars': 1}}, 'pos': {'x': 6, 'y': 13}}, 'j_mail': {'order': 83, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 1, 'cost': 4, 'name': 'Mail-In Rebate', 'set': 'Joker', 'config': {'extra': 5}, 'pos': {'x': 7, 'y': 13}}, 'j_to_the_moon': {'order': 84, 'unlocked': True, 'discovered': True, 'blueprint_compat': False, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 2, 'cost': 5, 'name': 'To the Moon', 'set': 'Joker', 'config': {'extra': 1}, 'pos': {'x': 8, 'y': 13}}, 'j_hallucination': {'order': 85, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 1, 'cost': 4, 'name': 'Hallucination', 'set': 'Joker', 'config': {'extra': 2}, 'pos': {'x': 9, 'y': 13}}, 'j_fortune_teller': {'order': 86, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 1, 'cost': 6, 'name': 'Fortune Teller', 'pos': {'x': 7, 'y': 5}, 'set': 'Joker', 'effect': '', 'config': {'extra': 1}}, 'j_juggler': {'order': 87, 'unlocked': True, 'discovered': True, 'blueprint_compat': False, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 1, 'cost': 4, 'name': 'Juggler', 'pos': {'x': 0, 'y': 1}, 'set': 'Joker', 'effect': 'Hand Size', 'cost_mult': 1.0, 'config': {'h_size': 1}}, 'j_drunkard': {'order': 88, 'unlocked': True, 'discovered': True, 'blueprint_compat': False, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 1, 'cost': 4, 'name': 'Drunkard', 'pos': {'x': 1, 'y': 1}, 'set': 'Joker', 'effect': 'Discard Size', 'cost_mult': 1.0, 'config': {'d_size': 1}}, 'j_stone': {'order': 89, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 2, 'cost': 6, 'name': 'Stone Joker', 'pos': {'x': 9, 'y': 0}, 'set': 'Joker', 'effect': 'Stone Card Buff', 'cost_mult': 1.0, 'config': {'extra': 25}, 'enhancement_gate': 'm_stone'}, 'j_golden': {'order': 90, 'unlocked': True, 'discovered': True, 'blueprint_compat': False, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 1, 'cost': 6, 'name': 'Golden Joker', 'pos': {'x': 9, 'y': 2}, 'set': 'Joker', 'effect': 'Bonus dollars', 'cost_mult': 1.0, 'config': {'extra': 4}}, 'j_lucky_cat': {'order': 91, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': False, 'eternal_compat': True, 'rarity': 2, 'cost': 6, 'name': 'Lucky Cat', 'set': 'Joker', 'config': {'Xmult': 1, 'extra': 0.25}, 'pos': {'x': 5, 'y': 14}, 'enhancement_gate': 'm_lucky'}, 'j_baseball': {'order': 92, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 3, 'cost': 8, 'name': 'Baseball Card', 'set': 'Joker', 'config': {'extra': 1.5}, 'pos': {'x': 6, 'y': 14}}, 'j_bull': {'order': 93, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 2, 'cost': 6, 'name': 'Bull', 'set': 'Joker', 'config': {'extra': 2}, 'pos': {'x': 7, 'y': 14}}, 'j_diet_cola': {'order': 94, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': False, 'rarity': 2, 'cost': 6, 'name': 'Diet Cola', 'set': 'Joker', 'config': {}, 'pos': {'x': 8, 'y': 14}}, 'j_trading': {'order': 95, 'unlocked': True, 'discovered': True, 'blueprint_compat': False, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 2, 'cost': 6, 'name': 'Trading Card', 'set': 'Joker', 'config': {'extra': 3}, 'pos': {'x': 9, 'y': 14}}, 'j_flash': {'order': 96, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': False, 'eternal_compat': True, 'rarity': 2, 'cost': 5, 'name': 'Flash Card', 'set': 'Joker', 'config': {'extra': 2, 'mult': 0}, 'pos': {'x': 0, 'y': 15}}, 'j_popcorn': {'order': 97, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': False, 'rarity': 1, 'cost': 5, 'name': 'Popcorn', 'set': 'Joker', 'config': {'mult': 20, 'extra': 4}, 'pos': {'x': 1, 'y': 15}}, 'j_trousers': {'order': 98, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': False, 'eternal_compat': True, 'rarity': 2, 'cost': 6, 'name': 'Spare Trousers', 'set': 'Joker', 'config': {'extra': 2}, 'pos': {'x': 4, 'y': 15}}, 'j_ancient': {'order': 99, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 3, 'cost': 8, 'name': 'Ancient Joker', 'set': 'Joker', 'config': {'extra': 1.5}, 'pos': {'x': 7, 'y': 15}}, 'j_ramen': {'order': 100, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': False, 'rarity': 2, 'cost': 6, 'name': 'Ramen', 'set': 'Joker', 'config': {'Xmult': 2, 'extra': 0.01}, 'pos': {'x': 2, 'y': 15}}, 'j_walkie_talkie': {'order': 101, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 1, 'cost': 4, 'name': 'Walkie Talkie', 'set': 'Joker', 'config': {'extra': {'chips': 10, 'mult': 4}}, 'pos': {'x': 8, 'y': 15}}, 'j_selzer': {'order': 102, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': False, 'rarity': 2, 'cost': 6, 'name': 'Seltzer', 'set': 'Joker', 'config': {'extra': 10}, 'pos': {'x': 3, 'y': 15}}, 'j_castle': {'order': 103, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': False, 'eternal_compat': True, 'rarity': 2, 'cost': 6, 'name': 'Castle', 'set': 'Joker', 'config': {'extra': {'chips': 0, 'chip_mod': 3}}, 'pos': {'x': 9, 'y': 15}}, 'j_smiley': {'order': 104, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 1, 'cost': 4, 'name': 'Smiley Face', 'set': 'Joker', 'config': {'extra': 5}, 'pos': {'x': 6, 'y': 15}}, 'j_campfire': {'order': 105, 'unlocked': True, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 3, 'cost': 9, 'name': 'Campfire', 'set': 'Joker', 'config': {'extra': 0.25}, 'pos': {'x': 5, 'y': 15}}, 'j_ticket': {'order': 106, 'unlocked': False, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 1, 'cost': 5, 'name': 'Golden Ticket', 'pos': {'x': 5, 'y': 3}, 'set': 'Joker', 'effect': 'dollars for Gold cards', 'cost_mult': 1.0, 'config': {'extra': 4}, 'unlock_condition': {'type': 'hand_contents', 'extra': 'Gold'}, 'enhancement_gate': 'm_gold'}, 'j_mr_bones': {'order': 107, 'unlocked': False, 'discovered': True, 'blueprint_compat': False, 'perishable_compat': True, 'eternal_compat': False, 'rarity': 2, 'cost': 5, 'name': 'Mr. Bones', 'pos': {'x': 3, 'y': 4}, 'set': 'Joker', 'effect': 'Prevent Death', 'cost_mult': 1.0, 'config': {}, 'unlock_condition': {'type': 'c_losses', 'extra': 5}}, 'j_acrobat': {'order': 108, 'unlocked': False, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 2, 'cost': 6, 'name': 'Acrobat', 'pos': {'x': 2, 'y': 1}, 'set': 'Joker', 'effect': 'Shop size', 'cost_mult': 1.0, 'config': {'extra': 3}, 'unlock_condition': {'type': 'c_hands_played', 'extra': 200}}, 'j_sock_and_buskin': {'order': 109, 'unlocked': False, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 2, 'cost': 6, 'name': 'Sock and Buskin', 'pos': {'x': 3, 'y': 1}, 'set': 'Joker', 'effect': 'Face card double', 'cost_mult': 1.0, 'config': {'extra': 1}, 'unlock_condition': {'type': 'c_face_cards_played', 'extra': 300}}, 'j_swashbuckler': {'order': 110, 'unlocked': False, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 1, 'cost': 4, 'name': 'Swashbuckler', 'pos': {'x': 9, 'y': 5}, 'set': 'Joker', 'effect': 'Set Mult', 'cost_mult': 1.0, 'config': {'mult': 1}, 'unlock_condition': {'type': 'c_jokers_sold', 'extra': 20}}, 'j_troubadour': {'order': 111, 'unlocked': False, 'discovered': True, 'blueprint_compat': False, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 2, 'cost': 6, 'name': 'Troubadour', 'pos': {'x': 0, 'y': 2}, 'set': 'Joker', 'effect': 'Hand Size, Plays', 'cost_mult': 1.0, 'config': {'extra': {'h_size': 2, 'h_plays': -1}}, 'unlock_condition': {'type': 'round_win', 'extra': 5}}, 'j_certificate': {'order': 112, 'unlocked': False, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 2, 'cost': 6, 'name': 'Certificate', 'pos': {'x': 8, 'y': 8}, 'set': 'Joker', 'effect': '', 'config': {}, 'unlock_condition': {'type': 'double_gold'}}, 'j_smeared': {'order': 113, 'unlocked': False, 'discovered': True, 'blueprint_compat': False, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 2, 'cost': 7, 'name': 'Smeared Joker', 'pos': {'x': 4, 'y': 6}, 'set': 'Joker', 'effect': '', 'config': {}, 'unlock_condition': {'type': 'modify_deck', 'extra': {'count': 3, 'enhancement': 'Wild Card', 'e_key': 'm_wild'}}}, 'j_throwback': {'order': 114, 'unlocked': False, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 2, 'cost': 6, 'name': 'Throwback', 'pos': {'x': 5, 'y': 7}, 'set': 'Joker', 'effect': '', 'config': {'extra': 0.25}, 'unlock_condition': {'type': 'continue_game'}}, 'j_hanging_chad': {'order': 115, 'unlocked': False, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 1, 'cost': 4, 'name': 'Hanging Chad', 'pos': {'x': 9, 'y': 6}, 'set': 'Joker', 'effect': '', 'config': {'extra': 2}, 'unlock_condition': {'type': 'round_win', 'extra': 'High Card'}}, 'j_rough_gem': {'order': 116, 'unlocked': False, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 2, 'cost': 7, 'name': 'Rough Gem', 'pos': {'x': 9, 'y': 7}, 'set': 'Joker', 'effect': '', 'config': {'extra': 1}, 'unlock_condition': {'type': 'modify_deck', 'extra': {'count': 30, 'suit': 'Diamonds'}}}, 'j_bloodstone': {'order': 117, 'unlocked': False, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 2, 'cost': 7, 'name': 'Bloodstone', 'pos': {'x': 0, 'y': 8}, 'set': 'Joker', 'effect': '', 'config': {'extra': {'odds': 2, 'Xmult': 1.5}}, 'unlock_condition': {'type': 'modify_deck', 'extra': {'count': 30, 'suit': 'Hearts'}}}, 'j_arrowhead': {'order': 118, 'unlocked': False, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 2, 'cost': 7, 'name': 'Arrowhead', 'pos': {'x': 1, 'y': 8}, 'set': 'Joker', 'effect': '', 'config': {'extra': 50}, 'unlock_condition': {'type': 'modify_deck', 'extra': {'count': 30, 'suit': 'Spades'}}}, 'j_onyx_agate': {'order': 119, 'unlocked': False, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 2, 'cost': 7, 'name': 'Onyx Agate', 'pos': {'x': 2, 'y': 8}, 'set': 'Joker', 'effect': '', 'config': {'extra': 7}, 'unlock_condition': {'type': 'modify_deck', 'extra': {'count': 30, 'suit': 'Clubs'}}}, 'j_glass': {'order': 120, 'unlocked': False, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': False, 'eternal_compat': True, 'rarity': 2, 'cost': 6, 'name': 'Glass Joker', 'pos': {'x': 1, 'y': 3}, 'set': 'Joker', 'effect': 'Glass Card', 'cost_mult': 1.0, 'config': {'extra': 0.75, 'Xmult': 1}, 'unlock_condition': {'type': 'modify_deck', 'extra': {'count': 5, 'enhancement': 'Glass Card', 'e_key': 'm_glass'}}, 'enhancement_gate': 'm_glass'}, 'j_ring_master': {'order': 121, 'unlocked': False, 'discovered': True, 'blueprint_compat': False, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 2, 'cost': 5, 'name': 'Showman', 'pos': {'x': 6, 'y': 5}, 'set': 'Joker', 'effect': '', 'config': {}, 'unlock_condition': {'type': 'ante_up', 'ante': 4}}, 'j_flower_pot': {'order': 122, 'unlocked': False, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 2, 'cost': 6, 'name': 'Flower Pot', 'pos': {'x': 0, 'y': 6}, 'set': 'Joker', 'effect': '', 'config': {'extra': 3}, 'unlock_condition': {'type': 'ante_up', 'ante': 8}}, 'j_blueprint': {'order': 123, 'unlocked': False, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 3, 'cost': 10, 'name': 'Blueprint', 'pos': {'x': 0, 'y': 3}, 'set': 'Joker', 'effect': 'Copycat', 'cost_mult': 1.0, 'config': {}, 'unlock_condition': {'type': 'win_custom'}}, 'j_wee': {'order': 124, 'unlocked': False, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': False, 'eternal_compat': True, 'rarity': 3, 'cost': 8, 'name': 'Wee Joker', 'pos': {'x': 0, 'y': 0}, 'set': 'Joker', 'effect': '', 'config': {'extra': {'chips': 0, 'chip_mod': 8}}, 'unlock_condition': {'type': 'win', 'n_rounds': 18}}, 'j_merry_andy': {'order': 125, 'unlocked': False, 'discovered': True, 'blueprint_compat': False, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 2, 'cost': 7, 'name': 'Merry Andy', 'pos': {'x': 8, 'y': 0}, 'set': 'Joker', 'effect': '', 'cost_mult': 1.0, 'config': {'d_size': 3, 'h_size': -1}, 'unlock_condition': {'type': 'win', 'n_rounds': 12}}, 'j_oops': {'order': 126, 'unlocked': False, 'discovered': True, 'blueprint_compat': False, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 2, 'cost': 4, 'name': 'Oops! All 6s', 'pos': {'x': 5, 'y': 6}, 'set': 'Joker', 'effect': '', 'config': {}, 'unlock_condition': {'type': 'chip_score', 'chips': 10000}}, 'j_idol': {'order': 127, 'unlocked': False, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 2, 'cost': 6, 'name': 'The Idol', 'pos': {'x': 6, 'y': 7}, 'set': 'Joker', 'effect': '', 'config': {'extra': 2}, 'unlock_condition': {'type': 'chip_score', 'chips': 1000000}}, 'j_seeing_double': {'order': 128, 'unlocked': False, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 2, 'cost': 6, 'name': 'Seeing Double', 'pos': {'x': 4, 'y': 4}, 'set': 'Joker', 'effect': 'X1.5 Mult club 7', 'cost_mult': 1.0, 'config': {'extra': 2}, 'unlock_condition': {'type': 'hand_contents', 'extra': 'four 7 of Clubs'}}, 'j_matador': {'order': 129, 'unlocked': False, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 2, 'cost': 7, 'name': 'Matador', 'pos': {'x': 4, 'y': 5}, 'set': 'Joker', 'effect': '', 'config': {'extra': 8}, 'unlock_condition': {'type': 'round_win'}}, 'j_hit_the_road': {'order': 130, 'unlocked': False, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 3, 'cost': 8, 'name': 'Hit the Road', 'pos': {'x': 8, 'y': 5}, 'set': 'Joker', 'effect': 'Jack Discard Effect', 'cost_mult': 1.0, 'config': {'extra': 0.5}, 'unlock_condition': {'type': 'discard_custom'}}, 'j_duo': {'order': 131, 'unlocked': False, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 3, 'cost': 8, 'name': 'The Duo', 'pos': {'x': 5, 'y': 4}, 'set': 'Joker', 'effect': 'X1.5 Mult', 'cost_mult': 1.0, 'config': {'Xmult': 2, 'type': 'Pair'}, 'unlock_condition': {'type': 'win_no_hand', 'extra': 'Pair'}}, 'j_trio': {'order': 132, 'unlocked': False, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 3, 'cost': 8, 'name': 'The Trio', 'pos': {'x': 6, 'y': 4}, 'set': 'Joker', 'effect': 'X2 Mult', 'cost_mult': 1.0, 'config': {'Xmult': 3, 'type': 'Three of a Kind'}, 'unlock_condition': {'type': 'win_no_hand', 'extra': 'Three of a Kind'}}, 'j_family': {'order': 133, 'unlocked': False, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 3, 'cost': 8, 'name': 'The Family', 'pos': {'x': 7, 'y': 4}, 'set': 'Joker', 'effect': 'X3 Mult', 'cost_mult': 1.0, 'config': {'Xmult': 4, 'type': 'Four of a Kind'}, 'unlock_condition': {'type': 'win_no_hand', 'extra': 'Four of a Kind'}}, 'j_order': {'order': 134, 'unlocked': False, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 3, 'cost': 8, 'name': 'The Order', 'pos': {'x': 8, 'y': 4}, 'set': 'Joker', 'effect': 'X3 Mult', 'cost_mult': 1.0, 'config': {'Xmult': 3, 'type': 'Straight'}, 'unlock_condition': {'type': 'win_no_hand', 'extra': 'Straight'}}, 'j_tribe': {'order': 135, 'unlocked': False, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 3, 'cost': 8, 'name': 'The Tribe', 'pos': {'x': 9, 'y': 4}, 'set': 'Joker', 'effect': 'X3 Mult', 'cost_mult': 1.0, 'config': {'Xmult': 2, 'type': 'Flush'}, 'unlock_condition': {'type': 'win_no_hand', 'extra': 'Flush'}}, 'j_stuntman': {'order': 136, 'unlocked': False, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 3, 'cost': 7, 'name': 'Stuntman', 'pos': {'x': 8, 'y': 6}, 'set': 'Joker', 'effect': '', 'config': {'extra': {'h_size': 2, 'chip_mod': 250}}, 'unlock_condition': {'type': 'chip_score', 'chips': 100000000}}, 'j_invisible': {'order': 137, 'unlocked': False, 'discovered': True, 'blueprint_compat': False, 'perishable_compat': True, 'eternal_compat': False, 'rarity': 3, 'cost': 8, 'name': 'Invisible Joker', 'pos': {'x': 1, 'y': 7}, 'set': 'Joker', 'effect': '', 'config': {'extra': 2}, 'unlock_condition': {'type': 'win_custom'}}, 'j_brainstorm': {'order': 138, 'unlocked': False, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 3, 'cost': 10, 'name': 'Brainstorm', 'pos': {'x': 7, 'y': 7}, 'set': 'Joker', 'effect': 'Copycat', 'config': {}, 'unlock_condition': {'type': 'discard_custom'}}, 'j_satellite': {'order': 139, 'unlocked': False, 'discovered': True, 'blueprint_compat': False, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 2, 'cost': 6, 'name': 'Satellite', 'pos': {'x': 8, 'y': 7}, 'set': 'Joker', 'effect': '', 'config': {'extra': 1}, 'unlock_condition': {'type': 'money', 'extra': 400}}, 'j_shoot_the_moon': {'order': 140, 'unlocked': False, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 1, 'cost': 5, 'name': 'Shoot the Moon', 'pos': {'x': 2, 'y': 6}, 'set': 'Joker', 'effect': '', 'config': {'extra': 13}, 'unlock_condition': {'type': 'play_all_hearts'}}, 'j_drivers_license': {'order': 141, 'unlocked': False, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 3, 'cost': 7, 'name': "Driver's License", 'pos': {'x': 0, 'y': 7}, 'set': 'Joker', 'effect': '', 'config': {'extra': 3}, 'unlock_condition': {'type': 'modify_deck', 'extra': {'count': 16, 'tally': 'total'}}}, 'j_cartomancer': {'order': 142, 'unlocked': False, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 2, 'cost': 6, 'name': 'Cartomancer', 'pos': {'x': 7, 'y': 3}, 'set': 'Joker', 'effect': 'Tarot Buff', 'cost_mult': 1.0, 'config': {}, 'unlock_condition': {'type': 'discover_amount', 'tarot_count': 22}}, 'j_astronomer': {'order': 143, 'unlocked': False, 'discovered': True, 'blueprint_compat': False, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 2, 'cost': 8, 'name': 'Astronomer', 'pos': {'x': 2, 'y': 7}, 'set': 'Joker', 'effect': '', 'config': {}, 'unlock_condition': {'type': 'discover_amount', 'planet_count': 12}}, 'j_burnt': {'order': 144, 'unlocked': False, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 3, 'cost': 8, 'name': 'Burnt Joker', 'pos': {'x': 3, 'y': 7}, 'set': 'Joker', 'effect': '', 'config': {'h_size': 0, 'extra': 4}, 'unlock_condition': {'type': 'c_cards_sold', 'extra': 50}}, 'j_bootstraps': {'order': 145, 'unlocked': False, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 2, 'cost': 7, 'name': 'Bootstraps', 'pos': {'x': 9, 'y': 8}, 'set': 'Joker', 'effect': '', 'config': {'extra': {'mult': 2, 'dollars': 5}}, 'unlock_condition': {'type': 'modify_jokers', 'extra': {'polychrome': True, 'count': 2}}}, 'j_caino': {'order': 146, 'unlocked': False, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 4, 'cost': 20, 'name': 'Caino', 'pos': {'x': 3, 'y': 8}, 'soul_pos': {'x': 3, 'y': 9}, 'set': 'Joker', 'effect': '', 'config': {'extra': 1}, 'unlock_condition': {'type': '', 'extra': '', 'hidden': True}}, 'j_triboulet': {'order': 147, 'unlocked': False, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 4, 'cost': 20, 'name': 'Triboulet', 'pos': {'x': 4, 'y': 8}, 'soul_pos': {'x': 4, 'y': 9}, 'set': 'Joker', 'effect': '', 'config': {'extra': 2}, 'unlock_condition': {'type': '', 'extra': '', 'hidden': True}}, 'j_yorick': {'order': 148, 'unlocked': False, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 4, 'cost': 20, 'name': 'Yorick', 'pos': {'x': 5, 'y': 8}, 'soul_pos': {'x': 5, 'y': 9}, 'set': 'Joker', 'effect': '', 'config': {'extra': {'xmult': 1, 'discards': 23}}, 'unlock_condition': {'type': '', 'extra': '', 'hidden': True}}, 'j_chicot': {'order': 149, 'unlocked': False, 'discovered': True, 'blueprint_compat': False, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 4, 'cost': 20, 'name': 'Chicot', 'pos': {'x': 6, 'y': 8}, 'soul_pos': {'x': 6, 'y': 9}, 'set': 'Joker', 'effect': '', 'config': {}, 'unlock_condition': {'type': '', 'extra': '', 'hidden': True}}, 'j_perkeo': {'order': 150, 'unlocked': False, 'discovered': True, 'blueprint_compat': True, 'perishable_compat': True, 'eternal_compat': True, 'rarity': 4, 'cost': 20, 'name': 'Perkeo', 'pos': {'x': 7, 'y': 8}, 'soul_pos': {'x': 7, 'y': 9}, 'set': 'Joker', 'effect': '', 'config': {}, 'unlock_condition': {'type': '', 'extra': '', 'hidden': True}}, 'c_fool': {'order': 1, 'discovered': True, 'cost': 3, 'consumeable': True, 'name': 'The Fool', 'pos': {'x': 0, 'y': 0}, 'set': 'Tarot', 'effect': 'Disable Blind Effect', 'cost_mult': 1.0, 'config': {}}, 'c_magician': {'order': 2, 'discovered': True, 'cost': 3, 'consumeable': True, 'name': 'The Magician', 'pos': {'x': 1, 'y': 0}, 'set': 'Tarot', 'effect': 'Enhance', 'cost_mult': 1.0, 'config': {'mod_conv': 'm_lucky', 'max_highlighted': 2}}, 'c_high_priestess': {'order': 3, 'discovered': True, 'cost': 3, 'consumeable': True, 'name': 'The High Priestess', 'pos': {'x': 2, 'y': 0}, 'set': 'Tarot', 'effect': 'Round Bonus', 'cost_mult': 1.0, 'config': {'planets': 2}}, 'c_empress': {'order': 4, 'discovered': True, 'cost': 3, 'consumeable': True, 'name': 'The Empress', 'pos': {'x': 3, 'y': 0}, 'set': 'Tarot', 'effect': 'Enhance', 'cost_mult': 1.0, 'config': {'mod_conv': 'm_mult', 'max_highlighted': 2}}, 'c_emperor': {'order': 5, 'discovered': True, 'cost': 3, 'consumeable': True, 'name': 'The Emperor', 'pos': {'x': 4, 'y': 0}, 'set': 'Tarot', 'effect': 'Round Bonus', 'cost_mult': 1.0, 'config': {'tarots': 2}}, 'c_heirophant': {'order': 6, 'discovered': True, 'cost': 3, 'consumeable': True, 'name': 'The Hierophant', 'pos': {'x': 5, 'y': 0}, 'set': 'Tarot', 'effect': 'Enhance', 'cost_mult': 1.0, 'config': {'mod_conv': 'm_bonus', 'max_highlighted': 2}}, 'c_lovers': {'order': 7, 'discovered': True, 'cost': 3, 'consumeable': True, 'name': 'The Lovers', 'pos': {'x': 6, 'y': 0}, 'set': 'Tarot', 'effect': 'Enhance', 'cost_mult': 1.0, 'config': {'mod_conv': 'm_wild', 'max_highlighted': 1}}, 'c_chariot': {'order': 8, 'discovered': True, 'cost': 3, 'consumeable': True, 'name': 'The Chariot', 'pos': {'x': 7, 'y': 0}, 'set': 'Tarot', 'effect': 'Enhance', 'cost_mult': 1.0, 'config': {'mod_conv': 'm_steel', 'max_highlighted': 1}}, 'c_justice': {'order': 9, 'discovered': True, 'cost': 3, 'consumeable': True, 'name': 'Justice', 'pos': {'x': 8, 'y': 0}, 'set': 'Tarot', 'effect': 'Enhance', 'cost_mult': 1.0, 'config': {'mod_conv': 'm_glass', 'max_highlighted': 1}}, 'c_hermit': {'order': 10, 'discovered': True, 'cost': 3, 'consumeable': True, 'name': 'The Hermit', 'pos': {'x': 9, 'y': 0}, 'set': 'Tarot', 'effect': 'Dollar Doubler', 'cost_mult': 1.0, 'config': {'extra': 20}}, 'c_wheel_of_fortune': {'order': 11, 'discovered': True, 'cost': 3, 'consumeable': True, 'name': 'The Wheel of Fortune', 'pos': {'x': 0, 'y': 1}, 'set': 'Tarot', 'effect': 'Round Bonus', 'cost_mult': 1.0, 'config': {'extra': 4}}, 'c_strength': {'order': 12, 'discovered': True, 'cost': 3, 'consumeable': True, 'name': 'Strength', 'pos': {'x': 1, 'y': 1}, 'set': 'Tarot', 'effect': 'Round Bonus', 'cost_mult': 1.0, 'config': {'mod_conv': 'up_rank', 'max_highlighted': 2}}, 'c_hanged_man': {'order': 13, 'discovered': True, 'cost': 3, 'consumeable': True, 'name': 'The Hanged Man', 'pos': {'x': 2, 'y': 1}, 'set': 'Tarot', 'effect': 'Card Removal', 'cost_mult': 1.0, 'config': {'remove_card': True, 'max_highlighted': 2}}, 'c_death': {'order': 14, 'discovered': True, 'cost': 3, 'consumeable': True, 'name': 'Death', 'pos': {'x': 3, 'y': 1}, 'set': 'Tarot', 'effect': 'Card Conversion', 'cost_mult': 1.0, 'config': {'mod_conv': 'card', 'max_highlighted': 2, 'min_highlighted': 2}}, 'c_temperance': {'order': 15, 'discovered': True, 'cost': 3, 'consumeable': True, 'name': 'Temperance', 'pos': {'x': 4, 'y': 1}, 'set': 'Tarot', 'effect': 'Joker Payout', 'cost_mult': 1.0, 'config': {'extra': 50}}, 'c_devil': {'order': 16, 'discovered': True, 'cost': 3, 'consumeable': True, 'name': 'The Devil', 'pos': {'x': 5, 'y': 1}, 'set': 'Tarot', 'effect': 'Enhance', 'cost_mult': 1.0, 'config': {'mod_conv': 'm_gold', 'max_highlighted': 1}}, 'c_tower': {'order': 17, 'discovered': True, 'cost': 3, 'consumeable': True, 'name': 'The Tower', 'pos': {'x': 6, 'y': 1}, 'set': 'Tarot', 'effect': 'Enhance', 'cost_mult': 1.0, 'config': {'mod_conv': 'm_stone', 'max_highlighted': 1}}, 'c_star': {'order': 18, 'discovered': True, 'cost': 3, 'consumeable': True, 'name': 'The Star', 'pos': {'x': 7, 'y': 1}, 'set': 'Tarot', 'effect': 'Suit Conversion', 'cost_mult': 1.0, 'config': {'suit_conv': 'Diamonds', 'max_highlighted': 3}}, 'c_moon': {'order': 19, 'discovered': True, 'cost': 3, 'consumeable': True, 'name': 'The Moon', 'pos': {'x': 8, 'y': 1}, 'set': 'Tarot', 'effect': 'Suit Conversion', 'cost_mult': 1.0, 'config': {'suit_conv': 'Clubs', 'max_highlighted': 3}}, 'c_sun': {'order': 20, 'discovered': True, 'cost': 3, 'consumeable': True, 'name': 'The Sun', 'pos': {'x': 9, 'y': 1}, 'set': 'Tarot', 'effect': 'Suit Conversion', 'cost_mult': 1.0, 'config': {'suit_conv': 'Hearts', 'max_highlighted': 3}}, 'c_judgement': {'order': 21, 'discovered': True, 'cost': 3, 'consumeable': True, 'name': 'Judgement', 'pos': {'x': 0, 'y': 2}, 'set': 'Tarot', 'effect': 'Random Joker', 'cost_mult': 1.0, 'config': {}}, 'c_world': {'order': 22, 'discovered': True, 'cost': 3, 'consumeable': True, 'name': 'The World', 'pos': {'x': 1, 'y': 2}, 'set': 'Tarot', 'effect': 'Suit Conversion', 'cost_mult': 1.0, 'config': {'suit_conv': 'Spades', 'max_highlighted': 3}}, 'c_mercury': {'order': 1, 'discovered': True, 'cost': 3, 'consumeable': True, 'freq': 1, 'name': 'Mercury', 'pos': {'x': 0, 'y': 3}, 'set': 'Planet', 'effect': 'Hand Upgrade', 'cost_mult': 1.0, 'config': {'hand_type': 'Pair'}}, 'c_venus': {'order': 2, 'discovered': True, 'cost': 3, 'consumeable': True, 'freq': 1, 'name': 'Venus', 'pos': {'x': 1, 'y': 3}, 'set': 'Planet', 'effect': 'Hand Upgrade', 'cost_mult': 1.0, 'config': {'hand_type': 'Three of a Kind'}}, 'c_earth': {'order': 3, 'discovered': True, 'cost': 3, 'consumeable': True, 'freq': 1, 'name': 'Earth', 'pos': {'x': 2, 'y': 3}, 'set': 'Planet', 'effect': 'Hand Upgrade', 'cost_mult': 1.0, 'config': {'hand_type': 'Full House'}}, 'c_mars': {'order': 4, 'discovered': True, 'cost': 3, 'consumeable': True, 'freq': 1, 'name': 'Mars', 'pos': {'x': 3, 'y': 3}, 'set': 'Planet', 'effect': 'Hand Upgrade', 'cost_mult': 1.0, 'config': {'hand_type': 'Four of a Kind'}}, 'c_jupiter': {'order': 5, 'discovered': True, 'cost': 3, 'consumeable': True, 'freq': 1, 'name': 'Jupiter', 'pos': {'x': 4, 'y': 3}, 'set': 'Planet', 'effect': 'Hand Upgrade', 'cost_mult': 1.0, 'config': {'hand_type': 'Flush'}}, 'c_saturn': {'order': 6, 'discovered': True, 'cost': 3, 'consumeable': True, 'freq': 1, 'name': 'Saturn', 'pos': {'x': 5, 'y': 3}, 'set': 'Planet', 'effect': 'Hand Upgrade', 'cost_mult': 1.0, 'config': {'hand_type': 'Straight'}}, 'c_uranus': {'order': 7, 'discovered': True, 'cost': 3, 'consumeable': True, 'freq': 1, 'name': 'Uranus', 'pos': {'x': 6, 'y': 3}, 'set': 'Planet', 'effect': 'Hand Upgrade', 'cost_mult': 1.0, 'config': {'hand_type': 'Two Pair'}}, 'c_neptune': {'order': 8, 'discovered': True, 'cost': 3, 'consumeable': True, 'freq': 1, 'name': 'Neptune', 'pos': {'x': 7, 'y': 3}, 'set': 'Planet', 'effect': 'Hand Upgrade', 'cost_mult': 1.0, 'config': {'hand_type': 'Straight Flush'}}, 'c_pluto': {'order': 9, 'discovered': True, 'cost': 3, 'consumeable': True, 'freq': 1, 'name': 'Pluto', 'pos': {'x': 8, 'y': 3}, 'set': 'Planet', 'effect': 'Hand Upgrade', 'cost_mult': 1.0, 'config': {'hand_type': 'High Card'}}, 'c_planet_x': {'order': 10, 'discovered': True, 'cost': 3, 'consumeable': True, 'freq': 1, 'name': 'Planet X', 'pos': {'x': 9, 'y': 2}, 'set': 'Planet', 'effect': 'Hand Upgrade', 'cost_mult': 1.0, 'config': {'hand_type': 'Five of a Kind', 'softlock': True}}, 'c_ceres': {'order': 11, 'discovered': True, 'cost': 3, 'consumeable': True, 'freq': 1, 'name': 'Ceres', 'pos': {'x': 8, 'y': 2}, 'set': 'Planet', 'effect': 'Hand Upgrade', 'cost_mult': 1.0, 'config': {'hand_type': 'Flush House', 'softlock': True}}, 'c_eris': {'order': 12, 'discovered': True, 'cost': 3, 'consumeable': True, 'freq': 1, 'name': 'Eris', 'pos': {'x': 3, 'y': 2}, 'set': 'Planet', 'effect': 'Hand Upgrade', 'cost_mult': 1.0, 'config': {'hand_type': 'Flush Five', 'softlock': True}}, 'c_familiar': {'order': 1, 'discovered': True, 'cost': 4, 'consumeable': True, 'name': 'Familiar', 'pos': {'x': 0, 'y': 4}, 'set': 'Spectral', 'config': {'remove_card': True, 'extra': 3}}, 'c_grim': {'order': 2, 'discovered': True, 'cost': 4, 'consumeable': True, 'name': 'Grim', 'pos': {'x': 1, 'y': 4}, 'set': 'Spectral', 'config': {'remove_card': True, 'extra': 2}}, 'c_incantation': {'order': 3, 'discovered': True, 'cost': 4, 'consumeable': True, 'name': 'Incantation', 'pos': {'x': 2, 'y': 4}, 'set': 'Spectral', 'config': {'remove_card': True, 'extra': 4}}, 'c_talisman': {'order': 4, 'discovered': True, 'cost': 4, 'consumeable': True, 'name': 'Talisman', 'pos': {'x': 3, 'y': 4}, 'set': 'Spectral', 'config': {'extra': 'Gold', 'max_highlighted': 1}}, 'c_aura': {'order': 5, 'discovered': True, 'cost': 4, 'consumeable': True, 'name': 'Aura', 'pos': {'x': 4, 'y': 4}, 'set': 'Spectral', 'config': {}}, 'c_wraith': {'order': 6, 'discovered': True, 'cost': 4, 'consumeable': True, 'name': 'Wraith', 'pos': {'x': 5, 'y': 4}, 'set': 'Spectral', 'config': {}}, 'c_sigil': {'order': 7, 'discovered': True, 'cost': 4, 'consumeable': True, 'name': 'Sigil', 'pos': {'x': 6, 'y': 4}, 'set': 'Spectral', 'config': {}}, 'c_ouija': {'order': 8, 'discovered': True, 'cost': 4, 'consumeable': True, 'name': 'Ouija', 'pos': {'x': 7, 'y': 4}, 'set': 'Spectral', 'config': {}}, 'c_ectoplasm': {'order': 9, 'discovered': True, 'cost': 4, 'consumeable': True, 'name': 'Ectoplasm', 'pos': {'x': 8, 'y': 4}, 'set': 'Spectral', 'config': {}}, 'c_immolate': {'order': 10, 'discovered': True, 'cost': 4, 'consumeable': True, 'name': 'Immolate', 'pos': {'x': 9, 'y': 4}, 'set': 'Spectral', 'config': {'remove_card': True, 'extra': {'destroy': 5, 'dollars': 20}}}, 'c_ankh': {'order': 11, 'discovered': True, 'cost': 4, 'consumeable': True, 'name': 'Ankh', 'pos': {'x': 0, 'y': 5}, 'set': 'Spectral', 'config': {'extra': 2}}, 'c_deja_vu': {'order': 12, 'discovered': True, 'cost': 4, 'consumeable': True, 'name': 'Deja Vu', 'pos': {'x': 1, 'y': 5}, 'set': 'Spectral', 'config': {'extra': 'Red', 'max_highlighted': 1}}, 'c_hex': {'order': 13, 'discovered': True, 'cost': 4, 'consumeable': True, 'name': 'Hex', 'pos': {'x': 2, 'y': 5}, 'set': 'Spectral', 'config': {'extra': 2}}, 'c_trance': {'order': 14, 'discovered': True, 'cost': 4, 'consumeable': True, 'name': 'Trance', 'pos': {'x': 3, 'y': 5}, 'set': 'Spectral', 'config': {'extra': 'Blue', 'max_highlighted': 1}}, 'c_medium': {'order': 15, 'discovered': True, 'cost': 4, 'consumeable': True, 'name': 'Medium', 'pos': {'x': 4, 'y': 5}, 'set': 'Spectral', 'config': {'extra': 'Purple', 'max_highlighted': 1}}, 'c_cryptid': {'order': 16, 'discovered': True, 'cost': 4, 'consumeable': True, 'name': 'Cryptid', 'pos': {'x': 5, 'y': 5}, 'set': 'Spectral', 'config': {'extra': 2, 'max_highlighted': 1}}, 'c_soul': {'order': 17, 'discovered': True, 'cost': 4, 'consumeable': True, 'name': 'The Soul', 'pos': {'x': 2, 'y': 2}, 'set': 'Spectral', 'effect': 'Unlocker', 'config': {}, 'hidden': True}, 'c_black_hole': {'order': 18, 'discovered': True, 'cost': 4, 'consumeable': True, 'name': 'Black Hole', 'pos': {'x': 9, 'y': 3}, 'set': 'Spectral', 'config': {}, 'hidden': True}, 'v_overstock_norm': {'order': 1, 'discovered': True, 'unlocked': True, 'available': True, 'cost': 10, 'name': 'Overstock', 'pos': {'x': 0, 'y': 0}, 'set': 'Voucher', 'config': {}}, 'v_clearance_sale': {'order': 3, 'discovered': True, 'unlocked': True, 'available': True, 'cost': 10, 'name': 'Clearance Sale', 'pos': {'x': 3, 'y': 0}, 'set': 'Voucher', 'config': {'extra': 25}}, 'v_hone': {'order': 5, 'discovered': True, 'unlocked': True, 'available': True, 'cost': 10, 'name': 'Hone', 'pos': {'x': 4, 'y': 0}, 'set': 'Voucher', 'config': {'extra': 2}}, 'v_reroll_surplus': {'order': 7, 'discovered': True, 'unlocked': True, 'available': True, 'cost': 10, 'name': 'Reroll Surplus', 'pos': {'x': 0, 'y': 2}, 'set': 'Voucher', 'config': {'extra': 2}}, 'v_crystal_ball': {'order': 9, 'discovered': True, 'unlocked': True, 'available': True, 'cost': 10, 'name': 'Crystal Ball', 'pos': {'x': 2, 'y': 2}, 'set': 'Voucher', 'config': {'extra': 3}}, 'v_telescope': {'order': 11, 'discovered': True, 'unlocked': True, 'available': True, 'cost': 10, 'name': 'Telescope', 'pos': {'x': 3, 'y': 2}, 'set': 'Voucher', 'config': {'extra': 3}}, 'v_grabber': {'order': 13, 'discovered': True, 'unlocked': True, 'available': True, 'cost': 10, 'name': 'Grabber', 'pos': {'x': 5, 'y': 0}, 'set': 'Voucher', 'config': {'extra': 1}}, 'v_wasteful': {'order': 15, 'discovered': True, 'unlocked': True, 'available': True, 'cost': 10, 'name': 'Wasteful', 'pos': {'x': 6, 'y': 0}, 'set': 'Voucher', 'config': {'extra': 1}}, 'v_tarot_merchant': {'order': 17, 'discovered': True, 'unlocked': True, 'available': True, 'cost': 10, 'name': 'Tarot Merchant', 'pos': {'x': 1, 'y': 0}, 'set': 'Voucher', 'config': {'extra': 9.6 / 4, 'extra_disp': 2}}, 'v_planet_merchant': {'order': 19, 'discovered': True, 'unlocked': True, 'available': True, 'cost': 10, 'name': 'Planet Merchant', 'pos': {'x': 2, 'y': 0}, 'set': 'Voucher', 'config': {'extra': 9.6 / 4, 'extra_disp': 2}}, 'v_seed_money': {'order': 21, 'discovered': True, 'unlocked': True, 'available': True, 'cost': 10, 'name': 'Seed Money', 'pos': {'x': 1, 'y': 2}, 'set': 'Voucher', 'config': {'extra': 50}}, 'v_blank': {'order': 23, 'discovered': True, 'unlocked': True, 'available': True, 'cost': 10, 'name': 'Blank', 'pos': {'x': 7, 'y': 0}, 'set': 'Voucher', 'config': {'extra': 5}}, 'v_magic_trick': {'order': 25, 'discovered': True, 'unlocked': True, 'available': True, 'cost': 10, 'name': 'Magic Trick', 'pos': {'x': 4, 'y': 2}, 'set': 'Voucher', 'config': {'extra': 4}}, 'v_hieroglyph': {'order': 27, 'discovered': True, 'unlocked': True, 'available': True, 'cost': 10, 'name': 'Hieroglyph', 'pos': {'x': 5, 'y': 2}, 'set': 'Voucher', 'config': {'extra': 1}}, 'v_directors_cut': {'order': 29, 'discovered': True, 'unlocked': True, 'available': True, 'cost': 10, 'name': "Director's Cut", 'pos': {'x': 6, 'y': 2}, 'set': 'Voucher', 'config': {'extra': 10}}, 'v_paint_brush': {'order': 31, 'discovered': True, 'unlocked': True, 'available': True, 'cost': 10, 'name': 'Paint Brush', 'pos': {'x': 7, 'y': 2}, 'set': 'Voucher', 'config': {'extra': 1}}, 'v_overstock_plus': {'order': 2, 'discovered': True, 'unlocked': False, 'available': True, 'cost': 10, 'name': 'Overstock Plus', 'pos': {'x': 0, 'y': 1}, 'set': 'Voucher', 'config': {}, 'requires': {1: 'v_overstock_norm'}, 'unlock_condition': {'type': 'c_shop_dollars_spent', 'extra': 2500}}, 'v_liquidation': {'order': 4, 'discovered': True, 'unlocked': False, 'available': True, 'cost': 10, 'name': 'Liquidation', 'pos': {'x': 3, 'y': 1}, 'set': 'Voucher', 'config': {'extra': 50}, 'requires': {1: 'v_clearance_sale'}, 'unlock_condition': {'type': 'run_redeem', 'extra': 10}}, 'v_glow_up': {'order': 6, 'discovered': True, 'unlocked': False, 'available': True, 'cost': 10, 'name': 'Glow Up', 'pos': {'x': 4, 'y': 1}, 'set': 'Voucher', 'config': {'extra': 4}, 'requires': {1: 'v_hone'}, 'unlock_condition': {'type': 'have_edition', 'extra': 5}}, 'v_reroll_glut': {'order': 8, 'discovered': True, 'unlocked': False, 'available': True, 'cost': 10, 'name': 'Reroll Glut', 'pos': {'x': 0, 'y': 3}, 'set': 'Voucher', 'config': {'extra': 2}, 'requires': {1: 'v_reroll_surplus'}, 'unlock_condition': {'type': 'c_shop_rerolls', 'extra': 100}}, 'v_omen_globe': {'order': 10, 'discovered': True, 'unlocked': False, 'available': True, 'cost': 10, 'name': 'Omen Globe', 'pos': {'x': 2, 'y': 3}, 'set': 'Voucher', 'config': {'extra': 4}, 'requires': {1: 'v_crystal_ball'}, 'unlock_condition': {'type': 'c_tarot_reading_used', 'extra': 25}}, 'v_observatory': {'order': 12, 'discovered': True, 'unlocked': False, 'available': True, 'cost': 10, 'name': 'Observatory', 'pos': {'x': 3, 'y': 3}, 'set': 'Voucher', 'config': {'extra': 1.5}, 'requires': {1: 'v_telescope'}, 'unlock_condition': {'type': 'c_planetarium_used', 'extra': 25}}, 'v_nacho_tong': {'order': 14, 'discovered': True, 'unlocked': False, 'available': True, 'cost': 10, 'name': 'Nacho Tong', 'pos': {'x': 5, 'y': 1}, 'set': 'Voucher', 'config': {'extra': 1}, 'requires': {1: 'v_grabber'}, 'unlock_condition': {'type': 'c_cards_played', 'extra': 2500}}, 'v_recyclomancy': {'order': 16, 'discovered': True, 'unlocked': False, 'available': True, 'cost': 10, 'name': 'Recyclomancy', 'pos': {'x': 6, 'y': 1}, 'set': 'Voucher', 'config': {'extra': 1}, 'requires': {1: 'v_wasteful'}, 'unlock_condition': {'type': 'c_cards_discarded', 'extra': 2500}}, 'v_tarot_tycoon': {'order': 18, 'discovered': True, 'unlocked': False, 'available': True, 'cost': 10, 'name': 'Tarot Tycoon', 'pos': {'x': 1, 'y': 1}, 'set': 'Voucher', 'config': {'extra': 32 / 4, 'extra_disp': 4}, 'requires': {1: 'v_tarot_merchant'}, 'unlock_condition': {'type': 'c_tarots_bought', 'extra': 50}}, 'v_planet_tycoon': {'order': 20, 'discovered': True, 'unlocked': False, 'available': True, 'cost': 10, 'name': 'Planet Tycoon', 'pos': {'x': 2, 'y': 1}, 'set': 'Voucher', 'config': {'extra': 32 / 4, 'extra_disp': 4}, 'requires': {1: 'v_planet_merchant'}, 'unlock_condition': {'type': 'c_planets_bought', 'extra': 50}}, 'v_money_tree': {'order': 22, 'discovered': True, 'unlocked': False, 'available': True, 'cost': 10, 'name': 'Money Tree', 'pos': {'x': 1, 'y': 3}, 'set': 'Voucher', 'config': {'extra': 100}, 'requires': {1: 'v_seed_money'}, 'unlock_condition': {'type': 'interest_streak', 'extra': 10}}, 'v_antimatter': {'order': 24, 'discovered': True, 'unlocked': False, 'available': True, 'cost': 10, 'name': 'Antimatter', 'pos': {'x': 7, 'y': 1}, 'set': 'Voucher', 'config': {'extra': 15}, 'requires': {1: 'v_blank'}, 'unlock_condition': {'type': 'blank_redeems', 'extra': 10}}, 'v_illusion': {'order': 26, 'discovered': True, 'unlocked': False, 'available': True, 'cost': 10, 'name': 'Illusion', 'pos': {'x': 4, 'y': 3}, 'set': 'Voucher', 'config': {'extra': 4}, 'requires': {1: 'v_magic_trick'}, 'unlock_condition': {'type': 'c_playing_cards_bought', 'extra': 20}}, 'v_petroglyph': {'order': 28, 'discovered': True, 'unlocked': False, 'available': True, 'cost': 10, 'name': 'Petroglyph', 'pos': {'x': 5, 'y': 3}, 'set': 'Voucher', 'config': {'extra': 1}, 'requires': {1: 'v_hieroglyph'}, 'unlock_condition': {'type': 'ante_up', 'ante': 12, 'extra': 12}}, 'v_retcon': {'order': 30, 'discovered': True, 'unlocked': False, 'available': True, 'cost': 10, 'name': 'Retcon', 'pos': {'x': 6, 'y': 3}, 'set': 'Voucher', 'config': {'extra': 10}, 'requires': {1: 'v_directors_cut'}, 'unlock_condition': {'type': 'blind_discoveries', 'extra': 25}}, 'v_palette': {'order': 32, 'discovered': True, 'unlocked': False, 'available': True, 'cost': 10, 'name': 'Palette', 'pos': {'x': 7, 'y': 3}, 'set': 'Voucher', 'config': {'extra': 1}, 'requires': {1: 'v_paint_brush'}, 'unlock_condition': {'type': 'min_hand_size', 'extra': 5}}, 'b_red': {'name': 'Red Deck', 'stake': 1, 'unlocked': True, 'order': 1, 'pos': {'x': 0, 'y': 0}, 'set': 'Back', 'config': {'discards': 1}, 'discovered': True}, 'b_blue': {'name': 'Blue Deck', 'stake': 1, 'unlocked': False, 'order': 2, 'pos': {'x': 0, 'y': 2}, 'set': 'Back', 'config': {'hands': 1}, 'unlock_condition': {'type': 'discover_amount', 'amount': 20}}, 'b_yellow': {'name': 'Yellow Deck', 'stake': 1, 'unlocked': False, 'order': 3, 'pos': {'x': 1, 'y': 2}, 'set': 'Back', 'config': {'dollars': 10}, 'unlock_condition': {'type': 'discover_amount', 'amount': 50}}, 'b_green': {'name': 'Green Deck', 'stake': 1, 'unlocked': False, 'order': 4, 'pos': {'x': 2, 'y': 2}, 'set': 'Back', 'config': {'extra_hand_bonus': 2, 'extra_discard_bonus': 1, 'no_interest': True}, 'unlock_condition': {'type': 'discover_amount', 'amount': 75}}, 'b_black': {'name': 'Black Deck', 'stake': 1, 'unlocked': False, 'order': 5, 'pos': {'x': 3, 'y': 2}, 'set': 'Back', 'config': {'hands': -1, 'joker_slot': 1}, 'unlock_condition': {'type': 'discover_amount', 'amount': 100}}, 'b_magic': {'name': 'Magic Deck', 'stake': 1, 'unlocked': False, 'order': 6, 'pos': {'x': 0, 'y': 3}, 'set': 'Back', 'config': {'voucher': 'v_crystal_ball', 'consumables': {1: 'c_fool', 2: 'c_fool'}}, 'unlock_condition': {'type': 'win_deck', 'deck': 'b_red'}}, 'b_nebula': {'name': 'Nebula Deck', 'stake': 1, 'unlocked': False, 'order': 7, 'pos': {'x': 3, 'y': 0}, 'set': 'Back', 'config': {'voucher': 'v_telescope', 'consumable_slot': -1}, 'unlock_condition': {'type': 'win_deck', 'deck': 'b_blue'}}, 'b_ghost': {'name': 'Ghost Deck', 'stake': 1, 'unlocked': False, 'order': 8, 'pos': {'x': 6, 'y': 2}, 'set': 'Back', 'config': {'spectral_rate': 2, 'consumables': {1: 'c_hex'}}, 'unlock_condition': {'type': 'win_deck', 'deck': 'b_yellow'}}, 'b_abandoned': {'name': 'Abandoned Deck', 'stake': 1, 'unlocked': False, 'order': 9, 'pos': {'x': 3, 'y': 3}, 'set': 'Back', 'config': {'remove_faces': True}, 'unlock_condition': {'type': 'win_deck', 'deck': 'b_green'}}, 'b_checkered': {'name': 'Checkered Deck', 'stake': 1, 'unlocked': False, 'order': 10, 'pos': {'x': 1, 'y': 3}, 'set': 'Back', 'config': {}, 'unlock_condition': {'type': 'win_deck', 'deck': 'b_black'}}, 'b_zodiac': {'name': 'Zodiac Deck', 'stake': 1, 'unlocked': False, 'order': 11, 'pos': {'x': 3, 'y': 4}, 'set': 'Back', 'config': {'vouchers': {1: 'v_tarot_merchant', 2: 'v_planet_merchant', 3: 'v_overstock_norm'}}, 'unlock_condition': {'type': 'win_stake', 'stake': 2}}, 'b_painted': {'name': 'Painted Deck', 'stake': 1, 'unlocked': False, 'order': 12, 'pos': {'x': 4, 'y': 3}, 'set': 'Back', 'config': {'hand_size': 2, 'joker_slot': -1}, 'unlock_condition': {'type': 'win_stake', 'stake': 3}}, 'b_anaglyph': {'name': 'Anaglyph Deck', 'stake': 1, 'unlocked': False, 'order': 13, 'pos': {'x': 2, 'y': 4}, 'set': 'Back', 'config': {}, 'unlock_condition': {'type': 'win_stake', 'stake': 4}}, 'b_plasma': {'name': 'Plasma Deck', 'stake': 1, 'unlocked': False, 'order': 14, 'pos': {'x': 4, 'y': 2}, 'set': 'Back', 'config': {'ante_scaling': 2}, 'unlock_condition': {'type': 'win_stake', 'stake': 5}}, 'b_erratic': {'name': 'Erratic Deck', 'stake': 1, 'unlocked': False, 'order': 15, 'pos': {'x': 2, 'y': 3}, 'set': 'Back', 'config': {'randomize_rank_suit': True}, 'unlock_condition': {'type': 'win_stake', 'stake': 7}}, 'b_challenge': {'name': 'Challenge Deck', 'stake': 1, 'unlocked': True, 'order': 16, 'pos': {'x': 0, 'y': 4}, 'set': 'Back', 'config': {}, 'omit': True}, 'm_bonus': {'max': 500, 'order': 2, 'name': 'Bonus', 'set': 'Enhanced', 'pos': {'x': 1, 'y': 1}, 'effect': 'Bonus Card', 'label': 'Bonus Card', 'config': {'bonus': 30}}, 'm_mult': {'max': 500, 'order': 3, 'name': 'Mult', 'set': 'Enhanced', 'pos': {'x': 2, 'y': 1}, 'effect': 'Mult Card', 'label': 'Mult Card', 'config': {'mult': 4}}, 'm_wild': {'max': 500, 'order': 4, 'name': 'Wild Card', 'set': 'Enhanced', 'pos': {'x': 3, 'y': 1}, 'effect': 'Wild Card', 'label': 'Wild Card', 'config': {}}, 'm_glass': {'max': 500, 'order': 5, 'name': 'Glass Card', 'set': 'Enhanced', 'pos': {'x': 5, 'y': 1}, 'effect': 'Glass Card', 'label': 'Glass Card', 'config': {'Xmult': 2, 'extra': 4}}, 'm_steel': {'max': 500, 'order': 6, 'name': 'Steel Card', 'set': 'Enhanced', 'pos': {'x': 6, 'y': 1}, 'effect': 'Steel Card', 'label': 'Steel Card', 'config': {'h_x_mult': 1.5}}, 'm_stone': {'max': 500, 'order': 7, 'name': 'Stone Card', 'set': 'Enhanced', 'pos': {'x': 5, 'y': 0}, 'effect': 'Stone Card', 'label': 'Stone Card', 'config': {'bonus': 50}}, 'm_gold': {'max': 500, 'order': 8, 'name': 'Gold Card', 'set': 'Enhanced', 'pos': {'x': 6, 'y': 0}, 'effect': 'Gold Card', 'label': 'Gold Card', 'config': {'h_dollars': 3}}, 'm_lucky': {'max': 500, 'order': 9, 'name': 'Lucky Card', 'set': 'Enhanced', 'pos': {'x': 4, 'y': 1}, 'effect': 'Lucky Card', 'label': 'Lucky Card', 'config': {'mult': 20, 'p_dollars': 20}}, 'e_base': {'order': 1, 'unlocked': True, 'discovered': True, 'name': 'Base', 'pos': {'x': 0, 'y': 0}, 'atlas': 'Joker', 'set': 'Edition', 'config': {}}, 'e_foil': {'order': 2, 'unlocked': True, 'discovered': True, 'name': 'Foil', 'pos': {'x': 0, 'y': 0}, 'atlas': 'Joker', 'set': 'Edition', 'config': {'extra': 50}}, 'e_holo': {'order': 3, 'unlocked': True, 'discovered': True, 'name': 'Holographic', 'pos': {'x': 0, 'y': 0}, 'atlas': 'Joker', 'set': 'Edition', 'config': {'extra': 10}}, 'e_polychrome': {'order': 4, 'unlocked': True, 'discovered': True, 'name': 'Polychrome', 'pos': {'x': 0, 'y': 0}, 'atlas': 'Joker', 'set': 'Edition', 'config': {'extra': 1.5}}, 'e_negative': {'order': 5, 'unlocked': True, 'discovered': True, 'name': 'Negative', 'pos': {'x': 0, 'y': 0}, 'atlas': 'Joker', 'set': 'Edition', 'config': {'extra': 1}}, 'p_arcana_normal_1': {'order': 1, 'discovered': True, 'name': 'Arcana Pack', 'weight': 1, 'kind': 'Arcana', 'cost': 4, 'pos': {'x': 0, 'y': 0}, 'atlas': 'Booster', 'set': 'Booster', 'config': {'extra': 3, 'choose': 1}}, 'p_arcana_normal_2': {'order': 2, 'discovered': True, 'name': 'Arcana Pack', 'weight': 1, 'kind': 'Arcana', 'cost': 4, 'pos': {'x': 1, 'y': 0}, 'atlas': 'Booster', 'set': 'Booster', 'config': {'extra': 3, 'choose': 1}}, 'p_arcana_normal_3': {'order': 3, 'discovered': True, 'name': 'Arcana Pack', 'weight': 1, 'kind': 'Arcana', 'cost': 4, 'pos': {'x': 2, 'y': 0}, 'atlas': 'Booster', 'set': 'Booster', 'config': {'extra': 3, 'choose': 1}}, 'p_arcana_normal_4': {'order': 4, 'discovered': True, 'name': 'Arcana Pack', 'weight': 1, 'kind': 'Arcana', 'cost': 4, 'pos': {'x': 3, 'y': 0}, 'atlas': 'Booster', 'set': 'Booster', 'config': {'extra': 3, 'choose': 1}}, 'p_arcana_jumbo_1': {'order': 5, 'discovered': True, 'name': 'Jumbo Arcana Pack', 'weight': 1, 'kind': 'Arcana', 'cost': 6, 'pos': {'x': 0, 'y': 2}, 'atlas': 'Booster', 'set': 'Booster', 'config': {'extra': 5, 'choose': 1}}, 'p_arcana_jumbo_2': {'order': 6, 'discovered': True, 'name': 'Jumbo Arcana Pack', 'weight': 1, 'kind': 'Arcana', 'cost': 6, 'pos': {'x': 1, 'y': 2}, 'atlas': 'Booster', 'set': 'Booster', 'config': {'extra': 5, 'choose': 1}}, 'p_arcana_mega_1': {'order': 7, 'discovered': True, 'name': 'Mega Arcana Pack', 'weight': 0.25, 'kind': 'Arcana', 'cost': 8, 'pos': {'x': 2, 'y': 2}, 'atlas': 'Booster', 'set': 'Booster', 'config': {'extra': 5, 'choose': 2}}, 'p_arcana_mega_2': {'order': 8, 'discovered': True, 'name': 'Mega Arcana Pack', 'weight': 0.25, 'kind': 'Arcana', 'cost': 8, 'pos': {'x': 3, 'y': 2}, 'atlas': 'Booster', 'set': 'Booster', 'config': {'extra': 5, 'choose': 2}}, 'p_celestial_normal_1': {'order': 9, 'discovered': True, 'name': 'Celestial Pack', 'weight': 1, 'kind': 'Celestial', 'cost': 4, 'pos': {'x': 0, 'y': 1}, 'atlas': 'Booster', 'set': 'Booster', 'config': {'extra': 3, 'choose': 1}}, 'p_celestial_normal_2': {'order': 10, 'discovered': True, 'name': 'Celestial Pack', 'weight': 1, 'kind': 'Celestial', 'cost': 4, 'pos': {'x': 1, 'y': 1}, 'atlas': 'Booster', 'set': 'Booster', 'config': {'extra': 3, 'choose': 1}}, 'p_celestial_normal_3': {'order': 11, 'discovered': True, 'name': 'Celestial Pack', 'weight': 1, 'kind': 'Celestial', 'cost': 4, 'pos': {'x': 2, 'y': 1}, 'atlas': 'Booster', 'set': 'Booster', 'config': {'extra': 3, 'choose': 1}}, 'p_celestial_normal_4': {'order': 12, 'discovered': True, 'name': 'Celestial Pack', 'weight': 1, 'kind': 'Celestial', 'cost': 4, 'pos': {'x': 3, 'y': 1}, 'atlas': 'Booster', 'set': 'Booster', 'config': {'extra': 3, 'choose': 1}}, 'p_celestial_jumbo_1': {'order': 13, 'discovered': True, 'name': 'Jumbo Celestial Pack', 'weight': 1, 'kind': 'Celestial', 'cost': 6, 'pos': {'x': 0, 'y': 3}, 'atlas': 'Booster', 'set': 'Booster', 'config': {'extra': 5, 'choose': 1}}, 'p_celestial_jumbo_2': {'order': 14, 'discovered': True, 'name': 'Jumbo Celestial Pack', 'weight': 1, 'kind': 'Celestial', 'cost': 6, 'pos': {'x': 1, 'y': 3}, 'atlas': 'Booster', 'set': 'Booster', 'config': {'extra': 5, 'choose': 1}}, 'p_celestial_mega_1': {'order': 15, 'discovered': True, 'name': 'Mega Celestial Pack', 'weight': 0.25, 'kind': 'Celestial', 'cost': 8, 'pos': {'x': 2, 'y': 3}, 'atlas': 'Booster', 'set': 'Booster', 'config': {'extra': 5, 'choose': 2}}, 'p_celestial_mega_2': {'order': 16, 'discovered': True, 'name': 'Mega Celestial Pack', 'weight': 0.25, 'kind': 'Celestial', 'cost': 8, 'pos': {'x': 3, 'y': 3}, 'atlas': 'Booster', 'set': 'Booster', 'config': {'extra': 5, 'choose': 2}}, 'p_spectral_normal_1': {'order': 29, 'discovered': True, 'name': 'Spectral Pack', 'weight': 0.3, 'kind': 'Spectral', 'cost': 4, 'pos': {'x': 0, 'y': 4}, 'atlas': 'Booster', 'set': 'Booster', 'config': {'extra': 2, 'choose': 1}}, 'p_spectral_normal_2': {'order': 30, 'discovered': True, 'name': 'Spectral Pack', 'weight': 0.3, 'kind': 'Spectral', 'cost': 4, 'pos': {'x': 1, 'y': 4}, 'atlas': 'Booster', 'set': 'Booster', 'config': {'extra': 2, 'choose': 1}}, 'p_spectral_jumbo_1': {'order': 31, 'discovered': True, 'name': 'Jumbo Spectral Pack', 'weight': 0.3, 'kind': 'Spectral', 'cost': 6, 'pos': {'x': 2, 'y': 4}, 'atlas': 'Booster', 'set': 'Booster', 'config': {'extra': 4, 'choose': 1}}, 'p_spectral_mega_1': {'order': 32, 'discovered': True, 'name': 'Mega Spectral Pack', 'weight': 0.07, 'kind': 'Spectral', 'cost': 8, 'pos': {'x': 3, 'y': 4}, 'atlas': 'Booster', 'set': 'Booster', 'config': {'extra': 4, 'choose': 2}}, 'p_standard_normal_1': {'order': 17, 'discovered': True, 'name': 'Standard Pack', 'weight': 1, 'kind': 'Standard', 'cost': 4, 'pos': {'x': 0, 'y': 6}, 'atlas': 'Booster', 'set': 'Booster', 'config': {'extra': 3, 'choose': 1}}, 'p_standard_normal_2': {'order': 18, 'discovered': True, 'name': 'Standard Pack', 'weight': 1, 'kind': 'Standard', 'cost': 4, 'pos': {'x': 1, 'y': 6}, 'atlas': 'Booster', 'set': 'Booster', 'config': {'extra': 3, 'choose': 1}}, 'p_standard_normal_3': {'order': 19, 'discovered': True, 'name': 'Standard Pack', 'weight': 1, 'kind': 'Standard', 'cost': 4, 'pos': {'x': 2, 'y': 6}, 'atlas': 'Booster', 'set': 'Booster', 'config': {'extra': 3, 'choose': 1}}, 'p_standard_normal_4': {'order': 20, 'discovered': True, 'name': 'Standard Pack', 'weight': 1, 'kind': 'Standard', 'cost': 4, 'pos': {'x': 3, 'y': 6}, 'atlas': 'Booster', 'set': 'Booster', 'config': {'extra': 3, 'choose': 1}}, 'p_standard_jumbo_1': {'order': 21, 'discovered': True, 'name': 'Jumbo Standard Pack', 'weight': 1, 'kind': 'Standard', 'cost': 6, 'pos': {'x': 0, 'y': 7}, 'atlas': 'Booster', 'set': 'Booster', 'config': {'extra': 5, 'choose': 1}}, 'p_standard_jumbo_2': {'order': 22, 'discovered': True, 'name': 'Jumbo Standard Pack', 'weight': 1, 'kind': 'Standard', 'cost': 6, 'pos': {'x': 1, 'y': 7}, 'atlas': 'Booster', 'set': 'Booster', 'config': {'extra': 5, 'choose': 1}}, 'p_standard_mega_1': {'order': 23, 'discovered': True, 'name': 'Mega Standard Pack', 'weight': 0.25, 'kind': 'Standard', 'cost': 8, 'pos': {'x': 2, 'y': 7}, 'atlas': 'Booster', 'set': 'Booster', 'config': {'extra': 5, 'choose': 2}}, 'p_standard_mega_2': {'order': 24, 'discovered': True, 'name': 'Mega Standard Pack', 'weight': 0.25, 'kind': 'Standard', 'cost': 8, 'pos': {'x': 3, 'y': 7}, 'atlas': 'Booster', 'set': 'Booster', 'config': {'extra': 5, 'choose': 2}}, 'p_buffoon_normal_1': {'order': 25, 'discovered': True, 'name': 'Buffoon Pack', 'weight': 0.6, 'kind': 'Buffoon', 'cost': 4, 'pos': {'x': 0, 'y': 8}, 'atlas': 'Booster', 'set': 'Booster', 'config': {'extra': 2, 'choose': 1}}, 'p_buffoon_normal_2': {'order': 26, 'discovered': True, 'name': 'Buffoon Pack', 'weight': 0.6, 'kind': 'Buffoon', 'cost': 4, 'pos': {'x': 1, 'y': 8}, 'atlas': 'Booster', 'set': 'Booster', 'config': {'extra': 2, 'choose': 1}}, 'p_buffoon_jumbo_1': {'order': 27, 'discovered': True, 'name': 'Jumbo Buffoon Pack', 'weight': 0.6, 'kind': 'Buffoon', 'cost': 6, 'pos': {'x': 2, 'y': 8}, 'atlas': 'Booster', 'set': 'Booster', 'config': {'extra': 4, 'choose': 1}}, 'p_buffoon_mega_1': {'order': 28, 'discovered': True, 'name': 'Mega Buffoon Pack', 'weight': 0.15, 'kind': 'Buffoon', 'cost': 8, 'pos': {'x': 3, 'y': 8}, 'atlas': 'Booster', 'set': 'Booster', 'config': {'extra': 4, 'choose': 2}}, 'soul': {'pos': {'x': 0, 'y': 1}}, 'undiscovered_joker': {'pos': {'x': 5, 'y': 3}}, 'undiscovered_tarot': {'pos': {'x': 6, 'y': 3}}}
        self.P_CENTER_POOLS = {'Booster': {}, 'Default': {}, 'Enhanced': {}, 'Edition': {}, 'Joker': {}, 'Tarot': {}, 'Planet': {}, 'Tarot_Planet': {}, 'Spectral': {}, 'Consumeables': {}, 'Voucher': {}, 'Back': {}, 'Tag': {}, 'Seal': {}, 'Stake': {}, 'Demo': {}}
        self.P_JOKER_RARITY_POOLS = {1: {}, 2: {}, 3: {}, 4: {}}
        self.P_LOCKED = {}self.save_progress()
        TESTHELPER_unlocks = False & (not _RELEASE_MODE)
        if not love.filesystem.getInfo():love.filesystem.createDirectory()
        if not love.filesystem.getInfo():love.filesystem.append()convert_save_to_meta()
        meta = STR_UNPACK()
        meta.unlocked = meta.unlocked if meta.unlocked else {}
        meta.discovered = meta.discovered if meta.discovered else {}
        meta.alerted = meta.alerted if meta.alerted else {}
        for kv in pairs():
            if (not v.wip) & (not v.demo):
                if TESTHELPER_unlocks:
                    v.unlocked = True';'
                    v.discovered = True';'
                    v.alerted = True
                if (not v.unlocked) & ((string.find(k, ^j_) if string.find(k, ^j_) else string.find(k, ^b_)) if (string.find(k, ^j_) if string.find(k, ^j_) else string.find(k, ^b_)) else string.find(k, ^v_)) & 'k[meta.unlocked]':
                    v.unlocked = True
                if (not v.unlocked) & ((string.find(k, ^j_) if string.find(k, ^j_) else string.find(k, ^b_)) if (string.find(k, ^j_) if string.find(k, ^j_) else string.find(k, ^b_)) else string.find(k, ^v_)):
                    '#self.P_LOCKED + 1[self.P_LOCKED]' = v
                if (not v.discovered) & (((((string.find(k, ^j_) if string.find(k, ^j_) else string.find(k, ^b_)) if (string.find(k, ^j_) if string.find(k, ^j_) else string.find(k, ^b_)) else string.find(k, ^e_)) if ((string.find(k, ^j_) if string.find(k, ^j_) else string.find(k, ^b_)) if (string.find(k, ^j_) if string.find(k, ^j_) else string.find(k, ^b_)) else string.find(k, ^e_)) else string.find(k, ^c_)) if (((string.find(k, ^j_) if string.find(k, ^j_) else string.find(k, ^b_)) if (string.find(k, ^j_) if string.find(k, ^j_) else string.find(k, ^b_)) else string.find(k, ^e_)) if ((string.find(k, ^j_) if string.find(k, ^j_) else string.find(k, ^b_)) if (string.find(k, ^j_) if string.find(k, ^j_) else string.find(k, ^b_)) else string.find(k, ^e_)) else string.find(k, ^c_)) else string.find(k, ^p_)) if ((((string.find(k, ^j_) if string.find(k, ^j_) else string.find(k, ^b_)) if (string.find(k, ^j_) if string.find(k, ^j_) else string.find(k, ^b_)) else string.find(k, ^e_)) if ((string.find(k, ^j_) if string.find(k, ^j_) else string.find(k, ^b_)) if (string.find(k, ^j_) if string.find(k, ^j_) else string.find(k, ^b_)) else string.find(k, ^e_)) else string.find(k, ^c_)) if (((string.find(k, ^j_) if string.find(k, ^j_) else string.find(k, ^b_)) if (string.find(k, ^j_) if string.find(k, ^j_) else string.find(k, ^b_)) else string.find(k, ^e_)) if ((string.find(k, ^j_) if string.find(k, ^j_) else string.find(k, ^b_)) if (string.find(k, ^j_) if string.find(k, ^j_) else string.find(k, ^b_)) else string.find(k, ^e_)) else string.find(k, ^c_)) else string.find(k, ^p_)) else string.find(k, ^v_)) & 'k[meta.discovered]':
                    v.discovered = True
                if (v.discovered & 'k[meta.alerted]' if v.discovered & 'k[meta.alerted]' else v.set == 'Back') if (v.discovered & 'k[meta.alerted]' if v.discovered & 'k[meta.alerted]' else v.set == 'Back') else v.start_alerted:
                    v.alerted = True
                elif v.discovered:
                    v.alerted = Falsetable.sort()
        for kv in pairs():
            v.key = k
            if (not v.wip) & (not v.demo):
                if TESTHELPER_unlocks:
                    v.discovered = True';'
                    v.alerted = True
                if (not v.discovered) & 'k[meta.discovered]':
                    v.discovered = True
                if v.discovered & 'k[meta.alerted]':
                    v.alerted = True
                elif v.discovered:
                    v.alerted = False
        for kv in pairs():
            v.key = k
            if (not v.wip) & (not v.demo):
                if TESTHELPER_unlocks:
                    v.discovered = True';'
                    v.alerted = True
                if (not v.discovered) & 'k[meta.discovered]':
                    v.discovered = True
                if v.discovered & 'k[meta.alerted]':
                    v.alerted = True
                elif v.discovered:
                    v.alerted = Falsetable.insert('Tag'[self.P_CENTER_POOLS], v)
        for kv in pairs():
            v.key = k
            if (not v.wip) & (not v.demo):
                if TESTHELPER_unlocks:
                    v.discovered = True';'
                    v.alerted = True
                if (not v.discovered) & 'k[meta.discovered]':
                    v.discovered = True
                if v.discovered & 'k[meta.alerted]':
                    v.alerted = True
                elif v.discovered:
                    v.alerted = Falsetable.insert('Seal'[self.P_CENTER_POOLS], v)
        for kv in pairs():
            v.key = ktable.insert('Stake'[self.P_CENTER_POOLS], v)
        for kv in pairs():
            v.key = k
            if v.set == 'Joker':table.insert('Joker'[self.P_CENTER_POOLS], v)
            if v.set & v.demo & v.pos:table.insert('Demo'[self.P_CENTER_POOLS], v)
            if not v.wip:
                if v.set & (v.set != 'Joker') & (not v.skip_pool) & (not v.omit):table.insert(v.set[self.P_CENTER_POOLS], v)
                if v.set == 'Tarot' if v.set == 'Tarot' else v.set == 'Planet':table.insert('Tarot_Planet'[self.P_CENTER_POOLS], v)
                if v.consumeable:table.insert('Consumeables'[self.P_CENTER_POOLS], v)
                if v.rarity & (v.set == 'Joker') & (not v.demo):table.insert(v.rarity[self.P_JOKER_RARITY_POOLS], v)table.sort("Joker"[self.P_CENTER_POOLS])table.sort("Tarot"[self.P_CENTER_POOLS])table.sort("Planet"[self.P_CENTER_POOLS])table.sort("Tarot_Planet"[self.P_CENTER_POOLS])table.sort("Spectral"[self.P_CENTER_POOLS])table.sort("Voucher"[self.P_CENTER_POOLS])table.sort("Booster"[self.P_CENTER_POOLS])table.sort("Consumeables"[self.P_CENTER_POOLS])table.sort("Back"[self.P_CENTER_POOLS])table.sort("Enhanced"[self.P_CENTER_POOLS])table.sort("Stake"[self.P_CENTER_POOLS])table.sort("Tag"[self.P_CENTER_POOLS])table.sort("Seal"[self.P_CENTER_POOLS])table.sort("Demo"[self.P_CENTER_POOLS])
        for i in range(1, 4, ):table.sort(i[self.P_JOKER_RARITY_POOLS])

    def load_profile(self, _profile):
        if not '_profile[G.PROFILES]':
            _profile = 1
        G.SETTINGS.profile = _profile
        info = get_compressed()
        if info != 'None':
            for kv in pairs():
                'k[G.PROFILES[G.SETTINGS.profile]]' = v
        temp_profile = {'MEMORY': {'deck': 'Red Deck', 'stake': 1}, 'stake': 1, 'high_scores': {'hand': {'label': 'Best Hand', 'amt': 0}, 'furthest_round': {'label': 'Highest Round', 'amt': 0}, 'furthest_ante': {'label': 'Highest Ante', 'amt': 0}, 'most_money': {'label': 'Most Money', 'amt': 0}, 'boss_streak': {'label': 'Most Bosses in a Row', 'amt': 0}, 'collection': {'label': 'Collection', 'amt': 0, 'tot': 1}, 'win_streak': {'label': 'Best Win Streak', 'amt': 0}, 'current_streak': {'label': '', 'amt': 0}, 'poker_hand': {'label': 'Most Played Hand', 'amt': 0}}, 'career_stats': {'c_round_interest_cap_streak': 0, 'c_dollars_earned': 0, 'c_shop_dollars_spent': 0, 'c_tarots_bought': 0, 'c_planets_bought': 0, 'c_playing_cards_bought': 0, 'c_vouchers_bought': 0, 'c_tarot_reading_used': 0, 'c_planetarium_used': 0, 'c_shop_rerolls': 0, 'c_cards_played': 0, 'c_cards_discarded': 0, 'c_losses': 0, 'c_wins': 0, 'c_rounds': 0, 'c_hands_played': 0, 'c_face_cards_played': 0, 'c_jokers_sold': 0, 'c_cards_sold': 0, 'c_single_hand_round_streak': 0}, 'progress': {}, 'joker_usage': {}, 'consumeable_usage': {}, 'voucher_usage': {}, 'hand_usage': {}, 'deck_usage': {}, 'deck_stakes': {}, 'challenges_unlocked': 'None', 'challenge_progress': {'completed': {}, 'unlocked': {}}}
        recursive_init = None
        recursive_init = lambda t1t2: 
        for kv in pairs(t1):
            if not 'k[t2]':
                'k[t2]' = v
            elif (type(k[t2]) == 'table') & (type(v) == 'table'):recursive_init(v, k[t2])recursive_init(temp_profile, G.SETTINGS.profile[G.PROFILES])

    def set_language(self):
        if not self.LANGUAGES:
            if not love.filesystem.read() if not love.filesystem.read() else G.F_ENGLISH_ONLY:
                G.SETTINGS.language = 'en-us'
            self.LANGUAGES = {'en-us': {'font': 1, 'label': 'English', 'key': 'en-us', 'button': 'Language Feedback', 'warning': {1: 'This language is still in Beta. To help us', 2: 'improve it, please click on the feedback button.', 3: 'Click again to confirm'}}, 'de': {'font': 1, 'label': 'Deutsch', 'key': 'de', 'beta': 'None', 'button': 'Feedback zur Übersetzung', 'warning': {1: 'Diese Übersetzung ist noch im Beta-Stadium. Willst du uns helfen,', 2: 'sie zu verbessern? Dann klicke bitte auf die Feedback-Taste.', 3: 'Zum Bestätigen erneut klicken'}}, 'es_419': {'font': 1, 'label': 'Español (México)', 'key': 'es_419', 'beta': 'None', 'button': 'Sugerencias de idioma', 'warning': {1: 'Este idioma todav�\xada está en Beta. Pulsa el botón', 2: 'de sugerencias para ayudarnos a mejorarlo.', 3: 'Haz clic de nuevo para confirmar'}}, 'es_ES': {'font': 1, 'label': 'Español (España)', 'key': 'es_ES', 'beta': 'None', 'button': 'Sugerencias de idioma', 'warning': {1: 'Este idioma todav�\xada está en Beta. Pulsa el botón', 2: 'de sugerencias para ayudarnos a mejorarlo.', 3: 'Haz clic de nuevo para confirmar'}}, 'fr': {'font': 1, 'label': 'Français', 'key': 'fr', 'beta': 'None', 'button': 'Partager votre avis', 'warning': {1: 'La traduction française est encore en version bêta. ', 2: 'Veuillez cliquer sur le bouton pour nous donner votre avis.', 3: 'Cliquez �\xa0 nouveau pour confirmer'}}, 'id': {'font': 1, 'label': 'Bahasa Indonesia', 'key': 'id', 'beta': True, 'button': 'Umpan Balik Bahasa', 'warning': {1: 'Bahasa ini masih dalam tahap Beta. Untuk membantu', 2: 'kami meningkatkannya, silakan klik tombol umpan balik.', 3: 'Klik lagi untuk mengonfirmasi'}}, 'it': {'font': 1, 'label': 'Italiano', 'key': 'it', 'beta': 'None', 'button': 'Feedback traduzione', 'warning': {1: 'Questa traduzione è ancora in Beta. Per', 2: 'aiutarci a migliorarla, clicca il tasto feedback', 3: 'Fai clic di nuovo per confermare'}}, 'ja': {'font': 5, 'label': '日本語', 'key': 'ja', 'beta': 'None', 'button': '�案�る', 'warning': {1: '��翻訳��在ベータ版��。�案�����\xa0���', 2: 'ボタンをクリック����\xa0��。', 3: 'も�一度クリック��確�'}}, 'ko': {'font': 4, 'label': '한�\xad어', 'key': 'ko', 'beta': True, 'button': '번�\xad 피드백', 'warning': {1: '� 언어는 아� �\xa0타 단계� 있습니다. ', 2: '번�\xad� �와주시�\xa0�면 피드백 버튼� 눌러주세요.', 3: '다시 ���\xad해서 확�하세요'}}, 'nl': {'font': 1, 'label': 'Nederlands', 'key': 'nl', 'beta': 'None', 'button': 'Taal suggesties', 'warning': {1: 'Deze taal is nog in de Beta fase. Help ons het te ', 2: 'verbeteren door op de suggestie knop te klikken.', 3: 'Klik opnieuw om te bevestigen'}}, 'pl': {'font': 1, 'label': 'Polski', 'key': 'pl', 'beta': 'None', 'button': 'Wyślij uwagi do tłumaczenia', 'warning': {1: 'Polska wersja językowa jest w fazie Beta. By pomóc nam poprawić', 2: ' jakość tłumaczenia, kliknij przycisk i podziel się swoją opinią i uwagami.', 3: 'Kliknij ponownie, aby potwierdzić'}}, 'pt_BR': {'font': 1, 'label': 'Português', 'key': 'pt_BR', 'beta': 'None', 'button': 'Feedback de Tradução', 'warning': {1: 'Esta tradução ainda está em Beta. Se quiser nos ajudar', 2: 'a melhorá-la, clique no botão de feedback por favor', 3: 'Clique novamente para confirmar'}}, 'ru': {'font': 6, 'label': '�\xa0у��кий', 'key': 'ru', 'beta': True, 'button': 'Отзыв о �зыке', 'warning': {1: '�\xadтот �зык в�е еще находит�� в Бета-вер�ии. Чтобы помочь', 2: 'нам его улучшить, пожалуй�та, нажмите на кнопку обратной �в�зи.', 3: 'Щелкните �нова, чтобы подтвердить'}}, 'zh_CN': {'font': 2, 'label': '简体�\xad文', 'key': 'zh_CN', 'beta': 'None', 'button': '���馈', 'warning': {1: '这个�\xad言目�尚为Beta版本。 请帮助我们改善翻译�质，', 2: '点击����馈� ��供�\xa0的��。', 3: '�次点击确认'}}, 'zh_TW': {'font': 3, 'label': '�體�\xad文', 'key': 'zh_TW', 'beta': 'None', 'button': '�見回饋', 'warning': {1: '這個語言目�尚為Beta版本。請幫助我們改善翻�\xad��質，', 2: '點擊��見回饋� 來�供�\xa0的�見。', 3: '�按一下��確�'}}, 'all1': {'font': 8, 'label': 'English', 'key': 'all', 'omit': True}, 'all2': {'font': 9, 'label': 'English', 'key': 'all', 'omit': True}}
            self.FONTS = {1: {'file': 'resources/fonts/m6x11plus.ttf', 'render_scale': self.TILESIZE * 10, 'TEXT_HEIGHT_SCALE': 0.83, 'TEXT_OFFSET': {'x': 10, 'y': -20}, 'FONTSCALE': 0.1, 'squish': 1, 'DESCSCALE': 1}, 2: {'file': 'resources/fonts/NotoSansSC-Bold.ttf', 'render_scale': self.TILESIZE * 7, 'TEXT_HEIGHT_SCALE': 0.7, 'TEXT_OFFSET': {'x': 0, 'y': -35}, 'FONTSCALE': 0.12, 'squish': 1, 'DESCSCALE': 1.1}, 3: {'file': 'resources/fonts/NotoSansTC-Bold.ttf', 'render_scale': self.TILESIZE * 7, 'TEXT_HEIGHT_SCALE': 0.7, 'TEXT_OFFSET': {'x': 0, 'y': -35}, 'FONTSCALE': 0.12, 'squish': 1, 'DESCSCALE': 1.1}, 4: {'file': 'resources/fonts/NotoSansKR-Bold.ttf', 'render_scale': self.TILESIZE * 7, 'TEXT_HEIGHT_SCALE': 0.8, 'TEXT_OFFSET': {'x': 0, 'y': -20}, 'FONTSCALE': 0.12, 'squish': 1, 'DESCSCALE': 1}, 5: {'file': 'resources/fonts/NotoSansJP-Bold.ttf', 'render_scale': self.TILESIZE * 7, 'TEXT_HEIGHT_SCALE': 0.8, 'TEXT_OFFSET': {'x': 0, 'y': -20}, 'FONTSCALE': 0.12, 'squish': 1, 'DESCSCALE': 1}, 6: {'file': 'resources/fonts/NotoSans-Bold.ttf', 'render_scale': self.TILESIZE * 7, 'TEXT_HEIGHT_SCALE': 0.65, 'TEXT_OFFSET': {'x': 0, 'y': -40}, 'FONTSCALE': 0.12, 'squish': 1, 'DESCSCALE': 1}, 7: {'file': 'resources/fonts/m6x11plus.ttf', 'render_scale': self.TILESIZE * 10, 'TEXT_HEIGHT_SCALE': 0.9, 'TEXT_OFFSET': {'x': 10, 'y': 15}, 'FONTSCALE': 0.1, 'squish': 1, 'DESCSCALE': 1}, 8: {'file': 'resources/fonts/GoNotoCurrent-Bold.ttf', 'render_scale': self.TILESIZE * 10, 'TEXT_HEIGHT_SCALE': 0.8, 'TEXT_OFFSET': {'x': 10, 'y': -20}, 'FONTSCALE': 0.1, 'squish': 1, 'DESCSCALE': 1}, 9: {'file': 'resources/fonts/GoNotoCJKCore.ttf', 'render_scale': self.TILESIZE * 10, 'TEXT_HEIGHT_SCALE': 0.8, 'TEXT_OFFSET': {'x': 10, 'y': -20}, 'FONTSCALE': 0.1, 'squish': 1, 'DESCSCALE': 1}}
            for _v in ipairs():
                if love.filesystem.getInfo():
                    v.FONT = love.graphics.newFont()
            for _v in pairs():
                v.font = 'v.font[self.FONTS]'
        self.LANG = 'self.SETTINGS.language[self.LANGUAGES]' if 'self.SETTINGS.language[self.LANGUAGES]' else "'en-us'[self.LANGUAGES]"
        localization = love.filesystem.getInfo()
        if localization != 'None':
            self.localization = ()init_localization()

    def set_render_settings(self):
        self.SETTINGS.GRAPHICS.texture_scaling = self.SETTINGS.GRAPHICS.texture_scaling if self.SETTINGS.GRAPHICS.texture_scaling else 2love.graphics.setDefaultFilter()love.graphics.setLineStyle(rough)
        self.animation_atli = {1: {'name': 'blind_chips', 'path': 'resources/textures/' + self.SETTINGS.GRAPHICS.texture_scaling + 'x/BlindChips.png', 'px': 34, 'py': 34, 'frames': 21}, 2: {'name': 'shop_sign', 'path': 'resources/textures/' + self.SETTINGS.GRAPHICS.texture_scaling + 'x/ShopSignAnimation.png', 'px': 113, 'py': 57, 'frames': 4}}
        self.asset_atli = {1: {'name': 'cards_1', 'path': 'resources/textures/' + self.SETTINGS.GRAPHICS.texture_scaling + 'x/8BitDeck.png', 'px': 71, 'py': 95}, 2: {'name': 'cards_2', 'path': 'resources/textures/' + self.SETTINGS.GRAPHICS.texture_scaling + 'x/8BitDeck_opt2.png', 'px': 71, 'py': 95}, 3: {'name': 'centers', 'path': 'resources/textures/' + self.SETTINGS.GRAPHICS.texture_scaling + 'x/Enhancers.png', 'px': 71, 'py': 95}, 4: {'name': 'Joker', 'path': 'resources/textures/' + self.SETTINGS.GRAPHICS.texture_scaling + 'x/Jokers.png', 'px': 71, 'py': 95}, 5: {'name': 'Tarot', 'path': 'resources/textures/' + self.SETTINGS.GRAPHICS.texture_scaling + 'x/Tarots.png', 'px': 71, 'py': 95}, 6: {'name': 'Voucher', 'path': 'resources/textures/' + self.SETTINGS.GRAPHICS.texture_scaling + 'x/Vouchers.png', 'px': 71, 'py': 95}, 7: {'name': 'Booster', 'path': 'resources/textures/' + self.SETTINGS.GRAPHICS.texture_scaling + 'x/boosters.png', 'px': 71, 'py': 95}, 8: {'name': 'ui_1', 'path': 'resources/textures/' + self.SETTINGS.GRAPHICS.texture_scaling + 'x/ui_assets.png', 'px': 18, 'py': 18}, 9: {'name': 'ui_2', 'path': 'resources/textures/' + self.SETTINGS.GRAPHICS.texture_scaling + 'x/ui_assets_opt2.png', 'px': 18, 'py': 18}, 10: {'name': 'balatro', 'path': 'resources/textures/' + self.SETTINGS.GRAPHICS.texture_scaling + 'x/balatro.png', 'px': 333, 'py': 216}, 11: {'name': 'gamepad_ui', 'path': 'resources/textures/' + self.SETTINGS.GRAPHICS.texture_scaling + 'x/gamepad_ui.png', 'px': 32, 'py': 32}, 12: {'name': 'icons', 'path': 'resources/textures/' + self.SETTINGS.GRAPHICS.texture_scaling + 'x/icons.png', 'px': 66, 'py': 66}, 13: {'name': 'tags', 'path': 'resources/textures/' + self.SETTINGS.GRAPHICS.texture_scaling + 'x/tags.png', 'px': 34, 'py': 34}, 14: {'name': 'stickers', 'path': 'resources/textures/' + self.SETTINGS.GRAPHICS.texture_scaling + 'x/stickers.png', 'px': 71, 'py': 95}, 15: {'name': 'chips', 'path': 'resources/textures/' + self.SETTINGS.GRAPHICS.texture_scaling + 'x/chips.png', 'px': 29, 'py': 29}}
        self.asset_images = {1: {'name': 'playstack_logo', 'path': 'resources/textures/1x/playstack-logo.png', 'px': 1417, 'py': 1417}, 2: {'name': 'localthunk_logo', 'path': 'resources/textures/1x/localthunk-logo.png', 'px': 1390, 'py': 560}}
        for i in range(1, len(self.animation_atli), ):
            'self.animation_atli[i].name[self.ANIMATION_ATLAS]' = {}
            'self.animation_atli[i].name[self.ANIMATION_ATLAS]'.name = 'i[self.animation_atli]'.name
            'self.animation_atli[i].name[self.ANIMATION_ATLAS]'.image = love.graphics.newImage()
            'self.animation_atli[i].name[self.ANIMATION_ATLAS]'.px = 'i[self.animation_atli]'.px
            'self.animation_atli[i].name[self.ANIMATION_ATLAS]'.py = 'i[self.animation_atli]'.py
            'self.animation_atli[i].name[self.ANIMATION_ATLAS]'.frames = 'i[self.animation_atli]'.frames
        for i in range(1, len(self.asset_atli), ):
            'self.asset_atli[i].name[self.ASSET_ATLAS]' = {}
            'self.asset_atli[i].name[self.ASSET_ATLAS]'.name = 'i[self.asset_atli]'.name
            'self.asset_atli[i].name[self.ASSET_ATLAS]'.image = love.graphics.newImage()
            'self.asset_atli[i].name[self.ASSET_ATLAS]'.type = 'i[self.asset_atli]'.type
            'self.asset_atli[i].name[self.ASSET_ATLAS]'.px = 'i[self.asset_atli]'.px
            'self.asset_atli[i].name[self.ASSET_ATLAS]'.py = 'i[self.asset_atli]'.py
        for i in range(1, len(self.asset_images), ):
            'self.asset_images[i].name[self.ASSET_ATLAS]' = {}
            'self.asset_images[i].name[self.ASSET_ATLAS]'.name = 'i[self.asset_images]'.name
            'self.asset_images[i].name[self.ASSET_ATLAS]'.image = love.graphics.newImage()
            'self.asset_images[i].name[self.ASSET_ATLAS]'.type = 'i[self.asset_images]'.type
            'self.asset_images[i].name[self.ASSET_ATLAS]'.px = 'i[self.asset_images]'.px
            'self.asset_images[i].name[self.ASSET_ATLAS]'.py = 'i[self.asset_images]'.py
        for _v in pairs():v.reset()
        self.ASSET_ATLAS.Planet = self.ASSET_ATLAS.Tarot
        self.ASSET_ATLAS.Spectral = self.ASSET_ATLAS.Tarot

    def init_window(self, reset):
        self.ROOM_PADDING_H = 0.7
        self.ROOM_PADDING_W = 1
        self.WINDOWTRANS = {'x': 0, 'y': 0, 'w': self.TILE_W + 2 * self.ROOM_PADDING_W, 'h': self.TILE_H + 2 * self.ROOM_PADDING_H}
        self.window_prev = {'orig_scale': self.TILESCALE, 'w': self.WINDOWTRANS.w * self.TILESIZE * self.TILESCALE, 'h': self.WINDOWTRANS.h * self.TILESIZE * self.TILESCALE, 'orig_ratio': self.WINDOWTRANS.w * self.TILESIZE * self.TILESCALE / (self.WINDOWTRANS.h * self.TILESIZE * self.TILESCALE)}
        G.SETTINGS.QUEUED_CHANGE = G.SETTINGS.QUEUED_CHANGE if G.SETTINGS.QUEUED_CHANGE else {}
        G.SETTINGS.QUEUED_CHANGE.screenmode = G.SETTINGS.WINDOW.screenmodeG.FUNCS.apply_window_changes(True)

    def delete_run(self):
        if self.ROOM:remove_all(G.STAGE[G.STAGE_OBJECTS])
            self.load_shop_booster = 'None'
            self.load_shop_jokers = 'None'
            self.load_shop_vouchers = 'None'
            if self.buttons:self.buttons.remove()';'
                self.buttons = 'None'
            if self.deck_preview:self.deck_preview.remove()';'
                self.deck_preview = 'None'
            if self.shop:self.shop.remove()';'
                self.shop = 'None'
            if self.blind_select:self.blind_select.remove()';'
                self.blind_select = 'None'
            if self.booster_pack:self.booster_pack.remove()';'
                self.booster_pack = 'None'
            if self.MAIN_MENU_UI:self.MAIN_MENU_UI.remove()';'
                self.MAIN_MENU_UI = 'None'
            if self.SPLASH_FRONT:self.SPLASH_FRONT.remove()';'
                self.SPLASH_FRONT = 'None'
            if self.SPLASH_BACK:self.SPLASH_BACK.remove()';'
                self.SPLASH_BACK = 'None'
            if self.SPLASH_LOGO:self.SPLASH_LOGO.remove()';'
                self.SPLASH_LOGO = 'None'
            if self.GAME_OVER_UI:self.GAME_OVER_UI.remove()';'
                self.GAME_OVER_UI = 'None'
            if self.collection_alert:self.collection_alert.remove()';'
                self.collection_alert = 'None'
            if self.HUD:self.HUD.remove()';'
                self.HUD = 'None'
            if self.HUD_blind:self.HUD_blind.remove()';'
                self.HUD_blind = 'None'
            if self.HUD_tags:
                for kv in pairs():v.remove()
                self.HUD_tags = 'None'
            if self.OVERLAY_MENU:self.OVERLAY_MENU.remove()';'
                self.OVERLAY_MENU = 'None'
            if self.OVERLAY_TUTORIAL:G.OVERLAY_TUTORIAL.Jimbo.remove()
                if G.OVERLAY_TUTORIAL.content:G.OVERLAY_TUTORIAL.content.remove()G.OVERLAY_TUTORIAL.remove()
                G.OVERLAY_TUTORIAL = 'None'
            for kv in pairs(G):
                if (type(v) == 'table') & v.is & v.is(CardArea):
                    'k[G]' = 'None'
            G.I.CARD = {}
        G.VIEWING_DECK = 'None'G.E_MANAGER.clear_queue()G.CONTROLLER.mod_cursor_context_layer()
        G.CONTROLLER.focus_cursor_stack = {}
        G.CONTROLLER.focus_cursor_stack_level = 1
        if G.GAME:
            G.GAME.won = False
        G.STATE = -1

    def save_progress(self):
        G.ARGS.save_progress = G.ARGS.save_progress if G.ARGS.save_progress else {}
        G.ARGS.save_progress.UDA = EMPTY()
        G.ARGS.save_progress.SETTINGS = G.SETTINGS
        G.ARGS.save_progress.PROFILE = 'G.SETTINGS.profile[G.PROFILES]'
        for kv in pairs():
            'k[G.ARGS.save_progress.UDA]' = (v.unlocked & 'u' if v.unlocked & 'u' else '') + (v.discovered & 'd' if v.discovered & 'd' else '') + (v.alerted & 'a' if v.alerted & 'a' else '')
        for kv in pairs():
            'k[G.ARGS.save_progress.UDA]' = (v.unlocked & 'u' if v.unlocked & 'u' else '') + (v.discovered & 'd' if v.discovered & 'd' else '') + (v.alerted & 'a' if v.alerted & 'a' else '')
        for kv in pairs():
            'k[G.ARGS.save_progress.UDA]' = (v.unlocked & 'u' if v.unlocked & 'u' else '') + (v.discovered & 'd' if v.discovered & 'd' else '') + (v.alerted & 'a' if v.alerted & 'a' else '')
        for kv in pairs():
            'k[G.ARGS.save_progress.UDA]' = (v.unlocked & 'u' if v.unlocked & 'u' else '') + (v.discovered & 'd' if v.discovered & 'd' else '') + (v.alerted & 'a' if v.alerted & 'a' else '')
        G.FILE_HANDLER = G.FILE_HANDLER if G.FILE_HANDLER else {}
        G.FILE_HANDLER.progress = True
        G.FILE_HANDLER.update_queued = True

    def save_notify(self, card):G.SAVE_MANAGER.channel.push()

    def save_settings(self):
        G.ARGS.save_settings = G.SETTINGS
        G.FILE_HANDLER = G.FILE_HANDLER if G.FILE_HANDLER else {}
        G.FILE_HANDLER.settings = True
        G.FILE_HANDLER.update_queued = True

    def save_metrics(self):
        G.ARGS.save_metrics = G.METRICS
        G.FILE_HANDLER = G.FILE_HANDLER if G.FILE_HANDLER else {}
        G.FILE_HANDLER.settings = True
        G.FILE_HANDLER.update_queued = True

    def prep_stage(self, new_stage, new_state, new_game_obj):
        for kv in pairs():
            'k[self.CONTROLLER.locks]' = 'None'
        if new_game_obj:
            self.GAME = self.init_game_object()
        self.STAGE = new_stage if new_stage else self.STAGES.MAIN_MENU
        self.STATE = new_state if new_state else self.STATES.MENU
        self.STATE_COMPLETE = False
        self.SETTINGS.paused = False
        self.ROOM = Node()
        self.ROOM.jiggle = 0
        self.ROOM.states.drag.can = Falseself.ROOM.set_container()
        self.ROOM_ATTACH = Moveable()
        self.ROOM_ATTACH.states.drag.can = Falseself.ROOM_ATTACH.set_container()love.resize()

    def sandbox(self):
        G.TIMERS.REAL = 0
        G.TIMERS.TOTAL = 0self.prep_stage()
        self.GAME.selected_back = Back()ease_background_colour()
        G.SANDBOX = {'vort_time': 7, 'vort_speed': 0, 'col_op': {1: 'RED', 2: 'BLUE', 3: 'GREEN', 4: 'BLACK', 5: 'L_BLACK', 6: 'WHITE', 7: 'EDITION', 8: 'DARK_EDITION', 9: 'ORANGE', 10: 'PURPLE'}, 'col1': G.C.RED, 'col2': G.C.BLUE, 'mid_flash': 0, 'joker_text': '', 'edition': 'base', 'tilt': 1, 'card_size': 1, 'base_size': {'w': G.CARD_W, 'h': G.CARD_H}, 'gamespeed': 0}
        if G.SPLASH_FRONT:G.SPLASH_FRONT.remove()';'
            G.SPLASH_FRONT = 'None'
        if G.SPLASH_BACK:G.SPLASH_BACK.remove()';'
            G.SPLASH_BACK = 'None'
        G.SPLASH_BACK = Sprite()G.SPLASH_BACK.set_alignment()G.SPLASH_BACK.define_draw_steps()

        def create_UIBox_sandbox_controls():
            G.FUNCS.col1change = lambda args: 
            G.SANDBOX.col1 = 'args.to_val[G.C]'
            G.FUNCS.col2change = lambda args: 
            G.SANDBOX.col2 = 'args.to_val[G.C]'
            G.FUNCS.edition_change = lambda args: 
            G.SANDBOX.edition = args.to_val
            if G.SANDBOX.joker:G.SANDBOX.joker.set_edition()
            G.FUNCS.pulseme = lambda e: 
            if math.random() > 0.998:e.config.object.pulse(1)
            G.FUNCS.spawn_joker = lambda e: G.FUNCS.rem_joker()';'
            G.SANDBOX.joker = add_joker()
            G.FUNCS.rem_joker = lambda e: 
            if G.SANDBOX.joker:G.SANDBOX.joker.remove()';'
                G.SANDBOX.joker = 'None'
            G.FUNCS.do_time = lambda args: 
            if args.to_val == 'PLAY':
                G.SANDBOX.gamespeed = 1
            else:
                G.SANDBOX.gamespeed = 0
            G.FUNCS.cb = lambda rt: 
            G.CARD_W = 'rt.ref_value[rt.ref_table]' * G.SANDBOX.base_size.w';'
            G.CARD_H = 'rt.ref_value[rt.ref_table]' * G.SANDBOX.base_size.hG.E_MANAGER.add_event()
            t = {'n': G.UIT.ROOT, 'config': {'align': 'cm', 'colour': G.C.CLEAR}, 'nodes': {1: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.05, 'r': 0.1, 'emboss': 0.1, 'colour': G.C.L_BLACK}, 'nodes': {1: create_slider(), 2: create_option_cycle(), 3: create_slider(), 4: create_slider(), 5: create_option_cycle(), 6: create_option_cycle(), 7: {'n': G.UIT.R, 'config': {'align': 'cm', 'padding': 0.05}, 'nodes': {1: UIBox_button(), 2: create_text_input(), 3: UIBox_button()}}, 8: create_option_cycle()}}}}
            return t
        G.SANDBOX.UI = UIBox()G.SANDBOX.UI.recalculate(True)

    def splash_screen(self):
        if G.SETTINGS.skip_splash == 'Yes':G.main_menu()
            return Falseself.prep_stage()G.E_MANAGER.add_event()G.E_MANAGER.add_event()

    def main_menu(self, change_context):
        if change_context != 'splash':
            G.TIMERS.REAL = 12
            G.TIMERS.TOTAL = 12
        else:RESET_STATES()self.prep_stage()
        self.GAME.selected_back = Back()
        if (not G.SETTINGS.tutorial_complete) & "'big_blind'[G.SETTINGS.tutorial_progress.completed_parts]":
            G.SETTINGS.tutorial_complete = TrueG.FUNCS.change_shadows()ease_background_colour()
        if G.SPLASH_FRONT:G.SPLASH_FRONT.remove()';'
            G.SPLASH_FRONT = 'None'
        if G.SPLASH_BACK:G.SPLASH_BACK.remove()';'
            G.SPLASH_BACK = 'None'
        G.SPLASH_BACK = Sprite()G.SPLASH_BACK.set_alignment()
        splash_args = {'mid_flash': (change_context == 'splash') & 1.6 if (change_context == 'splash') & 1.6 else 0.0}ease_value(splash_args, mid_flash)G.SPLASH_BACK.define_draw_steps()G.E_MANAGER.add_event()
        SC_scale = 1.1 * (G.debug_splash_size_toggle & 0.8 if G.debug_splash_size_toggle & 0.8 else 1)
        CAI = {'TITLE_TOP_W': G.CARD_W, 'TITLE_TOP_H': G.CARD_H}
        self.title_top = CardArea(0, 0)
        G.SPLASH_LOGO = Sprite(0, 0)G.SPLASH_LOGO.set_alignment()G.SPLASH_LOGO.define_draw_steps()
        G.SPLASH_LOGO.dissolve_colours = {1: G.C.WHITE, 2: G.C.WHITE}
        G.SPLASH_LOGO.dissolve = 1
        replace_card = Card()self.title_top.emplace(replace_card)
        replace_card.states.visible = False
        replace_card.no_ui = True
        replace_card.ambient_tilt = 0.0G.E_MANAGER.add_event()G.E_MANAGER.add_event()delay()
        if replace_card & G.P_CENTERS.j_blueprint.unlocked:
            viable_unlockables = {}
            for kv in ipairs():
                if (v.set == 'Voucher' if v.set == 'Voucher' else v.set == 'Joker') & (not v.demo):
                    '#viable_unlockables + 1[viable_unlockables]' = v
            if len(viable_unlockables > 0):
                card = NoneG.E_MANAGER.add_event()G.E_MANAGER.add_event()G.E_MANAGER.add_event()set_screen_positions()self.title_top.sort(order)self.title_top.set_ranks()self.title_top.align_cards()self.title_top.hard_set_cards()G.E_MANAGER.add_event()
        for kv in pairs():check_for_unlock()check_for_unlock()G.E_MANAGER.add_event()UIBox()

    def demo_cta(self):self.prep_stage()
        self.GAME.selected_back = Back()G.FUNCS.change_shadows()ease_background_colour()
        if G.SPLASH_FRONT:G.SPLASH_FRONT.remove()';'
            G.SPLASH_FRONT = 'None'
        if G.SPLASH_BACK:G.SPLASH_BACK.remove()';'
            G.SPLASH_BACK = 'None'
        G.SPLASH_BACK = Sprite()G.SPLASH_BACK.set_alignment()
        splash_args = {'mid_flash': 1.6}ease_value(splash_args, mid_flash)G.SPLASH_BACK.define_draw_steps()
        SC_scale = 0.9 * (G.debug_splash_size_toggle & 0.8 if G.debug_splash_size_toggle & 0.8 else 1)
        CAI = {'TITLE_TOP_W': G.CARD_W, 'TITLE_TOP_H': G.CARD_H}
        self.title_top = CardArea(0, 0)
        G.SPLASH_LOGO = Sprite(0, 0)G.SPLASH_LOGO.set_alignment()G.SPLASH_LOGO.define_draw_steps()
        G.SPLASH_LOGO.dissolve_colours = {1: G.C.WHITE, 2: G.C.WHITE}
        G.SPLASH_LOGO.dissolve = 1
        replace_card = Card()self.title_top.emplace(replace_card)
        replace_card.states.visible = False
        replace_card.no_ui = True
        replace_card.ambient_tilt = 0.0G.E_MANAGER.add_event()G.E_MANAGER.add_event()delay()G.E_MANAGER.add_event()set_screen_positions()self.title_top.sort(order)self.title_top.set_ranks()self.title_top.align_cards()self.title_top.hard_set_cards()
        playstack = Sprite(0, 0, 1.7, 1.7, "playstack_logo"[G.ASSET_ATLAS])
        playstack.states.drag.can = False
        localthunk = Sprite(0, 0)
        localthunk.states.drag.can = False
        self.MAIN_MENU_UI = UIBox()
        self.MAIN_MENU_UI.states.visible = FalseG.E_MANAGER.add_event()

    def init_game_object(self):
        bosses_used = {}
        for kv in pairs():
            if v.boss:
                'k[bosses_used]' = 0
        return {'won': False, 'round_scores': {'furthest_ante': {'label': 'Ante', 'amt': 0}, 'furthest_round': {'label': 'Round', 'amt': 0}, 'hand': {'label': 'Best Hand', 'amt': 0}, 'poker_hand': {'label': 'Most Played Hand', 'amt': 0}, 'new_collection': {'label': 'New Discoveries', 'amt': 0}, 'cards_played': {'label': 'Cards Played', 'amt': 0}, 'cards_discarded': {'label': 'Cards Discarded', 'amt': 0}, 'times_rerolled': {'label': 'Times Rerolled', 'amt': 0}, 'cards_purchased': {'label': 'Cards Purchased', 'amt': 0}}, 'joker_usage': {}, 'consumeable_usage': {}, 'hand_usage': {}, 'last_tarot_planet': 'None', 'win_ante': 8, 'stake': 1, 'modifiers': {}, 'starting_params': get_starting_params(), 'banned_keys': {}, 'round': 0, 'probabilities': {'normal': 1}, 'bosses_used': bosses_used, 'pseudorandom': {}, 'starting_deck_size': 52, 'ecto_minus': 1, 'pack_size': 2, 'skips': 0, 'STOP_USE': 0, 'edition_rate': 1, 'joker_rate': 20, 'tarot_rate': 4, 'planet_rate': 4, 'spectral_rate': 0, 'playing_card_rate': 0, 'consumeable_buffer': 0, 'joker_buffer': 0, 'discount_percent': 0, 'interest_cap': 25, 'interest_amount': 1, 'inflation': 0, 'hands_played': 0, 'unused_discards': 0, 'perishable_rounds': 5, 'rental_rate': 3, 'blind': 'None', 'chips': 0, 'chips_text': '0', 'voucher_text': '', 'dollars': 0, 'max_jokers': 0, 'bankrupt_at': 0, 'current_boss_streak': 0, 'base_reroll_cost': 5, 'blind_on_deck': 'None', 'sort': 'desc', 'previous_round': {'dollars': 4}, 'tags': {}, 'tag_tally': 0, 'pool_flags': {}, 'used_jokers': {}, 'used_vouchers': {}, 'current_round': {'current_hand': {'chips': 0, 'chip_text': '0', 'mult': 0, 'mult_text': '0', 'chip_total': 0, 'chip_total_text': '', 'handname': '', 'hand_level': ''}, 'used_packs': {}, 'cards_flipped': 0, 'round_text': 'Round ', 'idol_card': {'suit': 'Spades', 'rank': 'Ace'}, 'mail_card': {'rank': 'Ace'}, 'ancient_card': {'suit': 'Spades'}, 'castle_card': {'suit': 'Spades'}, 'hands_left': 0, 'hands_played': 0, 'discards_left': 0, 'discards_used': 0, 'dollars': 0, 'reroll_cost': 5, 'reroll_cost_increase': 0, 'jokers_purchased': 0, 'free_rerolls': 0, 'round_dollars': 0, 'dollars_to_be_earned': '!!!', 'most_played_poker_hand': 'High Card'}, 'round_resets': {'hands': 1, 'discards': 1, 'reroll_cost': 1, 'temp_reroll_cost': 'None', 'temp_handsize': 'None', 'ante': 1, 'blind_ante': 1, 'blind_states': {'Small': 'Select', 'Big': 'Upcoming', 'Boss': 'Upcoming'}, 'loc_blind_states': {'Small': '', 'Big': '', 'Boss': ''}, 'blind_choices': {'Small': 'bl_small', 'Big': 'bl_big'}, 'boss_rerolled': False}, 'round_bonus': {'next_hands': 0, 'discards': 0}, 'shop': {'joker_max': 2}, 'cards_played': {'Ace': {'suits': {}, 'total': 0}, '2': {'suits': {}, 'total': 0}, '3': {'suits': {}, 'total': 0}, '4': {'suits': {}, 'total': 0}, '5': {'suits': {}, 'total': 0}, '6': {'suits': {}, 'total': 0}, '7': {'suits': {}, 'total': 0}, '8': {'suits': {}, 'total': 0}, '9': {'suits': {}, 'total': 0}, '10': {'suits': {}, 'total': 0}, 'Jack': {'suits': {}, 'total': 0}, 'Queen': {'suits': {}, 'total': 0}, 'King': {'suits': {}, 'total': 0}}, 'hands': {'Flush Five': {'visible': False, 'order': 1, 'mult': 16, 'chips': 160, 's_mult': 16, 's_chips': 160, 'level': 1, 'l_mult': 3, 'l_chips': 50, 'played': 0, 'played_this_round': 0, 'example': {1: {1: 'S_A', 2: True}, 2: {1: 'S_A', 2: True}, 3: {1: 'S_A', 2: True}, 4: {1: 'S_A', 2: True}, 5: {1: 'S_A', 2: True}}}, 'Flush House': {'visible': False, 'order': 2, 'mult': 14, 'chips': 140, 's_mult': 14, 's_chips': 140, 'level': 1, 'l_mult': 4, 'l_chips': 40, 'played': 0, 'played_this_round': 0, 'example': {1: {1: 'D_7', 2: True}, 2: {1: 'D_7', 2: True}, 3: {1: 'D_7', 2: True}, 4: {1: 'D_4', 2: True}, 5: {1: 'D_4', 2: True}}}, 'Five of a Kind': {'visible': False, 'order': 3, 'mult': 12, 'chips': 120, 's_mult': 12, 's_chips': 120, 'level': 1, 'l_mult': 3, 'l_chips': 35, 'played': 0, 'played_this_round': 0, 'example': {1: {1: 'S_A', 2: True}, 2: {1: 'H_A', 2: True}, 3: {1: 'H_A', 2: True}, 4: {1: 'C_A', 2: True}, 5: {1: 'D_A', 2: True}}}, 'Straight Flush': {'visible': True, 'order': 4, 'mult': 8, 'chips': 100, 's_mult': 8, 's_chips': 100, 'level': 1, 'l_mult': 4, 'l_chips': 40, 'played': 0, 'played_this_round': 0, 'example': {1: {1: 'S_Q', 2: True}, 2: {1: 'S_J', 2: True}, 3: {1: 'S_T', 2: True}, 4: {1: 'S_9', 2: True}, 5: {1: 'S_8', 2: True}}}, 'Four of a Kind': {'visible': True, 'order': 5, 'mult': 7, 'chips': 60, 's_mult': 7, 's_chips': 60, 'level': 1, 'l_mult': 3, 'l_chips': 30, 'played': 0, 'played_this_round': 0, 'example': {1: {1: 'S_J', 2: True}, 2: {1: 'H_J', 2: True}, 3: {1: 'C_J', 2: True}, 4: {1: 'D_J', 2: True}, 5: {1: 'C_3', 2: False}}}, 'Full House': {'visible': True, 'order': 6, 'mult': 4, 'chips': 40, 's_mult': 4, 's_chips': 40, 'level': 1, 'l_mult': 2, 'l_chips': 25, 'played': 0, 'played_this_round': 0, 'example': {1: {1: 'H_K', 2: True}, 2: {1: 'C_K', 2: True}, 3: {1: 'D_K', 2: True}, 4: {1: 'S_2', 2: True}, 5: {1: 'D_2', 2: True}}}, 'Flush': {'visible': True, 'order': 7, 'mult': 4, 'chips': 35, 's_mult': 4, 's_chips': 35, 'level': 1, 'l_mult': 2, 'l_chips': 15, 'played': 0, 'played_this_round': 0, 'example': {1: {1: 'H_A', 2: True}, 2: {1: 'H_K', 2: True}, 3: {1: 'H_T', 2: True}, 4: {1: 'H_5', 2: True}, 5: {1: 'H_4', 2: True}}}, 'Straight': {'visible': True, 'order': 8, 'mult': 4, 'chips': 30, 's_mult': 4, 's_chips': 30, 'level': 1, 'l_mult': 3, 'l_chips': 30, 'played': 0, 'played_this_round': 0, 'example': {1: {1: 'D_J', 2: True}, 2: {1: 'C_T', 2: True}, 3: {1: 'C_9', 2: True}, 4: {1: 'S_8', 2: True}, 5: {1: 'H_7', 2: True}}}, 'Three of a Kind': {'visible': True, 'order': 9, 'mult': 3, 'chips': 30, 's_mult': 3, 's_chips': 30, 'level': 1, 'l_mult': 2, 'l_chips': 20, 'played': 0, 'played_this_round': 0, 'example': {1: {1: 'S_T', 2: True}, 2: {1: 'C_T', 2: True}, 3: {1: 'D_T', 2: True}, 4: {1: 'H_6', 2: False}, 5: {1: 'D_5', 2: False}}}, 'Two Pair': {'visible': True, 'order': 10, 'mult': 2, 'chips': 20, 's_mult': 2, 's_chips': 20, 'level': 1, 'l_mult': 1, 'l_chips': 20, 'played': 0, 'played_this_round': 0, 'example': {1: {1: 'H_A', 2: True}, 2: {1: 'D_A', 2: True}, 3: {1: 'C_Q', 2: False}, 4: {1: 'H_4', 2: True}, 5: {1: 'C_4', 2: True}}}, 'Pair': {'visible': True, 'order': 11, 'mult': 2, 'chips': 10, 's_mult': 2, 's_chips': 10, 'level': 1, 'l_mult': 1, 'l_chips': 15, 'played': 0, 'played_this_round': 0, 'example': {1: {1: 'S_K', 2: False}, 2: {1: 'S_9', 2: True}, 3: {1: 'D_9', 2: True}, 4: {1: 'H_6', 2: False}, 5: {1: 'D_3', 2: False}}}, 'High Card': {'visible': True, 'order': 12, 'mult': 1, 'chips': 5, 's_mult': 1, 's_chips': 5, 'level': 1, 'l_mult': 1, 'l_chips': 10, 'played': 0, 'played_this_round': 0, 'example': {1: {1: 'S_A', 2: True}, 2: {1: 'D_Q', 2: False}, 3: {1: 'D_9', 2: False}, 4: {1: 'C_4', 2: False}, 5: {1: 'D_3', 2: False}}}}}

    def start_run(self, args):
        args = args if args else {}
        saveTable = args.savetext if args.savetext else 'None'
        G.SAVED_GAME = 'None'self.prep_stage()
        G.STAGE = G.STAGES.RUN
        if saveTable:check_for_unlock()
        G.STATE_COMPLETE = False
        G.RESET_BLIND_STATES = True
        if not saveTable:ease_background_colour_blind()
        else:ease_background_colour_blind()
        selected_back = (((saveTable & saveTable.BACK.name if saveTable & saveTable.BACK.name else args.challenge & args.challenge.deck & args.challenge.deck.type) if (saveTable & saveTable.BACK.name if saveTable & saveTable.BACK.name else args.challenge & args.challenge.deck & args.challenge.deck.type) else self.GAME.viewed_back & self.GAME.viewed_back.name) if ((saveTable & saveTable.BACK.name if saveTable & saveTable.BACK.name else args.challenge & args.challenge.deck & args.challenge.deck.type) if (saveTable & saveTable.BACK.name if saveTable & saveTable.BACK.name else args.challenge & args.challenge.deck & args.challenge.deck.type) else self.GAME.viewed_back & self.GAME.viewed_back.name) else self.GAME.selected_back & self.GAME.selected_back.name) if (((saveTable & saveTable.BACK.name if saveTable & saveTable.BACK.name else args.challenge & args.challenge.deck & args.challenge.deck.type) if (saveTable & saveTable.BACK.name if saveTable & saveTable.BACK.name else args.challenge & args.challenge.deck & args.challenge.deck.type) else self.GAME.viewed_back & self.GAME.viewed_back.name) if ((saveTable & saveTable.BACK.name if saveTable & saveTable.BACK.name else args.challenge & args.challenge.deck & args.challenge.deck.type) if (saveTable & saveTable.BACK.name if saveTable & saveTable.BACK.name else args.challenge & args.challenge.deck & args.challenge.deck.type) else self.GAME.viewed_back & self.GAME.viewed_back.name) else self.GAME.selected_back & self.GAME.selected_back.name) else 'Red Deck'
        selected_back = get_deck_from_name(selected_back)
        self.GAME = saveTable & saveTable.GAME if saveTable & saveTable.GAME else self.init_game_object()
        self.GAME.modifiers = self.GAME.modifiers if self.GAME.modifiers else {}
        self.GAME.stake = (args.stake if args.stake else self.GAME.stake) if (args.stake if args.stake else self.GAME.stake) else 1
        self.GAME.STOP_USE = 0
        self.GAME.selected_back = Back(selected_back)
        self.GAME.selected_back_key = selected_back
        '1[G.C.UI_CHIPS]' = '2[G.C.UI_CHIPS]' = '3[G.C.UI_CHIPS]' = '4[G.C.UI_CHIPS]' = ('1[G.C.BLUE]', '2[G.C.BLUE]', '3[G.C.BLUE]', '4[G.C.BLUE]')
        '1[G.C.UI_MULT]' = '2[G.C.UI_MULT]' = '3[G.C.UI_MULT]' = '4[G.C.UI_MULT]' = ('1[G.C.RED]', '2[G.C.RED]', '3[G.C.RED]', '4[G.C.RED]')
        if not saveTable:
            if self.GAME.stake >= 2:
                self.GAME.modifiers.no_blind_reward = self.GAME.modifiers.no_blind_reward if self.GAME.modifiers.no_blind_reward else {}
                self.GAME.modifiers.no_blind_reward.Small = True
            if self.GAME.stake >= 3:
                self.GAME.modifiers.scaling = 2
            if self.GAME.stake >= 4:
                self.GAME.modifiers.enable_eternals_in_shop = True
            if self.GAME.stake >= 5:
                self.GAME.starting_params.discards = self.GAME.starting_params.discards - 1
            if self.GAME.stake >= 6:
                self.GAME.modifiers.scaling = 3
            if self.GAME.stake >= 7:
                self.GAME.modifiers.enable_perishables_in_shop = True
            if self.GAME.stake >= 8:
                self.GAME.modifiers.enable_rentals_in_shop = Trueself.GAME.selected_back.apply_to_run()
            if args.challenge:
                self.GAME.challenge = args.challenge.id
                self.GAME.challenge_tab = args.challenge
                _ch = args.challenge
                if _ch.jokers:
                    for kv in ipairs():G.E_MANAGER.add_event()
                if _ch.consumeables:
                    for kv in ipairs():G.E_MANAGER.add_event()
                if _ch.vouchers:
                    for kv in ipairs():
                        'v.id[G.GAME.used_vouchers]' = TrueG.E_MANAGER.add_event()
                if _ch.rules:
                    if _ch.rules.modifiers:
                        for kv in ipairs():
                            'v.id[self.GAME.starting_params]' = v.value
                    if _ch.rules.custom:
                        for kv in ipairs():
                            if v.id == 'no_reward':
                                self.GAME.modifiers.no_blind_reward = self.GAME.modifiers.no_blind_reward if self.GAME.modifiers.no_blind_reward else {}
                                self.GAME.modifiers.no_blind_reward.Small = True
                                self.GAME.modifiers.no_blind_reward.Big = True
                                self.GAME.modifiers.no_blind_reward.Boss = True
                            elif v.id == 'no_reward_specific':
                                self.GAME.modifiers.no_blind_reward = self.GAME.modifiers.no_blind_reward if self.GAME.modifiers.no_blind_reward else {}
                                'v.value[self.GAME.modifiers.no_blind_reward]' = True
                            elif v.value:
                                'v.id[self.GAME.modifiers]' = v.value
                            elif v.id == 'no_shop_jokers':
                                self.GAME.joker_rate = 0
                            else:
                                'v.id[self.GAME.modifiers]' = True
                if _ch.restrictions:
                    if _ch.restrictions.banned_cards:
                        for kv in ipairs():
                            'v.id[G.GAME.banned_keys]' = True
                            if v.ids:
                                for kkvv in ipairs():
                                    'vv[G.GAME.banned_keys]' = True
                    if _ch.restrictions.banned_tags:
                        for kv in ipairs():
                            'v.id[G.GAME.banned_keys]' = True
                    if _ch.restrictions.banned_other:
                        for kv in ipairs():
                            'v.id[G.GAME.banned_keys]' = True
            self.GAME.round_resets.hands = self.GAME.starting_params.hands
            self.GAME.round_resets.discards = self.GAME.starting_params.discards
            self.GAME.round_resets.reroll_cost = self.GAME.starting_params.reroll_cost
            self.GAME.dollars = self.GAME.starting_params.dollars
            self.GAME.base_reroll_cost = self.GAME.starting_params.reroll_cost
            self.GAME.round_resets.reroll_cost = self.GAME.base_reroll_cost
            self.GAME.current_round.reroll_cost = self.GAME.base_reroll_cost
        G.GAME.chips_text = ''
        if not saveTable:
            if args.seed:
                self.GAME.seeded = True
            self.GAME.pseudorandom.seed = (args.seed if args.seed else (not (G.SETTINGS.tutorial_complete if G.SETTINGS.tutorial_complete else "'big_blind'[G.SETTINGS.tutorial_progress.completed_parts]")) & 'TUTORIAL') if (args.seed if args.seed else (not (G.SETTINGS.tutorial_complete if G.SETTINGS.tutorial_complete else "'big_blind'[G.SETTINGS.tutorial_progress.completed_parts]")) & 'TUTORIAL') else generate_starting_seed()
        for kv in pairs():
            if v == 0:
                'k[self.GAME.pseudorandom]' = pseudohash()
        self.GAME.pseudorandom.hashed_seed = pseudohash()G.save_settings()
        if not self.GAME.round_resets.blind_tags:
            self.GAME.round_resets.blind_tags = {}
        if not saveTable:
            self.GAME.round_resets.blind_choices.Boss = get_new_boss()
            self.GAME.current_round.voucher = G.SETTINGS.tutorial_progress & G.SETTINGS.tutorial_progress.forced_voucher if G.SETTINGS.tutorial_progress & G.SETTINGS.tutorial_progress.forced_voucher else get_next_voucher_key()
            self.GAME.round_resets.blind_tags.Small = G.SETTINGS.tutorial_progress & G.SETTINGS.tutorial_progress.forced_tags & '1[G.SETTINGS.tutorial_progress.forced_tags]' if G.SETTINGS.tutorial_progress & G.SETTINGS.tutorial_progress.forced_tags & '1[G.SETTINGS.tutorial_progress.forced_tags]' else get_next_tag_key()
            self.GAME.round_resets.blind_tags.Big = G.SETTINGS.tutorial_progress & G.SETTINGS.tutorial_progress.forced_tags & '2[G.SETTINGS.tutorial_progress.forced_tags]' if G.SETTINGS.tutorial_progress & G.SETTINGS.tutorial_progress.forced_tags & '2[G.SETTINGS.tutorial_progress.forced_tags]' else get_next_tag_key()
        elif self.GAME.round_resets.blind & self.GAME.round_resets.blind.key:
            self.GAME.round_resets.blind = 'self.GAME.round_resets.blind.key[G.P_BLINDS]'
        G.CONTROLLER.locks.load = TrueG.E_MANAGER.add_event()
        if saveTable & saveTable.ACTION:G.E_MANAGER.add_event()
        CAI = {'discard_W': G.CARD_W, 'discard_H': G.CARD_H, 'deck_W': G.CARD_W * 1.1, 'deck_H': 0.95 * G.CARD_H, 'hand_W': 6 * G.CARD_W, 'hand_H': 0.95 * G.CARD_H, 'play_W': 5.3 * G.CARD_W, 'play_H': 0.95 * G.CARD_H, 'joker_W': 4.9 * G.CARD_W, 'joker_H': 0.95 * G.CARD_H, 'consumeable_W': 2.3 * G.CARD_W, 'consumeable_H': 0.95 * G.CARD_H}
        self.consumeables = CardArea(0, 0)
        self.jokers = CardArea(0, 0)
        self.discard = CardArea(0, 0)
        self.deck = CardArea(0, 0)
        self.hand = CardArea(0, 0)
        self.play = CardArea(0, 0)
        G.playing_cards = {}set_screen_positions()
        G.SPLASH_BACK = Sprite()G.SPLASH_BACK.set_alignment()
        G.ARGS.spin = {'amount': 0, 'real': 0, 'eased': 0}G.SPLASH_BACK.define_draw_steps()G.E_MANAGER.add_event()
        if saveTable:
            cardAreas = saveTable.cardAreas
            for kv in pairs(cardAreas):
                if 'k[G]':'k[G]'.load(v)
                else:
                    "'load_'..k[G]" = vprint()
            for kv in pairs():
                if v.playing_card:table.insert()
            for kv in pairs():v.align_cards()v.hard_set_cards()table.sort()
        else:
            card_protos = 'None'
            _de = 'None'
            if args.challenge & args.challenge.deck:
                _de = args.challenge.deck
            if _de & _de.cards:
                card_protos = _de.cards
            if not card_protos:
                card_protos = {}
                for kv in pairs():
                    _ = 'None'
                    if self.GAME.starting_params.erratic_suits_and_ranks:
                        _ = k = pseudorandom_element()
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
                        if _de.gold_seal:
                            _g = _de.gold_seal
                    if self.GAME.starting_params.no_faces & ((_r == 'K' if _r == 'K' else _r == 'Q') if (_r == 'K' if _r == 'K' else _r == 'Q') else _r == 'J'):
                        keep = False
                    if keep:
                        '#card_protos + 1[card_protos]' = {'s': _s, 'r': _r, 'e': _e, 'd': _d, 'g': _g}
            if self.GAME.starting_params.extra_cards:
                for kv in pairs():
                    '#card_protos + 1[card_protos]' = vtable.sort(card_protos)
            for kv in ipairs(card_protos):card_from_control(v)
            self.GAME.starting_deck_size = len(G.playing_cards)delay(0.5)
        if not saveTable:
            G.GAME.current_round.discards_left = G.GAME.round_resets.discards
            G.GAME.current_round.hands_left = G.GAME.round_resets.handsself.deck.shuffle()self.deck.hard_set_T()reset_idol_card()reset_mail_rank()
            self.GAME.current_round.ancient_card.suit = 'None'reset_ancient_card()reset_castle_card()
        G.GAME.blind = Blind(0, 0, 2, 1)self.deck.align_cards()self.deck.hard_set_cards()
        self.HUD = UIBox()
        self.HUD_blind = UIBox()
        self.HUD_tags = {}
        G.hand_text_area = {'chips': self.HUD.get_UIE_by_ID(hand_chips), 'mult': self.HUD.get_UIE_by_ID(hand_mult), 'ante': self.HUD.get_UIE_by_ID(ante_UI_count), 'round': self.HUD.get_UIE_by_ID(round_UI_count), 'chip_total': self.HUD.get_UIE_by_ID(hand_chip_total), 'handname': self.HUD.get_UIE_by_ID(hand_name), 'hand_level': self.HUD.get_UIE_by_ID(hand_level), 'game_chips': self.HUD.get_UIE_by_ID(chip_UI_count), 'blind_chips': self.HUD_blind.get_UIE_by_ID(HUD_blind_count), 'blind_spacer': self.HUD.get_UIE_by_ID(blind_spacer)}check_and_set_high_score(most_money)
        if saveTable:G.GAME.blind.load()
            G.GAME.tags = {}
            tags = saveTable.tags if saveTable.tags else {}
            for kv in ipairs(tags):
                _tag = Tag(tag_uncommon)_tag.load(v)add_tag(_tag)
        else:G.GAME.blind.set_blind(None, None, True)reset_blinds()G.FUNCS.blind_chip_UI_scale()self.HUD.recalculate()G.E_MANAGER.add_event()

    def update(self, dt):nuGC(None, None, True)
        G.MAJORS = 0
        G.MINORS = 0
        G.FRAMES.MOVE = G.FRAMES.MOVE + 1timer_checkpoint(start->discovery, update)
        if not G.SETTINGS.tutorial_complete:G.FUNCS.tutorial_controller()timer_checkpoint(tallies, update)modulate_sound(dt)timer_checkpoint(sounds, update)update_canvas_juice(dt)timer_checkpoint(canvas and juice, update)
        self.TIMERS.REAL = self.TIMERS.REAL + dt
        self.TIMERS.REAL_SHADER = G.SETTINGS.reduced_motion & 300 if G.SETTINGS.reduced_motion & 300 else self.TIMERS.REAL
        self.TIMERS.UPTIME = self.TIMERS.UPTIME + dt
        self.SETTINGS.DEMO.total_uptime = (self.SETTINGS.DEMO.total_uptime if self.SETTINGS.DEMO.total_uptime else 0) + dt
        self.TIMERS.BACKGROUND = self.TIMERS.BACKGROUND + dt * (G.ARGS.spin & G.ARGS.spin.amount if G.ARGS.spin & G.ARGS.spin.amount else 0)
        self.real_dt = dt
        if self.real_dt > 0.05:print()
        if not G.fbf if not G.fbf else G.new_frame:
            G.new_frame = Falseset_alerts()timer_checkpoint(alerts, update)
            http_resp = G.HTTP_MANAGER.in_channel.pop()
            if http_resp:
                G.ARGS.HIGH_SCORE_RESPONSE = http_resp
            if G.SETTINGS.paused:
                dt = 0
            if G.STATE != G.ACC_state:
                G.ACC = 0
            G.ACC_state = G.STATE
            if G.STATE == G.STATES.HAND_PLAYED if G.STATE == G.STATES.HAND_PLAYED else G.STATE == G.STATES.NEW_ROUND:
                G.ACC = math.min()
            else:
                G.ACC = 0
            self.SPEEDFACTOR = (G.STAGE == G.STAGES.RUN) & (not G.SETTINGS.paused) & (not G.screenwipe) & self.SETTINGS.GAMESPEED if (G.STAGE == G.STAGES.RUN) & (not G.SETTINGS.paused) & (not G.screenwipe) & self.SETTINGS.GAMESPEED else 1
            self.SPEEDFACTOR = self.SPEEDFACTOR + math.max(0)
            self.TIMERS.TOTAL = self.TIMERS.TOTAL + dt * self.SPEEDFACTOR
            '1[self.C.DARK_EDITION]' = 0.6 + 0.2 * math.sin()
            '3[self.C.DARK_EDITION]' = 0.6 + 0.2 * (1 - math.sin())
            '2[self.C.DARK_EDITION]' = math.min(3[self.C.DARK_EDITION], 1[self.C.DARK_EDITION])
            '1[self.C.EDITION]' = 0.7 + 0.2 * (1 + math.sin())
            '3[self.C.EDITION]' = 0.7 + 0.2 * (1 + math.sin())
            '2[self.C.EDITION]' = 0.7 + 0.2 * (1 + math.sin())self.E_MANAGER.update()timer_checkpoint(e_manager, update)
            if G.GAME.blind & G.boss_throw_hand & (self.STATE == self.STATES.SELECTING_HAND):
                if not self.boss_warning_text:
                    self.boss_warning_text = UIBox()
                    self.boss_warning_text.attention_text = True
                    self.boss_warning_text.states.collide.can = FalseG.GAME.blind.children.animatedSprite.juice_up(0.05, 0.02)play_sound(chips1)
            else:
                G.boss_throw_hand = 'None'
                if self.boss_warning_text:self.boss_warning_text.remove()
                    self.boss_warning_text = 'None'
            if self.STATE == self.STATES.SELECTING_HAND:
                if (not '1[G.hand.cards]') & '1[G.deck.cards]':
                    G.STATE = G.STATES.DRAW_TO_HAND
                    G.STATE_COMPLETE = False
                else:self.update_selecting_hand(dt)
            if self.STATE == self.STATES.SHOP:self.update_shop(dt)
            if self.STATE == self.STATES.PLAY_TAROT:self.update_play_tarot(dt)
            if self.STATE == self.STATES.HAND_PLAYED:self.update_hand_played(dt)
            if self.STATE == self.STATES.DRAW_TO_HAND:self.update_draw_to_hand(dt)
            if self.STATE == self.STATES.NEW_ROUND:self.update_new_round(dt)
            if self.STATE == self.STATES.BLIND_SELECT:self.update_blind_select(dt)
            if self.STATE == self.STATES.ROUND_EVAL:self.update_round_eval(dt)
            if self.STATE == self.STATES.TAROT_PACK:self.update_arcana_pack(dt)
            if self.STATE == self.STATES.SPECTRAL_PACK:self.update_spectral_pack(dt)
            if self.STATE == self.STATES.STANDARD_PACK:self.update_standard_pack(dt)
            if self.STATE == self.STATES.BUFFOON_PACK:self.update_buffoon_pack(dt)
            if self.STATE == self.STATES.PLANET_PACK:self.update_celestial_pack(dt)
            if self.STATE == self.STATES.GAME_OVER:self.update_game_over(dt)
            if self.STATE == self.STATES.MENU:self.update_menu(dt)timer_checkpoint(states, update)remove_nils()
            for kv in pairs():v.animate()timer_checkpoint(animate, update)
            G.exp_times.xy = math.exp()
            G.exp_times.scale = math.exp()
            G.exp_times.r = math.exp()
            move_dt = math.min()
            G.exp_times.max_vel = 70 * move_dt
            for kv in pairs():
                if v.FRAME.MOVE < G.FRAMES.MOVE:v.move(move_dt)timer_checkpoint(move, update)
            for kv in pairs():v.update()
                v.states.collide.is = Falsetimer_checkpoint(update, update)self.CONTROLLER.update()
        if ((G.prev_small_state != G.GAME.round_resets.blind_states.Small if G.prev_small_state != G.GAME.round_resets.blind_states.Small else G.prev_large_state != G.GAME.round_resets.blind_states.Big) if (G.prev_small_state != G.GAME.round_resets.blind_states.Small if G.prev_small_state != G.GAME.round_resets.blind_states.Small else G.prev_large_state != G.GAME.round_resets.blind_states.Big) else G.prev_boss_state != G.GAME.round_resets.blind_states.Boss) if ((G.prev_small_state != G.GAME.round_resets.blind_states.Small if G.prev_small_state != G.GAME.round_resets.blind_states.Small else G.prev_large_state != G.GAME.round_resets.blind_states.Big) if (G.prev_small_state != G.GAME.round_resets.blind_states.Small if G.prev_small_state != G.GAME.round_resets.blind_states.Small else G.prev_large_state != G.GAME.round_resets.blind_states.Big) else G.prev_boss_state != G.GAME.round_resets.blind_states.Boss) else G.RESET_BLIND_STATES:
            G.RESET_BLIND_STATES = 'None'
            G.prev_small_state = G.GAME.round_resets.blind_states.Small
            G.prev_large_state = G.GAME.round_resets.blind_states.Big
            G.prev_boss_state = G.GAME.round_resets.blind_states.Boss
            G.GAME.round_resets.loc_blind_states.Small = localize()
            G.GAME.round_resets.loc_blind_states.Big = localize()
            G.GAME.round_resets.loc_blind_states.Boss = localize()
        if G.FILE_HANDLER & G.FILE_HANDLER & G.FILE_HANDLER.update_queued & (((G.FILE_HANDLER.force if G.FILE_HANDLER.force else G.FILE_HANDLER.last_sent_stage != G.STAGE) if (G.FILE_HANDLER.force if G.FILE_HANDLER.force else G.FILE_HANDLER.last_sent_stage != G.STAGE) else (G.FILE_HANDLER.last_sent_pause != G.SETTINGS.paused) & G.FILE_HANDLER.run) if ((G.FILE_HANDLER.force if G.FILE_HANDLER.force else G.FILE_HANDLER.last_sent_stage != G.STAGE) if (G.FILE_HANDLER.force if G.FILE_HANDLER.force else G.FILE_HANDLER.last_sent_stage != G.STAGE) else (G.FILE_HANDLER.last_sent_pause != G.SETTINGS.paused) & G.FILE_HANDLER.run) else not G.FILE_HANDLER.last_sent_time if not G.FILE_HANDLER.last_sent_time else G.FILE_HANDLER.last_sent_time < G.TIMERS.UPTIME - G.F_SAVE_TIMER):
            if G.FILE_HANDLER.metrics:G.SAVE_MANAGER.channel.push()
            if G.FILE_HANDLER.progress:G.SAVE_MANAGER.channel.push()
            elif G.FILE_HANDLER.settings:G.SAVE_MANAGER.channel.push()
            if G.FILE_HANDLER.run:G.SAVE_MANAGER.channel.push()
                G.SAVED_GAME = 'None'
            G.FILE_HANDLER.force = False
            G.FILE_HANDLER.last_sent_stage = G.STAGE
            G.FILE_HANDLER.last_sent_time = G.TIMERS.UPTIME
            G.FILE_HANDLER.last_sent_pause = G.SETTINGS.paused
            G.FILE_HANDLER.settings = 'None'
            G.FILE_HANDLER.progress = 'None'
            G.FILE_HANDLER.metrics = 'None'
            G.FILE_HANDLER.run = 'None'

    def draw(self):
        G.FRAMES.DRAW = G.FRAMES.DRAW + 1reset_drawhash()
        if G.OVERLAY_TUTORIAL & (not G.OVERLAY_MENU):
            G.under_overlay = Truetimer_checkpoint(start->canvas, draw)love.graphics.setCanvas()love.graphics.push()love.graphics.scale()love.graphics.setShader()love.graphics.clear(0, 0, 0, 1)
        if G.SPLASH_BACK:
            if G.debug_background_toggle:love.graphics.clear()
            else:love.graphics.push()G.SPLASH_BACK.translate_container()G.SPLASH_BACK.draw()love.graphics.pop()
        if not G.debug_UI_toggle:
            for kv in pairs():
                if not v.parent:love.graphics.push()v.translate_container()v.draw()love.graphics.pop()
            for kv in pairs():
                if not v.parent:love.graphics.push()v.translate_container()v.draw()love.graphics.pop()
            if G.SPLASH_LOGO:love.graphics.push()G.SPLASH_LOGO.translate_container()G.SPLASH_LOGO.draw()love.graphics.pop()
            if G.debug_splash_size_toggle:
                for kv in pairs():
                    if not v.parent:love.graphics.push()v.translate_container()v.draw()love.graphics.pop()
            else:
                if not self.OVERLAY_MENU if not self.OVERLAY_MENU else not self.F_HIDE_BG:timer_checkpoint(primatives, draw)
                    for kv in pairs():
                        if (not v.attention_text) & (not v.parent) & (v != self.OVERLAY_MENU) & (v != self.screenwipe) & (v != self.OVERLAY_TUTORIAL) & (v != self.debug_tools) & (v != self.online_leaderboard) & (v != self.achievement_notification):love.graphics.push()v.translate_container()v.draw()love.graphics.pop()timer_checkpoint(uiboxes, draw)
                    for kv in pairs():
                        if not v.parent:love.graphics.push()v.translate_container()v.draw()love.graphics.pop()
                    for kv in pairs():
                        if (not v.parent) & (v != self.CONTROLLER.dragging.target) & (v != self.CONTROLLER.focused.target):love.graphics.push()v.translate_container()v.draw()love.graphics.pop()
                    for kv in pairs():
                        if v.attention_text & (v != self.debug_tools) & (v != self.online_leaderboard) & (v != self.achievement_notification):love.graphics.push()v.translate_container()v.draw()love.graphics.pop()
                    if G.SPLASH_FRONT:love.graphics.push()G.SPLASH_FRONT.translate_container()G.SPLASH_FRONT.draw()love.graphics.pop()
                    G.under_overlay = False
                    if self.OVERLAY_TUTORIAL:love.graphics.push()self.OVERLAY_TUTORIAL.translate_container()self.OVERLAY_TUTORIAL.draw()love.graphics.pop()
                        if self.OVERLAY_TUTORIAL.highlights:
                            for kv in ipairs():love.graphics.push()v.translate_container()v.draw()
                                if v.draw_children:v.draw_self()v.draw_children()love.graphics.pop()
                if self.OVERLAY_MENU if self.OVERLAY_MENU else not self.F_HIDE_BG:
                    if self.OVERLAY_MENU & (self.OVERLAY_MENU != self.CONTROLLER.dragging.target):love.graphics.push()self.OVERLAY_MENU.translate_container()self.OVERLAY_MENU.draw()love.graphics.pop()
                if self.debug_tools:
                    if self.debug_tools != self.CONTROLLER.dragging.target:love.graphics.push()self.debug_tools.translate_container()self.debug_tools.draw()love.graphics.pop()
                G.ALERT_ON_SCREEN = 'None'
                for kv in pairs():love.graphics.push()v.translate_container()v.draw()
                    G.ALERT_ON_SCREEN = Truelove.graphics.pop()
                if self.CONTROLLER.dragging.target & (self.CONTROLLER.dragging.target != self.CONTROLLER.focused.target):love.graphics.push()G.CONTROLLER.dragging.target.translate_container()G.CONTROLLER.dragging.target.draw()love.graphics.pop()
                if self.CONTROLLER.focused.target & (getmetatable() == Card) & (self.CONTROLLER.focused.target.area != G.hand if self.CONTROLLER.focused.target.area != G.hand else self.CONTROLLER.focused.target == self.CONTROLLER.dragging.target):love.graphics.push()G.CONTROLLER.focused.target.translate_container()G.CONTROLLER.focused.target.draw()love.graphics.pop()
                for kv in pairs():love.graphics.push()v.translate_container()v.draw()love.graphics.pop()
                if self.achievement_notification:love.graphics.push()self.achievement_notification.translate_container()self.achievement_notification.draw()love.graphics.pop()
                if self.screenwipe:love.graphics.push()self.screenwipe.translate_container()self.screenwipe.draw()love.graphics.pop()love.graphics.push()self.CURSOR.translate_container()love.graphics.translate()self.CURSOR.draw()love.graphics.pop()timer_checkpoint(rest, draw)love.graphics.pop()love.graphics.setCanvas()love.graphics.push()love.graphics.setColor()
        if (not G.recording_mode if not G.recording_mode else G.video_control) & True:
            G.ARGS.eased_cursor_pos = G.ARGS.eased_cursor_pos if G.ARGS.eased_cursor_pos else {'x': G.CURSOR.T.x, 'y': G.CURSOR.T.y, 'sx': G.CONTROLLER.cursor_position.x, 'sy': G.CONTROLLER.cursor_position.y}
            G.screenwipe_amt = G.screenwipe_amt & 0.95 * G.screenwipe_amt + 0.05 * ((self.screenwipe & 0.4 if self.screenwipe & 0.4 else self.screenglitch & 0.4) if (self.screenwipe & 0.4 if self.screenwipe & 0.4 else self.screenglitch & 0.4) else 0) if G.screenwipe_amt & 0.95 * G.screenwipe_amt + 0.05 * ((self.screenwipe & 0.4 if self.screenwipe & 0.4 else self.screenglitch & 0.4) if (self.screenwipe & 0.4 if self.screenwipe & 0.4 else self.screenglitch & 0.4) else 0) else 1
            G.SETTINGS.GRAPHICS.crt = G.SETTINGS.GRAPHICS.crt * 0.3"'CRT'[G.SHADERS]".send(distortion_fac)"'CRT'[G.SHADERS]".send(scale_fac)"'CRT'[G.SHADERS]".send(feather_fac, 0.01)"'CRT'[G.SHADERS]".send(bloom_fac)"'CRT'[G.SHADERS]".send(time)"'CRT'[G.SHADERS]".send(noise_fac)"'CRT'[G.SHADERS]".send(crt_intensity)"'CRT'[G.SHADERS]".send(glitch_intensity, 0)"'CRT'[G.SHADERS]".send(scanlines)"'CRT'[G.SHADERS]".send(mouse_screen_pos)"'CRT'[G.SHADERS]".send(screen_scale)"'CRT'[G.SHADERS]".send(hovering, 1)love.graphics.setShader('CRT'[G.SHADERS])
            G.SETTINGS.GRAPHICS.crt = G.SETTINGS.GRAPHICS.crt / 0.3love.graphics.draw()love.graphics.pop()love.graphics.setCanvas()love.graphics.setShader()
        if G.AA_CANVAS:love.graphics.push()love.graphics.scale()love.graphics.draw()love.graphics.pop()timer_checkpoint(canvas, draw)
        if (not _RELEASE_MODE) & (not G.video_control) & G.F_VERBOSE:love.graphics.push()love.graphics.setColor(0, 1, 1, 1)
            fps = love.timer.getFPS()love.graphics.print()
            if G.check & G.SETTINGS.perf_mode:
                section_h = 30
                resolution = 60 * section_h
                poll_w = 1
                v_off = 100
                for ab in ipairs():
                    for kv in ipairs():love.graphics.setColor(0, 0, 0, 0.2)love.graphics.rectangle(fill, 12)
                        for kkvv in ipairs():
                            if a == 2:love.graphics.setColor(0.3, 0.7, 0.7, 1)
                            else:love.graphics.setColor()love.graphics.rectangle(fill)love.graphics.setColor()love.graphics.print()
                        v_off = v_off + section_hlove.graphics.pop()timer_checkpoint(debug, draw)

    def state_col(self, _state):
        return _state * 15251252.2 / 5.132 % 1_state * 1422.5641311 / 5.42 % 1_state * 1522.1523122 / 5.132 % 11

    def update_selecting_hand(self, dt):
        if (not self.deck_preview) & (not G.OVERLAY_MENU) & (self.deck & '1[self.deck.cards]' & '1[self.deck.cards]'.states.collide.is & (not '1[self.deck.cards]'.states.drag.is if not '1[self.deck.cards]'.states.drag.is else self.CONTROLLER.HID.touch) & (not self.CONTROLLER.HID.controller) if self.deck & '1[self.deck.cards]' & '1[self.deck.cards]'.states.collide.is & (not '1[self.deck.cards]'.states.drag.is if not '1[self.deck.cards]'.states.drag.is else self.CONTROLLER.HID.touch) & (not self.CONTROLLER.HID.controller) else G.CONTROLLER.held_buttons.triggerleft):
            if self.buttons:
                self.buttons.states.visible = False
            self.deck_preview = UIBox()self.E_MANAGER.add_event()
        if (not self.buttons) & (not self.deck_preview):
            self.buttons = UIBox()
        if self.buttons & (not self.buttons.states.visible) & (not self.deck_preview):
            self.buttons.states.visible = True
        if len(G.hand.cards < 1 & len(G.deck.cards < 1 & len(G.play.cards < 1))):end_round()
        if self.shop:self.shop.remove()';'
            self.shop = 'None'
        if not G.STATE_COMPLETE:
            G.STATE_COMPLETE = True
            if len(G.hand.cards < 1 & len(G.deck.cards < 1)):end_round()
            else:save_run()G.CONTROLLER.recall_cardarea_focus(hand)

    def update_shop(self, dt):
        if not G.STATE_COMPLETE:stop_use()ease_background_colour_blind()
            shop_exists = not not G.shop
            G.shop = G.shop if G.shop else UIBox()G.E_MANAGER.add_event()
            G.STATE_COMPLETE = True
        if self.buttons:self.buttons.remove()';'
            self.buttons = 'None'

    def update_play_tarot(self, dt):
        if self.buttons:self.buttons.remove()';'
            self.buttons = 'None'

    def update_hand_played(self, dt):
        if self.buttons:self.buttons.remove()';'
            self.buttons = 'None'
        if self.shop:self.shop.remove()';'
            self.shop = 'None'
        if not G.STATE_COMPLETE:
            G.STATE_COMPLETE = TrueG.E_MANAGER.add_event()

    def update_draw_to_hand(self, dt):
        if self.buttons:self.buttons.remove()';'
            self.buttons = 'None'
        if self.shop:self.shop.remove()';'
            self.shop = 'None'
        if not G.STATE_COMPLETE:
            G.STATE_COMPLETE = True
            for i in range(1, len(G.GAME.tags), ):'i[G.GAME.tags]'.apply_to_run()ease_background_colour_blind()G.E_MANAGER.add_event()

    def update_new_round(self, dt):
        if self.buttons:self.buttons.remove()';'
            self.buttons = 'None'
        if self.shop:self.shop.remove()';'
            self.shop = 'None'
        if not G.STATE_COMPLETE:
            G.STATE_COMPLETE = Trueend_round()

    def update_blind_select(self, dt):
        if self.buttons:self.buttons.remove()';'
            self.buttons = 'None'
        if self.shop:self.shop.remove()';'
            self.shop = 'None'
        if not G.STATE_COMPLETE:stop_use()ease_background_colour_blind()G.E_MANAGER.add_event()
            G.STATE_COMPLETE = True
            G.CONTROLLER.interrupt.focus = TrueG.E_MANAGER.add_event()

    def update_round_eval(self, dt):
        if self.buttons:self.buttons.remove()';'
            self.buttons = 'None'
        if self.shop:self.shop.remove()';'
            self.shop = 'None'
        if not G.STATE_COMPLETE:stop_use()
            G.STATE_COMPLETE = TrueG.E_MANAGER.add_event()

    def update_arcana_pack(self, dt):
        if self.buttons:self.buttons.remove()';'
            self.buttons = 'None'
        if self.shop:
            G.shop.alignment.offset.y = G.ROOM.T.y + 11
        if not G.STATE_COMPLETE:
            G.STATE_COMPLETE = True
            G.CONTROLLER.interrupt.focus = TrueG.E_MANAGER.add_event()

    def update_spectral_pack(self, dt):
        if self.buttons:self.buttons.remove()';'
            self.buttons = 'None'
        if self.shop:
            G.shop.alignment.offset.y = G.ROOM.T.y + 11
        if not G.STATE_COMPLETE:
            G.STATE_COMPLETE = True
            G.CONTROLLER.interrupt.focus = TrueG.E_MANAGER.add_event()

    def update_standard_pack(self, dt):
        if self.buttons:self.buttons.remove()';'
            self.buttons = 'None'
        if self.shop:
            G.shop.alignment.offset.y = G.ROOM.T.y + 11
        if not G.STATE_COMPLETE:
            G.STATE_COMPLETE = True
            G.CONTROLLER.interrupt.focus = TrueG.E_MANAGER.add_event()

    def update_buffoon_pack(self, dt):
        if self.buttons:self.buttons.remove()';'
            self.buttons = 'None'
        if self.shop:
            G.shop.alignment.offset.y = G.ROOM.T.y + 11
        if not G.STATE_COMPLETE:
            G.STATE_COMPLETE = True
            G.CONTROLLER.interrupt.focus = TrueG.E_MANAGER.add_event()

    def update_celestial_pack(self, dt):
        if self.buttons:self.buttons.remove()';'
            self.buttons = 'None'
        if self.shop:
            G.shop.alignment.offset.y = G.ROOM.T.y + 11
        if not G.STATE_COMPLETE:
            G.STATE_COMPLETE = True
            G.CONTROLLER.interrupt.focus = TrueG.E_MANAGER.add_event()

    def update_game_over(self, dt):
        if not G.STATE_COMPLETE:remove_save()
            if G.GAME.round_resets.ante <= G.GAME.win_ante:
                if (not G.GAME.seeded) & (not G.GAME.challenge):inc_career_stat(c_losses, 1)set_deck_loss()set_joker_loss()play_sound(negative, 0.5, 0.7)play_sound(whoosh2, 0.9, 0.7)
            G.SETTINGS.paused = TrueG.FUNCS.overlay_menu()
            G.ROOM.jiggle = G.ROOM.jiggle + 3
            if G.GAME.round_resets.ante <= G.GAME.win_ante:
                Jimbo = 'None'G.E_MANAGER.add_event()
            G.STATE_COMPLETE = True

    def update_menu(self, dt):