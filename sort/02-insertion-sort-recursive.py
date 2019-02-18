# Insertion Sort (Recursive): an in-place, stable sort
# 
# B(n) = n-1  (entire list is already in order)
# W(n) = (n*(n-1))/2  (entire list is in decreasing order)
# 
# Input: L[0:n-1] a list of size n
# Output: L[0:n-1] sorted in increasing order
def insertion_sort_recursive(l, size):
    if size == 1:
        return

    insertion_sort_recursive(l, size-1)

    last_item = l[size - 1]
    i = size - 2

    while i >= 0 and l[i] > last_item:
        l[i + 1] = l[i]
        i -= 1

    l[i + 1] = last_item


if __name__ == "__main__":
    one = [1, 10, 2, 5, -8, 473, 8]
    insertion_sort_recursive(one, len(one))

    two = [438, 23, -12, 0, 43, 0, 12, -9, 84]
    insertion_sort_recursive(two, len(two))
    
    assert one == [-8, 1, 2, 5, 8, 10, 473]
    assert two == [-12, -9, 0, 0, 12, 23, 43, 84, 438]

    print(one)
    print(two)
