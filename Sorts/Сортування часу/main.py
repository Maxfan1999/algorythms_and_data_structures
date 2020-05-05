n = int(input())
ar = []
for i in range(n):
    ar.append(tuple(map(int, input().split())))

for i in range(n - 1, 0, -1):
    for j in range(i):
        if ar[j][0] > ar[j + 1][0]:
            ar[j], ar[j + 1] = ar[j + 1], ar[j]
        elif ar[j][0] == ar[j + 1][0]:
            if ar[j][1] > ar[j + 1][1]:
                ar[j], ar[j + 1] = ar[j + 1], ar[j]
            elif ar[j][1] == ar[j + 1][1]:
                if ar[j][2] > ar[j + 1][2]:
                    ar[j], ar[j + 1] = ar[j + 1], ar[j]
for i in ar:
    print(" ".join(map(str, i)))
