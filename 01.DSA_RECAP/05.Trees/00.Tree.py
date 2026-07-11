

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.right: Node | None = None
        self.left: Node | None = None

class BinaryTree:
    def __init__(self) -> None:
        self.root: Node | None = None

    def print_tree(self, node: Node | None):
        if node is None:
            return

        print(node.value)

        self.print_tree(node.left)
        self.print_tree(node.right)

bt = BinaryTree()
bt.root = Node(10)

bt.root.left = Node(20)
bt.root.right = Node(30)

bt.root.left.left = Node(40)

bt.print_tree(bt.root)
