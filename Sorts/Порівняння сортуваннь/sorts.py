def bubble_sort(array):
    n = len(array)
    for i in range(n - 1, 0, -1):
        not_sorted = False
        for j in range(i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                not_sorted = True
        if not not_sorted:
            break
    # print(array)


def selection_sort(array):
    n = len(array)
    for i in range(n - 1, 0, -1):
        max_pos = 0
        for j in range(i + 1):
            if array[j] > array[max_pos]:
                max_pos = j
        array[i], array[max_pos] = array[max_pos], array[i]
    # print(array)


def merge_sort(array):
    if len(array) > 1:
        m = len(array) // 2
        left = array[:m]
        right = array[m:]
        merge_sort(left)
        merge_sort(right)
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1


def qsort(array, a, b):
    if a >= b:
        return
    left = a
    right = b
    pivot = array[left + (right - left) // 2]
    while True:
        while array[left] < pivot:
            left += 1
        while array[right] > pivot:
            right -= 1
        if left >= right:
            break
        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1

    qsort(array, a, right)
    qsort(array, right + 1, b)


if __name__ == '__main__':
    import random
    import time
    for N in [100, 1000, 10000, 100000]:
        ar = [random.randint(0, N) for _ in range(N)]
        for sort_func in [bubble_sort, selection_sort, merge_sort, sorted]:
            now = time.time()
            array = ar.copy()
            sort_func(array)
            work_time = time.time() - now
            func_name = sort_func.__name__
            print(f"N = {N}, sort_func = {func_name}, time = {work_time}",)

        now = time.time()
        array = ar.copy()
        qsort(array, 0, N - 1)
        work_time = time.time() - now
        print(f"N = {N}, sort_func = qsort, time = {work_time}", )
        print('\n')

