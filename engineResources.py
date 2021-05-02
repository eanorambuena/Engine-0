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

'''movement
px = 50
py = 200
ancho = 40
velocidad = 10

#Variables salto
salto = False
#Contador de salto
cuentaSalto = 10

#Variables dirección
izquierda = False
derecha = False

#Pasos
cuentaPasos = 0

#Opción tecla pulsada
keys = pygame.key.get_pressed()

#Tecla A - Moviemiento a la izquierda
if keys[pygame.K_a] and px > velocidad:
  px -= velocidad
  izquierda = True
  derecha = False

#Tecla D - Moviemiento a la derecha
elif keys[pygame.K_d] and px < 900 - velocidad - ancho:
  px += velocidad
  izquierda = False
  derecha = True

#Personaje quieto
else:
  izquierda = False
  derecha = False
  cuentaPasos = 0

#Tecla W - Moviemiento hacia arriba
if keys[pygame.K_w] and py > 100:
  py -= velocidad

#Tecla S - Moviemiento hacia abajo
if keys[pygame.K_s] and py < 300:
        py += velocidad
#Tecla SPACE - Salto
if not (salto):
  if keys[pygame.K_SPACE]:
    salto = True
    izquierda = False
    derecha = False
    cuentaPasos = 0
else:
  if cuentaSalto >= -10:
    py -= (cuentaSalto * abs(cuentaSalto)) * 0.5
    cuentaSalto -= 1
  else:
    cuentaSalto = 10
    salto = False
'''