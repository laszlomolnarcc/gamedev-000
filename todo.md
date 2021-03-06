# TODO
# Important
## * when I say print error/warning/trace msg, I mean to use the Logger class! *

## ccLogger
- when I say print error/warning/trace msg, I mean to use the Logger class!
- a simple logger class. First it calls print() and than also logs to file
- static class because it's needed everywhere

    ### Skeleton
        class ccLogger:
            filename = "" #"logs/sci-fi_game_" + a timestamp from the time module + ".log", so the filename will be different every time we start the game
            def __init__(self):
                #raise an exception (I know we usually don't raise execptions in init but this is an exceptional case :) and also print an error msg to Terminal
                pass
            @classmethod
            def error(cls, *args):
                #call print() but start with a timestamp and !E! and put the msg after. Also open the file and write the same line into it. An error msg would be something like this:
                #2017.02.25.19:23:00 !E! Texture not found: flying saucer.png
                pass
            @classmethod
            def warning(cls, *args):
                #same as error but with !W!
                pass
            @classmethod
            def trace(cls, *args):
                #same as error but with !T! and don't print it out, only write it to the file!
                pass


## ccFileLoader
- ccFileLoader class to parse JSON files. It is needed to decorate the JSON loader so we can use another format if we need to. Pick a JSON loader module what can parse JSON files, a simple one will do
- abstract class

    ### Skeleton:
        class ccFileLoader:
            def __init__(self):
                # init. Use it if you need it
                self.current_section=""
                pass
            def process_file(self, filename):
                #raise an exception that this is an abstract class
                pass
            def __load_file(self, filename):
                #make the json loading here and set an instance variable what will hold the json reader and can be accessed from now on
                pass
            def get_section(self, section_name, mandatory=True):
                #give back the named section. If it doesn't exists, send back None and if mandatory is True, print an error msg. If the file is not loaded, print out an error msg and send back None
                pass
            def get_field(self, field_name, mandatory=True, section_name=current_section):
                #give back the field data. If it doesn't exists, send back None and if mandatory is True, print an error msg. If the file is not loaded, print out an error msg and send back None. section_name is optional, set the current_section if not given. If current_section is invalid, write an error msg and send back None
                pass
            def set_section(self, section_name):
                #set self.current_section to the section_name. print error if it doesn't exists, or file is not loaded.
                pass
            def set_first_section(self):
                #set self.current_section to the first section in the file. print error if no file loaded or file doesn't have a single section
                pass
            def next_section(self):
                #if self.current_section is set, set the next section. Return true if there is a next section and False if there is no next section. print error msg if self.current_section is not set and return False
                pass
      
## ccSpritesFileLoader
- processes the sprites files and puts the instanced ccSprites to the ccSpriteManager
- inherits from ccFileLoader
- check the game\resources\sprites\test.sprites.json file to see how it's looking like

    ### Skeleton
        class ccSpritesFileLoader(ccFileLoader):
            def __init__(self):
                pass
            def process_file(self, filename):
                #load the file with the json reader(use load_file() from ancestor). 
                #If error happens, abort loading and print error msg.
                #If a sprites file was loaded before, release that file and initialize
                #before loading the new file. Go through all the sections. 
        #First process the 'Config' section, and process the sprites after Config was processed. 
        #Make as much private methods as you like and don't violate the single responsibility principle. 
        #In the Config section, read the name of the image file and add it to SpriteManager as a ccTexture 
        #(use the filename as the texture name when adding). 
        #Store the filename and when creating the sprites, use it to get the texture from SpriteManager
                pass
        #if there is a "num_of_sprites" field, it means you have to load more than one sprite, starting from
        #the offset_x, offset_y, using the provided width,height for all of them. Handle the case, when you reach the
        #width of the texture! Continue with the next row in this case.

