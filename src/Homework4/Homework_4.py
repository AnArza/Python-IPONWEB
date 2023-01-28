# Task 1
# Տրված է թվաբանական պրոգրեսիայի առաջին և երկրորդ անդամները։ Տրված n֊ի
# համար, վերադարձնել այդ պրոգրեսիայի n֊րդ անդամը։


def progression(a1, a2, n):
    d = a2 - a1
    an = a1 + (n - 1) * d
    return f"a[{n}]={an}"


# print(progression(1, 5, 3))
# print(progression(2.5, 3, 5))


# Task 2
# CodeMaster-ը նոր է վերադարձել գնումներից։ Նա սկանավորեց իր գնած ապրանքների
# չեկը և ստացված շարանը տվեց Ratiorg֊ին՝ պարզելու գնված ապրանքների
# ընդհանուր թիվը: Քանի որ Ratiorg-ը բոտ է, նա անպայման պատրաստվում է այն
# ավտոմատացնել, ուստի նրան անհրաժեշտ է ծրագիր, որը կամփոփի բոլոր թվերը,
# որոնք հայտնվում են տվյալ մուտքագրում:
# Օգնեք Ratiorg-ին՝ գրելով ֆունկցիա, որը վերադարձնում է տվյալ inputString-ում
# հայտնված թվերի գումարը։

def count_of_goods(input_string):
    num_str = ""
    count = 0
    for el in input_string:
        if el.isnumeric():
            num_str += el
        elif len(num_str) != 0:
            count += int(num_str)
            num_str = ""
    if len(num_str) != 0:
        count += int(num_str)
    return count


# print(count_of_goods("2 apples,12 oranges"))


# Task 3
# Մուտքագրեք երեք ամբողջ թիվ: Տպեք «Տեսակավորված» բառը, եթե թվերը նշված են
# ոչ աճող կամ չնվազող հերթականությամբ, իսկ «Չտեսակավորված» հակարակ
# դեփքում:

def sort_validation(a, b, c):
    if (b - a >= 0 and c - b >= 0) or (b - a <= 0 and c - b <= 0):
        return "Sorted"
    return "Unsorted"


# print(sort_validation(1, 2, 3))
# print(sort_validation(1, 3, 2))
# print(sort_validation(5, 0, -4))


# Task 4
# Գրել ֆունկցիա, որը տրված բնական թվի համար կստուգի, արդյոք այն
# կատարյալ թիվ է, թե ոչ։
# Հ․Գ Թիվը կոչվում է կատարյալ, եթե այն հավասար է իր բաժանարարների
# գումարին։

def is_perfect(n):
    sum = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            sum += i + n // i
    sum -= n
    return n == sum


# print(is_perfect(6))
# print(is_perfect(12))


# Task 5
# Գրել ծրագիր, որը տրված թվային արժեքներով ցուցակի համար, կհաշվի նրա
# էլեմենտների գումարը։

def sum_of_list(arr):
    sum = 0
    for num in arr:
        sum += num
    return sum


# print(sum_of_list([5, 9, -4]))
# print(sum_of_list([-1.5, 7.2, 6]))


# Task 6
# Գրել ֆունկցիա, որը տրված թվային արժեքներով ցուցակի համար, կվերադարձնի այդ
# ցուցակի ամենամեծ էլեմենտը։

def maximum(arr):
    if len(arr) == 0:
        return "Empty list"
    max = arr[0]
    for num in arr:
        if num > max:
            max = num
    return max


# print(maximum([5, 9, -1, 12, 55, 6]))
# print(maximum([]))


# Task 7
# Գրել ֆունկցիա, որը տրված ցուցակից կջնջի տրված արժեքին հավասար բոլոր
# էլեմենտները։

def delete_element(arr, val):
    indexes = []
    for i in range(len(arr)):
        if arr[i] == val:
            indexes.append(i)
    for i in range(len(indexes)):
        arr = arr[:indexes[i] - i] + arr[indexes[i] - i + 1:]
    return arr


