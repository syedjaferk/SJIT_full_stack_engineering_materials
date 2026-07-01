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


def is_balanced(expression):
    s = Stack()

    pairs = {")": "(", "]": "[", "}": "{"}

    for ch in expression:
        if ch in "([{":
            s.push(ch)

        elif ch in ")]}":
            if s.is_empty():
                return False

            if s.pop() != pairs[ch]:
                return False

    return s.is_empty()


res = is_balanced("{[({[]})]}")
print(res)


res = is_balanced("{[({([)]})]}")
print(res)
