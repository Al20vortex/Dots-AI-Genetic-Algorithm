import numpy as np
import random


class Brain:
    def __init__(self, size):
        self.size = size
        self.dot_brain = np.zeros((size,2))
        for x in range(0, size, 1):
            self.dot_brain[x, 0] = random.randint(-5, 5)
            self.dot_brain[x, 1] = random.randint(-5, 5)
        
