name = input("Enter your name: ")

if len(name) >= 6:
    print("Your name is loooooong my friend!")
elif len(name) <= 3:
    print("Your name is quite short!")
elif name.lower() == "piotr":
    print("That's the best name ever")
else:
    print("Your name is fine. Welcome!")
print(f"Welcome to Python class {name}!!!")