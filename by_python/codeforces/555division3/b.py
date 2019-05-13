input()

nums = input()
corres = list(map(int,input().split()))
result = ""
i = 0

while i < len(nums) and int(nums[i]) >= corres[int(nums[i])-1]:
    result += nums[i]
    i+=1

while i < len(nums) and int(nums[i]) <= corres[int(nums[i])-1]:
    result += str(corres[int(nums[i])-1])
    i+=1

while i < len(nums):
    result += nums[i]
    i+=1

print(result)