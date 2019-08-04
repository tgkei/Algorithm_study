# https://algospot.com/judge/problem/read/WILDCARD

def solve(idx1, idx2):
    while idx1 < len(s) and idx2 < len(com) and (com[idx2] == s[idx1] or s[idx1] == '?'): 
        idx1+=1
        idx2+=1
    if idx1 == len(s): return idx2 == len(com)
    if s[idx1] == '*':
        for i in range(idx2,len(com)+1):
            if solve(idx1+1,i): return True
    return False

for _ in range(int(input())):
    s = input()
    comp = [input() for i in range(int(input()))]
    res = []

    for com in comp:
        if solve(0, 0):
            res.append(com)
    for r in res:
        print(r)