import math

def foo(n):
    if n & 1:
        return 2 ** (r-1) | (n >> 1)
    else:
        return (n>>1)
    
n = int(input())
r = math.ceil(math.log(n, 2))

a = [n]
for i in range(r):
    a.append(foo(a[i]))

print(max(a))
    


    
