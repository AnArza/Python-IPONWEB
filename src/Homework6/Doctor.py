from company_job_person import Person, PersonError
from money import *


class Doctor(Person):
    def __init__(self, name, surname, gender, age, address, department, profession, patronymic, salary):
        super().__init__(name, surname, gender, age, address, [])
        if type(department) != str or type(profession) != str:
            raise DoctorError("Doctor's department and profession should be strings.")
        if type(patronymic) != str:
            raise DoctorError("Doctor's patronymic should be string.")
        if type(salary) != Money:
            raise DoctorError("Doctor's salary should be Money type.")
        self.__department = department
        self.__profession = profession
        self.__patronymic = patronymic
        self.__salary = salary

    def __repr__(self):
        return f"This is {self.__profession} {self.name} {self.__patronymic} {self.surname}. He/She works at {self.__department} and earns {self.__salary} a month."

    @property
    def department(self):
        return self.__department

    @department.setter
    def department(self, d):
        if type(d) != str:
            raise DoctorError("Doctor's department should be string.")
        self.__department = d

    @property
    def profession(self):
        return self.__profession

    @profession.setter
    def profession(self, prof):
        if type(prof) != str:
            raise DoctorError("Doctor's profession should be string.")
        self.__profession = prof

    @property
    def patronymic(self):
        return self.__patronymic

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, s):
        if type(s) != Money:
            raise DoctorError("Doctor's salary should be Money type.")
        self.__salary = s


class DoctorError(Exception):
    def __init__(self, message):
        super().__init__(message)


d = Doctor('Narine', 'Harutyunyan', 'Female', 54, 'Kapan city', "IDK", 'family doctor', 'Karleni', Money(1500, 'EUR'))

print(d)
