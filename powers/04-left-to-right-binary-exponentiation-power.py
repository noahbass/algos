# Left to Right Binary Method for Computing x^n
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
def left_to_right_binary_method_for_powers(x, n):
    n_binary_representation = get_binary_representation(n)
    power = x

    # Scan n_binary_representation left to right (start at second digit b/c we already took the first digit to be power = x)
    length = n.bit_length()
    i = 1
    while i != length:
        # get the most sig bit (scanning left to right)
        most_significant_bit_index = length - 1 - i
        
        # get the least significant bit (to check even or odd)
        bit = n >> most_significant_bit_index & 1
        
        if bit == 0:
            power = power * power
        else: # bit == 1
            power = x * power * power

        i = i + 1

    return power

def get_binary_representation(n):
    return bin(n)


assert left_to_right_binary_method_for_powers(2, 9) == 512
assert left_to_right_binary_method_for_powers(2, 14) == 16384

print(left_to_right_binary_method_for_powers(2, 9))
print(left_to_right_binary_method_for_powers(2, 14))
