from human import Human
from robot import Robot
class Planet:

    def __init__(self, hs = [], rs = [], name = ""):
        self.humans = hs
        self.robots = rs
        self.name = name

    def __str__(self):
        return f"Planet {self.name} contains {self.humans} and {self.robots}"

    def __repr__(self):
        return f"Planet(humans={self.humans}, robots={self.robots}, name={self.name})"

    def add_human(self, h):
        self.humans.append(h)

    def remove_human(self, h):
        if h in self.humans:
            self.humans.remove(h)

    def add_robot(self, h):
        self.robots.append(h)

    def remove_robot(self, h):
        if h in self.robots:
            self.robots.remove(h)

if __name__ == "__main__":
    p1 = Planet()
    h1 = Human("Radek", 31, 50)
    h2 = Human("Udoh", 40, 100)
    r1 = Robot("Dalek", 2)
    p2 = Planet([h1, h2], [r1], "Earth")
    print(p2, p1)
    p1.add_human(h2)
    print(p1)
    p2.remove_robot(r1)
    print(p2)