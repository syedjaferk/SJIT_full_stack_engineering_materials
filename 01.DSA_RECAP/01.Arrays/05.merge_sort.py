def merge(left, right):
    result = []

    left_ptr = 0
    right_ptr = 0

    while left_ptr < len(left) and right_ptr < len(right):
        if left[left_ptr] <= right[right_ptr]:
            result.append(left[left_ptr])
            left_ptr += 1
        else:
            result.append(right[right_ptr])
            right_ptr += 1

    # Append remaining elements.
    result.extend(left[left_ptr:])
    result.extend(right[right_ptr:])

    return result


def merge_sort(arr):
    # Base Condition
    if len(arr) <= 1:
        return arr

    # Recursive Condition.
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


arr = [38, 27, 43, 3, 9, 82, 10]
res = merge_sort(arr)

print("Response ", res)
