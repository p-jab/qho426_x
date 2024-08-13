import json

def shop():
    #x = {"eggs": 2.99, "ham":6.49, "honey": 3.49, "bread": 1.99, "cheese": 3.99, "apple": 0.99, "jam": 3.99}
    with open("shop.json") as f:
        x = json.load(f)
    return x

def save_json(dicto = {}):
    with open("shop.json", "w") as f:
        json.dump(dicto, f)

def view_all(dictio = {}):
    for k, v in dictio.items():
        print(f"{k} --------- £{v}")

def basket():
    b = []
    while True:
        p = input("Enter item or \"stop\": ")
        if p.upper() == "STOP":
            break
        q = int(input(f"Enter quantity of {p}: "))
        for i in range(q):
            b.append(p)
    return b

def till(basket = []):
    all_items = shop()
    total = 0
    for prod in basket:
        if prod.lower() in all_items:
            total += all_items[prod.lower()]
        else:
            print(f"Sorry! We don't sell {prod}. Go to LIDL!")
    return total

def run():
    print("Welcome to Piotr's shop! Please look around. We are watching you!")
    view_all(shop())
    b = basket()
    while True:
        response = input("Are you ready to pay [y/n]: ")
        if "y" in response.lower():
            to_pay = till(b)
            print(f"Pay £{to_pay:.2f} or I will come after you!")
            break
        else:
            b2 = basket()
            b.extend(b2)

run()
