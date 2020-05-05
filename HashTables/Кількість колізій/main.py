_input_file = open('input.txt', 'r')
_output_file = open('output.txt', 'w')

n, m = map(int, _input_file.read().split(" "))
res = 0 if n >= m else n - m
print('%.9f' % res, file=_output_file)
_input_file.close()
_output_file.close()