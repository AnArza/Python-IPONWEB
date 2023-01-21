# Classes

# Task 6

class Company:
    def __init__(self, company_name, founded_at, employees_count):
        self.company_name = company_name
        self.__founded_at = founded_at
        self.employees_count = employees_count
        self.new_employees = set()

    def __repr__(self):
        return "{} was founded in {}. It has {} employees.".format(self.company_name, self.__founded_at,
                                                                   self.employees_count)


class Job:
    def __init__(self, company, salary, experience_year, position):
        self.company = company
        self.__salary = salary
        self.__experience_year = experience_year
        self.position = position

    def __repr__(self):
        return "This job is available in {},with {} AMD salary, you need {} years experience for {} position.".format(
            self.company.company_name, self.__salary, self.__experience_year, self.position)

    def change_salary(self, new_salary):
        self.__salary = new_salary

    def change_experience_year(self, new_exp_year):
        self.__experience_year = new_exp_year

    def change_position(self, new_pos):
        self.position = new_pos


class Person:
    def __init__(self, name, surname, gender, age, address, jobs):
        self.__name = name
        self.__surname = surname
        self.__gender = gender
        self.__age = age
        self.__address = address
        self.__friends = []
        self.__jobs = jobs
        for job in self.__jobs:
            if self not in job.company.new_employees:
                job.company.employees_count += 1
            job.company.new_employees.add(self)

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

    def display_jobs(self):
        return [f'{job.position} at {job.company.company_name}' for job in self.__jobs]


apple = Company('Apple', 1976, 36786)
synergy = Company('Synergy', 1997, 150)
aarki = Company('Aarki', 2010, 201)
google = Company('Google', 1998, 156500)
iponweb = Company('IPONWEB', 2001, 270)

# print(iponweb)
# print(google)

f_dev_apple = Job(apple, 750000, 3, "Front-End Developer")
f_dev_synergy = Job(synergy, 300000, 0.5, "Front-End Developer")
f_dev_aarki = Job(aarki, 400000, 2, "Front-End Developer")
b_dev_google = Job(google, 1000000, 5, 'Back-End Developer')
b_dev_iponweb = Job(iponweb, 650000, 4, 'Back-End Developer')
b_dev_synergy = Job(synergy, 500000, 3, 'Back-End Developer')
full_stack_dev_aarki = Job(aarki, 2000000, 4, 'Full-Stack Developer')
ml_engineer_aarki = Job(aarki, 2200000, 4, 'Machine Learning Engineer')
ml_engineer_google = Job(google, 3000000, 5, 'Machine Learning Engineer')
ml_engineer_iponweb = Job(iponweb, 2000000, 4, 'Machine Learning Engineer')
project_manager_synergy = Job(synergy, 350000, 2, 'Project Manager')
project_manager_google = Job(google, 550000, 3, 'Project Manager')
db_admin_iponweb = Job(iponweb, 570000, 1, "DataBase Administrator")

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
# hrach.add_job(ml_engineer_iponweb)
# print(hrach.display_jobs())
# print(agnes.display_jobs())
# hrach.remove_job(project_manager_google)
# print(hrach.display_jobs())
# print(agnes.display_jobs())
#
# f_dev_apple.change_experience_year(6)
# f_dev_apple.change_salary(989898)
# print(f_dev_apple)


# Task 7

class Date:
    months_days = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }

    def __init__(self, year, month, day):
        self.__year = year
        self.__month = month
        self.__day = day

    def __repr__(self):
        return f'{self.__day}.{self.__month}.{self.__year}'

    def add_day(self, days_count):
        for d in range(days_count):
            if self.__is_leap_year():
                Date.months_days[2] = 29
            else:
                Date.months_days[2] = 28
            # year passed
            if self.__month == 12 and self.__day == Date.months_days[12]:
                self.__year += 1
                self.__day = 1
                self.__month = 1
            # month passed
            elif self.__day == Date.months_days[self.__month]:
                self.__day = 1
                self.__month += 1
            else:
                self.__day += 1

    def add_month(self, months_count):
        month_diff = months_count % 12
        res_month = (self.__month + month_diff) % 12
        if res_month == 0:
            res_month = 12
        one_more_year = 0
        if self.__month + month_diff != res_month:
            one_more_year = 1
        years_count = months_count // 12
        # adding the years
        self.__year += (years_count + one_more_year)
        # normal case
        if self.__day <= Date.months_days[res_month]:
            self.__month = res_month
        # december 30 -> february 28/29 // february and leap year case
        elif res_month == 2 and self.__day in [29, 30, 31]:
            self.__month = res_month
            if self.__is_leap_year():
                self.__day = 29
            else:
                self.__day = 28
        # march 31 -> april 30  // months passed from month's last day
        elif self.__day == Date.months_days[self.__month]:
            self.__month = res_month
            self.__day = Date.months_days[res_month]

    def add_year(self, years_count):
        self.__year += years_count
        if self.__month == 2 and self.__day == 29 and not self.__is_leap_year():
            self.__day = 28

    def __is_leap_year(self):
        return self.__year % 4 == 0


# date = Date(2021, 1, 1)
# date = Date(2003, 10, 1)
# date = Date(2004, 2, 29)
date = Date(2019, 1, 27)
print(date)
date.add_month(1)
date.add_year(1)
date.add_day(2)
# date.add_month(25)
# date.add_day(59)
# date.add_month(40)
# date.add_day(30)
# date.add_year(5)
print(date)


class Time:
    def __init__(self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def __repr__(self):
        return f'{self.__hour}:{self.__minute}:{self.__second}'

    def add_second(self, s):
        hours = s // 3600
        mins = s // 60 - hours * 60
        secs = s - hours * 3600 - mins * 60
        self.__hour += hours
        self.__minute += mins
        self.__second += secs
        if self.__second >= 60:
            self.__minute += 1
            self.__second %= 60
        if self.__minute >= 60:
            self.__hour += 1
            self.__minute %= 60
        if self.__hour >= 24:
            self.__hour %= 24

    def add_minute(self, m):
        hours = m // 60
        mins = m - hours * 60
        self.__hour += hours
        self.__minute += mins
        if self.__minute >= 60:
            self.__hour += 1
            self.__minute %= 60
        if self.__hour >= 24:
            self.__hour %= 24

    def add_hour(self, h):
        self.__hour += h
        if self.__hour >= 24:
            self.__hour %= 24

    @classmethod
    def sum(cls, t1, t2):
        t1.add_second(t2.__second)
        t1.add_minute(t2.__minute)
        t1.add_hour(t2.__hour)
        return t1

# time = Time(4, 30, 4)
# print(time)
# time.add_second(59)
# time.add_minute(35)
# print(time)
#
# print(Time.sum(Time(3, 56, 41), Time(13, 5, 5)))
# print(Time.sum(Time(23, 56, 41), Time(0, 5, 5)))
