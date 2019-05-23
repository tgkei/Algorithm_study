n, k = map(int,input().split())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

dic = {}

for i, f in zip(a,b):
    if i in dic:
        dic[i] +=[f]
    else:
        dic[i] =[f]

for _,value in dic.items():
    value.sort()
    value.pop()
    k-=1

res = []

for _,value in dic.items():
    for v in value:
        res.append(v)

res.sort()

print(sum(res[:k]))