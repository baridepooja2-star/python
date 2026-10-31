#Write a Python program to iterate through a dictionary and print all its keys and values
student = {
    "name": "Amit",
    "age": 20,
    "marks": 90
}
for key, value in student.items():
    print(key, value)