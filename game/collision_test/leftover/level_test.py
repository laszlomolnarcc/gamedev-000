import pygame
import sys
import os

white = (255, 255, 255)
black = (0,   0,   0)


# Player class
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join('blue.png'))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 300


class Rock(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join('green.png'))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 440

# essential pygame init
pygame.init()

# screen
screen_width = 800
screen_height = 600
screen_size = (screen_width, screen_height)
screen = pygame.display.set_mode(screen_size)

# List for all sprites
sprites = pygame.sprite.Group()
rocks = pygame.sprite.Group()


for x in range(0, 800, 40):
    rock = Rock()
    rock.rect.x = x
    rocks.add(rock)
    sprites.add(rock)

# Create player
player = Player()
sprites.add(player)

done = False

clock = pygame.time.Clock()
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            sys.exit()

    sprites.update()

    pressed = pygame.key.get_pressed()
    if pygame.sprite.spritecollide(player, rocks, False):
        player.rect.move_ip(0, 0)
    if pressed[pygame.K_LEFT]:
        move = (-5, 0)
        player.rect = player.rect.move(move)
        if pygame.sprite.spritecollide(player, rocks, False):
            player.rect.move_ip(5, 0)
    if pressed[pygame.K_RIGHT]:
        move = (5, 0)
        player.rect = player.rect.move(move)
        if pygame.sprite.spritecollide(player, rocks, False):
            player.rect.move_ip(-5, 0)
    if pressed[pygame.K_UP]:
        move = (0, -5)
        player.rect = player.rect.move(move)
        if pygame.sprite.spritecollide(player, rocks, False):
            player.rect.move_ip(0, 5)
    if pressed[pygame.K_DOWN]:
        move = (0, 5)
        player.rect = player.rect.move(move)
        if pygame.sprite.spritecollide(player, rocks, False):
            player.rect.move_ip(0, -5)

    screen.fill(white)

    sprites.draw(screen)

    pygame.display.flip()

    clock.tick(30)

pygame.quit()
