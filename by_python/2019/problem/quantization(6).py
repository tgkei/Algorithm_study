# https://algospot.com/judge/problem/read/QUANTIZE
import statistics
from math import inf

C = int(input())
def init():
    global prefix
    global seq_pref
    pre_sum = 0
    seq_sum = 0
    for i in range(n):
        pre_sum += l[i]
        seq_sum += (l[i]**2)
        prefix[i] = pre_sum
        seq_pref[i] = seq_sum

def find_mean(start,end):
    if start == 0: 
        t= prefix[end-1]
        t2 = seq_pref[end-1]
    else: 
        t = prefix[end-1] - prefix[start-1]
        t2 = seq_pref[end-1] - seq_pref[start-1]
    m = round(t / (end-start))
    return t2 - 2*m * t + m**2 *(end-start)

def solve(pos, parts):
    if pos == n: return 0
    if parts > m: return inf
    
    if cache[pos][parts] != -1: return cache[pos][parts]
    
    ret = inf
    for i in range(pos+1, n+1):
        ret = min(ret, find_mean(pos,i)+solve(i,parts+1))
    cache[pos][parts] = ret
    return ret

for _ in range(C):
    n, m = map(int,input().split())
    l = list(map(int,input().split()))
    l.sort()
    prefix = [-1] * n
    seq_pref = [-1] * n
    cache = [[-1 for _ in range(m+1)] for _ in range(n)]
    res = 0
    init()
    res = solve(0,1)
    print(res)