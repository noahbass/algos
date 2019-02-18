# Evaluate a polynomial at both x=v and x=-v (such as p(x) = a4x^4 + a3x^3 + a2x^2 + a1x + a0).
# 
# Uses Horner's rule twice to evaluate two polynomials simultaneously.
# Calculates x0, x1, x2, ..., xn/2 twice (once for evens, once for odds)
# 
# n/2    (for squaring the first half of the points) 
# + n2/2 - n  (Horner's rule for evaluating Even(x2) and Odd(x2) at these squares)
# + n      (for computing x*Odd(x2) and -x*Odd(x2)at these squares)
# = n(n + 1)/2 = n2/2 + n/2.
# 
# p(x)  = Even(x^2) + x*Odd(x^2)
# p(-x) = Even(x^2) - x*Odd(x^2)
# 
# Input:
#   a[0:n]: an array of real numbers
#   v: a real number
# 
# Output: a tuple containing the value of the polynomial at x=v and x=-v
def double_poly_eval(a, v):
    n = len(a)
    sum_poly_evens = 0 # sum of all even degree
    sum_poly_odds = 0 # sum of all odd degree

    i = n - 1
    while i >= 0:
        if i % 2 == 0: # even
            sum_poly_evens = (sum_poly_evens * v**2) + a[i]
        else: # odd
            sum_poly_odds = (sum_poly_odds * v**2) + a[i]

        i = i - 1

    return sum_poly_evens+(v*sum_poly_odds), sum_poly_evens-(v*sum_poly_odds)

if __name__ == "__main__":
    assert double_poly_eval([1, 1, 2], 2) == (11, 7)
    assert double_poly_eval([1, -2, 5, 2], 3) == (94, -2)

    print(double_poly_eval([1, 1, 2], 2)) # 1 + 1*(2)^1 + 2*(2)^2
    print(double_poly_eval([1, -2, 5, 2], 3)) # 1 + -2*(3)^1 + 5*(3)^2 + 2*(3)^3
