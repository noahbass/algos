# Finds the power of x^n with the recurrance formula for powers:
#   - x^n = (x^(n/2))^2  if n is even
#   - x^n = x*(x^((n-1)/2))^2  if n is odd
# 
# Performs n - 1 calulations.
# 
# Input:
#   x: a real number
#   n: a positive integer
def recurrance_relation_power_recursive(x, n):
    if n == 1:
        return x

    if n % 2 == 0: # even
        return recurrance_relation_power_recursive(x*x, n/2)
    else: # odd
        return x * recurrance_relation_power_recursive(x*x, (n - 1)/2)


if __name__ == "__main__":
    assert recurrance_relation_power_recursive(2, 3) == 8
    assert recurrance_relation_power_recursive(2, 12) == 4096

    print(recurrance_relation_power_recursive(2, 3))
    print(recurrance_relation_power_recursive(2, 12))
