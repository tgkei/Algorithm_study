n = int(input())

nums = list(map(int,input().split()))

temps = []
last_num = -1
left = 0
right = n-1

answer = ""

while left <= right and max(nums[left],nums[right])>last_num:
    if nums[left]>last_num>nums[right] or last_num<nums[left]<nums[right]:
        answer+="L"
        last_num=nums[left]
        left+=1
    else:
        answer+="R"
        last_num=nums[right]
        right-=1

print(len(answer))
print(answer)