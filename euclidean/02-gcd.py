
# gcd(a, b) = gcd(b, a mod b)
# When a is a multiple of b, gcd(a, b) = b and a mod b = 0
# 
# Executes in about log(max(a, b)) time  (the log is base 2)
# 
# Input:
#   a: non-negative integer
#   b: non-negative integer
def euclid_gcd(a, b):
    while b != 0:
        remainder = a % b # a mod b
        a = b
        b = remainder

    return a


print(euclid_gcd(88, 4))
