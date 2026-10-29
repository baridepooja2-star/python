#Write a Python program to count how many times a given element appears in a tuple
my_tuple = (10, 20, 30, 40, 50, 30, 30)
print("Created tuple:", my_tuple)
element = 30
count = my_tuple.count(element)
print(f"Element {element} appears {count} times in the tuple.")