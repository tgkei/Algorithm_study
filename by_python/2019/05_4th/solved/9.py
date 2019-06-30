"""
2018-2019 acpc
https://codeforces.com/problemset/problem/1089/L
"""

n , k = map(int,input().split())
jobs = list(map(int,input().split()))
per_time = list(map(int,input().split()))

dic = {}

for i in range(len(jobs)):
    if jobs[i] in dic:
        dic[jobs[i]] +=[per_time[i]]
    else:
        dic[jobs[i]] = [per_time[i]]

result = []

for _,v in dic.items():
    k-=1
    result += sorted(v)[:-1]

print(sum(sorted(result)[:k]))