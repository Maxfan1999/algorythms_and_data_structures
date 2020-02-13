def search(ar, k):
    l, r = 0, len(ar) - 1
    while l < r:
        m = l + (r - l) // 2
        if k == ar[m]:
            return "YES"
        elif k > ar[m]:
            l = m + 1
        else:
            r = m - 1
    if ar[r] == k:
        return "YES"
    else:
        return "NO"
    

input()
ar = list(map(int, input().split()))
input()
numbers = list(map(int, input().split()))
for number in numbers:
    print(search(ar, number))




    
