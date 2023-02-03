def counting_sort(arr):
    max = arr[0]
    for num in arr:
        if type(num) != int or num < 0:
            raise CountingSortError("You can use only positive integers in counting sort")
        if num > max:
            max = num

    counts = [0] * (max + 1)

    for num in arr:
        counts[num] += 1

    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]

    counts = [0] + counts[:-1]
    res = [0] * len(arr)

    for i in range(len(arr)):
        res[counts[arr[i]]] = arr[i]
        counts[arr[i]] += 1

    return res


class CountingSortError(Exception):
    pass


arr1 = [1, 0, 3, 1, 3, 1]
print(arr1)
print(counting_sort(arr1))
arr2 = [6, 1, 7, 9, 5, 2, 0, 7]
print(arr2)
print(counting_sort(arr2))
