class CircularQueue:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.queue = [None] * capacity

        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, data):
        if self.is_full():
            print("Queue Overflow")
            return

        if self.is_empty():
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity  # TODO

        self.queue[self.rear] = data

    def dequeue(self):
        if self.is_empty():
            print("Queue is underflow")
            return None

        data = self.queue[self.front]

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity

        return data

    def display(self):
        idx = self.front
        while True:
            print(self.queue[idx], end=" ")

            if idx == self.rear:
                break

            idx = (idx + 1) % self.capacity
        print()


cq = CircularQueue(capacity=5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)

cq.display()

cq.dequeue()

cq.display()
