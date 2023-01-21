# Task 1

def create_dict(sample_dict, keys):
    res_dict = {}
    for key in keys:
        res_dict[key] = sample_dict[key]
    return res_dict


# print(create_dict({'name': 'Kelly', "age": 25, "salary": 8000, "city": "New York"}, ['name', 'salary']))


# Task 2

def min_val_from_dict(sample_dict):
    keys = list(sample_dict.keys())
    min_val = sample_dict[keys[0]]
    min_key = keys[0]
    for key in keys:
        if sample_dict[key] < min_val:
            min_val = sample_dict[key]
            min_key = key
    return min_key


# print(min_val_from_dict({"Physics": 82, "Math": 65, "History": 75}))


# Task 3

def copy_to_file(file_to_copy_from, file_to_paste_in):
    with open(file_to_copy_from, "r") as f:
        content = f.read()
    with open(file_to_paste_in, "w") as f:
        f.write(content)


# copy_to_file("file_with_content.txt", "file_without_content.txt")


# Task 4
def word_frequency(file, word):
    with open(file, 'r') as f:
        content = f.read()
    content = content.replace(',', ' ').replace('.', ' ')
    count = 0
    for w in content.split():
        if w == word:
            count += 1
    return count


# print(word_frequency('file_with_content.txt', 'a'))


# Task 5

def last_lines(file, n):
    with open(file, 'r') as f:
        content = f.readlines()
    for line in content[-n:]:
        print(line[:-1])

# last_lines('file_with_content.txt', 3)