## ccTexture
- load the image file from disk and store it in a pygame Surface type

    ### Skeleton
        class ccTexture:
            def __init__(self):
                pass
            def load_image(self, file_name):
                #load the image as a pygame.Surface and store it
                pass
            def get_witdh(self):
                #give back loaded texture's width. print error if no texture is loaded and give back 0
                pass
            def get_height(self):
                #give back loaded texture's height. print error if no texture is loaded and give back 0
                pass
            def get_texture(self):
                #give back the texture stored. If no texture, give back None and print error msg

## ccSprite
- a sprite renders a quad from a ccTexture to screen when called

    ### Skeleton
        class ccSprite:
            def __init__(self, texture, rectangle):
                #needs an instance variable what stores the width, height and x,y offset. Probably a pygame.Rect type. Store the texture parameter also in an instance variable
                pass

      def draw(self, renderer, x, y):
                #draw the sprite to screen with pygame. Draw only the sprite from the texture to x,y position. Use the renderer, that's the pygame object
                pass

## ccObjectProps
- settings for objects: object visible, object enabled
- a simple class with some enums or bitfields or something what handles on/off values efficiently

## ccObject
- very basic object type abstract class. Has type variable, id, object properties, sprite
- it's abstract because we will make a special object class for tiles and this class will be it's ancestor (and this class is the ancestor of other types of objects also)

    ### Skeleton
        class ccObject:
            def __init__(self):
                # initialize instance variables
                self.type = 'ccObjectBase' #not sure this will be needed because python has type() function
                self.idTag = 0
                self.active_sprite = None
                self.object_props = ccObjectProps()
            def load(self, obj_file_loader):
                #receives a ccObjectsFileLoader what already has the file which contains the info for this object and it's current_section is set to this object. Loads all the data from it EXCEPT the active_sprite. Check out test.objects.json for the fields.
            def draw(self):
                # raise an exception that this is an abstract class
    
## ccBasicObject
- inherits from ccObject, loads the sprite and has drawing method, not abstract
- has position variable

    ### Skeleton
        class ccBasicObject(ccObject):
            def __init__(self):
                #call the ancestor's __init__()
                self.type = "ccBasicObject" #probably should use python's type(), so set that up with magic method(?)
                self.position = pygame.math.Vector2(0,0) #use Vector2. It should be able to store float values
                self.velocity = pygame.math.Vector2(0,0)
            def load(self, obj_file_loader):
                #call ancestor's load() method and get the sprite from SpriteManager. If sprite is not found, print error and set active_sprite to None
                pass
            def draw(self):
                #draw the active_sprite to the screen, to self.position position
                pass
            def step(self, time_passed):
                #change Object's position with velocity. Specialized object classes will override this method and do other logic here also
                pass

## ccSpriteManager
- handles all the loaded sprites and textures. Keeps dictionary where the key is the name of the sprite and the value is the ccSprite. Should have a getter what gives back a pointer to a sprite (no copying)
- this class is static, won't be instantiated because we need it all the time while we are running our program
*** make a separate dictionary what contains ccAnimSprites. Make an add and a get method for this, based on the same principles as the originals

    ### Skeleton
        class ccSpriteManager:
            textures = {}
            sprites = {}
            def __init__(self):
                #raise an exception (I know we usually don't raise execptions in init but this is an exceptional case :) and also print an error msg
                pass
            @classmethod
            def add_texture(cls, texture_name, texture):
                #add the ccTexture to the textures dictionary, but only if it's not already there (texture_name is the key). If it is there, don't add and print a warning msg that says that we wanted to load it twice
                pass
            @classmethod
            def get_texture(cls, texture_name):
                #give back the ccTexture. If it can't be found, write an error msg and return with None
                pass
            @classmethod
            def add_sprite(cls, sprite_name, sprite):
                #add ccSprite to sprites dictionary but only if it is not there (sprite_name is the key). If it is there, print a warning msg and don't overwrite the previous one
                pass
            @classmethod
            def get_sprite(cls, sprite_name):
                #give back the ccSprite. If it can't be found, write an error msg and return with None
                pass
            @classmethod
            def add_anim_sprite(cls, sprite_name, sprite):
                #add ccAnimSprite to anim_sprites dictionary but only if it is not there (sprite_name is the key). If it is there, print a warning msg and don't overwrite the previous one
                pass
            @classmethod
            def get_anim_sprite(cls, sprite_name):
                #give back the ccAnimSprite. If it can't be found, write an error msg and return with None
                pass

