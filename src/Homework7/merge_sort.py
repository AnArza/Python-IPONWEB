def merge(arr, start, mid, end):
    if len(arr) > 1:
        left = arr[start:mid + 1]
        right = arr[mid + 1:end + 1]
        i = 0
        j = 0
        k = start
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


def merge_sort(arr, start, end):
    if type(start) != int or type(end) != int or start < 0:
        raise MergeSortError("Start and end are indexes.")
    if start < end:
        mid = (start + end) // 2
        merge_sort(arr, start, mid)
        merge_sort(arr, mid + 1, end)
        merge(arr, start, mid, end)


class MergeSortError(Exception):
    pass


arr = [6, 1, -7, 9, 5, -2, 0]
print(arr)
merge_sort(arr, 0, 6)
print(arr)
