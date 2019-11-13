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

    def height(self):
        if self.root !=None:
            return self._height(self.root,0)
        else:
            return 0

    def _height(self,node,cur_height):
        if node==None:
            return cur_height
        left_height=self._height(node.left ,cur_height + 1)
        right_height = self._height(node.right, cur_height + 1)
        return max(left_height,right_height)

    def NodesSize(self, node, count=0):
        count = 1
        if self.root == None:
            return -1
        if self.root != None:
            if node.left != None:
                count += self.NodesSize(node.left)
            if node.right != None:
                count += self.NodesSize(node.right)
        return count

    def minValueNode(self, node):
        current = node
        while (current.left != None):
            current = current.left
        return current

    def DeleteNode(self, node,  data):
        if node is None:
            return node
        if data < node.data:
            node.left = self.DeleteNode(node.left, data)
        elif (data > node.data):
            node.right = self.DeleteNode(node.right, data)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp

            elif node.right is None:
                temp = node.left
                node = None
                return temp
            temp = self.minValueNode(node.right)
            node.data = temp.data
            node.right = self.DeleteNode(node.right, temp.data)
        return node

    def fillTree(tree, elem=10, maxint=1000):
        from random import randint
        for int in range(elem):
            currElem = randint(0, maxint)
            tree.addNode(currElem)
        tree.addNode(30)

def main():

    tree = BST()
    tree.fillTree()
    #tree.printTree()
    tree.inorder(tree.root)
    print("\n")
    tree.preorder(tree.root)
    print("\n")
    tree.postorder(tree.root)
    print("\n \ntree height: ", str(tree.height()))
    print("Number of Nodes in the tree is : ", tree.NodesSize(tree.root))
    tree.DeleteNode(tree.root,30)
    tree.inorder(tree.root)

main()
