class Node:

    def __init__(self, data, present):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.parent = parent


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data, None)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        if data < node.data:
            if node.leftChild:
                self.insert_node(data, node.leftChild)
            else:
                node.leftChild = Node(data, node)
        else:
            if node.rightChild:
                self.insert_node(data, node.rightChild)
            else:
                node.rightChild = Node(data, node)

    def remove_node(self, data, node):

        if node is None:
            return

        if data < node.data:
            self.remove_node(data, node.leftChild)
        elif data > node.data:
            self.remove_node(data, node.rightChild)
        else:

            if node.leftChild is None and node.rightChild is None:
                print("Removing a leaf node... %d" % node.data)

                parent = node.parent

                if parent is not None and parent.leftChild == node:
                    parent.leftChild = None
                if parent is not None and parent.rightChild == node:
                    parent.rightChild = None

                if parent is None:
                    self.root = None

                del node
            elif node.leftChild is None and node.rightChild is not None:
                print("Removing a node with single right child...")

                parent = node.parent

                if parent is not None:
                    if parent.leftChild == node:
                        parent.leftChild = node.rightChild
                    if parent.rightChild == node:
                        parent.rightChild = node.rightChild
                else:
                    self.root = node.rightChild

                node.rightChild.parent = parent
                del node

            elif node.rightChild is None and node.leftChild is not None:
                print("Removing a node with single left child...")

                parent = node.parent

                if parent is not None:
                    if parent.leftChild == node:
                        parent.leftChild = node.leftChild
                    if parent.rightChild == node:
                        parent.rightChild = node.leftChild
                else:
                    self.root = node.leftChild

                node.leftChild.parent = parent
                del node

            else:
                print('Removing node with two children...')

                predecessor = self.get_predecessor(node.leftChild)

                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp

                self.remove_node(data, predecessor)
    
    def get_predecessor(self,node):
        if node.rightChild:
            return self.get_predecessor(node.rightChild)
        
        return node

    def remove(self, data):
        if self.root is not None:
            self.remove_node(data, self.root)
    
    def traverse(self):
        if self.root is not None:
            self.traverse_in_order(self.root)

    def get_max_value(self):
        if self.root:
            return self.get_max(self.root)
    
    def get_max(self, node):
        actual = self.root

        while actual.rightChild is not None:
            actual = actual.rightChild

            return actual.data

    def get_min_value(self):
        if self.root:
            return self.get_min(node.leftChild)

        return node.data

    def traverse_in_order(self, node):
        
        if node.leftChild:
            self.traverse_in_order(node.leftChild)

            print('%' % node.data)

            if node.rightChild:
                self.traverse_in_order(node.rightChild)

bst = BinarySearchTree
bst.insert(10)
bst.insert(5)
bst.insert(-5)
bst.insert(1)
bst.insert(99)
bst.insert(34)
bst.insert(1000)

bst.remove(99)

bst.traverse()