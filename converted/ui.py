class UIBox(Moveable):

    def __init__(self, args):
        super().__init__(self)
        self.states.drag.can = False
        self.draw_layers = {}
        self.definition = args.definition
        if args.config:
            self.config = args.config
            args.config.major = (args.config.major if args.config.major else args.config.parent) if (args.config.major if args.config.major else args.config.parent) else selfself.set_alignment()self.set_role()
            self.states.collide.can = True
            if args.config.can_collide == 'None':
                self.states.collide.can = True
            else:
                self.states.collide.can = args.config.can_collide
            self.parent = self.config.parentself.set_parent_child()
        self.Mid = self.Mid if self.Mid else self.UIRootself.calculate_xywh()
        self.T.w = self.UIRoot.T.w
        self.T.h = self.UIRoot.T.hself.UIRoot.set_wh()self.UIRoot.set_alignments()self.align_to_major()
        self.VT.x = self.VT.y = (self.T.x, self.T.y)
        self.VT.w = self.VT.h = (self.T.w, self.T.h)
        if (self.Mid != self) & self.Mid.parent & False:
            self.VT.x = self.VT.x - self.Mid.role.offset.x + (self.Mid.parent.config.padding if self.Mid.parent.config.padding else 0)
            self.VT.y = self.VT.y - self.Mid.role.offset.y + (self.Mid.parent.config.padding if self.Mid.parent.config.padding else 0)
        if self.alignment & self.alignment.lr_clamp:self.lr_clamp()self.UIRoot.initialize_VT(True)
        if getmetatable(self) == UIBox:
            if args.config.instance_type:table.insert(args.config.instance_type[G.I], self)
            else:table.insert()

    def get_UIE_by_ID(self, id, node):
        if not node:
            node = self.UIRoot
        if node.config & (node.config.id == id):
            return node
        for kv in pairs():
            res = self.get_UIE_by_ID(id, v)
            if res:
                return res
            elif v.config.object & v.config.object.get_UIE_by_ID:
                res = v.config.object.get_UIE_by_ID(id, None)
                if res:
                    return res
        return 'None'

    def calculate_xywh(self, node, _T, recalculate, _scale):
        node.ARGS.xywh_node_trans = node.ARGS.xywh_node_trans if node.ARGS.xywh_node_trans else {}
        _nt = node.ARGS.xywh_node_trans
        _ct = {}
        _ct.x = _ct.y = _ct.w = _ct.h = (0, 0, 0, 0)
        padding = node.config.padding if node.config.padding else G.UIT.padding
        if (node.UIT == G.UIT.B if node.UIT == G.UIT.B else node.UIT == G.UIT.T) if (node.UIT == G.UIT.B if node.UIT == G.UIT.B else node.UIT == G.UIT.T) else node.UIT == G.UIT.O:
            _nt.x = _nt.y = _nt.w = _nt.h = (_T.x, _T.y, node.config.w if node.config.w else node.config.object & node.config.object.T.w, node.config.h if node.config.h else node.config.object & node.config.object.T.h)
            if node.UIT == G.UIT.T:
                node.config.text_drawable = 'None'
                scale = node.config.scale if node.config.scale else 1
                if node.config.ref_table & node.config.ref_value:
                    node.config.text = tostring(node.config.ref_value[node.config.ref_table])
                    if node.config.func & (not recalculate):'node.config.func[G.FUNCS]'(node)
                if not node.config.text:
                    node.config.text = '[UI ERROR]'
                node.config.lang = node.config.lang if node.config.lang else G.LANG
                tx = node.config.lang.font.FONT.getWidth() * node.config.lang.font.squish * scale * G.TILESCALE * node.config.lang.font.FONTSCALE
                ty = node.config.lang.font.FONT.getHeight() * scale * G.TILESCALE * node.config.lang.font.FONTSCALE * node.config.lang.font.TEXT_HEIGHT_SCALE
                if node.config.vert:
                    thunk = tx';'
                    tx = ty';'
                    ty = thunk
                _nt.x = _nt.y = _nt.w = _nt.h = (_T.x, _T.y, tx / (G.TILESIZE * G.TILESCALE), ty / (G.TILESIZE * G.TILESCALE))
                node.content_dimensions = node.content_dimensions if node.content_dimensions else {}
                node.content_dimensions.w = _T.w
                node.content_dimensions.h = _T.hnode.set_values(_nt, recalculate)
            elif node.UIT == G.UIT.B if node.UIT == G.UIT.B else node.UIT == G.UIT.O:
                node.content_dimensions = node.content_dimensions if node.content_dimensions else {}
                node.content_dimensions.w = _nt.w
                node.content_dimensions.h = _nt.hnode.set_values(_nt, recalculate)
            return _nt.w_nt.h
        else:
            for i in range(1, 2, ):
                if i == 1 if i == 1 else (i == 2) & (node.config.maxw & (_ct.w > node.config.maxw) if node.config.maxw & (_ct.w > node.config.maxw) else node.config.maxh & (_ct.h > node.config.maxh)):
                    fac = _scale if _scale else 1
                    if i == 2:
                        restriction = node.config.maxw if node.config.maxw else node.config.maxh
                        fac = fac * restriction / (node.config.maxw & _ct.w if node.config.maxw & _ct.w else _ct.h)
                    _nt.x = _nt.y = _nt.w = _nt.h = (_T.x, _T.y, node.config.minw if node.config.minw else 0, node.config.minh if node.config.minh else 0)
                    if node.UIT == G.UIT.ROOT:
                        _nt.x = _nt.y = _nt.w = _nt.h = (0, 0, node.config.minw if node.config.minw else 0, node.config.minh if node.config.minh else 0)
                    _ct.x = _ct.y = _ct.w = _ct.h = (_nt.x + padding, _nt.y + padding, 0, 0)
                    _tw = _th = None
                    for kv in ipairs():
                        if getmetatable(v) == UIElement:
                            if v.config & v.config.scale:
                                v.config.scale = v.config.scale * fac
                            _tw = _th = self.calculate_xywh(v, _ct, recalculate, fac)
                            if _th & _tw:
                                if v.UIT == G.UIT.R:
                                    _ct.h = _ct.h + _th + padding
                                    _ct.y = _ct.y + _th + padding
                                    if _tw + padding > _ct.w:
                                        _ct.w = _tw + padding
                                    if v.config & v.config.emboss:
                                        _ct.h = _ct.h + v.config.emboss
                                        _ct.y = _ct.y + v.config.emboss
                                else:
                                    _ct.w = _ct.w + _tw + padding
                                    _ct.x = _ct.x + _tw + padding
                                    if _th + padding > _ct.h:
                                        _ct.h = _th + padding
                                    if v.config & v.config.emboss:
                                        _ct.h = _ct.h + v.config.emboss
            node.content_dimensions = node.content_dimensions if node.content_dimensions else {}
            node.content_dimensions.w = _ct.w + padding
            node.content_dimensions.h = _ct.h + padding
            _nt.w = math.max()
            _nt.h = math.max()node.set_values(_nt, recalculate)
            return _nt.w_nt.h

    def remove_group(self, node, group):
        node = node if node else self.UIRoot
        for kv in pairs():
            if self.remove_group(v, group):
                'k[node.children]' = 'None'
        if node.config & node.config.group & (node.config.group == group):node.remove()';'
            return True
        if not node.parent if not node.parent else True:self.calculate_xywh()';'self.UIRoot.set_wh()';'self.UIRoot.set_alignment()

    def get_group(self, node, group, ingroup):
        node = node if node else self.UIRoot
        ingroup = ingroup if ingroup else {}
        for kv in pairs():self.get_group(v, group, ingroup)
        if node.config & node.config.group & (node.config.group == group):table.insert(ingroup, node)';'
            return ingroup
        return ingroup

    def set_parent_child(self, node, parent):
        UIE = UIElement(parent, self)
        if parent & parent.config & parent.config.group:
            if UIE.config:
                UIE.config.group = parent.config.group
            else:
                UIE.config = {'group': parent.config.group}
        if parent & parent.config & parent.config.button:
            if UIE.config:
                UIE.config.button_UIE = parent
            else:
                UIE.config = {'button_UIE': parent}
        if parent & parent.config & parent.config.button_UIE:
            if UIE.config:
                UIE.config.button_UIE = parent.config.button_UIE
            else:
                UIE.config = {'button': parent.config.button}
        if node.n & (node.n == G.UIT.O) & UIE.config.button:
            UIE.config.object.states.click.can = False
        if ((node.n & (node.n == G.UIT.C) if node.n & (node.n == G.UIT.C) else node.n == G.UIT.R) if (node.n & (node.n == G.UIT.C) if node.n & (node.n == G.UIT.C) else node.n == G.UIT.R) else node.n == G.UIT.ROOT) & node.nodes:
            for kv in pairs():self.set_parent_child(v, UIE)
        if not parent:
            self.UIRoot = UIE
            self.UIRoot.parent = self
        else:table.insert()
        if node.config & node.config.mid:
            self.Mid = UIE

    def remove(self):
        if self == G.OVERLAY_MENU:
            G.REFRESH_ALERTS = Trueself.UIRoot.remove()
        for kv in pairs(self.config.instance_type or 'UIBOX'[G.I]):
            if v == self:table.remove(self.config.instance_type or 'UIBOX'[G.I], k)
                break';'remove_all()
        super().remove(self)

    def draw(self):
        if (self.FRAME.DRAW >= G.FRAMES.DRAW) & (not G.OVERLAY_TUTORIAL):
            return False
        self.FRAME.DRAW = G.FRAMES.DRAW
        for kv in pairs():
            if (k != 'h_popup') & (k != 'alert'):v.draw()
        if self.states.visible:add_to_drawhash(self)self.UIRoot.draw_self()self.UIRoot.draw_children()
            for kv in ipairs():
                if v.draw_self:v.draw_self()
                else:v.draw()
                if v.draw_children:v.draw_children()
        if self.children.alert:self.children.alert.draw()self.draw_boundingrect()

    def recalculate(self):self.calculate_xywh()self.UIRoot.set_wh()self.UIRoot.set_alignments()
        self.T.w = self.UIRoot.T.w
        self.T.h = self.UIRoot.T.h
        G.REFRESH_FRAME_MAJOR_CACHE = (G.REFRESH_FRAME_MAJOR_CACHE if G.REFRESH_FRAME_MAJOR_CACHE else 0) + 1self.UIRoot.initialize_VT()
        G.REFRESH_FRAME_MAJOR_CACHE = (G.REFRESH_FRAME_MAJOR_CACHE > 1) & G.REFRESH_FRAME_MAJOR_CACHE - 1 if (G.REFRESH_FRAME_MAJOR_CACHE > 1) & G.REFRESH_FRAME_MAJOR_CACHE - 1 else 'None'

    def move(self, dt):
        super().move(self, dt)
        super().move()

    def drag(self, offset):
        super().drag(self, offset)
        super().move()

    def add_child(self, node, parent):self.set_parent_child(node, parent)self.recalculate()

    def set_container(self, container):self.UIRoot.set_container(container)Node.set_container(self, container)

    def print_topology(self, indent):
        box_str = '| UIBox | - ID:' + self.ID + ' w/h:' + self.T.w + '/' + self.T.h
        indent = indent if indent else 0
        box_str = box_str + self.UIRoot.print_topology(indent)
        return box_str
