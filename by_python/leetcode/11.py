""" hashtable
nums = list(map(int,input().split()))

res = []
for i in range(len(nums)-2):
    if i>0 and nums[i-1] == nums[i]: continue
    s = set()
    target = - nums[i]
    for j in range(i+1,len(nums)):
        if target - nums[j] in s:
            res.append(sorted([nums[i],nums[j],target-nums[j]]))
        else:
            s.add(nums[j])
res_set = set(tuple(i) for i in res)
res = list(list(i) for i in res_set)
print(*res)
"""
""" 2pointer
nums = list(map(int,input().split()))
nums.sort()
res = []
for i in range(len(nums)-2):
    if i>0 and nums[i-1] == nums[i]: continue
    l = i+1
    r = len(nums)-1
    target = - nums[i]
    while l != r:
        if nums[l]+nums[r] < target:
            l+=1
        elif nums[l] + nums[r] > target:
            r-=1
        else:
            res.append([nums[i],nums[l],nums[r]])
            while l != r and nums[l] == nums[l+1]:
                l +=1
            while l != r and nums[r] == nums[r-1]:
                r-=1
            l+=1, r-=1
return res
"""