n, x, y = map(int,input().split())

num = input()
res = 0

for i in range(x):
    if num[-(i+1)] != ('0' if y != i else '1'):
        res+=1

print(res)
