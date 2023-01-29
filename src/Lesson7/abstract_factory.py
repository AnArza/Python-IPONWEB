from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def voice(self):
        pass


class Tiger(Animal):
    def voice(self):
        print("Rrrrr")


class Snake(Animal):
    def voice(self):
        print("Sssss")


class Cow(Animal):
    def voice(self):
        print("Muuuuu")


class Shark(Animal):
    def voice(self):
        print("Haamp")


class Octopus(Animal):
    def voice(self):
        print("Quack")


class Eagle(Animal):
    def voice(self):
        print("Piyuuuu")


class Bat(Animal):
    def voice(self):
        print("Infravoice")


class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        pass

    @staticmethod
    def create_animal_factory(factory_type):
        if factory_type == "Land":
            return LandAnimalFactory()
        if factory_type == "Sea":
            return SeaAnimalFactory()
        if factory_type == "Air":
            return AirAnimalFactory()


class LandAnimalFactory(AnimalFactory):
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "Tiger":
            return Tiger()
        if animal_type == "Snake":
            return Snake()
        if animal_type == "Cow":
            return Cow()
        raise AnimalError(f"{animal_type} is not animal")


class SeaAnimalFactory(AnimalFactory):
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "Shark":
            return Shark()
        if animal_type == "Octopus":
            return Octopus()
        raise AnimalError(f"{animal_type} is not animal")


class AirAnimalFactory(AnimalFactory):
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "Bat":
            return Bat()
        if animal_type == "Eagle":
            return Eagle()
        raise AnimalError(f"{animal_type} is not animal")


class AnimalError(Exception):
    pass


factory = AnimalFactory.create_animal_factory("Air")
animal = factory.create_animal("Bat")
animal.voice()
