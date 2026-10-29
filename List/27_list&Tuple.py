#Write a Python program to convert a list into a tuple and a tuple into a list
my_list = [10, 20, 30, 40, 50]
print("Original list:", my_list)
my_tuple = tuple(my_list)
print("Converted tuple:", my_tuple)
my_new_list = list(my_tuple)
print("Converted list:", my_new_list)