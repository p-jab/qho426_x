#List -> box of strings where you can add to it, remove from it
#Expand/shrink a list
#Heterogenous data structure - mix data types
# use [] or list()

#Tuple - fixed (cannot be expanded/shrunk)
#Read-only data structure
# use () or tuple()

def adding(lista = []):
    n_member = input("Enter new avenger: ")
    lista.append(n_member)

def remove(lista = []):
    name = input("Enter avenger to be removed: ")
    if name in lista:
        lista.remove(name)

def printing(lista = []):
    for thing in lista:
        print(f"The mighty {thing} is part of the avengers!")

def run():
    avengers = []
    while True:
        opt = int(input(
            '''Avengers, Assemble!!!
1 - Add an Avenger
2 - Remove an Avenger
3 - Check the Team
0 - Exit
            
Option: '''))
        if opt == 1:
            adding(avengers)
        elif opt == 2:
            remove(avengers)
        elif opt == 3:
            printing(avengers)
        elif opt == 0:
            print("Thanks for using my App. Goodbye!")
            break
        else:
            print("No such option. Try again.")

run()