from math import inf

for T in range(10):
    N = int(input())
    nums = list(map(int,input().split()))
    
    answer = 0
    
    for i in range(N):
        left1 = nums[i-1] if i-1 >=0 else -inf
        left2 = nums[i-2] if i-2 >=0 else -inf
        
        right1 = -inf
        right2 = -inf
        if i + 1 < N:
            right1 = nums[i+1]
        if i + 2 < N:
            right2 = nums[i+2]
        highest = max(left1,left2,right1,right2)
        if nums[i] > highest:
            answer += nums[i] - highest

    print("#{} {}".format(T+1, answer))