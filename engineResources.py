import pygame, sys, os

#colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
cian = (0,255,255)
HC74225 = (199,66,37)
H61CD35 = (97,205,53)

#other variables
clock=pygame.time.Clock()

#classes
class Window():
  def __init__(self,width,hight,FPS):
    pygame.init()
    self.width=width
    self.hight=hight
    self.FPS=FPS
  def setScreen(self,screen):
    self.screen=screen

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
  def move(self,window,screen,velocity):
    rel_x = self.x % self.image.get_rect().width
    screen.blit(self.image, (rel_x - self.image.get_rect().width, 0))
    if rel_x < window.width:
      screen.blit(self.image, (rel_x, 0))
    self.x -= velocity

#functions
def setBackgroundImage(screen,background):
  f=background.image.convert()
  screen.blit(f,(0,0))

def setBackgroundColor(screen,color):
  screen.fill(color)

def setIcon(image):
  pygame.display.set_icon(image.image)

def initScreen(width,hight,title):
  screen = pygame.display.set_mode((width, hight))
  pygame.display.set_caption(title)
  return screen

def gameLoopSetup(window):
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      pygame.sys.exit()
  pygame.display.update() #=pygame.display.flip()
  clock.tick(window.FPS)