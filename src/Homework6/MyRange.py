class MyRange:
    def __init__(self, current, end, step):
        if type(current) != int and type(current) != float or type(end) != int and type(end) != float or type(
                step) != int and type(step) != float:
            raise MyRangeError
        if current < end and step < 0 or current > end and step > 0 or current == end and step != 0:
            raise MyRangeError
        self.__current = current
        self.__end = end
        self.__step = step
        # self.range_copy = copy.deepcopy(self)

    def __repr__(self):
        return f"Current: {self.__current}\nEnd: {self.__end}\nStep: {self.__step}"

    def __iter__(self):
        return self

    def __next__(self):
        if self.__step == 0:
            print(self.__current)
            raise StopIteration
        elif self.__step > 0:
            if self.__current > self.__end:
                raise StopIteration
        elif self.__step < 0:
            if self.__current < self.__end:
                raise StopIteration
        self.__current += self.__step
        return self.__current - self.__step

    def __len__(self):
        length = 0
        save_curr = self.__current
        for num in self:
            length += 1
        self.__current = save_curr
        return length

    def __getitem__(self, item):
        if type(item) != int or item < 0 or item >= len(self):
            raise MyRangeError("The index is out of range.")
        save_curr = self.__current
        i = 0
        for num in self:
            if i == item:
                self.__current = save_curr
                return num
            i += 1

    def __reversed__(self):
        new_end = self.__current
        new_curr = self[len(self) - 1]
        return MyRange(new_curr, new_end, -self.__step)


class MyRangeError(Exception):
    def __init__(self, message="Invalid range"):
        super().__init__(message)


r = MyRange(2, 15, 3)

print(r)
print("\nRange length", len(r))
print("Range's 3 index element", r[3])

revr = reversed(r)

print("\nNormal order")
for i in r:
    print(i, end=' ')
print("\nReversed order")
for i in revr:
    print(i, end=' ')
