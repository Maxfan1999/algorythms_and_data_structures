def dfs(ar, index=0):
    global s
    for child in ar[index]:
        s = s + child.item
        dfs(ar, child.key - 1)


n, c = map(int, input().split())
adj_list = [[] for _ in range(n)]
colors = {}
_ar = list(map(int, input().split()))
i = 1
while i < len(_ar):
    if _ar[i - 1] != _ar[i]:
        adj_list[_ar[i] - 1].append(_ar[i])
    i += 1
print(adj_list)


s = ''
dfs(adj_list)
# print(s)
flag = False
if str_to_check in s:
    print("YES")
    flag = True
elif str_to_check in s[::-1]:
    s = s[::-1]
    print("YES")
    flag = True
else:
    print("NO")

if flag:
    res = s.index(str_to_check)
    print(res + 1, res + len(str_to_check))






