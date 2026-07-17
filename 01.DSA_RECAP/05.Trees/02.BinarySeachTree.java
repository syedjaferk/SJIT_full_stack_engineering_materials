class Node {
    int data;
    Node left;
    Node right;

    Node(int data){
        this.data = data;
        left = right = null;
    }
}

class BinarySearchTree {
    Node root;

    Node insert(Node root, int data){
        if (root == null){
            return new Node(data);
        }

        if (data < root.data){
            root.left = insert(root.left, data);
        } else if (data > root.data){
            root.right = insert(root.right, data);
        }

        return root;
    }

    public void insert(int data){
        root = insert(root, data);
    }

    void inorder(Node root){
        if (root == null){
            return;
        }

        inorder(root.left);
        System.out.print(root.data+" ");
        inorder(root.right);
    }

    public void inorder(){
        inorder(root);
    }

    boolean search(Node root, int key){
        if (root == null){
            return false;
        }

        if (root.data == key){
            return true;
        }
        if (key < root.data){
            return search(root.left, key);
        }
        return search(root.right, key);
    }

    public boolean search(int key){
        return search(root, key);
    }

    public static void main(String[] args){
        BinarySearchTree bst = new BinarySearchTree();

        bst.insert(50);
        bst.insert(20);
        bst.insert(70);
        bst.insert(30);
        bst.insert(60);
        bst.insert(80);

        System.out.println("Inorder Value : ");
        bst.inorder();

        System.out.println("Searching 60 "+ bst.search(60));
        System.out.println("Searching 600 "+ bst.search(600));
    }
}
