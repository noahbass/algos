# Evaluate a polynomial (such as p(x) = a4x^4 + a3x^3 + a2x^2 + a1x + a0)
# with Horner's rule (https://wikipedia.org/wiki/Horner%27s_method) for optimal evaluation.
# 
# This implementation requires just n multiplications and n additions of a polynomial of degree n.
# 
# Input:
#   a[0:n-1]: an array of real numbers
#   v: a real number
# 
# Output: the value of the polynomial at x = v
def horner_poly_eval(a, v):
    n = len(a)
    sum_poly = a[n - 1] # sum of the polynomial

    i = n - 2 # (already did n-1 in sum_poly)
    while i >= 0:
        sum_poly = (sum_poly * v) + a[i]
        i = i - 1

    return sum_poly

if __name__ == "__main__":
    assert horner_poly_eval([1, 1, 2], 2) == 11
    assert horner_poly_eval([1, -2, 5, 2], 3) == 94

    print(horner_poly_eval([1, 1, 2], 2)) # 1 + 1*(2)^1 + 2*(2)^2
    print(horner_poly_eval([1, -2, 5, 2], 3)) # 1 + -2*(3)^1 + 5*(3)^2 + 2*(3)^3
