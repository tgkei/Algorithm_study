for T in range(int(input())):
    n, m = map(int,input().split())
    nums = sorted(list(map(int,input().split())))

    prefix_sum = []

    temp = 0
    for num in nums:
        temp += num
        prefix_sum.append(temp)

    result = (m-1) * nums[m-1]-prefix_sum[m-2]
    for i in range(m,n):
        result = min((m-1)* nums[i] - (prefix_sum[i-1]-prefix_sum[i-m]), result)
        

    print("Case #{}: {}".format(T+1, result))
