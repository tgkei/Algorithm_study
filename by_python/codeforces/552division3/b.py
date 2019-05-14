input()

nums = list(sorted(set(map(int,input().split()))))
if len(nums) > 3:
    print("-1")
elif len(nums) ==3:
    if nums[0]+nums[-1] != nums[1]*2:
        print("-1")
    else:
        print(nums[1]-nums[0])
elif len(nums)==1:
    print("0")
else:
    if (nums[0] + nums[1])%2:
        print(nums[1]-nums[0])
    else:
        print((nums[1]-nums[0])//2)