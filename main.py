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
population = 200

# of instructions given to the dots
brain_size = 300

# decimal representing the fraction of dots chosen for the next generation
# fraction_chosen = 0.5

# the dots that will be used for the next generation
chosen_ones = []

# mutation rate
mut_rate = 0.005

# generation number and label
gen_num = 1

score_label = pyglet.text.Label(text= 'Generation Number: ' + str(gen_num), color = (255, 255, 255, 255), font_size = 10, x = width - 200, y = 50)

fitness_list = []


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
        dot.fitness = 999999999999

# calculate the fitness of the given dot
def calculate_fitness(dot):
    if dot.loc[1] <= 0:
        dot.fitness
        return
    dot.fitness = 1.000000 / ((dot.loc[0] - goal_loc[0])**2 + (dot.loc[1] - goal_loc[1])**2)

# calculate the sum of every dot's fitness
def fitness_sum(lod):
    sum = 0.000
    for dot in lod:
        sum += float(dot.fitness)
    return sum

# selects the two fittest dots in a list using the fraction_chosen variable
def select_fittest(lod):
    total_fitness = fitness_sum(lod)
    global chosen_ones
    # num_chosen = int(population * fraction_chosen)
    chosen_ones = []
    global dots
    global fitness_list
    fitness_list = []
    for dot in dots:
        fitness_list.append(dot.fitness / total_fitness)

    for j in range (0, 2, 1):
        val = np.random.choice(np.arange(0, population), p = fitness_list)
        chosen_ones.append(dots[val])


## consumes two brains, returns a new combined brain
def crossover(parent1, parent2):
    crossover_point = random.randint(1, brain_size - 2)
    new1 = np.concatenate([parent1[:crossover_point,], parent2[crossover_point:]])
    new2 = np.concatenate([parent2[:crossover_point:,], parent1[crossover_point:]])
    random_num = random.randint(0, 1)
    if random_num == 0:
        return new1
    else:
        return new2

# produce a new population of nodes
def make_new_gen():
    global dots
    for i in range(0, population, 1):
        new_brain = crossover(chosen_ones[0].brain.dot_brain, chosen_ones[1].brain.dot_brain)
        # for everything in the new brain, apply mutation
        for j in range(0, brain_size):
            mutation_x = random.randint(-5, 5)
            mutation_y = random.randint(-5, 5)
            if random.uniform(0, population) <= float(float(population) * mut_rate):
                new_brain[j] = [mutation_x, mutation_y]
        full_brain = Brain(brain_size)
        full_brain.dot_brain = new_brain
        dots[i].loc = np.array([width / 2, height / 8])
        dots[i].stuck = False
        dots[i].brain = full_brain
            
# draw the dots and goal
@game_window.event
def on_draw():
    game_window.clear()
    batch.draw()
    score_label.draw()

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
            # if (not dot.stuck):
            dot.stuck = True
            calculate_fitness(dot)
        global gen_num
        gen_num += 1
        select_fittest(dots)
        make_new_gen()
        curr_instruction = 0
        global score_label
        score_label = pyglet.text.Label(text= 'Generation Number: ' + str(gen_num), color = (255, 255, 255, 255), font_size = 10, x = width - 150, y = 50)


if __name__ == '__main__':    
    # for x in range(0, dot1_brain.size, 1):
    #     d1.acc = dot1_brain.dot_brain[x]
    #     d1.move_dot()
    add_dots()
    pyglet.clock.schedule_interval(update, 1/60.0)
    pyglet.app.run()
