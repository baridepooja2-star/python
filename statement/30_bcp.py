#Write a program to search for a number in a list and stop when it is found
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = int(input("Enter the number to search for: "))

for num in numbers:
    if num == target:
        print(f"Number {target} found in the list.")
        break
else:
    print(f"Number {target} not found in the list.")