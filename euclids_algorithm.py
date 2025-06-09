def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)

a = 432
b = 126
print(f"The Greatest Common Divisor of {a} and {b} is {gcd(a, b)}")