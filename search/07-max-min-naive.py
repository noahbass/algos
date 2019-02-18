# MaxMin
# Find the largest and smallest element in a list
# 
# Has a 2n - 1 runtime.
# The basic operation is the comparison operation.
# 
# Input: L[0:n-1] a list of numbers
# Output: A tuple containing the largest and smallest elements
def max_min(l):
    n = len(l)
    largest = l[0]
    smallest = l[0]

    for i in range(1, n): # 1...n-1
        item = l[i]

        if item > largest:
            largest = item
        elif item < smallest:
            smallest = item

    return (largest, smallest)


if __name__ == "__main__":
    assert max_min([1, 10, 2, 5]) == (10, 1)
    assert max_min([-4, 1, 89, 4332, 438932, 123]) == (438932, -4)

    print(max_min([1, 10, 2, 5])) # 10, 1
    print(max_min([-4, 1, 89, 4332, 438932, 123])) # 438932, -4
