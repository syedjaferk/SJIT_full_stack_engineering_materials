from collections import deque

dq = deque()

dq.append(10)
dq.append(20)
dq.append(30)
dq.append(40)

dq.appendleft(50)

print(dq)
dq.pop()
print(dq)
