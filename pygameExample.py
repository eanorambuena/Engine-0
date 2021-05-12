'''
resources
'''
#moduls
import pygame, sys, os
from engineConstants import *
from pygame.locals import *
import ptkEngineResources as ptk

def pygameMain():
  ''' 
  params
  '''
  w = ptk.Window(1000,600,60,'Mi primer juego :D')
  fondo = ptk.Background("exampleImage.jpg")
  icono = ptk.Image(fondo.adress)
  s=w.screen

  ''' 
  screenSetup
  '''
  ptk.setBackgroundImage(s,fondo)
  ptk.setIcon(icono)

  '''
  gameSetup
  '''
  #pygame.draw.rect(s, RED, (100,50,100,50))
  #pygame.draw.line(s, BLUE, (100,104),(199,132), 1)
  #pygame.draw.circle(s, CIAN, (122, 250), 20, 0)
  #pygame.draw.ellipse(s, H61CD35, (275,200,40,80), 10)

  #points = [(100,300), (100,100), (150,100),(200,162)]
  #pygame.draw.polygon(s,(0,150,255), points, 3)

  pygame.mixer.music.load('exampleMusic.ogg')
  pygame.mixer.music.play(-1)
  pygame.mixer.music.set_volume(0.5)

  '''
  gameLoop
  '''
  while True:
    ptk.gameLoopSetup(w)

    fondo.move(w,1)