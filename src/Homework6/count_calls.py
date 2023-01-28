def func_calls_counter(f):
    def inner_func(*args, **kwargs):
        inner_func.count += 1
        return f(*args, **kwargs)

    inner_func.count = 0
    return inner_func


@func_calls_counter
def my_function():
    print("hi")


my_function()
my_function()
my_function()
my_function()
my_function()
my_function()
my_function()

print(my_function.count)
