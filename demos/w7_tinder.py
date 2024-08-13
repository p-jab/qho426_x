def interests():
    print("Enter all hobbies one after another, or \"Stop\": ")
    s = set()
    #list()       []
    #tuple()      (,)
    #set()        {"rat", "heat"}
    #dict()        {}
    interest = ""
    while True:
        interest = input()
        if interest.lower() == "stop":
            break
        s.add(interest)
    return s

def run():
    print("First candidate: ")
    s1 = interests()
    print("Second candidate: ")
    s2 = interests()
    common = s1.intersection(s2)
    if len(common) >= 3:
        print(f"You are a match made in heaven! You have {len(common)} hobbies in common")
    else:
        print("Oh no! It will probably not work. Find another human.")

#run()

# Look for number of unique items on a list/other data structure
# lista = ["Piotr", "Chathu", "Tendai", "Edita", "Khadija", "Tendai", "Piotr", "Rita"]
# x = set(lista)
# print(f"There are {len(x)} tutors. ")


