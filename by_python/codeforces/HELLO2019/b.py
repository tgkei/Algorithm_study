n = int(input())
nums = [int(input()) for _ in range(n)]

def calc(num,i):
    if i == n:
        return not num%360
    return calc(num+nums[i],i+1) or calc(num-nums[i],i+1)

if calc(0, 0):
    print("YES")
else:
    print("NO")