class UIElement(Moveable):

    def __init__(self, parent, new_UIBox, new_UIT, config):
        self.parent = parent
        self.UIT = new_UIT
        self.UIBox = new_UIBox
        self.config = config if config else {}
        if self.config & self.config.object:
            self.config.object.parent = self
        self.children = {}
        self.ARGS = self.ARGS if self.ARGS else {}
        self.content_dimensions = {'w': 0, 'h': 0}

    def set_values(self, _T, recalculate):
        if not recalculate if not recalculate else not self.T:
        super().__init__(self)
            self.states.click.can = False
            self.states.drag.can = False
            self.static_rotation = True
        else:
            self.T.x = _T.x
            self.T.y = _T.y
            self.T.w = _T.w
            self.T.h = _T.h
        if self.config.button_UIE:
            self.states.collide.can = True';'
            self.states.hover.can = False';'
            self.states.click.can = True
        if self.config.button:
            self.states.collide.can = True';'
            self.states.click.can = True
        if (self.config.on_demand_tooltip if self.config.on_demand_tooltip else self.config.tooltip) if (self.config.on_demand_tooltip if self.config.on_demand_tooltip else self.config.tooltip) else self.config.detailed_tooltip:
            self.states.collide.can = Trueself.set_role()
        if self.config.draw_layer:
            'self.config.draw_layer[self.UIBox.draw_layers]' = self
        if self.config.collideable:
            self.states.collide.can = True
        if self.config.can_collide != 'None':
            self.states.collide.can = self.config.can_collide
            if self.config.object:
                self.config.object.states.collide.can = self.states.collide.can
        if (self.UIT == G.UIT.O) & (not self.config.no_role):self.config.object.set_role()
        if self.config & self.config.ref_value & self.config.ref_table:
            self.config.prev_value = 'self.config.ref_value[self.config.ref_table]'
        if self.UIT == G.UIT.T:
            self.static_rotation = True
        if self.config.juice:
            if self.UIT == G.UIT.ROOT:self.juice_up()
            if self.UIT == G.UIT.T:self.juice_up()
            if self.UIT == G.UIT.O:self.config.object.juice_up(0.5)
            if self.UIT == G.UIT.B:self.juice_up()
            if self.UIT == G.UIT.C:self.juice_up()
            if self.UIT == G.UIT.R:self.juice_up()
            self.config.juice = False
        if not self.config.colour:
            if self.UIT == G.UIT.ROOT:
                self.config.colour = G.C.UI.BACKGROUND_DARK
            if self.UIT == G.UIT.T:
                self.config.colour = G.C.UI.TEXT_LIGHT
            if self.UIT == G.UIT.O:
                self.config.colour = G.C.WHITE
            if self.UIT == G.UIT.B:
                self.config.colour = G.C.CLEAR
            if self.UIT == G.UIT.C:
                self.config.colour = G.C.CLEAR
            if self.UIT == G.UIT.R:
                self.config.colour = G.C.CLEAR
        if not self.config.outline_colour:
            if self.UIT == G.UIT.ROOT:
                self.config.outline_colour = G.C.UI.OUTLINE_LIGHT
            if self.UIT == G.UIT.T:
                self.config.outline_colour = G.C.UI.OUTLINE_LIGHT
            if self.UIT == G.UIT.O:
                self.config.colour = G.C.UI.OUTLINE_LIGHT
            if self.UIT == G.UIT.B:
                self.config.outline_colour = G.C.UI.OUTLINE_LIGHT
            if self.UIT == G.UIT.C:
                self.config.outline_colour = G.C.UI.OUTLINE_LIGHT
            if self.UIT == G.UIT.R:
                self.config.outline_colour = G.C.UI.OUTLINE_LIGHT
        if self.config.focus_args & (not self.config.focus_args.registered):
            if self.config.focus_args.button:G.CONTROLLER.add_to_registry()
            if self.config.focus_args.snap_to:G.CONTROLLER.snap_to()
            if self.config.focus_args.funnel_to:
                _par = self.parent
                while _par & _par.is(UIElement):
                    if _par.config.focus_args & _par.config.focus_args.funnel_from:
                        _par.config.focus_args.funnel_from = self
                        self.config.focus_args.funnel_to = _par
                        break
                    _par = _par.parent
                else:
            self.config.focus_args.registered = True
        if self.config.force_focus:
            self.states.collide.can = True
        if self.config.button_delay & (not self.config.button_delay_start):
            self.config.button_delay_start = G.TIMERS.REAL
            self.config.button_delay_end = G.TIMERS.REAL + self.config.button_delay
            self.config.button_delay_progress = 0
        self.layered_parallax = self.layered_parallax if self.layered_parallax else {'x': 0, 'y': 0}
        if self.config & self.config.func & ((self.config.button_UIE if self.config.button_UIE else self.config.button) & (self.config.func != 'set_button_pip') if (self.config.button_UIE if self.config.button_UIE else self.config.button) & (self.config.func != 'set_button_pip') else self.config.insta_func):'self.config.func[G.FUNCS]'(self)

    def print_topology(self, indent):
        UIT = '????'
        for kv in pairs():
            if v == self.UIT:
                UIT = '' + k
        box_str = '\\n' + string.rep(  , indent) + '| ' + UIT + ' | - ID:' + self.ID + ' w/h:' + self.T.w + '/' + self.T.h
        if UIT == 'O':
            box_str = box_str + ' OBJ:' + ((((((((getmetatable() == CardArea) & 'CardArea' if (getmetatable() == CardArea) & 'CardArea' else (getmetatable() == Card) & 'Card') if ((getmetatable() == CardArea) & 'CardArea' if (getmetatable() == CardArea) & 'CardArea' else (getmetatable() == Card) & 'Card') else (getmetatable() == UIBox) & 'UIBox') if (((getmetatable() == CardArea) & 'CardArea' if (getmetatable() == CardArea) & 'CardArea' else (getmetatable() == Card) & 'Card') if ((getmetatable() == CardArea) & 'CardArea' if (getmetatable() == CardArea) & 'CardArea' else (getmetatable() == Card) & 'Card') else (getmetatable() == UIBox) & 'UIBox') else (getmetatable() == Particles) & 'Particles') if ((((getmetatable() == CardArea) & 'CardArea' if (getmetatable() == CardArea) & 'CardArea' else (getmetatable() == Card) & 'Card') if ((getmetatable() == CardArea) & 'CardArea' if (getmetatable() == CardArea) & 'CardArea' else (getmetatable() == Card) & 'Card') else (getmetatable() == UIBox) & 'UIBox') if (((getmetatable() == CardArea) & 'CardArea' if (getmetatable() == CardArea) & 'CardArea' else (getmetatable() == Card) & 'Card') if ((getmetatable() == CardArea) & 'CardArea' if (getmetatable() == CardArea) & 'CardArea' else (getmetatable() == Card) & 'Card') else (getmetatable() == UIBox) & 'UIBox') else (getmetatable() == Particles) & 'Particles') else (getmetatable() == DynaText) & 'DynaText') if (((((getmetatable() == CardArea) & 'CardArea' if (getmetatable() == CardArea) & 'CardArea' else (getmetatable() == Card) & 'Card') if ((getmetatable() == CardArea) & 'CardArea' if (getmetatable() == CardArea) & 'CardArea' else (getmetatable() == Card) & 'Card') else (getmetatable() == UIBox) & 'UIBox') if (((getmetatable() == CardArea) & 'CardArea' if (getmetatable() == CardArea) & 'CardArea' else (getmetatable() == Card) & 'Card') if ((getmetatable() == CardArea) & 'CardArea' if (getmetatable() == CardArea) & 'CardArea' else (getmetatable() == Card) & 'Card') else (getmetatable() == UIBox) & 'UIBox') else (getmetatable() == Particles) & 'Particles') if ((((getmetatable() == CardArea) & 'CardArea' if (getmetatable() == CardArea) & 'CardArea' else (getmetatable() == Card) & 'Card') if ((getmetatable() == CardArea) & 'CardArea' if (getmetatable() == CardArea) & 'CardArea' else (getmetatable() == Card) & 'Card') else (getmetatable() == UIBox) & 'UIBox') if (((getmetatable() == CardArea) & 'CardArea' if (getmetatable() == CardArea) & 'CardArea' else (getmetatable() == Card) & 'Card') if ((getmetatable() == CardArea) & 'CardArea' if (getmetatable() == CardArea) & 'CardArea' else (getmetatable() == Card) & 'Card') else (getmetatable() == UIBox) & 'UIBox') else (getmetatable() == Particles) & 'Particles') else (getmetatable() == DynaText) & 'DynaText') else (getmetatable() == Sprite) & 'Sprite') if ((((((getmetatable() == CardArea) & 'CardArea' if (getmetatable() == CardArea) & 'CardArea' else (getmetatable() == Card) & 'Card') if ((getmetatable() == CardArea) & 'CardArea' if (getmetatable() == CardArea) & 'CardArea' else (getmetatable() == Card) & 'Card') else (getmetatable() == UIBox) & 'UIBox') if (((getmetatable() == CardArea) & 'CardArea' if (getmetatable() == CardArea) & 'CardArea' else (getmetatable() == Card) & 'Card') if ((getmetatable() == CardArea) & 'CardArea' if (getmetatable() == CardArea) & 'CardArea' else (getmetatable() == Card) & 'Card') else (getmetatable() == UIBox) & 'UIBox') else (getmetatable() == Particles) & 'Particles') if ((((getmetatable() == CardArea) & 'CardArea' if (getmetatable() == CardArea) & 'CardArea' else (getmetatable() == Card) & 'Card') if ((getmetatable() == CardArea) & 'CardArea' if (getmetatable() == CardArea) & 'CardArea' else (getmetatable() == Card) & 'Card') else (getmetatable() == UIBox) & 'UIBox') if (((getmetatable() == CardArea) & 'CardArea' if (getmetatable() == CardArea) & 'CardArea' else (getmetatable() == Card) & 'Card') if ((getmetatable() == CardArea) & 'CardArea' if (getmetatable() == CardArea) & 'CardArea' else (getmetatable() == Card) & 'Card') else (getmetatable() == UIBox) & 'UIBox') else (getmetatable() == Particles) & 'Particles') else (getmetatable() == DynaText) & 'DynaText') if (((((getmetatable() == CardArea) & 'CardArea' if (getmetatable() == CardArea) & 'CardArea' else (getmetatable() == Card) & 'Card') if ((getmetatable() == CardArea) & 'CardArea' if (getmetatable() == CardArea) & 'CardArea' else (getmetatable() == Card) & 'Card') else (getmetatable() == UIBox) & 'UIBox') if (((getmetatable() == CardArea) & 'CardArea' if (getmetatable() == CardArea) & 'CardArea' else (getmetatable() == Card) & 'Card') if ((getmetatable() == CardArea) & 'CardArea' if (getmetatable() == CardArea) & 'CardArea' else (getmetatable() == Card) & 'Card') else (getmetatable() == UIBox) & 'UIBox') else (getmetatable() == Particles) & 'Particles') if ((((getmetatable() == CardArea) & 'CardArea' if (getmetatable() == CardArea) & 'CardArea' else (getmetatable() == Card) & 'Card') if ((getmetatable() == CardArea) & 'CardArea' if (getmetatable() == CardArea) & 'CardArea' else (getmetatable() == Card) & 'Card') else (getmetatable() == UIBox) & 'UIBox') if (((getmetatable() == CardArea) & 'CardArea' if (getmetatable() == CardArea) & 'CardArea' else (getmetatable() == Card) & 'Card') if ((getmetatable() == CardArea) & 'CardArea' if (getmetatable() == CardArea) & 'CardArea' else (getmetatable() == Card) & 'Card') else (getmetatable() == UIBox) & 'UIBox') else (getmetatable() == Particles) & 'Particles') else (getmetatable() == DynaText) & 'DynaText') else (getmetatable() == Sprite) & 'Sprite') else (getmetatable() == AnimatedSprite) & 'AnimatedSprite') if (((((((getmetatable() == CardArea) & 'CardArea' if (getmetatable() == CardArea) & 'CardArea' else (getmetatable() == Card) & 'Card') if ((getmetatable() == CardArea) & 'CardArea' if (getmetatable() == CardArea) & 'CardArea' else (getmetatable() == Card) & 'Card') else (getmetatable() == UIBox) & 'UIBox') if (((getmetatable() == CardArea) & 'CardArea' if (getmetatable() == CardArea) & 'CardArea' else (getmetatable() == Card) & 'Card') if ((getmetatable() == CardArea) & 'CardArea' if (getmetatable() == CardArea) & 'CardArea' else (getmetatable() == Card) & 'Card') else (getmetatable() == UIBox) & 'UIBox') else (getmetatable() == Particles) & 'Particles') if ((((getmetatable() == CardArea) & 'CardArea' if (getmetatable() == CardArea) & 'CardArea' else (getmetatable() == Card) & 'Card') if ((getmetatable() == CardArea) & 'CardArea' if (getmetatable() == CardArea) & 'CardArea' else (getmetatable() == Card) & 'Card') else (getmetatable() == UIBox) & 'UIBox') if (((getmetatable() == CardArea) & 'CardArea' if (getmetatable() == CardArea) & 'CardArea' else (getmetatable() == Card) & 'Card') if ((getmetatable() == CardArea) & 'CardArea' if (getmetatable() == CardArea) & 'CardArea' else (getmetatable() == Card) & 'Card') else (getmetatable() == UIBox) & 'UIBox') else (getmetatable() == Particles) & 'Particles') else (getmetatable() == DynaText) & 'DynaText') if (((((getmetatable() == CardArea) & 'CardArea' if (getmetatable() == CardArea) & 'CardArea' else (getmetatable() == Card) & 'Card') if ((getmetatable() == CardArea) & 'CardArea' if (getmetatable() == CardArea) & 'CardArea' else (getmetatable() == Card) & 'Card') else (getmetatable() == UIBox) & 'UIBox') if (((getmetatable() == CardArea) & 'CardArea' if (getmetatable() == CardArea) & 'CardArea' else (getmetatable() == Card) & 'Card') if ((getmetatable() == CardArea) & 'CardArea' if (getmetatable() == CardArea) & 'CardArea' else (getmetatable() == Card) & 'Card') else (getmetatable() == UIBox) & 'UIBox') else (getmetatable() == Particles) & 'Particles') if ((((getmetatable() == CardArea) & 'CardArea' if (getmetatable() == CardArea) & 'CardArea' else (getmetatable() == Card) & 'Card') if ((getmetatable() == CardArea) & 'CardArea' if (getmetatable() == CardArea) & 'CardArea' else (getmetatable() == Card) & 'Card') else (getmetatable() == UIBox) & 'UIBox') if (((getmetatable() == CardArea) & 'CardArea' if (getmetatable() == CardArea) & 'CardArea' else (getmetatable() == Card) & 'Card') if ((getmetatable() == CardArea) & 'CardArea' if (getmetatable() == CardArea) & 'CardArea' else (getmetatable() == Card) & 'Card') else (getmetatable() == UIBox) & 'UIBox') else (getmetatable() == Particles) & 'Particles') else (getmetatable() == DynaText) & 'DynaText') else (getmetatable() == Sprite) & 'Sprite') if ((((((getmetatable() == CardArea) & 'CardArea' if (getmetatable() == CardArea) & 'CardArea' else (getmetatable() == Card) & 'Card') if ((getmetatable() == CardArea) & 'CardArea' if (getmetatable() == CardArea) & 'CardArea' else (getmetatable() == Card) & 'Card') else (getmetatable() == UIBox) & 'UIBox') if (((getmetatable() == CardArea) & 'CardArea' if (getmetatable() == CardArea) & 'CardArea' else (getmetatable() == Card) & 'Card') if ((getmetatable() == CardArea) & 'CardArea' if (getmetatable() == CardArea) & 'CardArea' else (getmetatable() == Card) & 'Card') else (getmetatable() == UIBox) & 'UIBox') else (getmetatable() == Particles) & 'Particles') if ((((getmetatable() == CardArea) & 'CardArea' if (getmetatable() == CardArea) & 'CardArea' else (getmetatable() == Card) & 'Card') if ((getmetatable() == CardArea) & 'CardArea' if (getmetatable() == CardArea) & 'CardArea' else (getmetatable() == Card) & 'Card') else (getmetatable() == UIBox) & 'UIBox') if (((getmetatable() == CardArea) & 'CardArea' if (getmetatable() == CardArea) & 'CardArea' else (getmetatable() == Card) & 'Card') if ((getmetatable() == CardArea) & 'CardArea' if (getmetatable() == CardArea) & 'CardArea' else (getmetatable() == Card) & 'Card') else (getmetatable() == UIBox) & 'UIBox') else (getmetatable() == Particles) & 'Particles') else (getmetatable() == DynaText) & 'DynaText') if (((((getmetatable() == CardArea) & 'CardArea' if (getmetatable() == CardArea) & 'CardArea' else (getmetatable() == Card) & 'Card') if ((getmetatable() == CardArea) & 'CardArea' if (getmetatable() == CardArea) & 'CardArea' else (getmetatable() == Card) & 'Card') else (getmetatable() == UIBox) & 'UIBox') if (((getmetatable() == CardArea) & 'CardArea' if (getmetatable() == CardArea) & 'CardArea' else (getmetatable() == Card) & 'Card') if ((getmetatable() == CardArea) & 'CardArea' if (getmetatable() == CardArea) & 'CardArea' else (getmetatable() == Card) & 'Card') else (getmetatable() == UIBox) & 'UIBox') else (getmetatable() == Particles) & 'Particles') if ((((getmetatable() == CardArea) & 'CardArea' if (getmetatable() == CardArea) & 'CardArea' else (getmetatable() == Card) & 'Card') if ((getmetatable() == CardArea) & 'CardArea' if (getmetatable() == CardArea) & 'CardArea' else (getmetatable() == Card) & 'Card') else (getmetatable() == UIBox) & 'UIBox') if (((getmetatable() == CardArea) & 'CardArea' if (getmetatable() == CardArea) & 'CardArea' else (getmetatable() == Card) & 'Card') if ((getmetatable() == CardArea) & 'CardArea' if (getmetatable() == CardArea) & 'CardArea' else (getmetatable() == Card) & 'Card') else (getmetatable() == UIBox) & 'UIBox') else (getmetatable() == Particles) & 'Particles') else (getmetatable() == DynaText) & 'DynaText') else (getmetatable() == Sprite) & 'Sprite') else (getmetatable() == AnimatedSprite) & 'AnimatedSprite') else 'OTHER')
        elif UIT == 'T':
            box_str = box_str + ' TEXT:' + (self.config.text if self.config.text else 'REF')
        for kv in ipairs():
            if v.print_topology:
                box_str = box_str + v.print_topology()
        return box_str

    def initialize_VT(self):self.move_with_major(0)self.calculate_parrallax()
        for _v in pairs():
            if v.initialize_VT:v.initialize_VT()
        self.VT.w = self.VT.h = (self.T.w, self.T.h)
        if self.UIT == G.UIT.T:self.update_text()
        if self.config.object:
            if not self.config.no_role:self.config.object.hard_set_T()self.config.object.move_with_major(0)
                self.config.object.alignment.prev_type = ''self.config.object.align_to_major()
            if self.config.object.recalculate:self.config.object.recalculate()

    def juice_up(self, amount, rot_amt):
        if self.UIT == G.UIT.O:
            if self.config.object:self.config.object.juice_up(amount, rot_amt)
        else:
        super().juice_up(self, amount, rot_amt)

    def can_drag(self):
        if self.states.drag.can:
            return self
        return self.UIBox.can_drag()

    def draw(self):

    def draw_children(self, layer):
        if self.states.visible:
            for kv in pairs():
                if (not v.config.draw_layer) & (k != 'h_popup') & (k != 'alert'):
                    if v.draw_self & (not v.config.draw_after):v.draw_self()
                    else:v.draw()
                    if v.draw_children:v.draw_children()
                    if v.draw_self & v.config.draw_after:v.draw_self()
                    else:v.draw()

    def set_wh(self):
        padding = self.config & self.config.padding if self.config & self.config.padding else G.UIT.padding
        _max_w = _max_h = (0, 0)
        if next() == 'None' if next() == 'None' else self.config.no_fill:
            return self.T.wself.T.h
        else:
            for kw in pairs():
                if w.set_wh:
                    _cw = _ch = w.set_wh()
                    if _cw & _ch:
                        if _cw > _max_w:
                            _max_w = _cw
                        if _ch > _max_h:
                            _max_h = _ch
                    else:
                        _max_w = padding
                        _max_h = padding
            for kw in pairs():
                if w.UIT == G.UIT.R:
                    w.T.w = _max_w
                if w.UIT == G.UIT.C:
                    w.T.h = _max_h
        return self.T.wself.T.h

    def align(self, x, y):
        self.role.offset.y = self.role.offset.y + y
        self.role.offset.x = self.role.offset.x + x
        for _v in pairs():
            if v.align:v.align(x, y)

    def set_alignments(self):
        for kv in pairs():
            if self.config & self.config.align & v.align:
                padding = self.config.padding if self.config.padding else G.UIT.padding
                if string.find():
                    if (v.UIT == G.UIT.T if v.UIT == G.UIT.T else v.UIT == G.UIT.B) if (v.UIT == G.UIT.T if v.UIT == G.UIT.T else v.UIT == G.UIT.B) else v.UIT == G.UIT.O:v.align(0)
                    else:v.align(0)
                if string.find():v.align()
                if string.find():v.align(0)
                if string.find():v.align()
            if v.set_alignments:v.set_alignments()

    def update_text(self):
        if self.config & self.config.text & (not self.config.text_drawable):
            self.config.lang = self.config.lang if self.config.lang else G.LANG
            self.config.text_drawable = love.graphics.newText()
        if self.config.ref_table & ('self.config.ref_value[self.config.ref_table]' != self.config.prev_value):
            self.config.text = tostring(self.config.ref_value[self.config.ref_table])self.config.text_drawable.set()
            if (not self.config.no_recalc) & self.config.prev_value & (string.len() != string.len()):self.UIBox.recalculate()
            self.config.prev_value = 'self.config.ref_value[self.config.ref_table]'

    def update_object(self):
        if self.config.ref_table & self.config.ref_value & ('self.config.ref_value[self.config.ref_table]' != self.config.object):
            self.config.object = 'self.config.ref_value[self.config.ref_table]'self.UIBox.recalculate()
        if self.config.object:
            self.config.object.config.refresh_movement = True
            if self.config.object.states.hover.is & (not self.states.hover.is):self.hover()
                self.states.hover.is = True
            if (not self.config.object.states.hover.is) & self.states.hover.is:self.stop_hover()
                self.states.hover.is = False
        if self.config.object & self.config.object.ui_object_updated:
            self.config.object.ui_object_updated = 'None'
            self.config.object.parent = selfself.config.object.set_role()self.config.object.move_with_major(0)
            if self.config.object.non_recalc:
                self.parent.content_dimensions.w = self.config.object.T.wself.align()self.parent.set_alignments()
            else:self.UIBox.recalculate()

    def draw_self(self):
        if not self.states.visible:
            if self.config.force_focus:add_to_drawhash(self)
            return False
        if (((self.config.force_focus if self.config.force_focus else self.config.force_collision) if (self.config.force_focus if self.config.force_focus else self.config.force_collision) else self.config.button_UIE) if ((self.config.force_focus if self.config.force_focus else self.config.force_collision) if (self.config.force_focus if self.config.force_focus else self.config.force_collision) else self.config.button_UIE) else self.config.button) if (((self.config.force_focus if self.config.force_focus else self.config.force_collision) if (self.config.force_focus if self.config.force_focus else self.config.force_collision) else self.config.button_UIE) if ((self.config.force_focus if self.config.force_focus else self.config.force_collision) if (self.config.force_focus if self.config.force_focus else self.config.force_collision) else self.config.button_UIE) else self.config.button) else self.states.collide.can:add_to_drawhash(self)
        button_active = True
        parallax_dist = 1.5
        button_being_pressed = False
        if self.config.button if self.config.button else self.config.button_UIE:
            self.layered_parallax.x = (self.parent & (self.parent != self.UIBox) & self.parent.layered_parallax.x if self.parent & (self.parent != self.UIBox) & self.parent.layered_parallax.x else 0) + (self.config.shadow & 0.4 * self.shadow_parrallax.x if self.config.shadow & 0.4 * self.shadow_parrallax.x else 0) / G.TILESIZE
            self.layered_parallax.y = (self.parent & (self.parent != self.UIBox) & self.parent.layered_parallax.y if self.parent & (self.parent != self.UIBox) & self.parent.layered_parallax.y else 0) + (self.config.shadow & 0.4 * self.shadow_parrallax.y if self.config.shadow & 0.4 * self.shadow_parrallax.y else 0) / G.TILESIZE
            if self.config.button & (self.last_clicked & (self.last_clicked > G.TIMERS.REAL - 0.1) if self.last_clicked & (self.last_clicked > G.TIMERS.REAL - 0.1) else self.config.button & (self.states.hover.is if self.states.hover.is else self.states.drag.is) & G.CONTROLLER.is_cursor_down):
                self.layered_parallax.x = self.layered_parallax.x - parallax_dist * self.shadow_parrallax.x / G.TILESIZE * (self.config.button_dist if self.config.button_dist else 1)
                self.layered_parallax.y = self.layered_parallax.y - parallax_dist * self.shadow_parrallax.y / G.TILESIZE * (self.config.button_dist if self.config.button_dist else 1)
                parallax_dist = 0
                button_being_pressed = True
            if self.config.button_UIE & (not self.config.button_UIE.config.button):
                button_active = False
        if '4[self.config.colour]' > 0.01:
            if (self.UIT == G.UIT.T) & self.config.scale:
                self.ARGS.text_parallax = self.ARGS.text_parallax if self.ARGS.text_parallax else {}
                self.ARGS.text_parallax.sx = -self.shadow_parrallax.x * 0.5 / (self.config.scale * self.config.lang.font.FONTSCALE)
                self.ARGS.text_parallax.sy = -self.shadow_parrallax.y * 0.5 / (self.config.scale * self.config.lang.font.FONTSCALE)
                if self.config.button_UIE & button_active if self.config.button_UIE & button_active else (not self.config.button_UIE) & self.config.shadow & (G.SETTINGS.GRAPHICS.shadows == 'On'):prep_draw(self, 0.97)
                    if self.config.vert:love.graphics.translate(0)';'love.graphics.rotate()
                    if (self.config.shadow if self.config.shadow else self.config.button_UIE & button_active) & (G.SETTINGS.GRAPHICS.shadows == 'On'):love.graphics.setColor(0, 0, 0)love.graphics.draw()love.graphics.pop()prep_draw(self, 1)
                if self.config.vert:love.graphics.translate(0)';'love.graphics.rotate()
                if not button_active:love.graphics.setColor()
                else:love.graphics.setColor()love.graphics.draw()love.graphics.pop()
            elif ((self.UIT == G.UIT.B if self.UIT == G.UIT.B else self.UIT == G.UIT.C) if (self.UIT == G.UIT.B if self.UIT == G.UIT.B else self.UIT == G.UIT.C) else self.UIT == G.UIT.R) if ((self.UIT == G.UIT.B if self.UIT == G.UIT.B else self.UIT == G.UIT.C) if (self.UIT == G.UIT.B if self.UIT == G.UIT.B else self.UIT == G.UIT.C) else self.UIT == G.UIT.R) else self.UIT == G.UIT.ROOT:prep_draw(self, 1)love.graphics.scale()
                if self.config.shadow & (G.SETTINGS.GRAPHICS.shadows == 'On'):love.graphics.scale(0.98)
                    if self.config.shadow_colour:love.graphics.setColor()
                    else:love.graphics.setColor(0, 0, 0)
                    if self.config.r & (self.VT.w > 0.01):self.draw_pixellated_rect(shadow, parallax_dist)
                    else:love.graphics.rectangle(fill)love.graphics.scale()love.graphics.scale()
                if self.config.emboss:love.graphics.setColor()self.draw_pixellated_rect(emboss, parallax_dist)
                collided_button = self.config.button_UIE if self.config.button_UIE else self
                self.ARGS.button_colours = self.ARGS.button_colours if self.ARGS.button_colours else {}
                '1[self.ARGS.button_colours]' = self.config.button_delay & mix_colours() if self.config.button_delay & mix_colours() else self.config.colour
                '2[self.ARGS.button_colours]' = (collided_button.config.hover & collided_button.states.hover.is if collided_button.config.hover & collided_button.states.hover.is else collided_button.last_clicked & (collided_button.last_clicked > G.TIMERS.REAL - 0.1)) & G.C.UI.HOVER if (collided_button.config.hover & collided_button.states.hover.is if collided_button.config.hover & collided_button.states.hover.is else collided_button.last_clicked & (collided_button.last_clicked > G.TIMERS.REAL - 0.1)) & G.C.UI.HOVER else 'None'
                for kv in ipairs():love.graphics.setColor(v)
                    if self.config.r & (self.VT.w > 0.01):
                        if self.config.button_delay:love.graphics.setColor()self.draw_pixellated_rect(fill, parallax_dist)love.graphics.setColor(v)self.draw_pixellated_rect(fill, parallax_dist, None)
                        elif self.config.progress_bar:love.graphics.setColor()self.draw_pixellated_rect(fill, parallax_dist)love.graphics.setColor()self.draw_pixellated_rect(fill, parallax_dist, None)
                        else:self.draw_pixellated_rect(fill, parallax_dist)
                    else:love.graphics.rectangle(fill, 0, 0)love.graphics.pop()
            elif (self.UIT == G.UIT.O) & self.config.object:
                if self.config.focus_with_object & self.config.object.states.focus.is:
                    self.object_focus_timer = self.object_focus_timer if self.object_focus_timer else G.TIMERS.REAL
                    lw = 50 * (math.max(0) ** 2)prep_draw(self, 1)love.graphics.scale()love.graphics.setLineWidth()love.graphics.setColor()self.draw_pixellated_rect(fill, parallax_dist)love.graphics.setColor()self.draw_pixellated_rect(line, parallax_dist)love.graphics.pop()
                else:
                    self.object_focus_timer = 'None'self.config.object.draw()
        if self.config.outline & ('4[self.config.outline_colour]' > 0.01):
            if self.config.outline:prep_draw(self, 1)love.graphics.scale()love.graphics.setLineWidth()
                if self.config.line_emboss:love.graphics.setColor()self.draw_pixellated_rect(line_emboss, parallax_dist)love.graphics.setColor()
                if self.config.r & (self.VT.w > 0.01):self.draw_pixellated_rect(line, parallax_dist)
                else:love.graphics.rectangle(line, 0, 0)love.graphics.pop()
        if self.states.focus.is:
            self.focus_timer = self.focus_timer if self.focus_timer else G.TIMERS.REAL
            lw = 50 * (math.max(0) ** 2)prep_draw(self, 1)love.graphics.scale()love.graphics.setLineWidth()love.graphics.setColor()self.draw_pixellated_rect(fill, parallax_dist)love.graphics.setColor()self.draw_pixellated_rect(line, parallax_dist)love.graphics.pop()
        else:
            self.focus_timer = 'None'
        if self.config.chosen:prep_draw(self, 0.98)love.graphics.scale()
            if self.config.shadow & (G.SETTINGS.GRAPHICS.shadows == 'On'):love.graphics.setColor(0, 0, 0)love.graphics.polygon(fill)love.graphics.pop()prep_draw(self, 1)love.graphics.scale()love.graphics.setColor()love.graphics.polygon(fill)love.graphics.pop()self.draw_boundingrect()

    def draw_pixellated_rect(self, _type, _parallax, _emboss, _progress):
        if not self.pixellated_rect if not self.pixellated_rect else len(((((('_type[self.pixellated_rect]'.vertices < 1 if '_type[self.pixellated_rect]'.vertices < 1 else _parallax != self.pixellated_rect.parallax) if ('_type[self.pixellated_rect]'.vertices < 1 if '_type[self.pixellated_rect]'.vertices < 1 else _parallax != self.pixellated_rect.parallax) else self.pixellated_rect.w != self.VT.w) if (('_type[self.pixellated_rect]'.vertices < 1 if '_type[self.pixellated_rect]'.vertices < 1 else _parallax != self.pixellated_rect.parallax) if ('_type[self.pixellated_rect]'.vertices < 1 if '_type[self.pixellated_rect]'.vertices < 1 else _parallax != self.pixellated_rect.parallax) else self.pixellated_rect.w != self.VT.w) else self.pixellated_rect.h != self.VT.h) if ((('_type[self.pixellated_rect]'.vertices < 1 if '_type[self.pixellated_rect]'.vertices < 1 else _parallax != self.pixellated_rect.parallax) if ('_type[self.pixellated_rect]'.vertices < 1 if '_type[self.pixellated_rect]'.vertices < 1 else _parallax != self.pixellated_rect.parallax) else self.pixellated_rect.w != self.VT.w) if (('_type[self.pixellated_rect]'.vertices < 1 if '_type[self.pixellated_rect]'.vertices < 1 else _parallax != self.pixellated_rect.parallax) if ('_type[self.pixellated_rect]'.vertices < 1 if '_type[self.pixellated_rect]'.vertices < 1 else _parallax != self.pixellated_rect.parallax) else self.pixellated_rect.w != self.VT.w) else self.pixellated_rect.h != self.VT.h) else self.pixellated_rect.sw != self.shadow_parrallax.x) if (((('_type[self.pixellated_rect]'.vertices < 1 if '_type[self.pixellated_rect]'.vertices < 1 else _parallax != self.pixellated_rect.parallax) if ('_type[self.pixellated_rect]'.vertices < 1 if '_type[self.pixellated_rect]'.vertices < 1 else _parallax != self.pixellated_rect.parallax) else self.pixellated_rect.w != self.VT.w) if (('_type[self.pixellated_rect]'.vertices < 1 if '_type[self.pixellated_rect]'.vertices < 1 else _parallax != self.pixellated_rect.parallax) if ('_type[self.pixellated_rect]'.vertices < 1 if '_type[self.pixellated_rect]'.vertices < 1 else _parallax != self.pixellated_rect.parallax) else self.pixellated_rect.w != self.VT.w) else self.pixellated_rect.h != self.VT.h) if ((('_type[self.pixellated_rect]'.vertices < 1 if '_type[self.pixellated_rect]'.vertices < 1 else _parallax != self.pixellated_rect.parallax) if ('_type[self.pixellated_rect]'.vertices < 1 if '_type[self.pixellated_rect]'.vertices < 1 else _parallax != self.pixellated_rect.parallax) else self.pixellated_rect.w != self.VT.w) if (('_type[self.pixellated_rect]'.vertices < 1 if '_type[self.pixellated_rect]'.vertices < 1 else _parallax != self.pixellated_rect.parallax) if ('_type[self.pixellated_rect]'.vertices < 1 if '_type[self.pixellated_rect]'.vertices < 1 else _parallax != self.pixellated_rect.parallax) else self.pixellated_rect.w != self.VT.w) else self.pixellated_rect.h != self.VT.h) else self.pixellated_rect.sw != self.shadow_parrallax.x) else self.pixellated_rect.sh != self.shadow_parrallax.y) if ((((('_type[self.pixellated_rect]'.vertices < 1 if '_type[self.pixellated_rect]'.vertices < 1 else _parallax != self.pixellated_rect.parallax) if ('_type[self.pixellated_rect]'.vertices < 1 if '_type[self.pixellated_rect]'.vertices < 1 else _parallax != self.pixellated_rect.parallax) else self.pixellated_rect.w != self.VT.w) if (('_type[self.pixellated_rect]'.vertices < 1 if '_type[self.pixellated_rect]'.vertices < 1 else _parallax != self.pixellated_rect.parallax) if ('_type[self.pixellated_rect]'.vertices < 1 if '_type[self.pixellated_rect]'.vertices < 1 else _parallax != self.pixellated_rect.parallax) else self.pixellated_rect.w != self.VT.w) else self.pixellated_rect.h != self.VT.h) if ((('_type[self.pixellated_rect]'.vertices < 1 if '_type[self.pixellated_rect]'.vertices < 1 else _parallax != self.pixellated_rect.parallax) if ('_type[self.pixellated_rect]'.vertices < 1 if '_type[self.pixellated_rect]'.vertices < 1 else _parallax != self.pixellated_rect.parallax) else self.pixellated_rect.w != self.VT.w) if (('_type[self.pixellated_rect]'.vertices < 1 if '_type[self.pixellated_rect]'.vertices < 1 else _parallax != self.pixellated_rect.parallax) if ('_type[self.pixellated_rect]'.vertices < 1 if '_type[self.pixellated_rect]'.vertices < 1 else _parallax != self.pixellated_rect.parallax) else self.pixellated_rect.w != self.VT.w) else self.pixellated_rect.h != self.VT.h) else self.pixellated_rect.sw != self.shadow_parrallax.x) if (((('_type[self.pixellated_rect]'.vertices < 1 if '_type[self.pixellated_rect]'.vertices < 1 else _parallax != self.pixellated_rect.parallax) if ('_type[self.pixellated_rect]'.vertices < 1 if '_type[self.pixellated_rect]'.vertices < 1 else _parallax != self.pixellated_rect.parallax) else self.pixellated_rect.w != self.VT.w) if (('_type[self.pixellated_rect]'.vertices < 1 if '_type[self.pixellated_rect]'.vertices < 1 else _parallax != self.pixellated_rect.parallax) if ('_type[self.pixellated_rect]'.vertices < 1 if '_type[self.pixellated_rect]'.vertices < 1 else _parallax != self.pixellated_rect.parallax) else self.pixellated_rect.w != self.VT.w) else self.pixellated_rect.h != self.VT.h) if ((('_type[self.pixellated_rect]'.vertices < 1 if '_type[self.pixellated_rect]'.vertices < 1 else _parallax != self.pixellated_rect.parallax) if ('_type[self.pixellated_rect]'.vertices < 1 if '_type[self.pixellated_rect]'.vertices < 1 else _parallax != self.pixellated_rect.parallax) else self.pixellated_rect.w != self.VT.w) if (('_type[self.pixellated_rect]'.vertices < 1 if '_type[self.pixellated_rect]'.vertices < 1 else _parallax != self.pixellated_rect.parallax) if ('_type[self.pixellated_rect]'.vertices < 1 if '_type[self.pixellated_rect]'.vertices < 1 else _parallax != self.pixellated_rect.parallax) else self.pixellated_rect.w != self.VT.w) else self.pixellated_rect.h != self.VT.h) else self.pixellated_rect.sw != self.shadow_parrallax.x) else self.pixellated_rect.sh != self.shadow_parrallax.y) else self.pixellated_rect.progress != (_progress if _progress else 1)):
            self.pixellated_rect = {'w': self.VT.w, 'h': self.VT.h, 'sw': self.shadow_parrallax.x, 'sh': self.shadow_parrallax.y, 'progress': _progress if _progress else 1, 'fill': {'vertices': {}}, 'shadow': {'vertices': {}}, 'line': {'vertices': {}}, 'emboss': {'vertices': {}}, 'line_emboss': {'vertices': {}}, 'parallax': _parallax}
            ext_up = self.config.ext_up & self.config.ext_up * G.TILESIZE if self.config.ext_up & self.config.ext_up * G.TILESIZE else 0
            res = ((self.config.res if self.config.res else (math.min() > 3.5) & 0.8) if (self.config.res if self.config.res else (math.min() > 3.5) & 0.8) else (math.min() > 0.3) & 0.6) if ((self.config.res if self.config.res else (math.min() > 3.5) & 0.8) if (self.config.res if self.config.res else (math.min() > 3.5) & 0.8) else (math.min() > 0.3) & 0.6) else 0.15
            totw = toth = subw = subh = (self.VT.w * G.TILESIZE, (self.VT.h + math.abs(ext_up) / G.TILESIZE) * G.TILESIZE, self.VT.w * G.TILESIZE - 4 * res, (self.VT.h + math.abs(ext_up) / G.TILESIZE) * G.TILESIZE - 4 * res)
            vertices = {1: subw / 2, 2: subh / 2 - ext_up, 3: 0, 4: 4 * res - ext_up, 5: 1 * res, 6: 4 * res - ext_up, 7: 1 * res, 8: 2 * res - ext_up, 9: 2 * res, 10: 2 * res - ext_up, 11: 2 * res, 12: 1 * res - ext_up, 13: 4 * res, 14: 1 * res - ext_up, 15: 4 * res, 16: 0 * res - ext_up, 17: subw, 18: 0 * res - ext_up, 19: subw, 20: 1 * res - ext_up, 21: subw + 2 * res, 22: 1 * res - ext_up, 23: subw + 2 * res, 24: 2 * res - ext_up, 25: subw + 3 * res, 26: 2 * res - ext_up, 27: subw + 3 * res, 28: 4 * res - ext_up, 29: totw, 30: 4 * res - ext_up, 31: totw, 32: subh - ext_up, 33: subw + 3 * res, 34: subh - ext_up, 35: subw + 3 * res, 36: subh + 2 * res - ext_up, 37: subw + 2 * res, 38: subh + 2 * res - ext_up, 39: subw + 2 * res, 40: subh + 3 * res - ext_up, 41: subw, 42: subh + 3 * res - ext_up, 43: subw, 44: toth - ext_up, 45: 4 * res, 46: toth - ext_up, 47: 4 * res, 48: subh + 3 * res - ext_up, 49: 2 * res, 50: subh + 3 * res - ext_up, 51: 2 * res, 52: subh + 2 * res - ext_up, 53: 1 * res, 54: subh + 2 * res - ext_up, 55: 1 * res, 56: subh - ext_up, 57: 0, 58: subh - ext_up, 59: 0, 60: 4 * res - ext_up}
            for kv in ipairs(vertices):
                if ((k % 2) == 1) & (v > totw * self.pixellated_rect.progress):
                    v = totw * self.pixellated_rect.progress
                'k[self.pixellated_rect.fill.vertices]' = v
                if k > 4:
                    'k - 4[self.pixellated_rect.line.vertices]' = v
                    if _emboss:
                        'k - 4[self.pixellated_rect.line_emboss.vertices]' = v + (((k % 2) == 0) & -_emboss * self.shadow_parrallax.y if ((k % 2) == 0) & -_emboss * self.shadow_parrallax.y else -0.7 * _emboss * self.shadow_parrallax.x)
                if (k % 2) == 0:
                    'k[self.pixellated_rect.shadow.vertices]' = v - self.shadow_parrallax.y * _parallax
                    if _emboss:
                        'k[self.pixellated_rect.emboss.vertices]' = v + _emboss * G.TILESIZE
                else:
                    'k[self.pixellated_rect.shadow.vertices]' = v - self.shadow_parrallax.x * _parallax
                    if _emboss:
                        'k[self.pixellated_rect.emboss.vertices]' = vlove.graphics.polygon()

    def update(self, dt):
        G.ARGS.FUNC_TRACKER = G.ARGS.FUNC_TRACKER if G.ARGS.FUNC_TRACKER else {}
        if self.config.button_delay:
            self.config.button_temp = self.config.button if self.config.button else self.config.button_temp
            self.config.button = 'None'
            self.config.button_delay_progress = (G.TIMERS.REAL - self.config.button_delay_start) / self.config.button_delay
            if G.TIMERS.REAL >= self.config.button_delay_end:
                self.config.button_delay = 'None'
        if self.config.button_temp & (not self.config.button_delay):
            self.config.button = self.config.button_temp
        if self.button_clicked:
            self.button_clicked = 'None'
        if self.config & self.config.func:
            'self.config.func[G.ARGS.FUNC_TRACKER]' = ('self.config.func[G.ARGS.FUNC_TRACKER]' if 'self.config.func[G.ARGS.FUNC_TRACKER]' else 0) + 1'self.config.func[G.FUNCS]'(self)
        if self.UIT == G.UIT.T:self.update_text()
        if self.UIT == G.UIT.O:self.update_object()Node.update(self, dt)

    def collides_with_point(self, cursor_trans):
        if self.UIBox.states.collide.can:
            return Node.collides_with_point(self, cursor_trans)
        else:
            return False

    def click(self):
        if self.config.button & (not self.last_clicked if not self.last_clicked else self.last_clicked + 0.1 < G.TIMERS.REAL) & self.states.visible & (not self.under_overlay) & (not self.disable_button):
            if self.config.one_press:
                self.disable_button = True
            self.last_clicked = G.TIMERS.REAL
            if self.config.id == 'overlay_menu_back_button':G.CONTROLLER.mod_cursor_context_layer()
                G.NO_MOD_CURSOR_STACK = True
            if G.OVERLAY_TUTORIAL & (G.OVERLAY_TUTORIAL.button_listen == self.config.button):G.FUNCS.tut_next()'self.config.button[G.FUNCS]'(self)
            G.NO_MOD_CURSOR_STACK = 'None'
            if self.config.choice:
                choices = self.UIBox.get_group(None)
                for kv in pairs(choices):
                    if v.config & v.config.choice:
                        v.config.chosen = False
                self.config.chosen = Trueplay_sound(button, 1, 0.3)
            G.ROOM.jiggle = G.ROOM.jiggle + 0.5
            self.button_clicked = True
        if self.config.button_UIE:self.config.button_UIE.click()

    def put_focused_cursor(self):
        if self.config.focus_args & (self.config.focus_args.type == 'tab'):
            for kv in pairs():
                if '1[v.children]'.config.chosen:
                    return '1[v.children]'.put_focused_cursor()
        else:
            return Node.put_focused_cursor(self)

    def remove(self):
        if self.config & self.config.object:self.config.object.remove()
            self.config.object = 'None'
        if self == G.CONTROLLER.text_input_hook:
            G.CONTROLLER.text_input_hook = 'None'remove_all()
        super().remove(self)

    def hover(self):
        if self.config & self.config.on_demand_tooltip:
            self.config.h_popup = create_popup_UIBox_tooltip()
            self.config.h_popup_config = {'align': (self.T.y > G.ROOM.T.h / 2) & 'tm' if (self.T.y > G.ROOM.T.h / 2) & 'tm' else 'bm', 'offset': {'x': 0, 'y': (self.T.y > G.ROOM.T.h / 2) & -0.1 if (self.T.y > G.ROOM.T.h / 2) & -0.1 else 0.1}, 'parent': self}
        if self.config.tooltip:
            self.config.h_popup = create_popup_UIBox_tooltip()
            self.config.h_popup_config = {'align': 'tm', 'offset': {'x': 0, 'y': -0.1}, 'parent': self}
        if self.config.detailed_tooltip & G.CONTROLLER.HID.pointer:
            self.config.h_popup = create_UIBox_detailed_tooltip()
            self.config.h_popup_config = {'align': 'tm', 'offset': {'x': 0, 'y': -0.1}, 'parent': self}Node.hover(self)

    def stop_hover(self):Node.stop_hover(self)
        if self.config & self.config.on_demand_tooltip:
            self.config.h_popup = 'None'

    def release(self, other):
        if self.parent:self.parent.release(other)
def is_UI_containter(node):
    if (node.UIT != G.UIT.C) & (node.UIT != G.UIT.R) & (node.UIT != G.UIT.ROOT):
        return False
    return True