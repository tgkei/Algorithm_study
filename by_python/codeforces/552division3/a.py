"""nums = list(map(int,input().split()))

nums.sort()

result = []

for num in reversed(nums[:-1]):
    result.append(str(nums[-1]-num))

print(" ".join(result))"""

a, b, c, d = sorted(map(int, input().split()))

print(d-c, d-b, d-a)