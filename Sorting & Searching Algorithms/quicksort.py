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


numbers = [67, 1, 99, 100, 4, 53, 23, 56, 872, 23, 43, 6]

sorted_num = quicksort(numbers)
print(sorted_num)
