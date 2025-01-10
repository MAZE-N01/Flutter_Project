# Program to determine category based on age
age = int(input("Enter your age: "))

# Age categories
if age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
elif age < 30:
    print("You are a young adult.")
elif age < 60:
    print("You are an adult.")
else:
    print("You are a senior.")

# Program to check if a number is positive, negative, or zero
number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# Program to check if a number is even or odd
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# Program to find the largest of three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("The largest number is:", a)
elif b >= a and b >= c:
    print("The largest number is:", b)
else:
    print("The largest number is:", c)

# Program to check if someone can vote
voting_age = int(input("Enter your age: "))

if voting_age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# Program to classify a grade
grade = int(input("Enter your grade: "))

if grade >= 90:
    print("Grade: A")
elif grade >= 80:
    print("Grade: B")
elif grade >= 70:
    print("Grade: C")
elif grade >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# Program to calculate discount based on purchase amount
purchase_amount = float(input("Enter the purchase amount: "))

if purchase_amount > 100:
    discount = 0.10  # 10% discount
else:
    discount = 0.05  # 5% discount

discount_amount = purchase_amount * discount
final_price = purchase_amount - discount_amount

print("Discount:", discount_amount)
print("Final price:", final_price)

# Program to check if a year is a leap year
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

# Program to categorize temperature
temperature = int(input("Enter the temperature in Celsius: "))

if temperature > 30:
    print("It's hot.")
elif temperature > 20:
    print("It's warm.")
elif temperature > 10:
    print("It's cool.")
else:
    print("It's cold.")

# Program to determine if a student passes or fails
marks = int(input("Enter your marks: "))

if marks >= 50:
    print("You passed.")
else:
    print("You failed.")

# Program to find the smallest of two numbers
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

if x < y:
    print("The smallest number is:", x)
else:
    print("The smallest number is:", y)

# Program to check eligibility for driving license
driver_age = int(input("Enter your age: "))

if driver_age >= 18:
    print("You are eligible for a driving license.")
else:
    print("You are not eligible for a driving license.")

# Program to find if a number is divisible by 5
number = int(input("Enter a number: "))

if number % 5 == 0:
    print("The number is divisible by 5.")
else:
    print("The number is not divisible by 5.")

# Program to check if a number is a multiple of both 3 and 7
num = int(input("Enter a number: "))

if num % 3 == 0 and num % 7 == 0:
    print("The number is a multiple of both 3 and 7.")
else:
    print("The number is not a multiple of both 3 and 7.")

# Program to find if a number is between 10 and 50
number = int(input("Enter a number: "))

if 10 <= number <= 50:
    print("The number is between 10 and 50.")
else:
    print("The number is not between 10 and 50.")

# Program to classify speed of a car
speed = int(input("Enter the speed of the car: "))

if speed > 120:
    print("You are overspeeding!")
elif speed > 80:
    print("You are driving fast.")
else:
    print("You are driving at a normal speed.")

# Program to check if two numbers are equal
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 == num2:
    print("Both numbers are equal.")
else:
    print("The numbers are not equal.")

# Program to determine whether a character is a vowel or consonant
char = input("Enter a character: ")

if char in 'aeiouAEIOU':
    print(char, "is a vowel.")
else:
    print(char, "is a consonant.")

# Program to find if a person is tall enough for a ride
height = int(input("Enter your height in cm: "))

if height >= 140:
    print("You are tall enough for the ride.")
else:
    print("You are not tall enough for the ride.")
