'''
resources
'''
#moduls
import pygame, sys, os
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from engineResources import *

''' 
params
'''
w = Window(1000,600,60,'Mi primer juego :D')
fondo = Background("BG City.jpg")
icono = Image(fondo.adress)
s1=w.screen
''' 
screenSetup
'''
setBackgroundImage(s1,fondo)
setIcon(icono)

'''
gameSetup
'''
pygame.draw.rect(s1, red, (100,50,100,50))
pygame.draw.line(s1, blue, (100,104),(199,132), 1)
pygame.draw.circle(s1, cian, (122, 250), 20, 0)
pygame.draw.ellipse(s1, H61CD35, (275,200,40,80), 10)

points = [(100,300), (100,100), (150,100),(200,162)]
pygame.draw.polygon(s1,(0,150,255), points, 3)

'''
gameLoop
'''
while True:
  gameLoopSetup(w)
  
  fondo.move(w,0.5)