def split(given_list):
    """
    Divide the unsorted list at midpoint into sublists
    Return two sublists - left and right

    Takes overall O(log n) time*

    *(given the slicing it actually takes O(k.n.log m) time
    """

    mid = len(given_list) // 2

    # This runs in O(k.log n)
    left = given_list[:mid]
    right = given_list[mid:]

    return left, right


def merge(left, right):
    """
    Merges two lists (arrays), sorting them in the process
    Returns a new merged list

    Runs overall O(n) time
    """

    new_list = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            new_list.append(left[i])
            i += 1
        else:
            new_list.append(right[j])
            j += 1

    while i < len(left):
        new_list.append(left[i])
        i += 1

    while j < len(right):
        new_list.append(right[j])
        j += 1

    return new_list


def merge_sort(given_list):
    """
    Sorts a list in ascending order
    Returns a new sorted list

    Divide: Find the midpoint of the list and divide into sublists
    Conquer: Recursively sort the sublists in previous step
    Combine: Merge the sorted sublists created in previous step

    Takes O(n.log n) time
    """

    if len(given_list) <= 1:
        return given_list

    left_half, right_half = split(given_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def verify_sorted(given_list):
    n = len(given_list)

    if n == 0 or n == 1:
        return True

    # compares every item in the list recursively
    return given_list[0] < given_list[1] and verify_sorted(given_list[1:])


alist = [54, 71, 19, 0, 10, 27, 5, 8, 20, 2]

sorting = merge_sort(alist)

print()
print("Non sorted list:")
print(alist)
print(verify_sorted(alist))

print()
print("Sorted list")
print(sorting)
print(verify_sorted(sorting))
