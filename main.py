from numpy.lib.scimath import sqrt
import pyglet
from pyglet import shapes
from pyglet.libs.win32.constants import NULL
from dot import Dot
import random
import numpy as np
from brain import Brain

# create window
height = 700
width = 1200
game_window = pyglet.window.Window(width, height)

# create the batch of items
batch = pyglet.graphics.Batch()

# the index of the current instruction in the brains being executed
curr_instruction = 0

# the list of dots
dots = []

# location of the goal
goal_loc = [width/2, height - 30]

# make the goal
goal = shapes.Circle(goal_loc[0], goal_loc[1], 12, color=(255,69,0), batch=batch)

# of dots in the simulation, must be greater than 10
population = 100

# of instructions given to the dots
brain_size = 100

# decimal representing the fraction of dots chosen for the next generation
fraction_chosen = 0.5

# the dots that will be used for the next generation
chosen_ones = []

def add_dots():
    global dots
    #clears existing dots first
    dots = []
    for i in range(0, population, 1):
        r = random.randint(10, 254)
        g = random.randint(10, 254)
        b = random.randint(10, 254)
        dots.append(Dot(np.array([width / 2, height / 8]), np.array([0, 0]), np.array([0, 0]), NULL, [r, g, b]))
        dots[i].brain = Brain(brain_size)

# check if dot is colliding with wall, if it is then set dot to stuck
def check_collision_wall(dot):
    if (dot.loc[0] < 0) or (dot.loc[0] > width) or (dot.loc[1] < 0) or (dot.loc[1] > height):
        dot.stuck = True
        calculate_fitness(dot)
    succeeded(dot)


# check if dot reached goal, if so get it stuck
def succeeded(dot):
    if (sqrt((dot.loc[0] - goal_loc[0])**2 + (dot.loc[1] - goal_loc[1])**2) < 12):
        dot.stuck = True
        dot.fitness = 0

# calculate the fitness of the given dot
def calculate_fitness(dot):
    dot.fitness = (dot.loc[0] - goal_loc[0])**2 + (dot.loc[1] - goal_loc[1])**2

# draw the dots and goal
@game_window.event
def on_draw():
    game_window.clear()
    batch.draw()

def update(dt):
    global curr_instruction
    out_of_instructions = curr_instruction + 1 >= brain_size
    if not out_of_instructions:
        curr_instruction += 1
        for dot in dots:
            dot.acc = dot.brain.dot_brain[curr_instruction]
            dot.move_dot()
            dot.graphics = shapes.Circle(dot.loc[0], dot.loc[1], 4, color = (dot.color[0], dot.color[1], dot.color[2]), batch=batch)
            check_collision_wall(dot)
    else:
        for dot in dots:
            dot.stuck = True


if __name__ == '__main__':    
    # for x in range(0, dot1_brain.size, 1):
    #     d1.acc = dot1_brain.dot_brain[x]
    #     d1.move_dot()
    add_dots()
    pyglet.clock.schedule_interval(update, 1/60.0)
    pyglet.app.run()
