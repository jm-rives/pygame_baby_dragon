#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7
# -*- coding: utf-8 -*-
import os, pygame
from pygame.locals import *
# Parent Class
class Dragon:
    def __init__(self, Sprite, name, snuggled,
     sleep, hunger, cloaca,
      fire, energy, maturity
      ):
        Sprite.__init__(self)
        self.name = name
        self.snuggled = snuggled
        self.sleep = sleep
        self.hunger = hunger
        self.cloaca = cloaca
        self.fire = fire
        self.energy = energy
        self.maturity = maturity
        self.image, self.rect = load_image('baby_dragon_by_kaitlynclinkscales-d55vsza.png', -1)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.STEP = 9
        self.MARGIN = 12
        self.xstep = self.STEP
        self.ystep = 0
        self.degrees = 0
        self.direction = 'right'
