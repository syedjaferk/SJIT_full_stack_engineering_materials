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


def reverse_string(text):
    s = Stack()

    for ch in text:
        s.push(ch)

    result = ""
    while not s.is_empty():
        result = result + str(s.pop())
    return result


result = reverse_string("Hi How Are You ?")
print(result)
