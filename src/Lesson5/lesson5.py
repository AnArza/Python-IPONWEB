# Task 1
def unique(arr):
    return set(arr)


# print(unique([5, 6, 5, 1, 9]))


# Task 2
def common_els(arr1, arr2):
    return set(arr1) & set(arr2)


# print(common_els([5, 6, 5, 1, 9], [1, 3, 4, 5]))


# Task 3
def els_of_first(arr1, arr2):
    return set(arr1) - set(arr2)


# print(minus([5, 6, 5, 1, 9], [1, 3, 4, 5]))


# Task 4
def first_or_second(arr1, arr2):
    return (set(arr1) | set(arr2)) - (set(arr1) & set(arr2))


def first_or_second_2(arr1, arr2):
    return set(arr1) ^ set(arr2)


# print(first_or_second([5, 6, 5, 1, 9], [1, 3, 4, 5]))
# print(first_or_second_2([5, 6, 5, 1, 9], [1, 3, 4, 5]))

# Task 5
def first_or_second_or_both(arr1, arr2):
    return set(arr1) | set(arr2)


# print(first_or_second_or_both([5, 6, 5, 1, 9], [1, 3, 4, 5]))

# Task 6
def del_el(my_set, val):
    if my_set & set([val]):
        return my_set - set([val])
    return my_set


def del_el_2(my_set, val):
    my_set.remove(val)
    return my_set


# print(del_el({5, 6, 7, 11, 0, 2}, 2))
# print(del_el_2({5, 6, 7, 11, 0, 2}, 2))


# Task 7
def cube_list(my_set):
    res = [num ** 3 for num in my_set]
    return res


# print(cube_list({5, 3, 4, 9}))


# Task 8
def add_val(dict, key, val):
    dict.update({key: val})
    return dict


# print(add_val({"A": 2, "B": 5, "K": 1}, "B", 18))

# Task 9
def concat_dicts(dict1, dict2):
    dict1.update(dict2)
    return dict1


# print(concat_dicts({"A": 2, "B": 5, "K": 1}, {"O": 54, "U": 4, "A": 4}))

# Task 10
def create_dict(N):
    dict = {}
    for i in range(1, N + 1):
        dict[i] = i ** 3
    return dict


# print(create_dict(5))

# Task 11
def create_dict_from_lists(arr1, arr2):
    my_dict = {}
    for i in range(len(arr1)):
        my_dict[arr1[i]] = arr2[i]
    return my_dict


# print(create_dict_from_lists([5, 6, 7, 9], ['a', 'b', 'c', 'd']))


# Task 12
def min_and_max(my_dict):
    vals = list(my_dict.values())
    vals.sort()
    return vals[0], vals[-1]


# print(min_and_max({"A": 2, "B": 5, "K": 1, "O": 54, "U": 4}))

# Working with files

# Task 13
def read_n_lines(n):
    my_file = open("nonempty.txt", "r")
    lines = my_file.readlines()
    for i in range(n):
        print(lines[i][:-1])
    my_file.close()


# read_n_lines(5)

# Task 14
def longest_word():
    with open('nonempty.txt', 'r') as f:
        text = f.read()
        arr = text.split()
        arr = sorted(arr, key=len)
        return arr[-1]


# print(longest_word())

# Task 15
def count_words(file_name):
    with open(file_name, 'r') as f:
        text = f.read()
        text = text.replace(',', ' ')
        res = text.split()
        return len(res)


# print(count_words('nonempty.txt'))

# Task 16
import string


def alphabet(n):
    with open('empty.txt', 'w') as f:
        text = string.ascii_uppercase
        for i in range(len(text) // n + 1):
            f.write(text[i * n:i * n + n] + "\n")


# alphabet(2)

# Task 17
def check_age(age):
    return (age in range(0, 1)) * "Just born" + (age in range(1, 10)) * "Child" + (
            age in range(10, 18)) * "Teenager" + (age in range(18, 50)) * "Young" + (age in range(50, 1500)) * "Old"


print(check_age(9))
