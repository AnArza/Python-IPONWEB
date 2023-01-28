from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, animal_type):
        self.animal_type = animal_type

    @abstractmethod
    def voice(self):
        pass


class Tiger(Animal):
    def __init__(self):
        super().__init__("Tiger")

    def voice(self):
        print("Rrrrr")


class Snake(Animal):
    def __init__(self):
        super().__init__("Snake")

    def voice(self):
        print("Sssss")


class Cow(Animal):
    def __init__(self):
        super().__init__("Cow")

    def voice(self):
        print("Muuuuu")


c = Cow()
print(c.animal_type)
c.voice()
print()
t = Tiger()
print(t.animal_type)
t.voice()
print()
s = Snake()
print(s.animal_type)
s.voice()
