import datetime


def sc(x):
    sum = 0
    while x != 0:
        sum += x % 10
        x = x // 10
    return sum


def check(m):
    a = m // 9
    b = m % 9
    start = int(str(b) + "9")
    start_i = start // m

    while True:
        num = start_i * m
        if sc(num) == m:
            return num
            break
        else:
            start_i += 1


i = 2
while True:
    now = datetime.datetime.now()
    print(i, check(i), datetime.datetime.now() - now)
    i += 1

