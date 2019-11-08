class Node:
    def __init__(self, data=None):
        self.data = data
        self.right = None
        self.left = None

class BST:
    def __init__(self):
        self.root = None

    def addNode(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            self._addNode(data, self.root)

    def _addNode(self, data, node):
        if data < node.data:
            if node.left == None:
                node.left = Node(data)
            else:
                self._addNode(data, node.left)
        elif data > node.data:
            if node.right == None:
                node.right = Node(data)
            else:
                self._addNode(data, node.right)
        else:
            print("value already in tree")

    def preorder(self, node):
        if node != None:
            print(node.data, end=" ")
            self.inorder(node.left)
            self.inorder(node.right)

    def inorder(self, node):
        if node != None:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    def postorder(self, node):
        if node != None:
            self.inorder(node.left)
            self.inorder(node.right)
            print(node.data, end=" ")

    def height(self, node):
        if self.root != None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, node, height):
        if node == None:
            return height
        left_height = self._height(node.left, height + 1)
        right_height = self._height(node.right, height + 1)
        return max(left_height, right_height)

    def NodesSize(self, root):
        if root is None:
            return 0
        else:
            return self.NodesSize(root.left) + self.NodesSize(root.right) + 1

def main():

    my_BST = BST()
    print((my_BST))

    my_BST.addNode(50)
    my_BST.addNode(4)
    my_BST.addNode(56)
    my_BST.addNode(890)
    my_BST.addNode(2)

    print("Inorder")
    my_BST.inorder(my_BST.root)
    print("\nPreorder")
    my_BST.preorder(my_BST.root)
    print("\nPostorder")
    my_BST.postorder(my_BST.root)
    print("\nHeight")
    my_BST.height(my_BST.root)
    print("\nNumber of nodes")
    my_BST.NodesSize(my_BST.root)

main()
