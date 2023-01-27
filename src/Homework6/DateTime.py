import copy


class Date:
    months_days = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }

    def __init__(self, year, month, day):
        self.__year = year
        self.__month = month
        self.__day = day
        if type(year) != int or type(month) != int or type(day) != int:
            raise DateError('Year, month and day should be integers.')
        if not self.is_leap_year():
            if not (1 <= month <= 12 and 1 <= day <= Date.months_days[month]):
                raise DateError
        elif self.is_leap_year():
            if month == 2 and not 1 <= day <= 29:
                raise DateError
            if month != 2:
                if not (1 <= month <= 12 and 1 <= day <= Date.months_days[month]):
                    raise DateError

    def __repr__(self):
        return f'{self.__day}.{self.__month}.{self.__year}'

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, y):
        self.__year = y

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, m):
        if type(m) != int or not (1 <= m <= 12):
            raise DateError('Invalid month')
        self.__month = m

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, d):
        if type(d) != int:
            raise DateError('Invalid day')
        if self.__month == 2 and self.is_leap_year() and not 1 <= d <= 29:
            raise DateError('Invalid day')
        if not (1 <= d <= Date.months_days[self.__month]) and (self.__month != 2 and not self.is_leap_year()):
            raise DateError('Invalid day')
        self.__day = d

    def add_day(self, days_count):
        if type(days_count) != int or days_count < 0:
            raise TimeError("Days added should be positive integer.")
        for d in range(days_count):
            if self.is_leap_year():
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
        if type(months_count) != int or months_count < 0:
            raise TimeError("Months added should be positive integer.")
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
            if self.is_leap_year():
                self.__day = 29
            else:
                self.__day = 28
        # march 31 -> april 30  // months passed from month's last day
        elif self.__day == Date.months_days[self.__month]:
            self.__month = res_month
            self.__day = Date.months_days[res_month]

    def add_year(self, years_count):
        if type(years_count) != int or years_count < 0:
            raise TimeError("Years added should be positive integer.")
        self.__year += years_count
        if self.__month == 2 and self.__day == 29 and not self.is_leap_year():
            self.__day = 28

    def is_leap_year(self):
        return self.__year % 4 == 0

    def __eq__(self, other):
        return self.year == other.year and self.month == other.month and self.day == other.day


class DateError(Exception):
    def __init__(self, message="Invalid date."):
        super().__init__(message)


# date = Date(2021, 1, 1)
# date = Date(2003, 10, 1)
# date = Date(2004, 2, 29)
# date = Date(2019, 1, 27)
# date = Date(2001, 2, 28)
# date.add_day(366)
# print(date)
#
# print(date)
# date.add_month(1)
# date.add_year(1)
# date.add_day(2)
# date.add_month(25)
# date.add_day(59)
# date.add_month(40)
# date.add_day(30)
# date.add_year(5)
# print(date)


# Exception case
# date = Date(2001, 2, 29)
# date = Date(2001, 13, 5)
# date = Date(2001, 5.4, 5)


class Time:
    def __init__(self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second
        if type(hour) != int or type(minute) != int or type(second) != int:
            raise TimeError("Hour, minute and second should be integers.")
        if not (0 <= hour < 24 and 0 <= minute < 60 and 0 <= second < 60):
            raise TimeError

    def __repr__(self):
        return f'{self.__hour}:{self.__minute}:{self.__second}'

    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, h):
        if type(h) != int:
            raise TimeError("Invalid hour")
        self.__hour = h

    @property
    def minute(self):
        return self.__minute

    @minute.setter
    def minute(self, m):
        if type(m) != int:
            raise TimeError("Invalid minute")
        self.__minute = m

    @property
    def second(self):
        return self.__second

    @second.setter
    def second(self, s):
        if type(s) != int:
            raise TimeError("Invalid second")
        self.__second = s

    def add_second(self, s):
        if type(s) != int or s < 0:
            raise TimeError("Second should be positive integer.")
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
        if type(m) != int or m < 0:
            raise TimeError("Minute should be positive integer.")
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
        if type(h) != int or h < 0:
            raise TimeError("Hour should be positive integer.")
        self.__hour += h
        if self.__hour >= 24:
            self.__hour %= 24

    @classmethod
    def sum(cls, t1, t2):
        if type(t1) != Time or type(t2) != Time:
            raise TimeError('You should add two Time type objects.')
        t1.add_second(t2.__second)
        t1.add_minute(t2.__minute)
        t1.add_hour(t2.__hour)
        return t1


