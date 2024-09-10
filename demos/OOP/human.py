from inhabitant import Inhabitant
class Human(Inhabitant):

    def __init__(self, n = "Adam", a = 1, e = 50):
        super().__init__(n, a, e)

    def __str__(self):
        return f"Hey, I am {self.name}. I am {self.age} years old with {self.energy} energy"

    def __repr__(self):
        return f"Human(name={self.name}, age={self.age}, energy={self.energy})"



if __name__ == "__main__":
    h1 = Human("Thadeus", 42, 90)
    h2 = Human("Elen", 15, 40)
    h2.eat(12)
    h2.eat(23)
    print(h2)
    h2.grow()
    h2.grow()
    h2.move(9)
    print(h2)