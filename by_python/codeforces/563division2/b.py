input()

nums = list(map(int,input().split()))

odd = 0
even = 0

for num in nums:
    if num % 2:
        odd+=1
    else:
        even+=1

if odd and even:
    nums.sort()
print(*nums)