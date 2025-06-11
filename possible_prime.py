def possible_prime(a, n):
    if n < 2 or a < 1 or a >= n:
        return False
    return pow(a, n - 1, n) == 1

print(possible_prime(8, 561))
