class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert Beginning
    def insert_beginning(self, data):
        new_node = DNode(data)

        if self.head:
            self.head.prev = new_node
            new_node.next = self.head

        self.head = new_node

    # Insert End
    def insert_end(self, data):
        new_node = DNode(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node
        new_node.prev = current

    # Insert After Value
    def insert_after(self, target, data):
        current = self.head

        while current:
            if current.data == target:
                new_node = DNode(data)

                new_node.next = current.next
                new_node.prev = current

                if current.next:
                    current.next.prev = new_node

                current.next = new_node
                return

            current = current.next

        print("Target not found")

    # Delete
    def delete(self, key):
        if self.head is None:
            return

        current = self.head

        if current.data == key:
            self.head = current.next

            if self.head:
                self.head.prev = None

            return

        while current:
            if current.data == key:
                current.prev.next = current.next

                if current.next:
                    current.next.prev = current.prev

                return

            current = current.next

        print("Node not found")

    # Search
    def search(self, key):
        current = self.head

        while current:
            if current.data == key:
                return True

            current = current.next

        return False

    # Forward Traversal
    def display_forward(self):
        current = self.head

        while current:
            print(current.data, end=" <-> ")
            last = current
            current = current.next

        print("None")

    # Reverse Traversal
    def display_backward(self):
        current = self.head

        if current is None:
            return

        while current.next:
            current = current.next

        while current:
            print(current.data, end=" <-> ")
            current = current.prev

        print("None")
