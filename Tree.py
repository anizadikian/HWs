class Node:
    def __init__(self, data=None):
        self.data = data
        self.right = None
        self.left = None

class BST:
    def __init__(self):
        self.root = None

    def __str__(self):
        if self.root == None:
            print("Root is Empty")
        else:
            return str(self.root.data)

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

    def printTree(self):
        if self.root != None:
            self._printTree(self.root)

    def _printTree(self, node):
        if node != None:
            self._printTree(node.left)
            print(str(node.data))
            self._printTree(node.right)

def main():

    my_BST = BST()
    print((my_BST))

    my_Node = Node(50)
    my_BST.addNode(my_Node)
    print(my_BST)

main()
