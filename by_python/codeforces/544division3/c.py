n = int(input())
nums = sorted(map(int,input().split()))
pref = []

if n ==1:
    print("1")
else:
    for i,j in zip(nums[:-1],nums[1:]):
        pref.append(j-i)

    n-=1

    l= 0
    r= 0

    prefix_sum = 0
    maximum = -1

    while r<n:
        while prefix_sum <= 5 and r<n:
            maximum = max(maximum, r+1-l)
            prefix_sum += pref[r]
            r+=1
        if r ==n and prefix_sum <=5:
            maximum = max(maximum, r+1-l)

        while prefix_sum > 5 and l<=r:
            prefix_sum -= pref[l]
            l+=1

    print(maximum)