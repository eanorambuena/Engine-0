import pygame, sys, os
from ptk.constants import *

#other variables
clock=pygame.time.Clock()

#classes
class Music():
  def __init__(self,adress):
    self.adress=adress
    pygame.mixer.music.load(adress)
  def newAdress(self,newAd):
    self.adress=newAd
    pygame.mixer.music.load(newAd)
  def play(self,times):
    pygame.mixer.music.play(times)
  def loop(self):
    pygame.mixer.music.play(-1)
  def volume(self,vol):
    pygame.mixer.music.set_volume(vol)
  def mute(self):
    pygame.mixer.music.set_volume(0.0)
  
class Window():
  def __init__(self,width,hight,FPS,title):
    pygame.init()
    self.width=width
    self.hight=hight
    self.FPS=FPS
    self.screen=initScreen(width,hight,title);

class Image():
  def __init__(self,adress):
    self.adress=adress
    self.image=pygame.image.load(adress)
  def newAdress(self,newAd):
    self.adress=newAd

class Background(Image):
  def __init__(self,adress):
    Image.__init__(self,adress)
    self.x = 0
  def move(self,window,velocity):
    rel_x = self.x % self.image.get_rect().width
    window.screen.blit(self.image, (rel_x - self.image.get_rect().width, 0))
    if rel_x < window.width:
      window.screen.blit(self.image, (rel_x, 0))
    self.x -= velocity

#functions
def initScreen(width,hight,title):
    screen = pygame.display.set_mode((width, hight))
    pygame.display.set_caption(title)
    return screen

def setBackgroundImage(screen,background):
  f=background.image.convert()
  screen.blit(f,(0,0))

def setBackgroundColor(screen,color):
  screen.fill(color)

def setIcon(image):
  pygame.display.set_icon(image.image)

def gameLoopSetup(window):
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      pygame.sys.exit()
  pygame.display.update() #=pygame.display.flip()
  clock.tick(window.FPS)

