from planet import Planet
from random import randint
from human import Human
from robot import Robot

class Universe:

    def __init__(self):
        self.planets = []

    def generate(self, p):
        n_humans = randint(1,10)
        n_robots = randint(1,10)
        for i in range(n_humans):
            h = Human()
            p.add_human(h)
        for i in range(n_robots):
            r = Robot()
            p.add_robot(r)
        self.planets.append(p)

if __name__ == "__main__":
    u = Universe()
    p1 = Planet()
    u.generate(p1)
    p2 = Planet()
    u.generate(p2)
    for item in u.planets:
        print(item)