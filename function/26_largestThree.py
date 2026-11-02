#Write a function to find the largest of three numbers
def find_largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print(find_largest(10, 20, 30))
print(find_largest(5, 15, 10))   