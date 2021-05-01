'''
resources
'''
#modules
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import sys
import os

#functions
def initScreen(width,hight,title):
  screen = pygame.display.set_mode((width, hight))
  pygame.display.set_caption(title)
  return screen

#colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
cian = (0,255,255)
HC74225 = (199,66,37)
H61CD35 = (97,205,53)

''' 
params
'''
w = 1000
h = 600
FPS = 60
clock = pygame.time.Clock()
fondo = pygame.image.load("BG City.jpg")

''' 
windowSetup
'''
pygame.init()
s1 = initScreen(w,h,'Mi primer juego :D')
#iconSetup
icon = fondo
pygame.display.set_icon(icon)
x = 0

'''
gameSetup
'''
s1.fill(H61CD35)
f=fondo.convert()
s1.blit(f,(0,0))

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
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            pygame.sys.exit()
    pygame.display.update()

    rel_x = x % fondo.get_rect().width
    s1.blit(fondo, (rel_x - fondo.get_rect().width, 0))
    if rel_x < w:
      s1.blit(fondo, (rel_x, 0))
    x -= 1
    pygame.display.update()
    clock.tick(FPS)
  