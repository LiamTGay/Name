import pygame
from pygame.locals import *
from start import start
from startscreen import startscreen
#import keyboard

s1 = startscreen()
s2 = start()
#g1 = GameSelector()

if s1.switch == False:
  s1.start_test2()
elif s1.switch == True:
  s2.start_test()
