arr = [5, 2, 4, 6, 1, 3]

for itr in range(1, len(arr)):
    key = arr[itr]  # 2, itr -> 1, arr[1] = 2
    jtr = itr - 1  # itr -> 1 - 1 = 0

    while jtr >= 0 and arr[jtr] > key:
        arr[jtr + 1] = arr[jtr]
        # [5, 5, 4, 6, 1, 3]
        jtr -= 1
    arr[jtr + 1] = key

print("Sorted Array ", arr)
