class Node:
    def __init__(self, data):
        if type(data) != int:
            raise NodeError("Node data is integer")
        self.__data = data
        self.__left = None
        self.__right = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, d):
        if type(d) != int:
            raise NodeError("Node data is integer")
        self.__data = d

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, l):
        if type(l) != Node and l is not None:
            raise NodeError("Left is node type")
        self.__left = l

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, r):
        if type(r) != Node and r is not None:
            raise NodeError("Right is node type")
        self.__right = r


class BinarySearchTree:
    def __init__(self):
        self.__root = None

    @property
    def root(self):
        return self.__root

    @root.setter
    def root(self, r):
        if type(r) != Node and r is not None:
            raise NodeError("BST root is node type.")
        self.__root = r

    def search(self, data):
        if self.__root is None:
            raise NodeError('The tree is empty.')
        node = self.__root
        while node and node.data != data:
            if data < node.data:
                node = node.left
            else:
                node = node.right
        if node is None:
            raise NodeError('No such node in the tree')
        return node

    def insert(self, data):
        if type(data) != int:
            raise NodeError("Node data is integer")
        if self.__root is None:
            self.__root = Node(data)
            return None
        prev = None
        node = self.__root
        while node:
            if data < node.data:
                prev = node
                node = node.left
            elif data > node.data:
                prev = node
                node = node.right
            else:
                raise NodeError(f"{data} already exists in the tree.")
        if data < prev.data:
            prev.left = Node(data)
        elif data > prev.data:
            prev.right = Node(data)

    def delete(self, node, data):
        if type(node) != Node and node is not None:
            raise NodeError("The given node should be Node type.")
        if self.__root is None:
            raise NodeError('The tree is empty.')
        prev = None
        current = node
        while current and current.data != data:
            if data < current.data:
                prev = current
                current = current.left
            elif data > current.data:
                prev = current
                current = current.right
        if current is None:
            raise NodeError('No such node in the tree')
        if not current.left and not current.right:
            if current == prev.left:
                prev.left = None
            else:
                prev.right = None
        elif not current.left and current.right:
            if current == prev.left:
                prev.left = current.right
            else:
                prev.right = current.right
        elif not current.right and current.left:
            if current == prev.left:
                prev.left = current.left
            else:
                prev.right = current.left
        else:
            successor = current.right
            while successor.left:
                successor = successor.left
            save_succ_data = successor.data
            self.delete(current, successor.data)
            current.data = save_succ_data
        return node

    def inorder_traversal(self, node):
        if type(node) != Node and node is not None:
            raise NodeError("The given node should be Node type.")
        if node:
            self.inorder_traversal(node.left)
            print(node.data)
            self.inorder_traversal(node.right)


class NodeError(Exception):
    pass


bst = BinarySearchTree()
bst.insert(15)
bst.insert(5)
bst.insert(10)
bst.insert(12)
bst.insert(20)
bst.insert(13)
bst.insert(4)
bst.inorder_traversal(bst.root)
print("\nAfter")
bst.delete(bst.root, 15)
bst.inorder_traversal(bst.root)
