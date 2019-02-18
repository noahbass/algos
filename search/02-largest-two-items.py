# Find the two largest items (that is the largest and next largest)
# in the given list.
# 
# B(n) = n-1   (n-1 comparison in the best case - second largest is first to be compared and largest is last to be compared)
# W(n) = 3n-1  (3n-1 comparisons in the worst case)
# 
# Input: list of integers
# Output: two largest integers
def two_largest(l):
    n = len(l)
    largest = l[0]
    second_largest = l[1]

    i = 1
    while i != n:
        if l[i] > largest:
            second_largest = largest
            largest = l[i]
        elif l[i] > second_largest and l[i] < largest:
            second_largest = l[i]
        i += 1

    return (largest, second_largest)


if __name__ == "__main__":
    assert two_largest([1, 10, 2, 5]) == (10, 5)
    assert two_largest([-4, 1, 89, 4332, 438932, 123]) == (438932, 4332)

    print(two_largest([1, 10, 2, 5]))
    print(two_largest([-4, 1, 89, 4332, 438932, 123]))
