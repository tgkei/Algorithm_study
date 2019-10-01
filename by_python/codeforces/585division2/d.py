left = 0
right = 0
n = int(input())
nums = input()
l_erase = []
r_erase = []
for idx,num in enumerate(nums[:n//2]):
    if num == '?':
        l_erase.append(idx)
        continue
    left += int(num)
for idx,num in enumerate(nums[n//2:]):
    if num == '?': 
        r_erase.append(idx+n//2)
        continue
    right += int(num)
