n, m = map(int,input().split())

a = [0] * n

unorder = []

for _ in range(m):
    t, l, r = map(int,input().split())

    if not t: 
        unorder.append((l,r))
        continue
    for i in range(l,r): a[i] = 1

for l, r in unorder:
    if set(a[l:r]) == {1}: 
        print("NO")
        exit(0)
print("YES")
v = 10**5
for e in a:
    if e:v+=1
    else: v-=1
    print(v,end=" ")