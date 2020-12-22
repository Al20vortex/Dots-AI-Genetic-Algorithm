

class Dot:
    def __init__(self, loc, vel, acc):
        self.loc = loc
        self.vel = vel
        self.acc = acc

    # moves dot to next position
    def move_dot(self):
        self.vel[0] += self.acc[0]
        self.vel[1] += self.acc[1]
        if self.vel[0] > 5:
            self.vel[0] = 5
        if (self.vel[0] < -5):
            self.vel[0] = -5
        if (self.vel[1] > 5):
            self.vel[1] = 5
        if (self.vel[1] < -5):
            self.vel[1] = -5
        self.loc[0] += self.vel[0]
        self.loc[1] += self.vel[1]





