def selection_sort(values):
    sorted_list = []

    for i in range(0, len(values)):
        index_to_move = index_of_min(values)
        sorted_list.append(values.pop(index_to_move))
    return sorted_list


def index_of_min(values):
    min_index = 0
    for i in range(1, len(values)):
        if values[i] < values[min_index]:
            min_index = i
    return min_index


# Takes O(n^2) time
# Bad for large numbers
numbers = [67, 1, 99, 100, 4, 53, 23, 56, 872, 23, 43, 6]

print(selection_sort(numbers))
