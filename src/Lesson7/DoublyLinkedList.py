class Node:
    def __init__(self, data):
        self.__data = data
        self.__prev = None
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, d):
        self.__data = d

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, p):
        if type(p) != Node and p is not None:
            raise DoubleLinkedListError("Prev is node type")
        self.__prev = p

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, n):
        if type(n) != Node and n is not None:
            raise DoubleLinkedListError("Next is node type")
        self.__next = n


class DoublyLinkedList:
    def __init__(self, data):
        self.__head = Node(data)
        self.__tail = self.__head

    def __repr__(self):
        res = ''
        node = self.__head
        while node:
            res += f"{node.data} "
            node = node.next
        return res

    def insert_at_head(self, data):
        node = Node(data)
        node.next = self.__head
        self.__head.prev = node
        self.__head = node

    def insert_at_tail(self, data):
        node = Node(data)
        node.prev = self.__tail
        self.__tail.next = node
        self.__tail = node

    def delete_at_head(self):
        self.__head = self.__head.next
        self.__head.prev = None

    def delete_at_tail(self):
        self.__tail = self.__tail.prev
        self.__tail.next = None

    def search(self, dataa):
        node = self.__head
        i = 0
        while node and node.data != dataa:
            i += 1
            node = node.next
        return i


class DoubleLinkedListError(Exception):
    pass


dl = DoublyLinkedList(5)
dl.insert_at_tail(6)
dl.insert_at_tail(9)
dl.insert_at_tail(77)
dl.insert_at_head(554)
dl.insert_at_head(0)
dl.insert_at_head(11)
dl.insert_at_head(6)
dl.delete_at_head()
dl.delete_at_tail()
print(dl)
print(dl.search(554))
