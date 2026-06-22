# arr = [1,1,2]

# unique = []
# for item in arr:
# 	if item not in unique:
# 		unique.append(item)

# for index in range(len(unique)):
# 	arr[index] = unique[index]

# index += 1
# while index < len(arr):
# 	arr[index] = "_"
# 	index += 1

# print(arr)



# arr = [1,1,2]

# unique = {}
# for item in arr:
# 	unique.add(item)

# for index in range(len(unique)):
# 	arr[index] = unique[index]

# index += 1
# while index < len(arr):
# 	arr[index] = "_"
# 	index += 1

# print(arr)


arr = [0,0,1,1,1,2,2,3,3,4]

prev = arr[0]
next_index = 1

for itr in range(1, len(arr)):
	if arr[itr] != prev:
		arr[next_index] = arr[itr]
		next_index += 1
		prev = arr[itr]
		
print(next_index)
print(arr)