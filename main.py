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
d1 = Dot(np.array([width / 2, height / 8]), np.array([0, 0]), np.array([0, 0]))
dot1_brain = Brain(10000)
circle = shapes.Circle(d1.loc[0], d1.loc[1], 4, color=(50, 225, 30), batch=batch)
goal = shapes.Circle(width/2, height - 15, 12, color=(255,69,0), batch=batch)


@game_window.event
def on_draw():
    game_window.clear()
    batch.draw()

def update(dt):
    global curr_instruction
    curr_instruction += 1
    d1.acc = dot1_brain.dot_brain[curr_instruction]
    d1.move_dot()
    global circle
    circle = shapes.Circle(d1.loc[0], d1.loc[1], 4, color=(50, 225, 30), batch=batch)


if __name__ == '__main__':
    rand_x = random.randint(100, 900)
    rand_y = random.randint(100, 500)
    # for x in range(0, dot1_brain.size, 1):
    #     d1.acc = dot1_brain.dot_brain[x]
    #     d1.move_dot()
    pyglet.clock.schedule_interval(update, 1/30.0)
    pyglet.app.run()