# print(delete_element([4, 6, 7, 4, 3, 1, 2, 4, 6, 4, 9, 9, 7, 8, 8, 6, 5, 4], 4))
# print(delete_element(['a', 'b', 'a', 4, 'z', 87, 'q', 'a', 'p', 3, 2], 'a'))


# Task 8
# Գրեք ֆունկցիա որը կվերադարձնի տրված թվային արժեքներով ցուցակի բոլոր
# էլեմենտների արտադրյալը։

def product_of_nums(arr):
    product = 1
    for num in arr:
        product *= num
    return product


# print(product_of_nums([5, 6, -9, 1, 2, 3]))
# print(product_of_nums([1.5, 3, 8, 1, 4]))

# Task 9
# Գրեք ֆունկցիա՝ տողը հակադարձելու համար, եթե դրա երկարությունը 4-ի
# բազմապատիկ է։

def reverse_string(string):
    if len(string) % 4 == 0:
        string = string[::-1]
    return string


# print(reverse_string("he this is my string"))


# Task 10
# Գրեք ֆունկցիա՝ որը տրված բնական n թվի համար վերադարձնում է Ֆիբոնաչիի n-րդ
# անդամը։ Խնդիրը լուծել և ռեկուրսիվ, և իտերատիվ մեթոդներով։

def fibonacci(n):
    if n <= 0:
        return "Wrong input"
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_2(n):
    if n <= 0:
        return "Wrong input"
    a = 1
    b = 1
    for i in range(n - 2):
        a, b = b, a + b
    return b


# print(fibonacci(-4))
# print(fibonacci(7))
# print(fibonacci(20))

# print(fibonacci_2(-4))
# print(fibonacci_2(7))
# print(fibonacci_2(20))

# Task 11
# Գրել ֆունկցիա, որը տրված 2 բնական թվերի համար կվերադարձնի նրանց
# ամենափոքր ընդհանուր բազմապատիկը։

def lcm(a, b):
    if a >= b:
        start = a
    else:
        start = b
    while start < a * b:
        if start % a == 0 and start % b == 0:
            return start
        start += 1
    return a * b


# print(lcm(16, 24))
# print(lcm(72, 45))

# Task 12
# Գրեք python ծրագիր՝ նշված թվի հաջորդ ամենափոքր պալինդրոմը գտնելու համար:

