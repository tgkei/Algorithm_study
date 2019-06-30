n = int(input())

l = [-1] * (n+1)

used = False
num = 1
for i in range(2,n+1):
    j = i
    while j <n+1:
        if l[j] == -1:
            l[j]= num
            used= True
        j+=i
    if used:
        used= False
        num+=1
l = l[2:]
print(*l)