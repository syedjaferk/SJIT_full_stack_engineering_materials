class Stack:
    def __init__(self) -> None:
        self.stack = []

    def is_empty(self) -> bool:
        return len(self.stack) == 0

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def display(self):
        print(self.stack)


if __name__ == "__main__":
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)

    s.display()

    print("remove last element ", s.pop())
    s.display()
