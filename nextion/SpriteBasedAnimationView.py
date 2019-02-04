import string

import serial

from nextion.NextionView import NextionView


class SpriteBasedAnimationView(NextionView):

    def __init__(self, conn:serial.Serial, name: string, sprite_indices: [], disabled_sprite: int):
        NextionView.__init__(self, conn=conn)
        self.enabled = True
        self.disabled_sprite = disabled_sprite
        self.sprite_indices = sprite_indices
        self.name = name
        self.sprite_index = 0
        self.sprite_offset = 0
        self.set_sprite(self.sprite_indices[self.sprite_index])
        self.set_callback(lambda: (True, 0))

    def set_sprite(self, index):
        self.send_command("%s.pic=%d" % (self.name, index + self.sprite_offset))

    def set_value(self, value):
        if not self.enabled:
            return
        self.sprite_index = (self.sprite_index + 1) % len(self.sprite_indices)
        self.set_sprite(self.sprite_indices[self.sprite_index])

    def disable(self):
        self.enabled = False
        self.send_command("vis %s,0" % self.name)
        # self.set_sprite(self.disabled_sprite)
        self.sprite_index = 0

    def enable(self):
        self.enabled = True
        self.sprite_index = 0
        self.send_command("vis %s,1" % self.name)
        self.set_sprite(self.sprite_indices[self.sprite_index])

    def set_offset(self, offset):
        self.sprite_offset = offset

