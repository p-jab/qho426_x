def populate(path):
    with open(path, "w") as f:
        while True:
            sauce = input("Enter a sauce you like or \"stop\" ")
            if sauce.lower() == "stop":
                break
            f.write(sauce + "\n")

def reading(path):
    with open(path) as f:
        print(f.read())

# name = input("Enter your name: ")
# populate("sauces/" + name + ".txt")
reading("sauces/Te.txt")