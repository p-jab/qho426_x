h = input("Are you happy? (y/n): ").lower()
k = input("Do you know it? (y/n): ").lower()

#AND -> true and true => true
if h == "y" and k == "y":
    print("Clap your hands")
elif h == "y" and k == "n":
    print("Appreciate what you have, you little...")
elif h == "n" and k == "y":
    print("It will get better, one day!")
else:
    print("Seek help!")
print("Glad you here!")

#OR -> F or F => F
if h == "y" or k == "y":
    print("You answered yes to at least one question")