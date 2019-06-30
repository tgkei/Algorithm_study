n, _ = map(int,input().split())

nums = list(map(lambda x: int(x)-1,input().split()))

l = [0] * n
total = 0

for num in nums:
    if l[num] == 0:
        total += 1
    l[num] +=1
    if total == n:
        print(1,end="")
        total = 0
        for i in range(n):
            l[i] -=1
            if l[i]:
                total+=1
    else:
        print(0,end="")