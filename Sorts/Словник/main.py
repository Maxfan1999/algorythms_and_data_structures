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


n = int(input())
array = []
for i in range(n):
    array.append(input())
qsort(array, 0, n - 1)

for i in array:
    print(i)