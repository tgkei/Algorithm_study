def solve(start, end): #start index(starting from 0) and end index not include end
    if start+1 == end:
        return nums[start]
    mid = (end+start)//2
    left = solve(start,mid)
    right = solve(mid, end)
    
    cur_left = mid-1
    cur_right = mid
    
    height = min(nums[cur_left],nums[cur_right])
    width = 2
    
    middle = height* width
    max_mid = middle
    
    for _ in range(n-2):
        width +=1
        if cur_left==0:
            cur_right +=1
            height = min(height, nums[cur_right])
        elif cur_right == n-1:
            cur_left -= 1
            height = min(height, nums[cur_left])
        elif nums[cur_left] < nums[cur_right]:
            cur_right+=1
            height = min(height, nums[cur_right])
        else:
            cur_left-=1
            height = min(height,nums[cur_left])

        middle = height * width
        max_mid = max(max_mid, middle)
    res = max(left, right)
    res = max(res,max_mid)

    return res

for _ in range(int(input())):
    n = int(input())
    nums = list(map(int,input().split()))
    print(solve(0,n))