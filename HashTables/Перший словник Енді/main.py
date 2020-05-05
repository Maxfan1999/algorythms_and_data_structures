import re

lat_dict = {}
_input_file = open('input.txt', 'r', encoding="Cp1252")
_output_file = open('output.txt', 'w')

s = _input_file.read().lower().replace("\n", " ")

words = re.findall(r'[a-z]+', s)

for word in words:
    if word not in lat_dict:
        lat_dict[word] = 1

print("\n".join(sorted(lat_dict)), file=_output_file)
_input_file.close()
_output_file.close()