class Node:
    def __init__(self, data):
        if type(data) != int and data is not None:
            raise NodeError("Node data is integer")
        self.__data = data
        self.__parent = None
        self.__left = None
        self.__right = None
        self.__color = 'red'

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, d):
        if type(d) != int:
            raise NodeError("Node data is integer")
        self.__data = d

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, p):
        if type(p) != Node and p is not None:
            raise NodeError("Parent is node type")
        self.__parent = p

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

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, c):
        if c not in ['black', 'red']:
            raise NodeError("The color is either black or red")
        self.__color = c


class NodeError(Exception):
    pass


class RedBlackTree:
    def __init__(self):
        self.__NIL = Node(None)
        self.__NIL.color = 'black'
        self.__NIL.left = None
        self.__NIL.right = None
        self.__root = self.NIL

    @property
    def NIL(self):
        return self.__NIL

    @NIL.setter
    def NIL(self, nil):
        if type(nil) != Node:
            raise NodeError("The NIL is Node type")
        self.__NIL = nil

    @property
    def root(self):
        return self.__root

    @root.setter
    def root(self, r):
        if type(r) != Node and r is not None:
            raise NodeError("BST root is node type.")
        self.__root = r

    def search(self, data):
        if type(data) != int:
            raise NodeError("Node data is integer")
        if self.root is None:
            raise NodeError('The tree is empty.')
        node = self.root
        while node and node.data != data:
            if data < node.data:
                node = node.left
            else:
                node = node.right
        if node is None or node == self.NIL:
            raise NodeError('No such node in the tree')
        return node

    def left_rotate(self, nodex):
        if type(nodex) != Node:
            raise NodeError("The node x is Node type")
        nodey = nodex.right
        nodex.right = nodey.left
        if nodey.left != self.NIL:
            nodey.left.parent = nodex
        nodey.parent = nodex.parent
        if nodex.parent == self.NIL:
            self.root = nodey
        elif nodex.parent.left == nodex:
            nodex.parent.left = nodey
        else:
            nodex.parent.right = nodey
        nodey.left = nodex
        nodex.parent = nodey

    def right_rotate(self, nodex):
        if type(nodex) != Node:
            raise NodeError("The node x is Node type")
        nodey = nodex.left
        nodex.left = nodey.right
        if nodey.right != self.NIL:
            nodey.right.parent = nodex
        nodey.parent = nodex.parent
        if nodex.parent == self.NIL:
            self.root = nodey
        elif nodex.parent.left == nodex:
            nodex.parent.left = nodey
        else:
            nodex.parent.right = nodey
        nodey.right = nodex
        nodex.parent = nodey

    def insert_fixup(self, node):
        while node.parent.color == 'red':
            if node.parent == node.parent.parent.left:
                nodey = node.parent.parent.right
                if nodey.color == 'red':
                    node.parent.color = 'black'
                    nodey.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self.right_rotate(node.parent.parent)
            else:
                nodey = node.parent.parent.left
                if nodey.color == 'red':
                    node.parent.color = 'black'
                    nodey.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self.left_rotate(node.parent.parent)
        self.root.color = 'black'

    def insert(self, data):
        if type(data) != int:
            raise NodeError("Node data is integer")
        node = Node(data)
        nodey = self.NIL
        nodex = self.root
        while nodex != self.NIL:
            nodey = nodex
            if node.data < nodex.data:
                nodex = nodex.left
            else:
                nodex = nodex.right
        node.parent = nodey
        if nodey == self.NIL:
            self.root = node
        elif node.data < nodey.data:
            nodey.left = node
        else:
            nodey.right = node
        node.left = self.NIL
        node.right = self.NIL
        node.color = 'red'
        self.insert_fixup(node)

    def inorder_traversal(self, node):
        if type(node) != Node and node is not None:
            raise NodeError("The given node should be Node type.")
        if node and node != self.NIL:
            self.inorder_traversal(node.left)
            print(f"{node.data} {node.color}")
            self.inorder_traversal(node.right)

    def transplant(self, u, v):
        if (type(u) != Node and u is not None) or (type(v) != Node and v is not None):
            raise NodeError("The given nodes u and v should be Node type.")
        if u.parent == self.NIL or not u.parent:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def delete_fixup(self, node):
        while node != self.root and node.color == 'black':
            if node == node.parent.left:
                nodex = node.parent.right
                if nodex.color == 'red':
                    nodex.color = 'black'
                    node.parent.color = 'red'
                    self.left_rotate(node.parent)
                    nodex = node.parent.right
                if nodex.left.color == 'black' and nodex.right.color == 'black':
                    nodex.color = 'red'
                    node = node.parent
                else:
                    if nodex.right.color == 'black':
                        nodex.left.color = 'black'
                        nodex.color = 'red'
                        self.right_rotate(nodex)
                        nodex = node.parent.right
                    nodex.color = node.parent.color
                    node.parent.color = 'black'
                    nodex.right.color = 'black'
                    self.left_rotate(node.parent)
                    node = self.root
            else:
                nodex = node.parent.left
                if nodex.color == 'red':
                    nodex.color = 'black'
                    node.parent.color = 'red'
                    self.right_rotate(node.parent)
                    nodex = node.parent.left
                if nodex.right.color == 'black' and nodex.left.color == 'black':
                    nodex.color = 'red'
                    node = node.parent
                else:
                    if nodex.left.color == 'black':
                        nodex.right.color = 'black'
                        nodex.color = 'red'
                        self.left_rotate(nodex)
                        nodex = node.parent.left
                    nodex.color = node.parent.color
                    node.parent.color = 'black'
                    nodex.left.color = 'black'
                    self.right_rotate(node.parent)
                    node = self.root
        node.color = 'black'

    def delete(self, data):
        if type(data) != int:
            raise NodeError("Node data is integer")
        node = self.search(data)
        nodey = node
        save_nodey_color = nodey.color
        if node.left == self.NIL:
            nodex = node.right
            self.transplant(node, node.right)
        elif node.right == self.NIL:
            nodex = node.left
            self.transplant(node, node.left)
        else:
            nodey = node.right
            while nodey and nodey.left != self.NIL:
                nodey = nodey.left
            save_nodey_color = nodey.color
            nodex = nodey.right
            if nodey.parent == node:
                nodex.parent = nodey
            else:
                self.transplant(nodey, nodey.right)
                nodey.right = node.right
                nodey.right.parent = nodey
            self.transplant(node, nodey)
            nodey.left = node.left
            nodey.left.parent = nodey
            nodey.color = node.color
        if save_nodey_color == 'black':
            self.delete_fixup(nodex)


rbt = RedBlackTree()
rbt.insert(15)
rbt.insert(5)
rbt.insert(10)
rbt.insert(12)
rbt.insert(20)
rbt.insert(13)
rbt.insert(4)
rbt.inorder_traversal(rbt.root)
print("\nAfter")
rbt.delete(15)
rbt.delete(5)
rbt.inorder_traversal(rbt.root)
