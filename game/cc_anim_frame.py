from cc_sprites_file_loader import *
from cc_resource_paths import *


class ccAnimFrame:

    def __init__(self, sprite, time, next_frame):
        self.sprite = sprite
        self.time = time
        self.next_frame = next_frame

    def get_time(self):
        return self.time

    def get_sprite(self):
        return self.sprite

    def get_next_frame(self):
        return self.next_frame

#sprite = ccSpritesFileLoader.process_file(ccResourcePaths.get_sprites() + sprites.json")
