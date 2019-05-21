"""
edu 59 division 2 c.py
https://codeforces.com/contest/1107/problem/C
"""

n, m = map(int,input().split())
nums = list(map(int,input().split()))
string = list(input())

dmg = 0
start = 0
end = 0 

while end < n:
    while end < n and string[start] == string[end]:
        end+=1
    if (end - start) <= m:
        dmg+= sum(nums[start:end])
    else:
        dmg += sum(sorted(nums[start:end],reverse= True)[:m])
    start = end

print(dmg)