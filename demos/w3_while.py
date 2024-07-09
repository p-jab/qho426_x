num = 5

while num >= 0:
    print(f"We have number {num}")
    num -= 1
    # Increase num by 1 -> num += 1
    # Multiply num by 2 -> num *= 2
    # Divide num by 2 -> num /= 2
print("-"*30)
num2 = float(input("Enter a number: "))
while num2 >= 0.00001:
    num2 /= 2
    print(f"We halved. Your number is {num2}")