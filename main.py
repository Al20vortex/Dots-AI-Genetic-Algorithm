import pyglet
from pyglet import shapes
from dot import Dot
import random
import numpy as np
from brain import Brain

height = 700
width = 1200
game_window = pyglet.window.Window(width, height)
batch = pyglet.graphics.Batch()
curr_instruction = 0
d1 = Dot(np.array([width / 2, height / 8]), np.array([0, 0]))
dot1_brain = Brain(100)

@game_window.event
def on_draw():
    global curr_instruction
    curr_instruction += 1
    d1.acc = dot1_brain.dot_brain[curr_instruction]
    d1.move_dot()
    batch.draw()


if __name__ == '__main__':
    rand_x = random.randint(100, 900)
    rand_y = random.randint(100, 500)
    # for x in range(0, dot1_brain.size, 1):
    #     d1.acc = dot1_brain.dot_brain[x]
    #     d1.move_dot()
    circle = shapes.Circle(rand_x, rand_y, 4, color=(50, 225, 30), batch=batch)
    pyglet.app.run()
