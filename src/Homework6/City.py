from company_job_person import *


class City:
    def __init__(self, name, mayor, population, language):
        if type(name) != str:
            raise CityError("The city name should be string.")
        if type(mayor) != Person:
            raise PersonError("The city mayor should be Person type.")
        if type(population) != int or population < 0:
            raise CityError("The city's population should be positive integer.")
        if type(language) != str:
            raise CityError("The language should be string.")
        self.__name = name
        self.__mayor = mayor
        self.__population = population
        self.__language = language

    def __repr__(self):
        return f"The {self.__name} city's population is {self.__population}. It's mayor is {self.__mayor.name} " \
               f"{self.__mayor.surname}. They speak {self.__language} there."

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, n):
        if type(n) != str:
            raise CityError("The city name should be string.")
        self.__name = n

    @property
    def mayor(self):
        return self.__mayor

    @mayor.setter
    def mayor(self, m):
        if type(m) != Person:
            raise CityError("The city mayor should be Person type.")
        self.__mayor = m

    @property
    def population(self):
        return self.__population

    @population.setter
    def population(self, p):
        if type(p) != int or p < 0:
            raise CityError("The city's population should be positive integer.")
        self.__population = p

    @property
    def language(self):
        return self.__language


class CityError(Exception):
    def __init__(self, message):
        super().__init__(message)


kapan = City("Kapan", magda, 45000, "Armenian")
kapan.mayor = hrach

# print(kapan)
