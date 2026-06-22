arr = [10, 20, 30, 40, 50, 60, 80, 100, 102]
target = 80


def linear_search(target):
    counter = 0
    for index, elem in enumerate(arr):
        counter += 1
        if elem == target:
            print("total iterations", counter)

            return index
    print("total iterations", counter)

    return False


response = linear_search(target)
print("Linear Search ", response)
