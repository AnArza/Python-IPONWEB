import math


# Task 1
def quadratic_equation(a, b, c):
    if a == 0:
        return "A cant be 0"
    D = b ** 2 - 4 * a * c
    if D < 0:
        return "No roots"
    if D == 0:
        return -b / 2 * a
    x1 = (-b + D ** 0.5) / 2 * a
    x2 = (-b - D ** 0.5) / 2 * a
    return x1, x2


# print(quadratic_equation(1, -6, 8))
# print(quadratic_equation(1, 5, 6))
# print(quadratic_equation(2, 0, -9))
# print(quadratic_equation(1, 2, 1))

# Task 2
def pythagoras(a, b):
    if a <= 0 or b <= 0:
        return "Invalid inputs"
    c = (a ** 2 + b ** 2) ** 0.5
    return c


# print(pythagoras(3, 4))
# print(pythagoras(3, -5))

# Task 3
def last_digit(n):
    if n <= 0 or (not int(n) == n):
        return "Invalid input"
    return str(n)[-1]
    # return n%10


# print(last_digit(1514))
# print(last_digit(10))
# print(last_digit(-55))


# Task 4
def sum_prod_of_digits(n):
    if n <= 0 or int(n) != n:
        return "Invalid input"
    sum = 0
    product = 1
    while n > 0:
        sum += n % 10
        product *= n % 10
        n = n // 10
    return sum, product


# print(sum_prod_of_digits(1065))
# print(sum_prod_of_digits(67354))

# Task 5
def distance(coord1, coord2):
    return ((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2) ** 0.5


# print(distance((1, 5), (5, 8)))


# Task 6
def delete_char(str, n):
    if n <= 0 or int(n) != n:
        return "Invalid input"
    str = str[:n - 1] + str[n:]
    return str


# print(delete_char("Helloo world", 4))
# print(delete_char("hatakapatakachexkapayt", 7))

# Task 7
def swap_chars(str):
    new_str = str[-1] + str[1:-1] + str[0]
    return new_str


# print(swap_chars("ANI"))


# Task 8
def round_2(num):
    n = int(num * 100)
    if n % 10 >= 5:
        res = (n + 1) / 100
    else:
        res = n / 100
    return res


# print(round_2(5.18676))
# print(round_2(2.456))

# Task 9
def max_min(a, b, c):
    if a > b and a > c:
        max = a
    elif b > c:
        max = b
    else:
        max = c
    if a < b and a < c:
        min = a
    elif b < c:
        min = b
    else:
        min = c
    return max, min


# print(max_min(1, 2, 8))
# print(max_min(5, 9, 0))
# print(max_min(100, 6, -4))


# Task 10
def even_odd(n):
    if n % 2 == 0:
        return "Even"
    return "Odd"


# print(even_odd(65))

# Task 11
def divisible(n):
    return n % 35 == 0


# print(divisible(70))

# Task 12
def third_chars(str):
    s = ""
    for i in range(0, len(str), 3):
        s += str[i]
    return s


def third_chars_1(str):
    return str[::3]


# print(third_chars_1("hello Malmo"))

# Task 13
def divisors(n):
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            print(i, n // i)


# divisors(12)


# Task 14
def stars(n, m):
    for i in range(n):
        for j in range(m):
            print("*", end=" ")
        print()


# stars(4, 9)


def stars_1(n, m):
    print(n * ((m * "* ") + "\n"))


# stars_1(4, 9)


# Task 15
def factorial(n):
    prod = 1
    if n < 0:
        return "Wrong input"
    if n == 0:
        return 1
    for i in range(1, n + 1):
        prod *= i
    return prod


def factorial_1(n):
    if n < 0 or int(n) != n:
        return "Wrong input"
    if n == 0 or n == 1:
        return 1
    return n * factorial_1(n - 1)


# print(factorial_1(4))

# Task 17
def gcd(a, b):
    while a % b:
        a, b = b, a % b
    return b


# print(gcd(12, 18))
# print(gcd(64, 48))


# Task 18
def step_of_num(n):
    if n <= 0 or int(n) != n:
        return "Invalid input"
    count = 0
    while n >= 10:
        sum = 0
        while n > 0:
            sum += n % 10
            n = n // 10
        n = sum
        count += 1

    return count

# print(step_of_num(159))
# print(step_of_num(9979878787987987))
