import matplotlib.pyplot as plt
def small():
    x = [3,3,4,4,3] #List of x-coordinates (horizontal)
    y = [3,4,4,3,3] #List of y-coordinates (vertical)
    plt.plot(x, y, "ro:")


def medium():
    x = [2,2,5,5,2] #List of x-coordinates (horizontal)
    y = [2,5,5,2,2] #List of y-coordinates (vertical)
    plt.plot(x, y, "sg--")


def large():
    x = [6,1,1,6,6] #List of x-coordinates (horizontal)
    y = [6,6,1,1,6] #List of y-coordinates (vertical)
    plt.plot(x, y, "xb-")

small()
large()
medium()
plt.show()

Break -> 15:55