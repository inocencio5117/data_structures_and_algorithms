from search_names import names
from quicksort_strings import quicksort


def binary_search(collection, target):
    first = 0
    last = len(collection) - 1

    while first <= last:
        midpoint = (first + last) // 2
        if collection[midpoint] == target:
            return midpoint
        elif collection[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None


sorted_names = quicksort(names)
# print(sorted_names)

for n in sorted_names:
    index = binary_search(sorted_names, n)
    print(index)
