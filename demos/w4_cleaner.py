def dimensions():
    w = float(input("Enter the width of the room: "))
    l = float(input("Enter the length of the room: "))
    return w*l

#print(dimensions() + dimensions())

def r_name():
    return input("Enter room name: ")

#print(r_name())

def price(name = "", area = 1):
    if name.lower() == "bathroom":
        return 12*area
    elif name.lower() == "bedroom":
        return 5*area
    elif name.lower() == "kitchen":
        return 8*area
    else:
        return 10*area

#print(price("bedroom", 5) + price("attic", 8) + price())

def run():
    t_price = 0
    num = int(input("Enter number of rooms to be cleaned: "))
    for i in range(num):
        room = r_name()
        area = dimensions()
        p = price(room, area)
        t_price += p

    print(f"The total price is £{t_price}")

run()