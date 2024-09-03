
class Human:

    MAX_ENERGY = 100

    def __init__(self, n = "Adam", a = 1, e = 50):
        self.name = n
        self.age = a
        if e > Human.MAX_ENERGY:
            self.energy = Human.MAX_ENERGY
        else:
            self.energy = e

    def __str__(self):
        return f"Hey, I am {self.name}. I am {self.age} years old with {self.energy} energy"

    def __repr__(self):
        return f"Human(name={self.name}, age={self.age}, energy={self.energy})"


    def display(self):
        print(f"I am {self.name}")

    def grow(self):
        self.age += 1

    def eat(self, amount):
        self.energy += amount
        if self.energy > Human.MAX_ENERGY:
            self.energy = Human.MAX_ENERGY

    def move(self, distance):
        self.energy -= distance
        if self.energy < 0:
            self.energy = 0


if __name__ == "__main__":
    h1 = Human("Thadeus", 42, 90)
    h2 = Human("Elen", 15, 40)
    h2.display()
    h1.display()
    h2.eat(12)
    h2.eat(23)
    print(h2)
    h2.grow()
    h2.grow()
    h2.move(9)
    print(h2)