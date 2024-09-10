from inhabitant import Inhabitant
class Robot(Inhabitant):

    def __init__(self, n = "RD500", a = 5):
        super().__init__(n, a)

    def __str__(self):
        return f"Hey, I am {self.name}. I am {self.age} years old with {self.energy} energy"

    def __repr__(self):
        return f"Robot(name={self.name}, age={self.age})"



if __name__ == "__main__":
    h1 = Robot("WALL-E", 3)
    h2 = Robot("EVA", 3)
    print(h1)
    print(h2)
    h1.eat(25)
    print(h1)
    print(repr(h1))