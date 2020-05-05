def bubble_sort():
    global library
    library = list(library.items())
    n = len(library)
    for i in range(n - 1, 0, -1):
        is_sorted = True
        for j in range(i):
            if library[j][0] > library[j + 1][0]:
                library[j], library[j + 1] = library[j + 1], library[j]
                is_sorted = False
        if is_sorted:
            break
    return library


_input_file = open('input.txt', 'r')
n = int(_input_file.readline())
library = {}
for _ in range(n):
    k = int(_input_file.readline())
    s = ''
    for i in range(k):
        new_line = _input_file.readline()
        if new_line[-1] == "\n" and i == k - 1:
            new_line = new_line[:-1]
        s = ''.join([s, new_line])
    library[len(s)] = s
_input_file.close()

with open('output.txt', 'w') as _output_file:
    print("\n***\n".join([x[1] for x in bubble_sort()]), file=_output_file)
