# Binary Search
#
# Best case: The target is found in the midpoint position (low + high) / 2
# Worst case: Twice the longest string of midpoints ever generated (2*(log2(n + 1)))
#
# Input:
#   l[0:n-1]: an array of integers, sorted in increasing order
#   low_point: integer
#   high_point: integer
#   target: a number
#
# Output: the index of the element if it exists, -1 if it doesn't
def binary_search(l, low_point, high_point, target):
    if low_point > high_point:
        return -1
    
    mid_point = (low_point + high_point) // 2

    if l[mid_point] == target:
        return mid_point
    elif l[mid_point] > target: # target is below mid_point
        return binary_search(l, low_point, mid_point - 1, target)
    else: # target is above mid_point
        return binary_search(l, mid_point + 1, high_point, target)

def binary_search_helper(l, target):
    return binary_search(l, 0, len(l) - 1, target)


if __name__ == "__main__":
    assert binary_search_helper([1, 4, 5, 10], 4) == 1
    assert binary_search_helper([-4, 1, 89, 123, 4332, 438932], 4332) == 4

    print(binary_search_helper([1, 4, 5, 10], 4)) # 1
    print(binary_search_helper([-4, 1, 89, 123, 4332, 438932], 4332)) # 4
