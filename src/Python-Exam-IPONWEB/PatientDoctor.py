from Homework6.DateTime import Date, Time, DateTime


class Patient:
    def __init__(self, name, surname, age, gender):
        if type(name) != str or type(surname) != str:
            raise PersonError("Person's name and surname should be strings.")
        if gender not in ['M', 'F']:
            raise PersonError('A person can be either male of female.')
        if type(age) != int or not 17 < age < 101:
            raise PersonError('The age of patient should be integer between 18 and 100.')
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.__gender = gender

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @property
    def gender(self):
        return self.__gender

    @property
    def age(self):
        return self.__age

    def __repr__(self):
        return f"{self.name} {self.surname} - {self.gender}, {self.age} years old."

    def __ne__(self, other):
        return not (
                self.__name == other.__name and self.__surname == other.__surname and self.__age == other.__age and self.__gender == other.__gender)


class Doctor:
    def __init__(self, name, surname):
        if type(name) != str or type(surname) != str:
            raise PersonError("Person's name and surname should be strings.")
        # if type(schedule) != dict:
        #     raise ScheduleError("Schedule should be a dictionary.")
        # for key in schedule.keys():
        #     if type(key) != DateTime:
        #         raise ScheduleError("Schedule's key is DateTime type.")
        #     if type(schedule[key]) != Patient:
        #         raise ScheduleError("Schedule's value is Patient type.")
        self.__name = name
        self.__surname = surname
        self.__schedule = {}

    def __repr__(self):
        return f"Doctor {self.__name}  {self.__surname} \nSchedule {self.__schedule}"

    def register_patient(self, patient, dt):
        if type(patient) != Patient or type(dt) != DateTime:
            raise ScheduleError("Invalid Patient or DateTime")
        if dt.time.hour < 9 or dt.time.hour > 16:
            raise ScheduleError("The register time is between 9 and 16.")
        if dt.time.minute != 30 and dt.time.minute != 0 or dt.time.second != 0:
            raise ScheduleError("You should register at strict times")
        if patient in self.__schedule.values():
            print(f"Patient {patient.name} already registered")
        if dt in self.__schedule.keys():
            print(f"Datetime {dt} already taken")
        if dt not in self.__schedule.keys() and dt.time and patient not in self.__schedule.values():
            self.__schedule[dt] = patient
            print(f"Patient {patient.name} successfully registered at {dt}")

    def is_free(self, dt):
        if dt.time.hour < 9 or dt.time.hour > 16:
            raise ScheduleError("The register time is between 9 and 16.")
        if dt.time.minute != 30 and dt.time.minute != 0 or dt.time.second != 0:
            raise ScheduleError("You should register at strict times")
        if dt not in self.__schedule.keys():
            return True
        return False

    def is_registered(self, patient):
        if type(patient) != Patient or type(dt) != DateTime:
            raise ScheduleError("Invalid Patient or DateTime")
        if patient in self.__schedule.values():
            return True
        return False


class PersonError(Exception):
    pass


class ScheduleError(Exception):
    pass


ani = Patient('Ani', 'Arzumanyan', 19, 'F')
magda = Patient('Magda', 'Gyurjyan', 20, 'F')

hrach = Patient('Hrach', 'Arzumanyan', 21, 'M')

dt = DateTime(Date(2021, 3, 31), Time(9, 30, 0))
other = DateTime(Date(2022, 7, 12), Time(16, 0, 0))
dt2 = DateTime(Date(2021, 3, 31), Time(12, 0, 0))

agnes = Doctor('Agnes', 'Muradyan')

agnes.register_patient(ani, dt)
print(agnes.is_free(other))
print(agnes.is_registered(magda))
agnes.register_patient(magda, other)
agnes.register_patient(magda, dt2)
agnes.register_patient(hrach, dt2)
