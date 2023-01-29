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


class AnimalFactory:
    @staticmethod
    def create_animal(animal):
        if animal == "Tiger":
            return Tiger()
        if animal == "Snake":
            return Snake()
        if animal == "Cow":
            return Cow()
        raise AnimalError(f"{animal} is not animal")


class AnimalError(Exception):
    pass


choice = input("What kind of animal do you wanna create?\n")
animal = AnimalFactory.create_animal(choice)
animal.voice()
