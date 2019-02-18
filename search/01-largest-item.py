# Find the largest item in the given list.
# 
# B(n) = n-1
# W(n) = n-1
# 
# Input: list of integers
# Output: largest integer
def largest(l):
    n = len(l)
    largest = l[0]

    i = 1
    while i != n:
        if l[i] > largest:
            largest = l[i]
        i += 1

    return largest


if __name__ == "__main__":
    assert largest([1, 10, 2, 5]) == 10
    assert largest([-4, 1, 89, 4332, 438932, 123]) == 438932

    print(largest([1, 10, 2, 5]))
    print(largest([-4, 1, 89, 4332, 438932, 123]))
