class Queue:
    def __init__(self) -> None:
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.is_empty():
            print("Queue is Underflow")
            return

        return self.queue.pop(0)  # Zeroth Index

    def front(self):
        if self.is_empty():
            return None
        return self.queue[0]

    def rear(self):
        if self.is_empty():
            return None
        return self.queue[-1]

    def size(self):
        return len(self.queue)

    def display(self):
        print(self.queue)


q = Queue()
q.enqueue(10)
q.enqueue(15)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)

q.display()

print("Front ", q.front())
print("Rear ", q.rear())
print("Dequeued Element ", q.dequeue())

q.display()
