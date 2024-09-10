from human import Human
from robot import Robot
class Planet:

    def __init__(self, name = "", inhabitants = []):
        self.inhabitants = inhabitants
        self.name = name

    def __str__(self):
        return f"Planet {self.name} contains {self.inhabitants}"

    def __repr__(self):
        return f"Planet(name={self.name}, inhabitants{self.inhabitants})"

    def add_inhabitant(self, i):
        self.inhabitants.append(i)

    def remove_inhabitant(self, i):
        if i in self.inhabitants:
            self.inhabitants.remove(i)


if __name__ == "__main__":
    p1 = Planet("Pluto")
    h1 = Human("Radek", 31, 50)
    h2 = Human("Udoh", 40, 100)
    r1 = Robot("Dalek", 2)
    p2 = Planet("Earth", [h2])
    print(p2, p1)
    p1.add_inhabitant(h2)
    p1.add_inhabitant(r1)
    print(p1)
    p2.remove_inhabitant(r1)
    print(p2)