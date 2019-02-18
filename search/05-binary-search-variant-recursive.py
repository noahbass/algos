# Binary Search Variant
#
# Design and analyze a variant of BinarySearch that performs a *single comparison*
# between the search element and the midpoint element (does not check for equality
# until the list is of size 1).
#
# Input:
#   l[0:n-1]: an array of integers, sorted in increasing order
#   low_point: integer
#   high_point: integer
#   target: a number
#
# Output: the index of the element if it exists, -1 if it doesn't
def binary_search_variant_recursive(l, low_point, high_point, target):
    if low_point > high_point:
        return -1
    
    difference = high_point - low_point
    if difference == 0 and l[low_point] == target: # only check for equality if no other operation possible
        return low_point

    mid_point = (low_point + high_point) // 2

    if l[mid_point] < target: # target is above mid_point
        return binary_search_variant_recursive(l, mid_point + 1, high_point, target)
    else: # target is below mid_point
        return binary_search_variant_recursive(l, low_point, mid_point, target)

def binary_search_helper(l, target):
    return binary_search_variant_recursive(l, 0, len(l) - 1, target)


if __name__ == "__main__":
    assert binary_search_helper([1, 4, 5, 9, 10, 14, 28], 14) == 5
    assert binary_search_helper([-4, 1, 89, 123, 4332, 438932], 4332) == 4

    print(binary_search_helper([1, 4, 5, 9, 10, 14, 28], 14)) # 5
    print(binary_search_helper([-4, 1, 89, 123, 4332, 438932], 4332)) # 4
