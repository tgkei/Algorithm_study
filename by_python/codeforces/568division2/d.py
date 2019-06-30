# https://codeforces.com/contest/1185/problem/D

def check(l):
    res = set()
    for i in range(len(l)-1):
        res.add(l[i+1]-l[i])
    return len(res) == 1

input()

nums = list(map(int,input().split()))
dic = {}
for idx, num in enumerate(nums):
    dic[num] = idx+1

nums.sort()

if check(nums):
    print(dic[nums[0]])
    exit(0)
elif check(nums[1:]):
    print(dic[nums[0]])
    exit(0)
elif check(nums[:1]+nums[2:]):
    print(dic[nums[1]])
    exit(0)

d = nums[1]-nums[0]

for i in range(2,len(nums)):
    if nums[i]-nums[i-1] != d:
        if check(nums[:i]+nums[i+1:]):
            print(dic[nums[i]])
        else:
            print(-1)
        exit(0)
