from math import floor

n = int(input())

not_change =[False] * n
res = []
total = 0

for i in range(n):
    t = float(input())
    t_int = floor(t)

    if t == t_int:
        not_change[i] = True
    total += t_int
    res.append(t_int)

i = 0
while total < 0 :
    if not_change[i]:
        i+=1
        continue
    res[i] += 1
    i +=1
    total +=1
for r in res:
    print(r)