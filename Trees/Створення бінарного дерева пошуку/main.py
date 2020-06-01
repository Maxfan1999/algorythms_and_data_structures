import math


def get_heads(a, b, s=''):
    global _output_file
    if b > a:
        m = int((a + b) / 2)
        s = s + str(m) + ' '
        s = get_heads(a, m, s)
        s = get_heads(m + 1, b, s)
        return s
    else:
        return s


_input_file = open('input.txt', 'r')
_output_file = open('output.txt', 'w')

for index, line in enumerate(_input_file.readlines()):
    index += 1
    n, h = map(int, line.split())
    if n == 0 and h == 0:
        break
    print(f"Case {index}:", end=" ", file=_output_file)
    if h < round(math.log2(n), 0):
        print("Impossible.", file=_output_file)
    else:
        s = get_heads(1, n)
        s = s + str(n)
        print(s, file=_output_file)

_output_file.close()
_input_file.close()

