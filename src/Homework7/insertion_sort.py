def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j > -1 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


arr = [6, 1, -7, 9, 5, -2, 0]
print(arr)
insertion_sort(arr)
print(arr)
