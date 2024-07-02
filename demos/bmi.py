f_name = input("Enter first name: ")
s_name = input("Enter surname: ")
age = int(input("Enter age: "))
h = float(input("Enter height: "))
w = float(input("Enter the weight: "))

bmi = w/(h*h) #Calculate BMI score, by dividing w by h^2

print(f"{f_name} {s_name} - your age next year will be {age+1} and your BMI is {bmi:.2f}")