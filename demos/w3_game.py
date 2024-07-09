import random #Take functions/definitions from "random" package

secret = random.randint(1, 20)
print("Welcome to my guess-game. I am thinking of a number between 1 and 20.")

for attempt in range(5):
    print(f"Attempt nr {attempt+1}")
    guess = int(input("Take a guess: "))
    if guess == secret:
        print("Congrats! You won it bro!")
        break
    elif guess > secret:
        print("Too high!")
    else:
        print("Too low!")
    if attempt == 3:
        print("Last chance, buddy!")
if guess != secret:
    print(f"Game over! Looser! My number was {secret}")