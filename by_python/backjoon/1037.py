n = int(input())
if n == 1:
    result = int(input())**2
else:
    t = list(map(int,input().split()))
    t.sort()
    result = t[0] * t[-1]

print(result)