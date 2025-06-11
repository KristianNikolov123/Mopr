def possible_strong_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    
    d = n - 1
    s = 0

    while d % 2 == 0:
        d //= 2
        s += 1
    
    test_bases = [2, 3, 5, 7, 11]

    for a in test_bases:
        if a > n - 2:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

print(possible_strong_prime(561))