from math import inf

n = int(input())-1

nums = list(map(int,input().split()))

minimum = inf

for idx, num in enumerate(nums):
    temp = inf
    mo = max(idx-0,n-idx)
    minimum = min(minimum,num // mo)

print(minimum)