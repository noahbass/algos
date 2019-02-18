# Binary Search for Find a Fixed Point
#
# Fixed point == a element that is equal to it's index
# 
# Input:
#   l[0:n-1]: an array of distinct integers (negatives allowed), sorted in increasing order
#   low_point: integer
#   high_point: integer
# 
# Output: the fixed point, i.e., an index i such that l[i] = i or returns -1 if no such index exists
def binary_search_fixed_point(l, low_point, high_point):
    if low_point > high_point:
        return -1

    mid_point = (low_point + high_point) // 2

    if l[mid_point] == mid_point:
        return mid_point
    elif l[mid_point] < mid_point: # below
        return binary_search_fixed_point(l, mid_point + 1, high_point)
    else: # above
        return binary_search_fixed_point(l, low_point, mid_point - 1)


def binary_search_fixed_point_helper(l):
    return binary_search_fixed_point(l, 0, len(l) - 1)


if __name__ == "__main__":
    assert binary_search_fixed_point_helper([]) == -1
    assert binary_search_fixed_point_helper([-3, -1, 2, 9, 10, 12, 28]) == 2
    assert binary_search_fixed_point_helper([-10, 1, 89, 123, 4, 438932]) == 1

    print(binary_search_fixed_point_helper([])) # -1
    print(binary_search_fixed_point_helper([-3, -1, 2, 9, 10, 12, 28])) # 2
    print(binary_search_fixed_point_helper([-10, 1, 89, 123, 4, 438932])) # 1
