from search_names import names


def index_of_item(collection, target):
    for i in range(0, len(collection)):
        if target == collection[i]:
            return i
    return None


index = index_of_item(names, "Nancie Rubalcaba")

if names[index] == "Nancie Rubalcaba":
    print("The name found was:", names[index])
    print()
    print("And the index is:", index)
    print()
