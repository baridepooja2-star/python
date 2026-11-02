#Write a recursive function to calculate the factorial of a number
def factorial_recursion(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursion(n - 1)

print(factorial_recursion(5))  # Output: 120