# MaxMin Optimal
#
# Find the largest and smallest element in a list by comparing
# elements in groups of 2.
#
# Works by pairing elements (except the first element when n is odd)
# in the list L[0:n-1] (size of list is n) and computing the max and
# min for each pair (n/2 comparisons).
#
# Has an optimal 3n/2 - 2 runtime.
# The basic operation is the comparison operation.
#
# Input: L[0:n-1] a list of numbers
# Output: A tuple containing the largest and smallest elements
def max_min(l):
    n = len(l)
    max_value, min_value = 0, 0

    if n % 2 == 0: # n is even
        max_value, min_value = max_and_min(l[0], l[1])
        
        for i in range(2, n - 1, 2): # move by 2 up from 1...n-2
            b, a = max_and_min(l[i], l[i + 1])
            
            if a < min_value:
                min_value = a
            if b > max_value:
                max_value = b
    
    else: # n is odd
        max_value = l[0]
        min_value = l[0]
        
        for i in range(1, n - 1, 2): # move by 2 from 1...n-2
            b, a = max_and_min(l[i], l[i + 1])
            
            if a < min_value:
                min_value = a
            if b > max_value:
                max_value = b

    return (max_value, min_value)


# Solves MaxMin for a list of size 2
def max_and_min(a, b):
    if a >= b:
        return (a, b)
    else:
        return (b, a)


if __name__ == "__main__":
    assert max_min([1, 10, 2, 5]) == (10, 1)
    assert max_min([-4, 1, 89, 4332, 438932, 123, -10]) == (438932, -10)

    print(max_min([1, 10, 2, 5])) # 10, 1
    print(max_min([-4, 1, 89, 4332, 438932, 123, -10])) # 438932, -10
