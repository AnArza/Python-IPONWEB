from company_job_person import *
from DateTime import Date, DateError
from City import City, CityError, kapan


class University:
    def __init__(self, name, founded_at, rector, city):
        if type(name) != str:
            raise UniversityError("University name should be string.")
        if type(founded_at) != Date:
            raise DateError("Founded at is a Date.")
        if type(rector) != Person:
            raise PersonError("Rector is a Person.")
        if type(city) != City:
            raise CityError("The  uni's city should be City type.")
        self.__name = name
        self.__founded_at = founded_at
        self.__rector = rector
        self.__city = city

    def __repr__(self):
        return f"The {self.__name} university was founded at {self.__founded_at} in {self.__city.name}."

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, n):
        if type(n) != str:
            raise UniversityError("University name should be string.")
        self.__name = n

    @property
    def founded_at(self):
        return self.__founded_at

    @property
    def rector(self):
        return self.__rector

    @rector.setter
    def rector(self, r):
        if type(r) != Person:
            raise UniversityError("Rector is a Person.")
        self.__rector = r

    @property
    def city(self):
        return self.__city


class UniversityError(Exception):
    def __init__(self, message):
        super().__init__(message)


harvard = University('Harvard', Date(1636, 9, 8), Person('Lawrence', 'Bacow', 'Male', 71, 'USA', []),
                     City('Cambridge', Person("Sumbul", "Siddiqui", 'Female', 35, 'Cambridge', []), 117090, 'English'))

print(harvard)


class Teacher(Person):
    def __init__(self, name, surname, gender, age, address, university, faculty, experience, start_work_at, subject,
                 salary):
        super().__init__(name, surname, gender, age, address, [])
        if type(university) != University:
            raise UniversityError("University should be University type.")
        if type(faculty) != str:
            raise TeacherError("Faculty should be string.")
        if type(experience) != int or experience < 0:
            raise TeacherError("Experience should be positive integer.")
        if type(start_work_at) != Date:
            raise DateError("Start work at should be Date type.")
        if type(subject) != str:
            raise TeacherError("Subject should be string.")
        if type(salary) != Money:
            raise MoneyError("Salary should be money type.")
        self.__university = university
        self.__faculty = faculty
        self.__experience = experience
        self.__start_work_at = start_work_at
        self.__subject = subject
        self.__salary = salary

    def __repr__(self):
        return f"This teacher's name is {self.name} {self.surname}. He/She works at {self.__university.name} at " \
               f"{self.__faculty} as {self.__subject} professor."

    @property
    def experience(self):
        return self.__experience

    @experience.setter
    def experience(self, exp):
        if type(exp) != int or exp < 0:
            raise TeacherError("Experience should be positive integer.")

    @property
    def start_work_at(self):
        return self.__start_work_at

    @property
    def subject(self):
        return self.__subject

    @property
    def faculty(self):
        return self.__faculty

    @faculty.setter
    def faculty(self, f):
        if type(f) != str:
            raise TeacherError("Faculty should be string.")
        self.__faculty = f

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, s):
        if type(s) != Money:
            raise MoneyError("Salary should be money type.")
        self.__salary = s


class TeacherError(Exception):
    def __init__(self, message):
        super().__init__(message)


teacher = Teacher("John", "Smith", "Male", 54, 'Yeghegnadzor', harvard, 'Software Engineering', 15, Date(2007, 8, 25),
                  'Intro to Programming', Money(4500, 'USD'))

print(teacher)


class Student(Person):
    def __init__(self, name, surname, gender, age, address, university, faculty, course, started_at):
        super().__init__(name, surname, gender, age, address, [])
        if type(university) != University:
            raise UniversityError("University should be University type.")
        if type(faculty) != str:
            raise StudentError("Faculty should be string.")
        if type(course) != int or not 0 < course <= 6:
            raise StudentError("The course is a positive integer between 1 and 6.")
        if type(started_at) != Date:
            raise DateError("The started at should be Date type.")
        self.__university = university
        self.__faculty = faculty
        self.__course = course
        self.__started_at = started_at

    def __repr__(self):
        return f"{self.name} studies at {self.__university.name} at {self.__faculty} faculty at the {self.__course}th year."

    @property
    def university(self):
        return self.__university

    @university.setter
    def university(self, uni):
        if type(uni) != University:
            raise UniversityError("University should be University type.")
        self.__university = uni

    @property
    def faculty(self):
        return self.__faculty

    @faculty.setter
    def faculty(self, f):
        if type(f) != str:
            raise StudentError("Faculty should be string.")
        self.__faculty = f

    @property
    def course(self):
        return self.__course

    @course.setter
    def course(self, c):
        if type(c) != int or 0 < c <= 6:
            raise StudentError("The course is a positive integer between 1 and 6.")
        self.__course = c

    @property
    def started_at(self):
        return self.started_at


class StudentError(Exception):
    def __init__(self, message):
        super().__init__(message)


student = Student('Hrach', 'Arzumanyan', 'Male', 21, 'Lepsius 23',
                  University('AUA', Date(1991, 9, 21), Person('Cajik', 'Bacow', 'Male', 55, 'Armenia', []), kapan),
                  'Politics and Governance',
                  1,
                  Date(2022, 8, 25))

print(student)
