# Insertion Sort: an in-place, stable sort
# 
# B(n) = n-1
# W(n) = (n*(n-1))/2
# 
# Input: L[0:n-1] a list of size n
# Output: L[0:n-1] sorted in increasing order
def insertion_sort(l):
    n = len(l)

    i = 1
    while i != n:
        current = l[i]
        position = i - 1

        while position >= 0 and current < l[position]:
            l[position + 1] = l[position]
            position -= 1

        l[position + 1] = current

        i += 1


if __name__ == "__main__":
    one = [1, 10, 2, 5, -8, 473, 8]
    insertion_sort(one)

    two = [438, 23, -12, 0, 43, 0, 12, -9, 84]
    insertion_sort(two)
    
    assert one == [-8, 1, 2, 5, 8, 10, 473]
    assert two == [-12, -9, 0, 0, 12, 23, 43, 84, 438]

    print(one)
    print(two)
