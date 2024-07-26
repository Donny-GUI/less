class Sprite(Moveable):

    def __init__(self, X, Y, W, H, new_sprite_atlas, sprite_pos):
        super().__init__(self, X, Y, W, H)
        self.CT = self.VT
        self.atlas = new_sprite_atlas
        self.scale = {'x': self.atlas.px, 'y': self.atlas.py}
        self.scale_mag = math.min()
        self.zoom = Trueself.set_sprite_pos(sprite_pos)
        if getmetatable(self) == Sprite:table.insert()

    def reset(self):
        self.atlas = G.ASSET_ATLAS[self.atlas.name]self.set_sprite_pos()

    def set_sprite_pos(self, sprite_pos):
        if sprite_pos & sprite_pos.v:
            self.sprite_pos = {'x': math.random() - 1, 'y': sprite_pos.y}
        else:
            self.sprite_pos = sprite_pos if sprite_pos else {'x': 0, 'y': 0}
        self.sprite_pos_copy = {'x': self.sprite_pos.x, 'y': self.sprite_pos.y}
        self.sprite = love.graphics.newQuad()
        self.image_dims = {}
        G.ASSET_ATLAS[self.atlas.name] = self.atlas.image.getDimensions()

    def get_pos_pixel(self):
        self.RETS.get_pos_pixel = self.RETS.get_pos_pixel if self.RETS.get_pos_pixel else {}
        G.ASSET_ATLAS[self.atlas.name] = self.sprite_pos.x
        G.ASSET_ATLAS[self.atlas.name] = self.sprite_pos.y
        G.ASSET_ATLAS[self.atlas.name] = self.atlas.px
        G.ASSET_ATLAS[self.atlas.name] = self.atlas.py
        return self.RETS.get_pos_pixel

    def get_image_dims(self):
        return self.image_dims

    def define_draw_steps(self, draw_step_definitions):
        self.draw_steps = EMPTY()
        for kv in ipairs(draw_step_definitions):
            G.ASSET_ATLAS[self.atlas.name] = {'shader': v.shader if v.shader else 'dissolve', 'shadow_height': v.shadow_height if v.shadow_height else 'None', 'send': v.send if v.send else 'None', 'no_tilt': v.no_tilt if v.no_tilt else 'None', 'other_obj': v.other_obj if v.other_obj else 'None', 'ms': v.ms if v.ms else 'None', 'mr': v.mr if v.mr else 'None', 'mx': v.mx if v.mx else 'None', 'my': v.my if v.my else 'None'}

    def draw_shader(self, _shader, _shadow_height, _send, _no_tilt, other_obj, ms, mr, mx, my, custom_shader, tilt_shadow):
        if G.SETTINGS.reduced_motion:
            _no_tilt = True
        _draw_major = self.role.draw_major if self.role.draw_major else self
        if _shadow_height:
            self.VT.y = self.VT.y - _draw_major.shadow_parrallax.y * _shadow_height
            self.VT.x = self.VT.x - _draw_major.shadow_parrallax.x * _shadow_height
            self.VT.scale = self.VT.scale * (1 - 0.2 * _shadow_height)
        if custom_shader:
            if _send:
                for kv in ipairs(_send):G.ASSET_ATLAS[self.atlas.name].send()
        elif _shader == 'vortex':"'vortex'[G.SHADERS]".send(vortex_amt)
        else:
            self.ARGS.prep_shader = self.ARGS.prep_shader if self.ARGS.prep_shader else {}
            self.ARGS.prep_shader.cursor_pos = self.ARGS.prep_shader.cursor_pos if self.ARGS.prep_shader.cursor_pos else {}
            G.ASSET_ATLAS[self.atlas.name] = _draw_major.tilt_var & _draw_major.tilt_var.mx * G.CANV_SCALE if _draw_major.tilt_var & _draw_major.tilt_var.mx * G.CANV_SCALE else G.CONTROLLER.cursor_position.x * G.CANV_SCALE
            G.ASSET_ATLAS[self.atlas.name] = _draw_major.tilt_var & _draw_major.tilt_var.my * G.CANV_SCALE if _draw_major.tilt_var & _draw_major.tilt_var.my * G.CANV_SCALE else G.CONTROLLER.cursor_position.y * G.CANV_SCALE"_shader or 'dissolve'[G.SHADERS]".send(mouse_screen_pos)"_shader or 'dissolve'[G.SHADERS]".send(screen_scale)"_shader or 'dissolve'[G.SHADERS]".send(hovering)"_shader or 'dissolve'[G.SHADERS]".send(dissolve)"_shader or 'dissolve'[G.SHADERS]".send(time)"_shader or 'dissolve'[G.SHADERS]".send(texture_details)"_shader or 'dissolve'[G.SHADERS]".send(image_details)"_shader or 'dissolve'[G.SHADERS]".send(burn_colour_1)"_shader or 'dissolve'[G.SHADERS]".send(burn_colour_2)"_shader or 'dissolve'[G.SHADERS]".send(shadow)
            if _send:"_shader or 'dissolve'[G.SHADERS]".send(_shader, _send)love.graphics.setShader(_shader or 'dissolve'[G.SHADERS], _shader or 'dissolve'[G.SHADERS])
        if other_obj:self.draw_from(other_obj, ms, mr, mx, my)
        else:self.draw_self()love.graphics.setShader()
        if _shadow_height:
            self.VT.y = self.VT.y + _draw_major.shadow_parrallax.y * _shadow_height
            self.VT.x = self.VT.x + _draw_major.shadow_parrallax.x * _shadow_height
            self.VT.scale = self.VT.scale / (1 - 0.2 * _shadow_height)

    def draw_self(self, overlay):
        if not self.states.visible:
            return False
        if self.sprite_pos.x != self.sprite_pos_copy.x if self.sprite_pos.x != self.sprite_pos_copy.x else self.sprite_pos.y != self.sprite_pos_copy.y:self.set_sprite_pos()prep_draw(self, 1)love.graphics.scale()love.graphics.setColor()
        if self.video:
            self.video_dims = self.video_dims if self.video_dims else {'w': self.video.getWidth(), 'h': self.video.getHeight()}love.graphics.draw()
        else:love.graphics.draw()love.graphics.pop()add_to_drawhash(self)self.draw_boundingrect()
        if self.shader_tab:love.graphics.setShader()

    def draw(self, overlay):
        if not self.states.visible:
            return False
        if self.draw_steps:
            for kv in ipairs():self.draw_shader()
        else:self.draw_self(overlay)add_to_drawhash(self)
        for kv in pairs():
            if k != 'h_popup':v.draw()add_to_drawhash(self)self.draw_boundingrect()

    def draw_from(self, other_obj, ms, mr, mx, my):
        self.ARGS.draw_from_offset = self.ARGS.draw_from_offset if self.ARGS.draw_from_offset else {}
        self.ARGS.draw_from_offset.x = mx if mx else 0
        self.ARGS.draw_from_offset.y = my if my else 0prep_draw(other_obj)love.graphics.scale()love.graphics.setColor()love.graphics.draw()self.draw_boundingrect()love.graphics.pop()

    def remove(self):
        if self.video:self.video.release()
        for kv in pairs():
            if v == self:table.remove()
        for kv in pairs():
            if v == self:table.remove()
        super().remove(self)