import heapq


class PriorityQueue:
    def __init__(self) -> None:
        self.heap = []

    def enqueue(self, priority, item):
        heapq.heappush(self.heap, (-priority, item))

    def dequeue(self):
        if not self.heap:
            return None

        return heapq.heappop(self.heap)

    def display(self):
        print(self.heap)


pq = PriorityQueue()
pq.enqueue(2, "Task A")
pq.enqueue(1, "Task b")
pq.enqueue(20, "Task D")
pq.enqueue(2, "Task C")
pq.enqueue(1, "Task F")

pq.display()
print(pq.dequeue())
print(pq.dequeue())
print(pq.dequeue())
print(pq.dequeue())
print(pq.dequeue())
