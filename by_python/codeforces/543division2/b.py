"""n = int(input())
l = list(map(int,input().split()))

dic = {}

for i in range(n-1):
    for j in range(i+1,n):
        s = l[i]+l[j]
        if s in dic.keys():
            dic[s] +=1
        else:
            dic[s] = 1
print(max(list(dic.values())))"""

from collections import Counter

n = int(input())
l = list(map(int, input().split()))

dic = Counter()

for i in range(n-1):
    for j in range(i+1,n):
        dic[l[i]+l[j]]+=1

print(dic.most_common()[0][1])