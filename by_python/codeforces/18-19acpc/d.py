"""
https://codeforces.com/problemset/problem/1070/D
"""

n, k = map(int,input().split())
nums = list(map(int,input().split()))

result = 0
remain = 0

for num in nums:
    if not (num+remain)//k and remain:
        result += 1
        remain = 0
        continue
    result += (num+remain)//k
    remain = (num+remain)%k

if remain:
    result+=1

print(result)