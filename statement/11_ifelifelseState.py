#Write a program to find the greatest of three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

if num1 >= num2 and num1 >= num3:
    print("The first number is the greatest.")
elif num2 >= num1 and num2 >= num3:
    print("The second number is the greatest.")
else:
    print("The third number is the greatest.")