# Task 1

lambda_f1 = lambda x: x + 15
lambda_f2 = lambda x, y: print(x * y)

# print(lambda_f1(5))
# lambda_f2(4, 6)

# Task 2

fib = lambda n: 1 if n <= 2 else fib(n - 1) + fib(n - 2)
res = lambda n: [print(fib(i), end=' ') for i in range(1, n + 1)]

# res(5)

# Task 3

reverse = lambda arr: arr[::-1]


# print(reverse([5, 6, 7, 1, 0, -4]))


def my_decorator(f):
    def wrapper():
        print("^^^^^^^^^")
        f()
        print("^^^^^^^^^")

    return wrapper


@my_decorator
def my_f():
    print('hiiiii')


# my_f()

# Task 6

import time
from time import perf_counter


def time_decorator(f):
    def wrapper(x):
        start_time = time.time()
        print(f(x))
        print(time.time() - start_time, 'seconds')

    return wrapper


def time_decorator_2(f):
    def wrapper(x):
        t1_start = perf_counter()
        print(f(x))
        t1_end = perf_counter()
        print(t1_end - t1_start, 'seconds')

    return wrapper


@time_decorator
def my_func(x):
    time.sleep(2)
    return x ** 8


# my_func(3)


def agnes_decortor(lambda_f):
    def my_d(f):
        def wrapper(n):
            return lambda_f(f(n))

        return wrapper

    return my_d


@agnes_decortor(lambda n: n + 1)
def my_ffff(n):
    return n


# print(my_ffff(5))


# Generators
# Task 7

def generator(x):
    i = 0
    while i <= x:
        yield i
        i += 1


def count_up_to(x):
    for val in generator(x):
        print(val)


count_up_to(5)


def even_numbers():
    i = 0
    while True:
        yield i
        i += 2


x = even_numbers()
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
