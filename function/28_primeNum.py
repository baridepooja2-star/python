#Write a function to check whether a number is prime
def check_prime(n):
    if n < 2:
        return "Not Prime"
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return "Not Prime"
    return "Prime"

print(check_prime(10)) 
print(check_prime(17))  