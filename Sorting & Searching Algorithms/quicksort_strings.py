from search_names import names


def quicksort(values):
    # This takes O(n^2) time
    if len(values) <= 1:
        return values

    less_than_pivot = []
    greater_than_pivot = []
    pivot = values[0]

    for value in values[1:]:
        if value <= pivot:
            less_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)
    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)


# sorted_names = quicksort(names)
# for n in sorted_names:
#     print(n)
