import pyglet
from pyglet import shapes
from dot import Dot
import random

height = 700
width = 1200
game_window = pyglet.window.Window(width, height)
batch = pyglet.graphics.Batch()

@game_window.event
def on_draw():
    batch.draw()


if __name__ == '__main__':
    rand_x = random.randint(100, 900)
    rand_y = random.randint(100, 500)
    d1 = Dot(width / 2, height / 8)
    circle = shapes.Circle(rand_x, rand_y, 4, color=(50, 225, 30), batch=batch)
    pyglet.app.run()
