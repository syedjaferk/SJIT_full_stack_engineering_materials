arr = [64, 25, 12, 23, 11, 34]

# Psuedocode
# 1. Find the minimum element
# 2. Swap with index 0, [11, 25, 12, 23, 64, 34]
# 3. Step 1.


def selection_sort(arr):
    total_elements = len(arr)

    for itr in range(total_elements):
        min_index = itr

        # Find the minimum element
        for jtr in range(itr + 1, total_elements):
            if arr[jtr] < arr[min_index]:
                min_index = jtr

        # Swap
        arr[itr], arr[min_index] = arr[min_index], arr[itr]
    return arr


response = selection_sort(arr)
print("Selection Sort ", response)
