"""
edu65 div2 b
https://codeforces.com/contest/1167/problem/B
"""
nums = (4, 8, 15, 16, 23, 42)

dic={}

for i in range(6):
    for j in range(6):
        dic[nums[i]*nums[j]] = (nums[i],nums[j])

print("? 1 2", flush = True)
(a1, a2) = dic[int(input())]

print("? 2 3", flush = True)
(a3, a4) = dic[int(input())]

result = []

if a1 == a3:
    result.append(a2)
    result.append(a3)
    result.append(a4)
    prev = a4
elif a1 == a4:
    result.append(a2)
    result.append(a1)
    result.append(a3)
    prev = a3
elif a2 == a3:
    result.append(a1)
    result.append(a2)
    result.append(a4)
    prev = a4
else:
    result.append(a1)
    result.append(a2)
    result.append(a3)
    prev = a3

for i,j in zip(range(3,5),range(4,6)):
    print("? {} {}".format(i,j),flush=True)
    (a1, a2) = dic[int(input())]
    if prev == a1:
        result.append(a2)
        prev = a2
    else:
        result.append(a1)
        prev = a1

for num in nums:
    if num not in result:
        result.append(num)
print("!",end=" ")
print(*result)