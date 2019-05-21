from math import inf

for _ in range(int(input())):
    n, x, y, d = map(int,input().split())

    res = -1
    
    if not (abs(y-x)%d):
        res = abs(y-x)//d
    else:
        temp = inf

        if not ((n-y) % d):
            temp = (n-x)//d + 1 + (n-y)//d
        if not ((y-1) % d):
            temp = min(temp,(x-1)//d + 1 + (y-1)//d)
        if temp != inf:
            res = temp
    print(res)