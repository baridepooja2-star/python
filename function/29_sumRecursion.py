# Write a function to calculate the sum of numbers from 1 to n using recursion

def sum_recursion(n):
    if n == 0:
        return 0
    else:
        return n + sum_recursion(n - 1)

print(sum_recursion(5))