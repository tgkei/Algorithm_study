def lis(cur):
    global cache
#    global nums

    if cache[cur] != -1: return cache[cur]
    res = 1
    for i in range(cur+1,n):
        if nums[cur]<nums[i]:
            res = max(res,lis(i)+1)
    cache[cur] = res
    return res

for _ in range(int(input())):
    n = int(input())
    cache = [-1] * n
    res = -1
    nums = list(map(int,input().split()))
    for i in range(n):
        res = max(res,lis(i))
    print(res)