## ccObjectsFileLoader
- inherits from ccFileLoader
- processes xx.objects.json files and fills ObjectManager with the created objects
- works with every type of Object what have now and will create later
- how to instantiate a class when you have it's name as a string (you should import all the classes you want to instantiate this way):
    class_string_name = "ccBasicObject"
    constructor = globals()[class_string_name]
    class_instance = constructor() ## same as class_instance = ccBasicObject()
- check the game\resources\objects\test.objects.json file to see how it's looking like
- in the 'Config' section, it should load all the sprites files (create ccSpritesFileLoader and load the file)
!!! works with xx.anims.json files what are also in the Config/filenames field. Instantiates ccAnimsFileLoader for loading

    ### Skeleton
        class ccObjectsFileLoader(ccFileLoader):
            def __init__(self):
                pass
            def process_file(self, filename):
                #load the file with the json reader(use load_file() from ancestor). 
                #If error happens, abort loading and print error msg.
                #If an objects file was loaded before, release that file and initialize before loading the new file.
                #Go through all the sections. 
                #First process the 'Config' section, and process the sprites after Config was processed. 
                #Make as much private methods as you like and don't violate the single responsibility principle. 
                #In the Config section, read the list of sprites.json files and create ccSpritesFileLoader instances and load the files. Something like this is what you need:
                  loader = ccSpritesFileLoader()
                  loader.process_file(sprites_json_file_name)
                #always check if the file is xx.sprites.json or not! There will be xx.anims.json file and it also have to be loaded when it's ready but with a different loader
                #when you are at the objects: Read the "type" field first and instantiate the object (check this class' starter comments for help how to do it).
                #after you have the object, don't fill it yourself! Give the self.current_dict[self.current_section] to the object's load() method and it will load itself. Something like this:
                  obj.load(self.current_dict[self.current_section])
                  where self.current_section is the current object's section's name as a string (you have to update self.current_section)
                #when everything is read, put it to ccObjectManager (call it's add method, find the exact name in that part of the todo)
                oass
  
## ccObjectManager
- stores object types and instantiates when needed  

  ### Skeleton
    class ccObjectManager:
      objects = {}
      def __init__(self):
        #raise an exception (I know we usually don't raise execptions in init but this is an exceptional case :) and also print an error msg
                pass
      @classmethod
      def add_object(cls, object_name, obj):
        #add the object into the objects dictionary. If it is there, print a warning msg and don't overwrite the previous one
        pass
      @classmethod
      def create_object(cls, object_name):
        #find and make a copy of the object and give back the copy (check out the copy.deepcopy in python and investigat if we can use it). If it can't be found, write an error msg and return with None
      
## ccResourcePaths
- this class helps in finding resources, so we don't have to wire in the paths everywhere
  ### Skeleton
    class ccResourcePaths:
      base_path = os.path.dirname(os.path.realpath(__file__))
      def __init__(self):
        #raise an exception (I know we usually don't raise execptions in init but this is an exceptional case :) and also print an error msg
                pass
      @classmethod
      def get_resources(cls):
        #it should be the /resources directory. Use the base_path and put the /resources/ after it. Be careful with the '/'-s. Don't give back things like this: C:/gamedir//resources/
        pass
      @classmethod
      def get_objects(cls):
        #it should be the /resources/objects directory. Use the base_path and put the /resources/objects/ after it. Be careful with the '/'-s. Don't give back things like this: C:/gamedir//resources/
        pass
      @classmethod
      def get_sprites(cls):
        #it should be the /resources/sprites directory. Use the base_path and put the /resources/sprites/ after it. Be careful with the '/'-s. Don't give back things like this: C:/gamedir//resources/
        pass
        
