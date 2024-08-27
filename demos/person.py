#The class Person is a blueprint for my objects to store info about
#humans/people
class Person:

    #Initialiser/Constructor -> function that is automatically invoked/called
    #when an object is instantiated (example of magic method)
    #DUNDER -> Double Underscore
    def __init__(self, n, a, j, w = 50):
        #Below we define attributes (features) of every Person
        self.name = n
        self.age = a
        self.job = j
        self.weight = w

    #Magic method str provides "informal" text representation of object
    #Invoked automatically when print() function is called
    def __str__(self):
        return f"{self.name} is {self.age} years old. They work as {self.job} and weight {self.weight}kg"
    #Magic method REPR provide "formal" representation of and object
    #That's how oyu want to store your object for later (re-create)
    def __repr__(self):
        return f"Person(n={self.name}, a={self.age}, j={self.job}, w={self.weight})"

    def eat(self, food, w):
        print(f"{self.name} have eaten {food}")
        self.weight += w
        print(f"{self.name} now weights {self.weight:.2f}kg")


#Initialisation/Instantiation of Persons
p1 = Person("Bob", 52, "Plumber", 100)
p2 = Person("Daphne", 30, "Influencer")
p3 = Person("Boris", 64, "Unemployed", 80)

print(f"The combined weight of {p2.name}, {p1.name} and {p3.name} is {p1.weight + p2.weight + p3.weight}kg")
p3.eat("Enchilladas", 0.8)
p2.eat("Sandwiches", 2)
p2.eat("Crisps", 5)
print(p2)
print(p1)
print(p3)
print(repr(p2))