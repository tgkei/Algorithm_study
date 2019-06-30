"""
https://codeforces.com/contest/1169/problem/B
"""
n, p = map(int,input().split())

nums=[]
done = False

for _ in range(p):
    n1, n2 = map(int,input().split())
    nums.append((n1,n2))

for i in range(2):
    j =1
    check=nums[0][i]
    while j < p and check in nums[j]:
        j+=1
    if j == p:
        done = True
        break
    else:
        for ii in range(2):
            k = j+1
            check = nums[j][ii]
            while k < p and check in nums[k]:
                k+=1
            if k== p:
                done = True
                break

print("YES" if done else "NO")