#Write a program to keep asking for a number until the user enters zero
while True:
    number = int(input("Enter a number (0 to exit): "))
    if number == 0:
        break
    print("You entered:", number)