#https://codeforces.com/problemset/problem/1195/C
#런타임 에러
import sys
sys.setrecursionlimit(100001)
p = 0
def solve(option,idx):
    global a
    global b
    global p
    if idx == n: return 0
    if cache[option-1][idx] != -1: return cache[option-1][idx]
    print(p,end=" ")
    p+=1
    res = 0
    if option == 1:
        res = max(b[idx] + solve(2,idx+1),solve(3,idx+1))
    elif option ==2:
        res = max(a[idx] + solve(1,idx+1), solve(3,idx+1))
    else:
        res = max(a[idx] + solve(1,idx+1), b[idx] + solve(2,idx+1))
    cache[option-1][idx] = res
    return res
f = open("testcase.txt","r")
n = int(f.readline())
a = list(map(int,f.readline().split()))
b = list(map(int,f.readline().split()))
f.close()
cache = [[-1 for _ in range(n)] for _ in range(3)]
res = solve(3,0)

print(res)