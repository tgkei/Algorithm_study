from math import floor

N, k = map(int, input().split())

total = 0
nums = []
for _ in range(N):
    tmp = float(input())
    nums.append(tmp)
    total += tmp

avg = total / k

top = max(nums)
avg = floor(avg * 1000)/1000.0

while (1):
    tmp = 0

    for num in nums:
        tmp += int(num//avg)

    if tmp> k:
        tmp2 = 0
        for num in nums:
            tmp2 += int(num//(avg-0.001))
        if tmp2 < k:
            print('{0:.2f}'.format(round(avg,2)))
            break
        avg = int((top+avg) /2 * 1000) / 1000
    elif tmp < k:
        tmp2 = 0
        for num in nums:
            tmp2 += int(num//(avg+0.001))
        if tmp2 > k:
            print('{0:.2f}'.format(round(avg,2)))
            break
        top = avg
        avg = int(avg /2 * 1000) / 1000
    else:
        print('{0:.2f}'.format(round(avg,2)))
        break