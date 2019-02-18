# Binary Search Variant
#
# Design and analyze a variant of BinarySearch that performs a *single comparison*
# between the search element and the midpoint element (does not check for equality
# until the list is of size 1).
#
# Input:
#   l[0:n-1]: an array of integers, sorted in increasing order
#   target: a number
#
# Output: the index of the element if it exists, -1 if it doesn't
def binary_search_variant(l, target):
    low_point = 0
    high_point = len(l) - 1
    mid_point = 0

    while low_point < high_point:
        mid_point = (low_point + high_point) // 2

        if l[mid_point] < target: # target is above mid_point
            low_point = mid_point + 1
        else: # target is below mid_point
            high_point = mid_point

    # high_point-low_point is now 0
    if l[low_point] == target:
        return low_point

    return -1 # element doesn't exist


if __name__ == "__main__":
    assert binary_search_variant([1, 4], 4) == 1
    assert binary_search_variant([1000], 4) == -1
    assert binary_search_variant([1, 4, 5, 9, 10, 14, 28], 14) == 5
    assert binary_search_variant([-4, 1, 89, 123, 4332, 438932], 4332) == 4

    print(binary_search_variant([1, 4, 5, 9, 10, 14, 28], 14)) # 5
    print(binary_search_variant([-4, 1, 89, 123, 4332, 438932], 4332)) # 4
