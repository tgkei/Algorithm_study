"""from collections import Counter

input()

l = list(map(int,input().split()))
c = Counter(l)
c2= sorted(c.keys(),reverse=True)
num_type = len(c2)
res=[]

if num_type > 2:
    res.append(c2[-1])
    c[c2[-1]]-=1
    if c[c2[-1]] ==0:
        num_type-=1

while num_type > 2:
    i = -1
    while c[c2[i]] == 0 or c2[i] == res[-1]+1:
        i-=1
    res.append(c2[i])
    c[c2[i]]-=1
    if c[c2[i]] == 0:
        num_type -=1

if num_type==2:
    if res:
        print(*res, end= " ")
    i = 0
    j = 0
    while c[c2[i]] == 0:
        i += 1
    while c[c2[j]] == 0 or j == i:
        j += 1
    if c2[i]-c2[j] == 1:
        for _ in range(c[c2[i]]):
            print(c2[i],end=" ")
        for _ in range(c[c2[j]]):
            print(c2[j],end=" ")
    else:
        for _ in range(c[c2[j]]):
            print(c2[j], end=" ")
        for _ in range(c[c2[i]]):
            print(c2[i],end= " ")
else:
    for _ in range(c[c2[0]]):
        print(c2[0],end=" ")"""

"""from collections import Counter

input()
l = list(map(int,input().split()))
c = Counter(l)
c2 = sorted(c,reverse=True)
num_type = len(c2)
res = []
if num_type>2:
    res.append(c2[-1])
    c[c2[-1]]-=1
    if c[c2[-1]] == 0:
        num_type -=1
while num_type >2:
    i = -1
    while c[c2[i]] == 0 or (res[-1]+1) ==c[c2[i]]:
        i-=1
    res.append(c2[i])
    c[c2[i]]-=1
    if c[c2[i]] == 0:
        num_type -=1

if num_type == 2:
    if res:
        print(" ".join(map(str,res)),end= " ")
    i = 0
    j = 0
    while c[c2[i]] == 0:
        i+=1
    while c[c2[j]] == 0 or j == i:
        j+=1
    if c2[i] == c2[j]+1:
        for _ in range(c[c2[i]]):
            print(c2[i], end= " ")
        for _ in range(c[c2[j]]):
            print(c2[j], end= " ")
    else:
        for _ in range(c[c2[j]]):
            print(c2[j], end= " ")
        for _ in range(c[c2[i]]):
            print(c2[i], end= " ")
else:
    print(*l)"""


from collections import Counter

input()

l = list(map(int,input().split()))
c = Counter(l)
c2= sorted(c.keys(),reverse=True)
num_type = len(c2)
res=[]

if num_type > 2:
    res.append(c2[-1])
    c[c2[-1]]-=1
    if c[c2[-1]] ==0:
        num_type-=1

while num_type > 2:
    i = -1
    while c[c2[i]] == 0 or c2[i] == res[-1]+1:
        i-=1
    res.append(c2[i])
    c[c2[i]]-=1
    if c[c2[i]] == 0:
        num_type -=1

if num_type==2:
    i = 0
    j = 0
    while c[c2[i]] == 0:
        i += 1
    while c[c2[j]] == 0 or j == i:
        j += 1
    if c2[i]-c2[j] == 1:
        for _ in range(c[c2[i]]):
            res.append(c2[i])
        for _ in range(c[c2[j]]):
            res.append(c2[j])
    else:
        for _ in range(c[c2[j]]):
            res.append(c2[j])
        for _ in range(c[c2[i]]):
            res.append(c2[i])
else:
    for _ in range(c[c2[0]]):
        res.append(c2[0])
print(*res)