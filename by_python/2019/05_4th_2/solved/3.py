"""
https://codeforces.com/problemset/problem/1159/B
"""
n = int(input())

nums = list(map(int,input().split()))

minimum = 10**9+1

for i in range(n):
    below = max((n-1-i),(i-0))
    upper = nums[i]
    minimum = min((upper//below),minimum)

print(minimum)