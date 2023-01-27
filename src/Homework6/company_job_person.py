from money import *


class Company:
    def __init__(self, company_name, founded_at, employees_count):
        self.__company_name = company_name
        self.__founded_at = founded_at
        self.__employees_count = employees_count
        self.__new_employees = set()
        if not (employees_count > 0 and type(employees_count) == int):
            raise CompanyError("Employees count should be a natural number.")
        if type(company_name) != str:
            raise CompanyError("Company name should be string.")
        if type(founded_at) != int:
            raise CompanyError("Founded at should be integer.")

    def __repr__(self):
        return "{} was founded in {}. It has {} employees.".format(self.__company_name, self.__founded_at,
                                                                   self.__employees_count)

    @property
    def company_name(self):
        return self.__company_name

    @property
    def employees_count(self):
        return self.__employees_count

    @employees_count.setter
    def employees_count(self, val):
        self.__employees_count = val

    @property
    def new_employees(self):
        return self.__new_employees


class CompanyError(Exception):
    def __init__(self, message):
        super().__init__(message)


class Job:
    def __init__(self, company, salary, experience_year, position):
        self.__company = company
        self.__salary = salary
        self.__experience_year = experience_year
        self.__position = position
        if type(company) != Company:
            raise JobError("Job's company should be Company type.")
        if (salary.amount < 0 or type(salary) != Money) or (
                experience_year < 0 or type(experience_year) not in [int, float]):
            raise JobError("Job salary and experience year should be positive numbers.")
        if type(position) != str:
            raise JobError("Job's position should be string.")

    def __repr__(self):
        return "This job is available in {},with {} AMD salary, you need {} years experience for {} position.".format(
            self.__company.company_name, self.__salary, self.__experience_year, self.__position)

    def change_salary(self, new_salary):
        if type(new_salary) != Money:
            raise JobError("Job salary should be type Money.")
        self.__salary = new_salary

    def change_experience_year(self, new_exp_year):
        if new_exp_year < 0:
            raise JobError("Job experience year should be positive.")
        self.__experience_year = new_exp_year

    def change_position(self, new_pos):
        self.__position = new_pos

    @property
    def company(self):
        return self.__company

    @property
    def position(self):
        return self.__position


class JobError(Exception):
    def __init__(self, message):
        super().__init__(message)


class Person:
    def __init__(self, name, surname, gender, age, address, jobs):
        self.__name = name
        self.__surname = surname
        self.__gender = gender
        self.__age = age
        self.__address = address
        self.__friends = []
        self.__jobs = jobs
        if type(name) != str or type(surname) != str or type(address) != str:
            raise PersonError("Person's name, surname and address should be strings.")
        if gender not in ['Male', 'Female']:
            raise PersonError('A person can be either male of female.')
        if age < 0:
            raise PersonError('The age of person should be >= 0 .')
        if type(jobs) != list:
            raise PersonError('The jobs should be a list.')
        for job in self.__jobs:
            if self not in job.company.new_employees:
                job.company.employees_count += 1
            job.company.new_employees.add(self)

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    def __repr__(self):
        return "This is {} {}, his/her gender is {}.".format(self.__name, self.__surname, self.__gender)

    def add_friend(self, f):
        if f not in self.__friends:
            self.__friends.append(f)
            f.__friends.append(self)

    def remove_friend(self, f):
        if f in self.__friends:
            self.__friends.remove(f)
            f.__friends.remove(self)

    def display_friends(self):
        return [f'{friend.__name} {friend.__surname}' for friend in self.__friends]

    def add_job(self, j):
        if j not in self.__jobs:
            self.__jobs.append(j)
        if self not in j.company.new_employees:
            j.company.employees_count += 1
        j.company.new_employees.add(self)

    def remove_job(self, j):
        if j in self.__jobs:
            self.__jobs.remove(j)
        if self in j.company.new_employees:
            j.company.employees_count -= 1
            j.company.new_employees.remove(self)
        for job in self.__jobs:
            if self not in job.company.new_employees:
                job.company.employees_count += 1
            job.company.new_employees.add(self)

    def display_jobs(self):
        return [f'{job.position} at {job.company.company_name}' for job in self.__jobs]


