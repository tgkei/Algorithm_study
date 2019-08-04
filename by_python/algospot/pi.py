import sys
sys.setrecursionlimit(99999)

def cost(start, end):
    temp = s[start:end]
    temp = list(map(int,temp))
    t_set = set(temp)
    if len(t_set) == 1: return 1
    
    prefix = temp[1] - temp[0]
    arith_seq = True
    for i in range(len(temp)-1):
        if prefix != temp[i+1] - temp[i]:
            arith_seq = False
            break
    if arith_seq and abs(prefix) == 1 :return 2
    elif arith_seq: return 5
    for i in range(len(temp)):
        if temp[i] != temp[i%2]: break
    else: return 4
    return 10

def solve(start):
    global cache
    if start == n: return 0
    if start+ 2 >= n: return 100
    if cache[start] != -1: return cache[start]
    res = 10000000
    for i in range(3,6):
        res = min(res, solve(start+i)+cost(start,start+i))
    cache[start] = res
    return res

for _ in range(int(input())):
    s = input().rstrip()
    n = len(s)
    cache = [-1] * n
    start = 0
    res = solve(start)
    print(res)