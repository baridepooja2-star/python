#Write a Python program to count the frequency of each character in a string using a dictionary
text = "hello world"
frequency = {}
for char in text:
    frequency[char] = frequency.get(char, 0) + 1
print(frequency)