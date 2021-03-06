from cc_file_loader import *
from cc_logger import *
from cc_sprite_manager import *
from cc_texture import *
from cc_sprite import *
from cc_anim_sprite import *
from cc_anim_frame import *
from cc_sprites_file_loader import *
from cc_resource_paths import *
from cc_sound_file_loader import ccSoundFileLoader
from cc_sound_manager import ccSoundManager


class ccAnimsFileLoader(ccFileLoader):

    def __init__(self):
        pass

    def process_file(self, filename):
        try:
            self.load_file(ccResourcePaths.get_anims() + filename)
        except:
            ccLogger.error(filename + ' could not be loaded.')
            raise RuntimeError(filename + ' could not be loaded.')
        self.__config()
        self.__process_all_anims_sprites()

    def __config(self):

        self.set_section("Config")
        file_name = self.get_field("filename")

        loader = ccSpritesFileLoader()
        loader.process_file(file_name)

        file_name = self.get_field("sound_filename")

        loader =ccSoundFileLoader()
        loader.process_file(file_name)

    def __process_all_anims_sprites(self):

        self.set_first_section()
        while self.next_section():
            self.__process_one_anims_sprite()

    def __process_one_anims_sprite(self):
        sprites = self.get_field("sprites")
        for i in range(len(sprites)):
            sprites[i] = ccSpriteManager.get_sprite(sprites[i])

        frames = self.get_field("frames")
        frame_list = []

        for i in range(len(frames)):
            splitted_frame = frames[i].split()
            frame_list.append(splitted_frame)

        for i in range(len(frame_list)):
            if frame_list[i][0] != 'goto': #need to be checked
                if len(frame_list[i]) == 1:
                    frame_list[i].append(frame_list[i - 1][1])
                if frame_list[i+1][0] != 'goto':
                    frame_list[i].append(str(i+1))
                else:
                    frame_list[i].append(frame_list[i+1][1])
            else:
                frame_list.remove(frame_list[i])

        frames = frame_list
        anim_sprite = ccAnimSprite()

        for i in range(len(frames)):
            sprite = sprites[int(frames[i][0])]
            time = int(frames[i][1][1:])
            next_frame = int(frames[i][2])
            anim_frame = ccAnimFrame(sprite, time, next_frame)
            anim_sprite.add_frame(anim_frame)


        sound_name = self.get_field("sound")
        sound = ccSoundManager.get_sound(sound_name)
        if sound is None:
            ccLogger.error(sound_name + 'could not be loaded')
        else:
            anim_sprite.add_sound(sound)
        ccSpriteManager.add_sprite(self.get_current_section_name(), anim_sprite)

