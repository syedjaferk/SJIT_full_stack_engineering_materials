class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at Beginning
    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at End
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    # Insert After a Value
    def insert_after(self, target, data):
        current = self.head

        while current:
            if current.data == target:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

        print("Target not found")

    # Delete Node
    def delete(self, key):
        if self.head is None:
            return

        if self.head.data == key:
            self.head = self.head.next
            return

        prev = None
        current = self.head

        while current:
            if current.data == key:
                prev.next = current.next
                return

            prev = current
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

    # Traverse
    def display(self):
        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")
