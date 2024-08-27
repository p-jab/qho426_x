import json
import matplotlib.pyplot as plt

def save(dictio = {}):
    with open("survey.json", "w") as f:
        json.dump(dictio, f)

def load():
    with open("survey.json") as f:
        d = json.load(f)
    return d

def survey(n=3):
    s = {}
    for i in range(n):
        resp = ""
        while resp not in {"me", "partner", "pet", "child"}:
            resp = input("Who rules in your house? (Me, partner, child, pet): ").lower()
            if resp not in {"pet", "partner", "me", "child"}:
                print(f"Response {resp} is not valid! Try again.")
        s[resp] = s.get(resp, 0) + 1
    return s

def run():
    data = {}
    while True:
        opt = int(input("Menu: \n\n1-New Survey\n2-Load Survey\n3-Save\n4-Visualise\n0-Exit\n\nOption: "))
        if opt == 1:
            n = int(input("Number of respondents: "))
            data = survey(n)
        elif opt == 2:
            data = load()
        elif opt == 3:
            save(data)
        elif opt == 4:
            opt2 = int(input("Choose type:\n1-Point Graph\n2-Bar Chart\n3-Pie Chart\nOption: "))
            if opt2 == 1:
                plt.plot(data.keys(), data.values(), "y^")
                plt.xlabel("The king of the house")
                plt.ylabel("Frequency")
            elif opt2 == 2:
                plt.bar(data.keys(), data.values(), color = "#c7893e")
                plt.xlabel("The king of the house")
                plt.ylabel("Frequency")
            elif opt2 == 3:
                plt.pie(data.values(), labels = data.keys(), autopct= "%.0f")
            else:
                print("Not valid option. Returning to main menu.")
            plt.title("Power struggle in students' houses")
            plt.show()
        elif opt == 0:
            print("End of the programme? Really? Okay, goodbye!")
            break
        else:
            print("No such option. Appreciate the menu again!")

run()

