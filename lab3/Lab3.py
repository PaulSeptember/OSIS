class Node:
    def __init__(self, v):
        self.left = None
        self.right = None
        self.value = v

class Tree:
    def __init__(self):
        self.root = None

    def deleteTree(self):
        self.root = None

    def getRoot(self):
        return self.root

    def printTree(self):
        if(self.root != None):
            self._printTree(self.root)

    def add(self, v):
        if(self.root == None):
            self.root = Node(v)
        else:
            self._add(v, self.root)

    def find(self, val):
        if(self.root != None):
            if (self._find(val, self.root) is not None):
                print("Finded. ")
                return self._find(val, self.root)
            else:
                print("Value does not exists")

    def _find(self, val, node):
        if(val == node.value):
            return node
        elif(val < node.value and node.left != None):
            self._find(val, node.left)

        elif(val > node.value and node.right != None):
            self._find(val, node.right)

    def _add(self, v, node):
        if(v < node.value):
            if(node.left != None):
                self._add(v, node.left)
            else:
                node.left = Node(v)
                
        else:
            if(node.right != None):
                self._add(v, node.right)
            else:
                node.right = Node(v)

    def _printTree(self, node):
        if(node != None):
            self._printTree(node.left)
            print (str(node.value) + ' ')
            self._printTree(node.right)

tree = Tree()
tree.add(1)
tree.add(4)
tree.add(8)
tree.printTree()
print ((tree.find(8)).value)