class TimeError(Exception):
    def __init__(self, message="Invalid time."):
        super().__init__(message)


# time = Time(4, 30, 4)
# print(time)
# time.add_second(59)
# time.add_minute(35)
# print(time)
#
# print(Time.sum(Time(3, 56, 41), Time(13, 5, 5)))
# print(Time.sum(Time(23, 56, 41), Time(0, 5, 5)))

# Exception case
# time = Time(25, 6, 1)


class DateTime:
    def __init__(self, date, time):
        self.__date = date
        self.__time = time

    def __repr__(self):
        return f"The date is {self.__date} and the time is {self.__time}."

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, other_date):
        if type(other_date) != Date:
            raise DateError("The date that you want to set, should be Date type.")
        self.__date = other_date

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, other_time):
        if type(other_time) != Time:
            raise TimeError("The time that you want to set, should be Time type.")
        self.__time = other_time

    def add_year(self, years_count):
        self.__date.add_year(years_count)

    def add_month(self, months_count):
        self.__date.add_month(months_count)

    def add_day(self, days_count):
        self.__date.add_day(days_count)

    def add_hour(self, h):
        if type(h) != int or h < 0:
            raise TimeError("Added hour should be positive integer.")
        days = h // 24
        h %= 24
        self.add_day(days)
        if self.__time.hour + h >= 24:
            self.__date.add_day(1)
        self.__time.add_hour(h)

    def add_minute(self, m):
        if type(m) != int or m < 0:
            raise TimeError("Added minute should be positive integer.")
        days = m // (60 * 24)
        m %= (60 * 24)
        self.add_day(days)
        if self.__time.hour == 23 and self.__time.minute + m >= 60:
            self.__date.add_day(1)
        self.__time.add_minute(m)

    def add_second(self, s):
        if type(s) != int or s < 0:
            raise TimeError("Added second should be positive integer.")
        days = s // (60 * 60 * 24)
        s %= (60 * 60 * 24)
        self.add_day(days)
        if self.__time.hour == 23 and self.__time.minute == 59 and self.__time.second + s >= 60:
            self.__date.add_day(1)
        self.__time.add_second(s)

    def sub_year(self, years_count):
        if type(years_count) != int or years_count < 0:
            raise TimeError("Years count should be positive integer.")
        self.__date.year -= years_count
        if self.__date.month == 2 and self.__date.day == 29 and not self.__date.is_leap_year():
            self.__date.day = 28

    def sub_month(self, months_count):
        if type(months_count) != int or months_count < 0:
            raise TimeError("Months count should be positive integer.")
        month_diff = months_count % 12
        res_month = (self.__date.month - month_diff) % 12
        if res_month == 0:
            res_month = 12
        one_year_less = 0
        if self.__date.month - month_diff != res_month:
            one_year_less = 1
        years_count = months_count // 12
        # subtracting the years
        self.__date.year -= (years_count + one_year_less)
        # normal case
        if self.__date.day <= Date.months_days[res_month]:
            self.__date.month = res_month
        # march 28/29 -> february 28/29 // february and leap year case
        elif res_month == 2 and self.__date.day in [29, 30, 31]:
            self.__date.month = res_month
            if self.__date.is_leap_year():
                self.__date.day = 29
            else:
                self.__date.day = 28
        # march 31 -> april 30  // months passed from month's last day
        elif self.__date.day == Date.months_days[self.__date.month]:
            self.__date.month = res_month
            self.__date.day = Date.months_days[res_month]

    def sub_day(self, days_count):
        if type(days_count) != int or days_count < 0:
            raise TimeError("Days count should be positive integer.")
        for d in range(days_count):
            if self.__date.is_leap_year():
                Date.months_days[2] = 29
            else:
                Date.months_days[2] = 28
            # year subtracted
            if self.__date.month == 1 and self.__date.day == 1:
                self.__date.year -= 1
                self.__date.day = Date.months_days[12]
                self.__date.month = 12
            # month subtracted
            elif self.__date.day == 1:
                self.__date.month -= 1
                self.__date.day = Date.months_days[self.__date.month]
            else:
                self.__date.day -= 1

    def sub_hour(self, h):
        if type(h) != int or h < 0:
            raise TimeError("Hour should be positive integer.")
        days = h // 24
        h %= 24
        self.sub_day(days)
        if self.__time.hour - h < 0:
            self.sub_day(1)
        self.__time.hour = (self.__time.hour - h) % 24

    def sub_minute(self, m):
        if type(m) != int or m < 0:
            raise TimeError("Minute should be positive integer.")
        hours = m // 60
        mins = m - hours * 60
        self.sub_hour(hours)
        self.__time.minute -= mins
        if self.__time.minute < 0:
            self.sub_hour(1)
        self.__time.minute %= 60

    def sub_second(self, s):
        if type(s) != int or s < 0:
            raise TimeError("Second should be positive integer.")
        mins = s // 60
        secs = s - mins * 60
        self.sub_minute(mins)
        self.__time.second -= secs
        if self.__time.second < 0:
            self.sub_minute(1)
        self.__time.second %= 60

    def __add__(self, other):
        first = copy.deepcopy(self)
        first.add_second(other.__time.second)
        first.add_minute(other.__time.minute)
        first.add_hour(other.__time.hour)
        first.add_day(other.__date.day)
        first.add_month(other.__date.month)
        first.add_year(other.__date.year)
        return first

    def __sub__(self, other):
        days = 0
        if self.__date.year > other.__date.year or (
                self.__date.year == other.__date.year and self.__date.month > other.__date.month) or (
                self.__date.year == other.__date.year and self.__date.month == other.__date.month and
                self.__date.day >= other.__date.day):
            first = copy.deepcopy(other)
            while not first.__date == self.__date:
                days += 1
                first.add_day(1)
            if first.__time.hour < other.__time.hour or (
                    first.__time.hour == other.__time.hour and first.__time.minute < other.__time.minute) or (
                    first.__time.hour == other.__time.hour and first.__time.minute == other.__time.minute and first.__time.second < other.__time.second):
                days -= 1
            sec1 = other.__time.hour * 3600 + other.__time.minute * 60 + other.__time.second
            sec2 = self.__time.hour * 3600 + self.__time.minute * 60 + self.__time.second
        else:
            first = copy.deepcopy(self)
            while not first.__date == other.__date:
                days += 1
                first.add_day(1)
            if first.__time.hour > other.__time.hour or (
                    first.__time.hour == other.__time.hour and first.__time.minute > other.__time.minute) or (
                    first.__time.hour == other.__time.hour and first.__time.minute == other.__time.minute and first.__time.second > other.__time.second):
                days -= 1
            sec2 = self.__time.hour * 3600 + other.__time.minute * 60 + other.__time.second
            sec1 = self.__time.hour * 3600 + self.__time.minute * 60 + self.__time.second
        diff_sec = (sec2 - sec1) % (24 * 3600)
        diff_hour = diff_sec // 3600
        diff_min = (diff_sec - diff_hour * 3600) // 60
        diff_sec = (diff_sec - diff_hour * 3600) % 60

        return f"{days} days, {diff_hour} hours, {diff_min} mins and {diff_sec} secs difference."


dt = DateTime(Date(2021, 3, 31), Time(23, 5, 6))
other = DateTime(Date(2022, 7, 12), Time(10, 5, 1))

# print(dt)
# print(other)
# print(dt + other)
# print(dt - other)
#
# dt.time = Time(12, 3, 4)
# dt.add_month(11)
# dt.add_year(2)
# dt.add_day(4)
#
# dt.add_minute(2440)
# dt.sub_month(13)
# dt.sub_day(555)
# dt.sub_month(13)
# dt.sub_hour(23)
# dt.sub_minute(1440)
# dt.sub_second(310)
# print(dt)
