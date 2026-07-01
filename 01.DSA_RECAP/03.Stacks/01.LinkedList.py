class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next: Node | None = None


class Stack:
    def __init__(self) -> None:
        self.top: Node | None = None
        self.count = 0

    def push(self, data):
        print(f"Top: {self.top if self.top is None else self.top.data}")
        node = Node(data=data)
        node.next = self.top
        self.top = node
        self.count += 1

    def pop(self):
        if self.top is None:
            return None

        value = self.top.data
        current = self.top
        self.top = self.top.next
        self.count -= 1
        del current
        return value

    def display(self):
        current = self.top
        while current:
            print(current.data, end=" --> ")
            current = current.next
        print("None")


s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)

s.display()
