import pyglet
from pyglet import shapes
from pyglet.libs.win32.constants import NULL
from dot import Dot
import random
import numpy as np
from brain import Brain

height = 700
width = 1200
game_window = pyglet.window.Window(width, height)
batch = pyglet.graphics.Batch()
curr_instruction = 0
dots = []

# todo
# d1 = Dot(np.array([width / 2, height / 8]), np.array([0, 0]), np.array([0, 0]))
# dot1_brain = Brain(10000)

goal = shapes.Circle(width/2, height - 15, 12, color=(255,69,0), batch=batch)
population = 100

def add_dots():
    global dots
    for i in range(0, population, 1):
        r = random.randint(10, 254)
        g = random.randint(10, 254)
        b = random.randint(10, 254)
        dots.append(Dot(np.array([width / 2, height / 8]), np.array([0, 0]), np.array([0, 0]), NULL, [r, g, b]))
        dots[i].brain = Brain(10000)

# check if dot is colliding with wall
def check_collision_wall():
    # todo
    return False

#check if dot reached goal
def succeeded():
    # todo
    return False

@game_window.event
def on_draw():
    game_window.clear()
    batch.draw()

def update(dt):
    # global curr_instruction
    # curr_instruction += 1
    # d1.acc = dot1_brain.dot_brain[curr_instruction]
    # d1.move_dot()
    # global circle
    # circle = shapes.Circle(d1.loc[0], d1.loc[1], 4, color=(50, 225, 30), batch=batch)
    global curr_instruction
    curr_instruction += 1
    for dot in dots:
        dot.acc = dot.brain.dot_brain[curr_instruction]
        dot.move_dot()
        dot.graphics = shapes.Circle(dot.loc[0], dot.loc[1], 4, color = (dot.color[0], dot.color[1], dot.color[2]), batch=batch)
    on_draw()


if __name__ == '__main__':    
    # for x in range(0, dot1_brain.size, 1):
    #     d1.acc = dot1_brain.dot_brain[x]
    #     d1.move_dot()
    add_dots()
    pyglet.clock.schedule_interval(update, 1/30.0)
    pyglet.app.run()
