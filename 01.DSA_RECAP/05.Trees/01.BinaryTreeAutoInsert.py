from collections import deque


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.right: Node | None = None
        self.left: Node | None = None

class BinaryTree:
    def __init__(self) -> None:
        self.root: Node | None = None

    def insert(self, value):
        new_node = Node(value)

        #  If root is not present
        if self.root is None:
            self.root = new_node
            return

        queue = deque([self.root])

        while queue:
            current_element = queue.popleft()

            if current_element.left is None:
                current_element.left = new_node
                return
            else:
                queue.append(current_element.left)

            if current_element.right is None:
                current_element.right = new_node
                return
            else:
                queue.append(current_element.right)

    def pre_order(self, node):
        if node is None:
            return

        print(node.value, end=" ")
        self.pre_order(node.left)
        self.pre_order(node.right)

tree = BinaryTree()
tree.insert(10)
tree.insert(20)
tree.insert(30)
tree.insert(40)
tree.insert(50)
tree.insert(60)

tree.pre_order(tree.root)
