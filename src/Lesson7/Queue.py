class Queue:
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
            raise QueueError("Queue has filled.")

    def pop(self):
        if not self.is_empty():
            save_head = self.list[self.head]
            self.list.pop(self.head)
            self.tail -= 1
            return save_head
        else:
            raise QueueError("Queue is empty.")

    def is_empty(self):
        return len(self.list) == 0


class QueueError(Exception):
    pass


q = Queue(7)
# q.pop()
q.push(5)
q.push(99)
q.pop()
q.push(54)
q.push(65)
q.push(5)
print(q)
