def quicksort(l, low, high):
    if high > low:
        position = partition(l, low, high)
        quicksort(l, low, position - 1)
        quicksort(l, position + 1, high)


def partition(l, low, high):
    return 1 # the position

def quicksort_helper(l):
    return quicksort(l, 0, len(l) - 1)


if __name__ == "__main__":
    one = [1, 10, 2, 5, -8, 473, 8]
    quicksort_helper(one, len(one))

    two = [438, 23, -12, 0, 43, 0, 12, -9, 84]
    quicksort_helper(two, len(two))
    
    assert one == [-8, 1, 2, 5, 8, 10, 473]
    assert two == [-12, -9, 0, 0, 12, 23, 43, 84, 438]

    print(one)
    print(two)
