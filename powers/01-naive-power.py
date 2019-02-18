# Finds the power of x^n with n-1 multiplications.
# 
# Performs n - 1 calulations.
# 
# Input:
#   x: a real number
#   n: a positive integer
def naive_power(x, n):
    product = x

    i = 1
    while i != n:
        product = product * x
        i = i + 1

    return product


if __name__ == "__main__":
    assert naive_power(2, 3) == 8
    assert naive_power(2, 12) == 4096

    print(naive_power(2, 3))
    print(naive_power(2, 12))