## ccAnimSprite
- a sprite class what contains more than one sprite and animation info about the playing of the anim
  ### Skeleton
    class ccAnimSprite:
      def __init__(self):
        #create an empty anim_frames list (ccAnimFrame)
        pass
      def add_frame(self, frame):
        # adds a ccAnimFrame to anim_frames list. Error if already exists
        pass
      def get_frame(self, frame_number):
        # gets a ccAnimFrame from anim_frames based on it's position in the list. Error and None if not found
        pass
        
## ccAnimFrame
- has a ccSprite what should be displayed, a time while the frame should be displayed and the next anim frame number
  ### Skeleton
    class ccAnimFrame:
      def __init__(self, sprite, time, next_frame):
        # self. sprite, time, next_frame
        pass
      def get_time(self):
        # self.time
        pass
      def get_sprite(self):
        # guess what
        pass
      def get_next_frame(self):
        # self.next_frame
        pass
        
## ccAnimObject
- animated object. Has at least one ccAnimSprite, handles the loading as other Object types and makes the animation running
- the anim
  ### Skeleton
    class ccAnimObject(ccBasicObject):
      def __init__(self):
          #call the ancestor's __init__()
          #sets the object type to ccAnimObject
          #and inits everything what's needed to default
          #NO loading happens here
          #anims list should contain the loaded ccAnimSprites
          #story the current animation/frame in variable(s) so you will know where are you currently and can step to the next frame/anim
          pass
      def load(self, obj_file_loader):
          #call ancestor's load() method and get the sprite from SpriteManager
          #print error if something bad happens
          #load the data. All the anim should already be in SpriteManager so get it from there!
          #check the last object in test.objects.json file
          pass
      def add_anim(self, anim):
          #add an animation to anims list. anim should be ccAnimSprite
          pass
      def draw(self):
          #this is not needed, it can use the ancestor's draw method
          pass
      def step(self, time_passed):
          #use the ancestor's step to do moving
          #handle the anim changing. The incoming time_passed has the passed millisecs since last frame. Use it to move forward in animation
          #if the displayed sprite should be changed, set the active_sprite with the currently active ccAnimSprite's sprite. active_sprite should always point to a ccSprite object, otherwise the program will crash
          pass
      def play(self, anim_name=current_anim):
          #set and start playing an anim. anim_name is optional, it should play the current animation if the anim_name is not set
          #if an anim was paused, resume from that point where is was
          pass
      def pause(self):
          #pause the current animation
          pass
      def reset(self):
          #don't change the animation but reset it to start
          #pause the animation
          pass

## ccAnimsFileLoader
- loads xx.anims.json files
- Config/filename contains only one sprites.json file
Example:
  "anim_00": { <-- name of the ccAnimSprite what should be pushed with to ccSpriteManager
    "sprites": ["test_00", <-- sprite name, loaded from ccSpriteManager, pushed to the ccAnimSprite's frame list
                "test_01",
                "test_02",
                "test_03",
                "test_04"
               ],
    "frames": ["0 t10", <-- 1st frame, info for one frame in ccAnimSprite, 0 means "test_00" ccSprite this time
               "1", <-- 2nd frame
               "2 t30",
               "3",
               "4",
               "goto 1" <-- the next frame is the second frame ("1")
              ]
  },
- the class' structure is the same as the other loaders. It's ancestor is ccFileLoader and should use that class' methods
- should process the config first and all the anims after that

