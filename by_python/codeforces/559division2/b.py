from math import inf

n = int(input())

nums = list(map(int,input().split()))

minimum = inf

for i in range(n):
    bot= max(i-0,n-1-i)
    minimum = min(minimum,nums[i]//bot)

print(minimum)