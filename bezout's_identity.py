def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x_next, y_next = extended_gcd(b, a % b)
        x = y_next
        y = x_next - (a // b) * y_next
        return gcd, x, y

print(extended_gcd(432, 126))