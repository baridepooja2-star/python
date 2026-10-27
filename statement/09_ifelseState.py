#Write a program to find the greater of two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if num1 > num2:
    print("The first number is greater.")
elif num2 > num1:
    print("The second number is greater.")
else:
    print("Both numbers are equal.")