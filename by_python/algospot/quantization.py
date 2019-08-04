from math import inf

def init():
    global prefix
    global seq_pref
    pre_sum = 0
    seq_sum = 0
    for i in range(n):
        pre_sum += nums[i]
        seq_sum += (nums[i]**2)
        prefix[i] = pre_sum
        seq_pref[i] = seq_sum

def min_ave(start, end):
    if start == 0: 
        t= prefix[end-1]
        t2 = seq_pref[end-1]
    else: 
        t = prefix[end-1] - prefix[start-1]
        t2 = seq_pref[end-1] - seq_pref[start-1]
    m = round(t / (end-start))
    return t2 - 2*m * t + m**2 *(end-start)

def solve(part,start):
    global cache
    if start == n: return 0
    if part == s: return inf
    if cache[part][start] != -1: return cache[part][start]
    res = inf
    for i in range(start+1, n+1):
        res = min(res,min_ave(start,i)+solve(part+1,i))
    cache[part][start] = res
    return res

for _ in range(int(input())):
    n, s = map(int,input().split())
    cache = [[-1 for _ in range(n)] for _ in range(s)]
    prefix = [-1] * n
    seq_pref = [-1] * n
    nums = list(map(int,input().split()))
    nums.sort()

    init()
    print(solve(0, 0))