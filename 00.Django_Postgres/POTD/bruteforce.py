
list1 = [1, 2, 4]
list2 = [1, 3, 4]

# Bruteforce

# merged = list1 + list2
# merged.sort() # O (n Log n)

# print(merged)

# Better approach

itr = 0 # list1
jtr = 0 # list2

result = []

while itr < len(list1) and jtr < len(list2):
	
	#     1            1
	if list1[itr] <= list2[jtr]:
		result.append(list1[itr])
		itr += 1
	else:
		result.append(list2[jtr])
		jtr += 1

while itr < len(list1):
	result.append(list1[itr])
	itr+=1

while jtr < len(list2):
	result.append(list2[jtr])
	jtr+=1

print(result)

