"""
https://codeforces.com/problemset/problem/1169/B
"""

"""_, n = map(int,input().split())

nums = []
for _ in range(n):
    nums.append(tuple(map(int,input().split())))

for i in nums[0]:
    for idx, num in enumerate(nums):
        if i not in num:
            for j in num:
                for num2 in nums[idx:]:
                    if j not in num2:
                        break
                else:
                    print("YES")
                    exit(0)
            break
    else:
        print("YES")
        exit(0)
print("NO")"""

n,m=map(int,input().split())
a=[]
for i in range(m):
    a.append(list(map(int,input().split())))
for x in a[0][0],a[0][1]:
    s=set(i for i in range(1,n))
    for i in a[1:]:
        if x not in i:
            s.intersection_update(set(i))
    if len(s):
        exit(print("YES"))
print("NO")