#https://codeforces.com/problemset/problem/1176/C

input()

nums = list(map(int,input().split()))
idx = [4,8,15,16,23,42]
d = {4:0,
    8:0,
    15:0,
    16:0,
    23:0,
    42:0}
res = 0
for num in nums:
    t_idx = idx.index(num)
    if t_idx ==0: d[4] +=1
    else:
        dic_idx = idx[t_idx - 1]
        if d[num] < d[dic_idx]: d[num]+=1
        else: res +=1

for _,value in d.items():
    res += (value - d[42])
print(res)