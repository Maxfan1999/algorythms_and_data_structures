lat_dict = {}
_input_file = open('input.txt', 'r')
_output_file = open('output.txt', 'w')
for s in _input_file.readlines():
    eng, lat = s.replace(" ", "").replace("\n", "").split("-")
    lat = lat.split(",")
    for lat_word in lat:
        if lat_word in lat_dict:
            lat_dict[lat_word].append(eng)
        else:
            lat_dict[lat_word] = [eng]
_input_file.close()
print(len(lat_dict), file=_output_file)
for key in sorted(lat_dict):
    print(key, lat_dict[key])
    print(key, "-", ", ".join(lat_dict[key]), file=_output_file)