class PersonError(Exception):
    def __init__(self, message):
        super().__init__(message)


apple = Company('Apple', 1976, 36786)
synergy = Company('Synergy', 1997, 150)
aarki = Company('Aarki', 2010, 201)
google = Company('Google', 1998, 156500)
iponweb = Company('IPONWEB', 2001, 270)

# Exception case
# arzumanyans = Company('Arzumanyans', 2023, 54.2)

# print(iponweb)
# print(google)

f_dev_apple = Job(apple, Money(750000, 'AMD'), 3, "Front-End Developer")
f_dev_synergy = Job(synergy, Money(300000, 'AMD'), 0.5, "Front-End Developer")
f_dev_aarki = Job(aarki, Money(400000, 'AMD'), 2, "Front-End Developer")
b_dev_google = Job(google, Money(1000000, 'AMD'), 5, 'Back-End Developer')
b_dev_iponweb = Job(iponweb, Money(650000, 'AMD'), 4, 'Back-End Developer')
b_dev_synergy = Job(synergy, Money(500000, 'AMD'), 3, 'Back-End Developer')
full_stack_dev_aarki = Job(aarki, Money(2000000, 'AMD'), 4, 'Full-Stack Developer')
ml_engineer_aarki = Job(aarki, Money(2200000, 'AMD'), 4, 'Machine Learning Engineer')
ml_engineer_google = Job(google, Money(3000000, 'AMD'), 5, 'Machine Learning Engineer')
ml_engineer_iponweb = Job(iponweb, Money(2000000, 'AMD'), 4, 'Machine Learning Engineer')
project_manager_synergy = Job(synergy, Money(350000, 'AMD'), 2, 'Project Manager')
project_manager_google = Job(google, Money(550000, 'AMD'), 3, 'Project Manager')
db_admin_iponweb = Job(iponweb, Money(570000, 'AMD'), 1, "DataBase Administrator")

# Exception case
# invalid_job = Job('google', 7, 5, 'Hehe')

ani = Person('Ani', 'Arzumanyan', 'Female', 19, 'Gr. Arzumanyan 3/13,Kapan,Armenia',
             [b_dev_iponweb, full_stack_dev_aarki])
hrach = Person('Hrach', 'Arzumanyan', 'Male', 21, 'Gr. Arzumanyan 3/13,Kapan,Armenia',
               [project_manager_google, f_dev_aarki])
asik = Person('Asya', 'Arzumanyan', 'Female', 26, 'Bangladesh,Yerevan',
              [full_stack_dev_aarki, ml_engineer_google])
eva = Person('Eva', 'Voskanyan', 'Female', 19, 'Monument,Yerevan',
             [b_dev_synergy, b_dev_google, ml_engineer_google])
agnes = Person('Agnesa', 'Muradyan', 'Female', 20, 'Masiv,Yerevan', [db_admin_iponweb, ml_engineer_aarki])
magda = Person('Magda', 'Gyurjyan', 'Female', 20, 'Masiv,Yerevan', [b_dev_iponweb, ml_engineer_aarki])
randy = Person('Randy', 'Cardwell', 'Male', 65, 'Arizona, USA', [project_manager_synergy])

# Exception case
# invalid_person = Person('Name', 'Nameyan', 'other', 2, 'somwhere', 'd')


# ani.add_friend(hrach)
# ani.add_friend(asik)
# eva.add_friend(ani)
# magda.add_friend(agnes)
# print(ani.display_friends())
# print(hrach.display_friends())
# print(agnes.display_friends())
# hrach.remove_friend(ani)
# print(hrach.display_friends())
# print(ani.display_friends())
# print(agnes.display_friends())
#
# print(iponweb)
# print(google)
#
# print(hrach.display_jobs())
# print(agnes.display_jobs())
#
# hrach.add_job(ml_engineer_iponweb)
#
# print(hrach.display_jobs())
#
# print(agnes.display_jobs())
#
# eva.remove_job(project_manager_google)
#
# print(iponweb)
# print(google)
#
# print(hrach.display_jobs())
# print(agnes.display_jobs())
#
# f_dev_apple.change_experience_year(6)
# Exception case
# f_dev_apple.change_salary(Money(-5, 'AMD'))
# print(f_dev_apple)
