from planet import Planet
from random import randint
from human import Human
from robot import Robot
import matplotlib.pyplot as plt

class Universe:

    def __init__(self):
        self.planets = []

    def generate(self, p):
        n_humans = randint(1,10)
        n_robots = randint(1,10)
        for i in range(n_humans):
            h = Human(f"H{i}")
            p.add_inhabitant(h)
        for i in range(n_robots):
            r = Robot(f"R{i}")
            p.add_inhabitant(r)
        self.planets.append(p)

    def show_populations(self, selection):
        x = []
        y = []
        for planet in u.planets:
            n = planet.name
            num = 0
            for citizen in planet.inhabitants:
                if "human" in selection.lower():
                    if isinstance(citizen, Human):
                        num += 1
                elif "robot" in selection.lower():
                    if isinstance(citizen, Robot):
                        num += 1
                else:
                    num+=1
            x.append(n)
            y.append(num)
        plt.bar(x, y)
        plt.show()



if __name__ == "__main__":
    u = Universe()
    p1 = Planet("Alpha", [])
    p2 = Planet("Beta", [])
    p3 = Planet("Gamma", [])
    u.generate(p2)
    u.generate(p1)
    u.generate(p3)
    for i in u.planets:
        print(i)
u.show_populations("robots")