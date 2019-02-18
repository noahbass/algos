# Evaluate a polynomial (such as p(x) = a4x^4 + a3x^3 + a2x^2 + a1x + a0).
# This implementation requires 2n multiplications and n additions of a polynomial of degree n.
# 
# Input:
#   a[0:n]: an array of real numbers
#   v: a real number
# 
# Output: the value of the polynomial at x = v
def naive_poly_eval(a, v):
    n = len(a)
    sum_poly = a[0] # sum of the polynomial
    product = 1

    i = 1
    while i < n:
        product = product * v
        sum_poly = sum_poly + a[i] * product
        i = i + 1

    return sum_poly

if __name__ == "__main__":
    assert naive_poly_eval([1, 1, 2], 2) == 11
    assert naive_poly_eval([1, -2, 5, 2], 3) == 94

    print(naive_poly_eval([1, 1, 2], 2))
    print(naive_poly_eval([1, -2, 5, 2], 3))
