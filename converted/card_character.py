class Card_Character(Moveable):

    def __init__(self, args):
        super().__init__(self)
        self.states.collide.can = False
        self.children = {}
        self.config = {'args': args}
        self.children.card = Card()
        self.children.card.states.visible = Falseself.children.card.start_materialize()self.children.card.set_alignment()
        self.children.card.jimbo = self
        self.children.card.states.collide.can = True
        self.children.card.states.focus.can = False
        self.children.card.states.hover.can = True
        self.children.card.states.drag.can = False
        self.children.card.hover = Node.hover
        self.children.particles = Particles(0, 0, 0, 0)
        self.children.particles.static_rotation = Trueself.children.particles.set_role()
        if getmetatable(self) == Card_Character:table.insert()

    def move(self, dt):
        super().move(self, dt)

    def hard_set_VT(self):self.align_to_major()
        super().hard_set_VT(self)self.align()self.children.card.hard_set_VT()

    def align(self):
        if self.children.card:
            self.children.card.T.x = self.T.x + (self.T.w - self.children.card.T.w) / 2
            self.children.card.T.y = self.T.y + (self.T.h - self.children.card.T.h) / 2

    def add_button(self, button, func, colour, update_func, snap_to, yoff):
        if self.children.button:self.children.button.remove()
        self.config.button_align = {'align': 'bm', 'offset': {'x': 0, 'y': yoff if yoff else 0.3}, 'major': self, 'parent': self}
        self.children.button = UIBox()
        if snap_to:G.CONTROLLER.snap_to()

    def add_speech_bubble(self, text_key, align, loc_vars):
        if self.children.speech_bubble:self.children.speech_bubble.remove()
        self.config.speech_bubble_align = {'align': align if align else 'bm', 'offset': {'x': 0, 'y': 0}, 'parent': self}
        self.children.speech_bubble = UIBox()self.children.speech_bubble.set_role()
        self.children.speech_bubble.states.visible = False

    def remove_button(self):
        if self.children.button:self.children.button.remove()';'
            self.children.button = 'None'

    def remove_speech_bubble(self):
        if self.children.speech_bubble:self.children.speech_bubble.remove()';'
            self.children.speech_bubble = 'None'

    def say_stuff(self, n, not_first):
        self.talking = True
        if not not_first:G.E_MANAGER.add_event()
        else:
            if n <= 0:
                self.talking = False';'
                return False
            new_said = math.random(1, 11)
            while new_said == self.last_said:
                new_said = math.random(1, 11)
            else:
            self.last_said = new_saidplay_sound()self.children.card.juice_up()G.E_MANAGER.add_event()

    def draw(self, dt):
        if self.highlight:self.children.highlight.draw()self.highlight.draw()
            if self.highlight.draw_children:self.highlight.draw_children()
        if self.children.particles:self.children.particles.draw()
        if self.children.speech_bubble:self.children.speech_bubble.draw()
        if self.children.button & (not self.talking):self.children.button.draw()
        if self.children.card:self.children.card.draw()add_to_drawhash(self)self.draw_boundingrect()

    def remove(self):
        G.jimboed = 'None'remove_all()
        for kv in pairs():
            if v == self:table.remove()
        super().remove(self)