class Money:
    exchange = {'AMD': 1, 'RUB': 5.8, 'USD': 400, 'EUR': 430}

    def __init__(self, amount, currency):
        if type(amount) != float and type(amount) != int or amount < 0:
            raise MoneyError("Amount should be positive number.")
        if currency not in ['AMD', 'RUB', 'USD', 'EUR']:
            raise MoneyError("Currency should be string and one of given below -> ['AMD','RUB','USD','EUR']")
        self.__amount = amount
        self.__currency = currency

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, a):
        if type(a) != float and type(a) != int or a < 0:
            raise MoneyError("Amount should be positive number.")
        self.__amount = a

    @property
    def currency(self):
        return self.__currency

    @currency.setter
    def currency(self, c):
        if c not in ['AMD', 'RUB', 'USD', 'EUR']:
            raise MoneyError("Currency should be string and one of given below -> ['AMD','RUB','USD','EUR']")
        self.__currency = c

    def __repr__(self):
        return f"{self.amount} {self.currency}"

    def convert(self, other):
        res_amount = Money.exchange[self.currency] * self.amount / Money.exchange[other.currency]
        res_curr = other.currency
        return Money(res_amount, res_curr)

    def __add__(self, other):
        res_curr = self.currency
        other = other.convert(self)
        res_amount = self.amount + other.amount
        return Money(res_amount, res_curr)

    def __sub__(self, other):
        res_curr = self.currency
        other = other.convert(self)
        if self.amount - other.amount < 0:
            return "Can't complete subtraction"
        res_amount = self.amount - other.amount
        return Money(res_amount, res_curr)

    def __truediv__(self, other):
        res = self.amount
        other = other.convert(self)
        res /= other.amount
        return res

    def __eq__(self, other):
        other = other.convert(self)
        return self.amount == other.amount

    def __ne__(self, other):
        other = other.convert(self)
        return self.amount != other.amount

    def __lt__(self, other):
        other = other.convert(self)
        return self.amount < other.amount

    def __gt__(self, other):
        other = other.convert(self)
        return self.amount > other.amount

    def __le__(self, other):
        other = other.convert(self)
        return self.amount <= other.amount

    def __ge__(self, other):
        other = other.convert(self)
        return self.amount >= other.amount


class MoneyError(Exception):
    def __init__(self, message):
        super().__init__(message)


am = Money(450, 'AMD')
us = Money(2, 'USD')
dram = Money(800, 'AMD')
rubli = Money(150, 'RUB')
euro = Money(5, 'EUR')

# print(am)
# print(us)
# print(rubli)
# print(am + us)
# print(us.convert(rubli))
# print(rubli - us)
# print(us - am)
# print(am / us)
# print(dram > us)
