import pyglet
from pyglet.window import key
from pyglet.window import mouse

def pygletMain():

  window = pyglet.window.Window()
  label = pyglet.text.Label('Hello, world',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')

  image = pyglet.resource.image('exampleImage.jpg')

  @window.event
  def on_key_press(symbol, modifiers):
    if symbol == key.A:
      print('The "A" key was pressed.')
    elif symbol == key.LEFT:
      print('The left arrow key was pressed.')
    elif symbol == key.ENTER:
      print('The enter key was pressed.')
    else:
      print('A key was pressed')

  @window.event
  def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print('The left mouse button was pressed.')

  @window.event
  def on_draw():
    window.clear()
    image.blit(0, 0)
    label.draw()

  pyglet.app.run()