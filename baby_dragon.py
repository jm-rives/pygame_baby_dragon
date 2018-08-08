#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7
# -*- coding: utf-8 -*-
import os, pygame
from pygame.locals import *

def load_image(name, colorkey=None):
    try:
        image = pygame.image.load(name)
    except pygame.error:
        print("Whoops! I'm unable to load: ", name, " sorry about that")

    image = image.convert()

    return image, image.get_rect()


# Parent Class
class Dragon(pygame.sprite.Sprite):

    def __init__(self, name, snuggled,
        sleep, hunger, cloaca, fire, energy, maturity):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.snuggled = snuggled
        self.sleep = sleep
        self.hunger = hunger
        self.cloaca = cloaca
        self.fire = fire
        self.energy = energy
        self.maturity = maturity
        # pygame instance attributes.
        self.image, self.rect = load_image('baby_dragon_by_kaitlynclinkscales-d55vsza.jpg', -1)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.STEP = 9
        self.MARGIN = 12
        self.xstep = self.STEP
        self.ystep = 0
        self.degrees = 0
        self.direction = 'right'

def main():
    pygame.init()
    screen = pygame.display.set_mode((700, 700))
    pygame.display.set_caption("Baby Dragon Display")

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((66, 244, 241))

    if pygame.font:
        font = pygame.font.Font(None, 36)
        text = font.render("Look at the cute BABBY DRAGON!!!!!", 1, (0, 0, 200))
        textpos = text.get_rect(centerx = background.get_width()/2, centery = background.get_height()/2)

    screen.blit(background, (0, 0))
    pygame.display.flip()

    clock = pygame.time.Clock()
    dragon = Dragon('Timmy', 5, 5, 0, 0, 0, 5, 5)
    sprite = pygame.sprite.RenderPlain(dragon)

    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT:
                return

        sprite.update()

        screen.blit(background, (0, 0))
        sprite.draw(screen)
        pygame.display.flip()


if __name__ == '__main__':
    main()
