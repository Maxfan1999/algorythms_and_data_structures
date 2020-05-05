def bubble_sort(array):
    n = len(array)
    number_of_changes = 0
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                number_of_changes += 1
    return number_of_changes


input()
array = list(map(int, input().split()))
print(bubble_sort(array))
