n, k = map(int, input().split())

circle = [x + 1 for x in range(n)]
counter = 0
while len(circle) != 1:
    for _ in range(k - 1):
        counter += 1
        if counter == n:
            counter = 0
    if counter >= n:
        counter %= n
    del circle[counter]
    n -= 1
print(circle[0])
