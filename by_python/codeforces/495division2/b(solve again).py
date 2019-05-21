"""n, m = map(int,input().split())

res = [0 for _ in range(n)]
t = [0 for _ in range(n)]

for _ in range(m):
    a, b = map(lambda x: int(x)-1 ,input())

    for i in range(a,b+1):
        t[i]+=1

new_l[]
start = 0
end = 0
for i in range(n):
    if t[i] >=2:
        if not start:
            start = i
        else:
            end = i
    else:
        if start != 0:
            new_l.append((start, end))
            start = 0
            end =0

"""

n, m = map(int,input().split())
for i in range(m):
    input()

res = ""

for i in range(n):
    if i %2:
        res+="1"
    else:
        res+="0"
print(res)