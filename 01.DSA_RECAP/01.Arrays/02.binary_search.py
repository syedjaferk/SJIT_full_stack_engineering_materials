arr = [10, 20, 30, 40, 50, 60, 80, 100, 102]
target = 80


def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    counter = 0

    while left <= right:
        counter += 1
        # Step 1
        mid = (left + right) // 2

        # Step 2
        if arr[mid] == target:
            print("total iterations", counter)
            return mid

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1
    print("total iterations", counter)
    return -1


response = binary_search(arr, target)
print("Response ", response)