## ccGlobals
- this name is temporary (or not if we can't find a better one)
- currently this will contain a pointer to the pygame renderer
- !!! when this class is ready, remove the renderer parameter from everywhere and use the one provided here
  ### Skeleton
    class ccGlobals:
      renderer = None
      
      @staticmethod
      def set_renderer(renderer):
        #set the renderer. Incoming param is what pygame provided
        pass
      @staticmethod
      def get_renderer():
        #get the self.renderer
        pass

## ccSceneProps
- scene properties
- check ccObjectProps for similarities and make an ancestor class for both (ccProps) if needed
  ### Skeleton
    class ccSceneProps:
      def _init__(self):
        # store if scene enabled, visible, set both to true here
        pass
      def set_enabled(self, enabled):
        # set enabled
        pass
      def set_visible(self, visible):
        # set visible
        pass
      def get_enabled(self):
        # return with enabled variable
        pass
      def get_visible(self):
        # return with visible variable
        pass

## ccScene
- basic scene type. A scene has objects which it can display and logic can be implemented here
- the ccActManager will handle all the created scenes and display them in a specified order
- everything is displayed through scenes and scene logic handles most of the input coming from the user
- there are several scene types, ccScene is the most basic
- ccScene is an abstract class
  ### skeleton
    class ccScene:
      def __init__(self):
        #create a type, name scene_props variable
        #scene_props should be ccSceneProps
        #type should be 'ccScene'
        #name should be ''. It will be used for identification later, when needed
        #no, there is no need for objects list right now
        pass
      def load(self, filename):
        #this will load the scene, currently it should just raise an exception
        pass
      def draw(self):
        #raise an exception. This will draw the objects to screen in the child classes 
        pass
      def step(self, time_passed):
        #raise an exception. This will contain the scene logic in child classes
        pass
#####
        def __process_config(self, config):
        #config is the config section of the JSON dict. 
        #fill the variables from it what are present in this class
        pass
#####

## ccObjectScene
- a specialized scene type. It holds a list of objects
- objects gets rendered to screen and logic is handled here
  ### Skeleton
    class ccObjectScene:
      def __init__(self):
        #call ancecstor's init
        #create self.objects list, it should be empty now
        #fill type field with ccObjectScene
        pass
      def load(self, filename):
        #this will load the scene. There will be a ccObjectSceneFileLoader for this type of scene
        #it is different from the previous load methods (like ccSprite) because you should instantiate ccObjectSceneFileLoader here and do the loading
        #This difference is because we have only one ObjectScene in a file and no more so it's more logical to handle the whole loading here
        #ccObjectSceneFileLoader will have getter methods, you can get the objects, scene props and anything you need from it
######        
        #__process_config() can be used here (it's in ccScene) to load common attributes
######        
       
        pass
        
      def draw(self):
        #go through the objects list and call every object's draw method
        pass
      def step(self, time_passed):
        #call all the object's step method with time_passed

## ccObjectSceneFileLoader
- loads the whole ccObjectScene
- check out resources/object_scenes/test.objectscene.json the structure
- as usual there can be a lot of private support methods what are not written down in this document
  ### Skeleton
    class ccObjectSceneFileLoader(ccFileLoader):
      def __init__(self):
        #call the ancestor's init
        #create objects list
        pass
      def process_file(self, filename):
        #handle the whole file (write __process_config and as much methods as you feel is needed)
        #don't forget to process the files first written in the Config section
        #store the infos present in the file (process the config part, instantiate objects with ccObjectManager, store scene name etc)
        pass
      def get_objects(self):
        #return with the objects list. If it is empty, log a warning also
        pass
      def get_scene_name(self):
        #gets the scene's name

## ccActManager
- handles all the loaded scenes and call it's draw, step.. methods
  ### Skeleton
    class ccActManager:
      scenes = []
      def __init__(self):
        #raise an exception (I know we usually don't raise execptions in init but this is an exceptional case :) and also print an error msg
        pass
      @classmethod
      def load(cls, filename):
        #creates a ccActFileLoader instance and processes the act file, makes the scenes
        #if something was loaded, removes it and initializes before loading
        pass
      @classmethod
      def draw(cls):
        #loops through all the scenes and calls it's draw method
        pass
      @classmethod
      def step(cls):
        #loops through all the scenes and calls it's step method
        pass
      @classmethod
      def push_scene(cls, scene):
        #appends the incoming scene to the end of the scenes list
        pass
      @classmethod
      def pop_scene(cls):
        #removes the last scene from the scenes list
        pass
