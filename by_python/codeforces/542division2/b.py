n = int(input())

nums = list(map(int,input().split()))
pos ={}

for i in range(len(nums)):
    if nums[i] in pos.keys():
        pos[nums[i]]+=[i]
    else:
        pos[nums[i]] = [i]

result = 0

for i in range(1,n):
    prev_pos = pos[i]
    aft_pos = pos[i+1]
    result += (abs(aft_pos[0] - prev_pos[0])+abs(aft_pos[1]-prev_pos[1]))

result += (pos[1][0]+pos[1][1])

print(result)