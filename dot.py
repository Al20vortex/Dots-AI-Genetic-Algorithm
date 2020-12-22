

class Dot:
    def __init__(self, loc, acc):
        self.loc = loc
        self.acc = acc

    def move_dot(self):
        self.loc[0] += self.acc[0]
        self.loc[1] += self.acc[1]





