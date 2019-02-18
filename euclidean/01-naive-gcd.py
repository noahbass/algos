# Find the Greatest Common Divisor (GCD) of two positive integers
# The GCD is a positive integer k that divides a and b with no remainder

# An integer divides both a and b if, and only if, it divides a-b and b
# gcd(a, b) = gcd(a - b, b) when a >= b
# gcd(a, a) = a
# 
# Note: When Euclid created this algorithm, the concept of 0 was not conceptialized
# 
# Input:
#   a: positive integer
#   b: positive integer
def naive_gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a

    return a


print(naive_gcd(88, 4))
