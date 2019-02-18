# Right to Left Binary Method for Computing x^n
# Finds the power of x^n with log2(n) to 2*log2(n) multiplcations.
# 
# Uses a recurrance formula for powers:
#   - x^n = (x^(n/2))^2  if n is even
#   - x^n = x*(x^((n-1)/2))^2  if n is odd
# 
# Finding if n is even or odd is found by the least significant digit
# (the trailing digit) in the binary representation of n (0 or 1).
# 
# Performs no more than 2*log2(n) calulations.
# 
# Input:
#   x: a real number
#   n: a positive integer
def right_to_left_binary_method_for_powers(x, n):
    n_binary_representation = get_binary_representation(n)
    power = x
    accum_powers = 1

    # Scan n_binary_representation left to right (start at second digit b/c we already took the first digit to be power = x)
    length = n.bit_length()
    i = 0
    while i != length - 1:
        # get the most sig bit (scanning left to right)
        least_significant_bit_index = i
        
        # get the least significant bit (to check even or odd)
        bit = n >> least_significant_bit_index & 1
        
        if bit == 1:
            accum_powers = power * accum_powers
        
        power = power * power

        i = i + 1

    return power * accum_powers

def get_binary_representation(n):
    return bin(n)


assert right_to_left_binary_method_for_powers(2, 9) == 512
assert right_to_left_binary_method_for_powers(2, 14) == 16384

print(right_to_left_binary_method_for_powers(2, 9))
print(right_to_left_binary_method_for_powers(2, 14))
