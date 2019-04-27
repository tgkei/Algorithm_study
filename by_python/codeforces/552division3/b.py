n = int(input())

if n %2==0:
    n = (n // 2)-1
else:
    n = (n//2)

nums = list(map(int,input().split()))

nums.sort()
set_num = set(nums)

sum_first_last = nums[0] + nums[-1]

result = -1

if sum_first_last % 2 == 1: # if sum of first and last number is odd
    if (nums[n] == nums[0]) or (nums[n] == nums[-1]):
        result = nums[-1] - nums[0]
else:
    result = sum_first_last//2 - nums[0]
    if len(set_num) == 3:
        if(nums[n] != (nums[0]+result)):
            result = -1

if len(set_num) > 3:
    result = -1

print(result)