def is_palindrome(n):
    string = str(n)
    for i in range(len(string) // 2):
        if string[i] != string[len(string) - i - 1]:
            return False
    return True


def next_palindrome(n):
    start = n + 1
    while True:
        if not is_palindrome(start):
            start += 1
        else:
            return start


# print(next_palindrome(19))
# print(next_palindrome(542))

# Task 13
# Ռոբոտը կանգնած է ուղղանկյուն ցանցի վրա և ներկայումս գտնվում է կետում (X0,
# Y0): Կոորդինատները ամբողջ թիվ են։ Այն ստանում է N հեռակառավարման
# հրամաններ: Յուրաքանչյուր հրաման մեկն է՝ վեր, վար, ձախ, աջ: Ճիշտ հրաման
# ստանալուց հետո ռոբոտը մեկ միավոր է տեղափոխում տվյալ ուղղությամբ։ Եթե
# ռոբոտը սխալ հրաման է ստանում, նա պարզապես անտեսում է այն: Որտե՞ղ է
# գտնվելու ռոբոտը բոլոր հրամաններին հետևելուց հետո:
# Ուշադրություն: աջը՝ x0+1, ձախը՝ x0-1, վերևը՝ y0+1, ներքևը՝ y0-1։


def move_robot(moves):
    x = 0
    y = 0
    for side in moves:
        if side == 'u':
            y += 1
        elif side == 'd':
            y -= 1
        elif side == 'r':
            x += 1
        elif side == 'l':
            x -= 1
    return x, y


# print(move_robot('udddllrjaddurrrrrr'))


# Task 14
# Ստուգեք, արդյոք 2 ցուցակները 1-քայլ ցիկլիկ են:

def is_cyclic(arr1, arr2):
    return arr1 == arr2[1:] + [arr2[0]] or arr2 == arr1[1:] + [arr1[0]]


# print(is_cyclic([1, 2, 3, 4, 5, 6], [6, 1, 2, 3, 4, 5]))
# print(is_cyclic([7, 4, 2, 5], [2, 5, 7, 4]))
# print(is_cyclic([4, 1, 2, 3], [1, 2, 3, 4]))


# Task 15
# Գրել ծրագիր, որը ստանւմ է թիվ, գտեք առավելագույն թիվը, որը կարող եք ստանալ՝
# ջնջելով տվյալ թվի ուղիղ մեկ թվանշանը:

def delete_digit(n):
    str_num = str(n)
    min_digit = int(str_num[0])
    index = 0
    for i in range(len(str_num)):
        if int(str_num[i]) < min_digit:
            min_digit = int(str_num[i])
            index = i
    return int(str_num[:index] + str_num[index + 1:])


# print(delete_digit(152))
# print(delete_digit(1001))
# print(delete_digit(7959))


# Task 16
# Գրեք ֆուկցիա որը ստանում է tuple տիպի օբյեկտ և վերադարձնում նոր tuple
# բաղկացած միայն առաջին tuple֊ի թվերից։


def tuple_with_nums(tuple_param):
    res_tuple = tuple(el for el in tuple_param if isinstance(el, (int, float)))
    return res_tuple


# print(tuple_with_nums((9, 'aas', 876, 5.54, 'sd', ['as', 54], (5, 6), 98)))


# Task 17
# Գրեք Python ֆուկցիա որը ստանում է tuple և ցանկացաց տիպի օբյեկտ և ավելացնում
# է ստացած արժեքը tuple մեջ։

def add_object_to_tuple(tuple_param, obj):
    my_list = list(tuple_param)
    my_list.append(obj)
    tuple_param = tuple(my_list)
    return tuple_param


# print(add_object_to_tuple((5, 'as', 'hehe', ['babam', 54, 1], 6, (87, 654)), ['this', 'is', 'my', 'list', 54]))
# print(add_object_to_tuple(('babam', 'Ani', 5.63), 5455))


# Task 18
# Գրեք Python ֆուկցիա որը ստանում է tuple դարձնում է string։ Tuplex֊ի էլեմենտները
# ստրինգում պետք է բաժանված լինեն ‘-’ նշանով։

def to_string(tuple):
    string = ''
    for el in tuple:
        string += str(el) + '-'
    string = string[:-1]
    return string


# print(to_string((5, 'a', 9, 74, 'zz')))


# Task 19
# Գրեք Python ֆուկցիա որը ստանում է list և պետքա գտնել նրա երկարությունը առանց
# len() ֆունկցիա֊ի օգտագորձմամբ։

def list_length(list):
    length = 0
    for el in list:
        length += 1
    return length


# print(list_length([5, 'a', 9, 74, 'zz', 'q', 1, 9]))


# Task 20
# Ticket numbers usually consist of an even number of digits. A ticket number is considered
# lucky if the sum of the first half of the digits is equal to the sum of the second half.
# Given a ticket number n, determine if it's lucky or not. Not using: string, list, tuple, set
# types.

def is_lucky(n):
    count = 0
    first_sum = 0
    second_sum = 0
    n_copy = n
    while n > 0:
        n //= 10
        count += 1
    for i in range(count):
        if i >= count // 2:
            first_sum += n_copy % 10
            n_copy //= 10
        else:
            second_sum += n_copy % 10
            n_copy //= 10

    return first_sum == second_sum


# print(is_lucky(1230))
# print(is_lucky(239017))
# print(is_lucky(91345971))


# Task 21
# Euler function is return a count of numbers not great than N, which are mutualy simple with N.

def gcd(a, b):
    while a % b:
        a, b = b, a % b
    return b


def euler(n):
    count = 0
    for i in range(1, n):
        if gcd(i, n) == 1:
            count += 1
    return count


# print(euler(6))
# print(euler(15))


# Task 22
# You are given a 0-indexed string array words, where words[i] consists of lowercase English
# letters. In one operation, select any index i such that 0 < i < words.length and words[i - 1]
# and words[i] are anagrams, and delete words[i] from words. Keep performing this operation
# as long as you can select an index that satisfies the conditions.
# Return words after performing all operations. It can be shown that selecting the indices for
# each operation in any arbitrary order will lead to the same result.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or
# phrase using all the original letters exactly once. For example, "dacb" is an anagram of
# "abdc".

def str_to_dict(string):
    dict = {}
    for char in string:
        dict.update({char: 0})
    for key in dict.keys():
        for char in string:
            if char == key:
                dict[key] += 1
    return dict


def are_anagrams(str1, str2):
    if len(str1) != len(str2):
        return False
    dict1 = str_to_dict(str1)
    dict2 = str_to_dict(str2)

    return dict1 == dict2


def delete_an_anagram(words):
    res = []
    i = 1
    while True:
        if i == len(words):
            break
        if are_anagrams(words[i - 1], words[i]):
            words.pop(i)
        else:
            i += 1

    return words


# print(delete_an_anagram(['abba', 'baba', 'bbaa', 'cd', 'cd']))
# print(delete_an_anagram(['a', 'b', 'c', 'd']))


# Task 23
# You are given an array of strings names, and an array heights that consists of distinct
# positive integers. Both arrays are of length n. For each index i, names[i] and heights[i]
# denote the name and height of the ith person. Return names sorted in descending
# order by the people's heights.

def partition(arr, start, end):
    pivot = arr[end]
    i = start - 1
    for j in range(start, end):
        if arr[j] >= pivot:
            i += 1
            (arr[i], arr[j]) = (arr[j], arr[i])

    (arr[i + 1], arr[end]) = (arr[end], arr[i + 1])

    return i + 1


def quick_sort(arr, start, end):
    if start < end:
        q = partition(arr, start, end)
        quick_sort(arr, start, q - 1)
        quick_sort(arr, q + 1, end)


def sort_heights(names, heights):
    names_heights = [(heights[i], names[i]) for i in range(len(names))]
    quick_sort(names_heights, 0, len(heights) - 1)
    names = [person[1] for person in names_heights]
    return names


# print(sort_heights(['Mary', 'John', 'Emma'], [180, 165, 170]))
# print(sort_heights(['Ani', 'Hrach', 'Zhanet', 'Laur', 'Mger', 'Hayko'], [150, 183, 162, 165, 170, 182]))


# Task 24
# In a special ranking system, each voter gives a rank from highest to lowest to all
# teams participating in the competition.
# The ordering of teams is decided by who received the most position-one votes. If two
# or more teams tie in the first position, we consider the second position to resolve the
# conflict, if they tie again, we continue this process until the ties are resolved. If two or
# more teams are still tied after considering all positions, we rank them alphabetically
# based on their team letter.
# You are given an array of strings votes which is the votes of all voters in the ranking
# systems. Sort all teams according to the ranking system described above.
# Return a string of all teams sorted by the ranking system.


def ranking(votes):
    if len(votes) == 1:
        return votes[0]

    dict = {}
    for team in votes[0]:
        dict.update({team: 0})
    for vote in votes:
        for team in dict.keys():
            i = vote.index(team)
            dict[team] += i
    team_points = [(dict[team], team) for team in dict.keys()]
    quick_sort(team_points, 0, len(votes[0]) - 1)
    res = ''
    for i in range(len(team_points) - 1, -1, -1):
        res += team_points[i][1]

    return res


def ranking_2(votes):
    if len(votes) == 1:
        return votes[0]

    dict = {}
    for team in votes[0]:
        dict.update({team: [0] * len(votes[0])})
    for i in range(len(votes)):
        for j in range(len(votes[0])):
            dict[votes[i][j]][j] += 1
    team_points = [(dict[team], team) for team in dict.keys()]
    quick_sort(team_points, 0, len(votes[0]) - 1)
    res = ''
    for team in team_points:
        res += team[1]

    return res


# Task 1
# Տրված է թվաբանական պրոգրեսիայի առաջին և երկրորդ անդամները։ Տրված n֊ի
# համար, վերադարձնել այդ պրոգրեսիայի n֊րդ անդամը։
import math


def progression(a1, a2, n):
    d = a2 - a1
    an = a1 + (n - 1) * d
    return f"a[{n}]={an}"


# print(progression(1, 5, 3))
# print(progression(2.5, 3, 5))


# Task 2
# CodeMaster-ը նոր է վերադարձել գնումներից։ Նա սկանավորեց իր գնած ապրանքների
# չեկը և ստացված շարանը տվեց Ratiorg֊ին՝ պարզելու գնված ապրանքների
# ընդհանուր թիվը: Քանի որ Ratiorg-ը բոտ է, նա անպայման պատրաստվում է այն
# ավտոմատացնել, ուստի նրան անհրաժեշտ է ծրագիր, որը կամփոփի բոլոր թվերը,
# որոնք հայտնվում են տվյալ մուտքագրում:
# Օգնեք Ratiorg-ին՝ գրելով ֆունկցիա, որը վերադարձնում է տվյալ inputString-ում
# հայտնված թվերի գումարը։

def count_of_goods(input_string):
    num_str = ""
    count = 0
    for el in input_string:
        if el.isnumeric():
            num_str += el
        elif len(num_str) != 0:
            count += int(num_str)
            num_str = ""
    if len(num_str) != 0:
        count += int(num_str)
    return count


# print(count_of_goods("2 apples,12 oranges"))


# Task 3
# Մուտքագրեք երեք ամբողջ թիվ: Տպեք «Տեսակավորված» բառը, եթե թվերը նշված են
# ոչ աճող կամ չնվազող հերթականությամբ, իսկ «Չտեսակավորված» հակարակ
# դեփքում:

def sort_validation(a, b, c):
    if (b - a >= 0 and c - b >= 0) or (b - a <= 0 and c - b <= 0):
        return "Sorted"
    return "Unsorted"


# print(sort_validation(1, 2, 3))
# print(sort_validation(1, 3, 2))
# print(sort_validation(5, 0, -4))


# Task 4
# Գրել ֆունկցիա, որը տրված բնական թվի համար կստուգի, արդյոք այն
# կատարյալ թիվ է, թե ոչ։
# Հ․Գ Թիվը կոչվում է կատարյալ, եթե այն հավասար է իր բաժանարարների
# գումարին։

def is_perfect(n):
    sum = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            sum += i + n // i
    sum -= n
    return n == sum


# print(is_perfect(6))
# print(is_perfect(12))


# Task 5
# Գրել ծրագիր, որը տրված թվային արժեքներով ցուցակի համար, կհաշվի նրա
# էլեմենտների գումարը։

def sum_of_list(arr):
    sum = 0
    for num in arr:
        sum += num
    return sum


# print(sum_of_list([5, 9, -4]))
# print(sum_of_list([-1.5, 7.2, 6]))


# Task 6
# Գրել ֆունկցիա, որը տրված թվային արժեքներով ցուցակի համար, կվերադարձնի այդ
# ցուցակի ամենամեծ էլեմենտը։

def maximum(arr):
    if len(arr) == 0:
        return "Empty list"
    max = arr[0]
    for num in arr:
        if num > max:
            max = num
    return max


# print(maximum([5, 9, -1, 12, 55, 6]))
# print(maximum([]))


# Task 7
# Գրել ֆունկցիա, որը տրված ցուցակից կջնջի տրված արժեքին հավասար բոլոր
# էլեմենտները։

def delete_element(arr, val):
    indexes = []
    for i in range(len(arr)):
        if arr[i] == val:
            indexes.append(i)
    for i in range(len(indexes)):
        arr = arr[:indexes[i] - i] + arr[indexes[i] - i + 1:]
    return arr


# print(delete_element([4, 6, 7, 4, 3, 1, 2, 4, 6, 4, 9, 9, 7, 8, 8, 6, 5, 4], 4))
# print(delete_element(['a', 'b', 'a', 4, 'z', 87, 'q', 'a', 'p', 3, 2], 'a'))


# Task 8
# Գրեք ֆունկցիա որը կվերադարձնի տրված թվային արժեքներով ցուցակի բոլոր
# էլեմենտների արտադրյալը։

def product_of_nums(arr):
    product = 1
    for num in arr:
        product *= num
    return product


# print(product_of_nums([5, 6, -9, 1, 2, 3]))
# print(product_of_nums([1.5, 3, 8, 1, 4]))

# Task 9
# Գրեք ֆունկցիա՝ տողը հակադարձելու համար, եթե դրա երկարությունը 4-ի
# բազմապատիկ է։

def reverse_string(string):
    if len(string) % 4 == 0:
        string = string[::-1]
    return string


# print(reverse_string("he this is my string"))


# Task 10
# Գրեք ֆունկցիա՝ որը տրված բնական n թվի համար վերադարձնում է Ֆիբոնաչիի n-րդ
# անդամը։ Խնդիրը լուծել և ռեկուրսիվ, և իտերատիվ մեթոդներով։

def fibonacci(n):
    if n <= 0:
        return "Wrong input"
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_2(n):
    if n <= 0:
        return "Wrong input"
    a = 1
    b = 1
    for i in range(n - 2):
        a, b = b, a + b
    return b


# print(fibonacci(-4))
# print(fibonacci(7))
# print(fibonacci(20))

# print(fibonacci_2(-4))
# print(fibonacci_2(7))
# print(fibonacci_2(20))

# Task 11
# Գրել ֆունկցիա, որը տրված 2 բնական թվերի համար կվերադարձնի նրանց
# ամենափոքր ընդհանուր բազմապատիկը։

def lcm(a, b):
    if a >= b:
        start = a
    else:
        start = b
    while start < a * b:
        if start % a == 0 and start % b == 0:
            return start
        start += 1
    return a * b


# print(lcm(16, 24))
# print(lcm(72, 45))

# Task 12
# Գրեք python ծրագիր՝ նշված թվի հաջորդ ամենափոքր պալինդրոմը գտնելու համար:

def is_palindrome(n):
    string = str(n)
    for i in range(len(string) // 2):
        if string[i] != string[len(string) - i - 1]:
            return False
    return True


def next_palindrome(n):
    start = n + 1
    while True:
        if not is_palindrome(start):
            start += 1
        else:
            return start


# print(next_palindrome(19))
# print(next_palindrome(542))

# Task 13
# Ռոբոտը կանգնած է ուղղանկյուն ցանցի վրա և ներկայումս գտնվում է կետում (X0,
# Y0): Կոորդինատները ամբողջ թիվ են։ Այն ստանում է N հեռակառավարման
# հրամաններ: Յուրաքանչյուր հրաման մեկն է՝ վեր, վար, ձախ, աջ: Ճիշտ հրաման
# ստանալուց հետո ռոբոտը մեկ միավոր է տեղափոխում տվյալ ուղղությամբ։ Եթե
# ռոբոտը սխալ հրաման է ստանում, նա պարզապես անտեսում է այն: Որտե՞ղ է
# գտնվելու ռոբոտը բոլոր հրամաններին հետևելուց հետո:
# Ուշադրություն: աջը՝ x0+1, ձախը՝ x0-1, վերևը՝ y0+1, ներքևը՝ y0-1։


def move_robot(moves):
    x = 0
    y = 0
    for side in moves:
        if side == 'u':
            y += 1
        elif side == 'd':
            y -= 1
        elif side == 'r':
            x += 1
        elif side == 'l':
            x -= 1
    return x, y


# print(move_robot('udddllrjaddurrrrrr'))


# Task 14
# Ստուգեք, արդյոք 2 ցուցակները 1-քայլ ցիկլիկ են:

def is_cyclic(arr1, arr2):
    return arr1 == arr2[1:] + [arr2[0]] or arr2 == arr1[1:] + [arr1[0]]


# print(is_cyclic([1, 2, 3, 4, 5, 6], [6, 1, 2, 3, 4, 5]))
# print(is_cyclic([7, 4, 2, 5], [2, 5, 7, 4]))
# print(is_cyclic([4, 1, 2, 3], [1, 2, 3, 4]))


# Task 15
# Գրել ծրագիր, որը ստանւմ է թիվ, գտեք առավելագույն թիվը, որը կարող եք ստանալ՝
# ջնջելով տվյալ թվի ուղիղ մեկ թվանշանը:

def delete_digit(n):
    str_num = str(n)
    min_digit = int(str_num[0])
    index = 0
    for i in range(len(str_num)):
        if int(str_num[i]) < min_digit:
            min_digit = int(str_num[i])
            index = i
    return int(str_num[:index] + str_num[index + 1:])


# print(delete_digit(152))
# print(delete_digit(1001))
# print(delete_digit(7959))


# Task 16
# Գրեք ֆուկցիա որը ստանում է tuple տիպի օբյեկտ և վերադարձնում նոր tuple
# բաղկացած միայն առաջին tuple֊ի թվերից։


def tuple_with_nums(tuple_param):
    res_tuple = tuple(el for el in tuple_param if isinstance(el, (int, float)))
    return res_tuple


# print(tuple_with_nums((9, 'aas', 876, 5.54, 'sd', ['as', 54], (5, 6), 98)))


# Task 17
# Գրեք Python ֆուկցիա որը ստանում է tuple և ցանկացաց տիպի օբյեկտ և ավելացնում
# է ստացած արժեքը tuple մեջ։

def add_object_to_tuple(tuple_param, obj):
    my_list = list(tuple_param)
    my_list.append(obj)
    tuple_param = tuple(my_list)
    return tuple_param


# print(add_object_to_tuple((5, 'as', 'hehe', ['babam', 54, 1], 6, (87, 654)), ['this', 'is', 'my', 'list', 54]))
# print(add_object_to_tuple(('babam', 'Ani', 5.63), 5455))


# Task 18
# Գրեք Python ֆուկցիա որը ստանում է tuple դարձնում է string։ Tuplex֊ի էլեմենտները
# ստրինգում պետք է բաժանված լինեն ‘-’ նշանով։

def to_string(tuple):
    string = ''
    for el in tuple:
        string += str(el) + '-'
    string = string[:-1]
    return string


# print(to_string((5, 'a', 9, 74, 'zz')))


# Task 19
# Գրեք Python ֆուկցիա որը ստանում է list և պետքա գտնել նրա երկարությունը առանց
# len() ֆունկցիա֊ի օգտագորձմամբ։

def list_length(list):
    length = 0
    for el in list:
        length += 1
    return length


# print(list_length([5, 'a', 9, 74, 'zz', 'q', 1, 9]))


# Task 20
# Ticket numbers usually consist of an even number of digits. A ticket number is considered
# lucky if the sum of the first half of the digits is equal to the sum of the second half.
# Given a ticket number n, determine if it's lucky or not. Not using: string, list, tuple, set
# types.

def is_lucky(n):
    count = 0
    first_sum = 0
    second_sum = 0
    n_copy = n
    while n > 0:
        n //= 10
        count += 1
    for i in range(count):
        if i >= count // 2:
            first_sum += n_copy % 10
            n_copy //= 10
        else:
            second_sum += n_copy % 10
            n_copy //= 10

    return first_sum == second_sum


# print(is_lucky(1230))
# print(is_lucky(239017))
# print(is_lucky(91345971))


# Task 21
# Euler function is return a count of numbers not great than N, which are mutualy simple with N.

def gcd(a, b):
    while a % b:
        a, b = b, a % b
    return b


def euler(n):
    count = 0
    for i in range(1, n):
        if gcd(i, n) == 1:
            count += 1
    return count


# print(euler(6))
# print(euler(15))


# Task 22
# You are given a 0-indexed string array words, where words[i] consists of lowercase English
# letters. In one operation, select any index i such that 0 < i < words.length and words[i - 1]
# and words[i] are anagrams, and delete words[i] from words. Keep performing this operation
# as long as you can select an index that satisfies the conditions.
# Return words after performing all operations. It can be shown that selecting the indices for
# each operation in any arbitrary order will lead to the same result.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or
# phrase using all the original letters exactly once. For example, "dacb" is an anagram of
# "abdc".

def str_to_dict(string):
    dict = {}
    for char in string:
        dict.update({char: 0})
    for key in dict.keys():
        for char in string:
            if char == key:
                dict[key] += 1
    return dict


def are_anagrams(str1, str2):
    if len(str1) != len(str2):
        return False
    dict1 = str_to_dict(str1)
    dict2 = str_to_dict(str2)

    return dict1 == dict2


def delete_an_anagram(words):
    res = []
    i = 1
    while True:
        if i == len(words):
            break
        if are_anagrams(words[i - 1], words[i]):
            words.pop(i)
        else:
            i += 1

    return words


# print(delete_an_anagram(['abba', 'baba', 'bbaa', 'cd', 'cd']))
# print(delete_an_anagram(['a', 'b', 'c', 'd']))


# Task 23
# You are given an array of strings names, and an array heights that consists of distinct
# positive integers. Both arrays are of length n. For each index i, names[i] and heights[i]
# denote the name and height of the ith person. Return names sorted in descending
# order by the people's heights.

def partition(arr, start, end):
    pivot = arr[end]
    i = start - 1
    for j in range(start, end):
        if arr[j] >= pivot:
            i += 1
            (arr[i], arr[j]) = (arr[j], arr[i])

    (arr[i + 1], arr[end]) = (arr[end], arr[i + 1])

    return i + 1


def quick_sort(arr, start, end):
    if start < end:
        q = partition(arr, start, end)
        quick_sort(arr, start, q - 1)
        quick_sort(arr, q + 1, end)


def sort_heights(names, heights):
    names_heights = [(heights[i], names[i]) for i in range(len(names))]
    quick_sort(names_heights, 0, len(heights) - 1)
    names = [person[1] for person in names_heights]
    return names


# print(sort_heights(['Mary', 'John', 'Emma'], [180, 165, 170]))
# print(sort_heights(['Ani', 'Hrach', 'Zhanet', 'Laur', 'Mger', 'Hayko'], [150, 183, 162, 165, 170, 182]))


# Task 24
# In a special ranking system, each voter gives a rank from highest to lowest to all
# teams participating in the competition.
# The ordering of teams is decided by who received the most position-one votes. If two
# or more teams tie in the first position, we consider the second position to resolve the
# conflict, if they tie again, we continue this process until the ties are resolved. If two or
# more teams are still tied after considering all positions, we rank them alphabetically
# based on their team letter.
# You are given an array of strings votes which is the votes of all voters in the ranking
# systems. Sort all teams according to the ranking system described above.
# Return a string of all teams sorted by the ranking system.


def ranking(votes):
    if len(votes) == 1:
        return votes[0]

    dict = {}
    for team in votes[0]:
        dict.update({team: 0})
    for vote in votes:
        for team in dict.keys():
            i = vote.index(team)
            dict[team] += i
    team_points = [(dict[team], team) for team in dict.keys()]
    quick_sort(team_points, 0, len(votes[0]) - 1)
    res = ''
    for i in range(len(team_points) - 1, -1, -1):
        res += team_points[i][1]

    return res


def ranking_2(votes):
    if len(votes) == 1:
        return votes[0]

    dict = {}
    for team in votes[0]:
        dict.update({team: [0] * len(votes[0]) + [team]})
    for i in range(len(votes)):
        for j in range(len(votes[0])):
            dict[votes[i][j]][j] -= 1
    team_points = [dict[team] for team in dict.keys()]
    quick_sort(team_points, 0, len(votes[0]) - 1)
    res = ''
    for team in team_points[::-1]:
        res += team[-1]

    return res


print(ranking(['ABC', 'ACB', 'ABC', 'ACB', 'ACB']))
print(ranking_2(['ABC', 'ACB', 'ABC', 'ACB', 'ACB']))

print(ranking(['WXYZ', 'XYZW']))
print(ranking_2(['WXYZ', 'XYZW']))

print(ranking(['ZMNAGUEDSJYLBOPHRQICWFXTVK']))
print(ranking_2(['ZMNAGUEDSJYLBOPHRQICWFXTVK']))

print(ranking(['qwer', 'wqre', 'werq', 'rewq', 'rqwe']))
print(ranking_2(['qwer', 'wqre', 'werq', 'rewq', 'rqwe']))
