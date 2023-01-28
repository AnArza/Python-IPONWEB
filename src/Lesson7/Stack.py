class Stack:
    def __init__(self, max_size):
        self.list = []
        self.head = -1
        self.tail = -1
        self.max_size = max_size

    def __repr__(self):
        return f"{self.list}"

    def push(self, el):
        if self.is_empty() and self.tail + 1 < self.max_size:
            self.head += 1
        if self.tail + 1 < self.max_size:
            self.list.append(el)
            self.tail += 1
        else:
            raise StackError("Queue has filled.")

    def pop(self):
        if not self.is_empty():
            save_tail = self.list[self.head]
            self.list.pop(self.tail)
            self.tail -= 1
            return save_tail
        else:
            raise StackError("Queue is empty.")

    def is_empty(self):
        return len(self.list) == 0


class StackError(Exception):
    pass


p = Stack(7)
# q.pop()
p.push(5)
p.push(99)
p.pop()
p.push(54)
p.push(65)
p.push(5)
print(p)
