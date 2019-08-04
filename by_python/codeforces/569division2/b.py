n = int(input())
nums = list(map(int,input().split()))

minimum = 1
min_idx = -1

for idx, num in enumerate(nums):
    if num >= 0:
        nums[idx] = -(num)-1
    if minimum > nums[idx]:
        minimum = nums[idx]
        min_idx = idx

if n % 2:
    nums[min_idx] = -(nums[min_idx])-1

print(*nums)