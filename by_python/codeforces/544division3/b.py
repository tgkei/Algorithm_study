_, k = map(int,input().split())

nums = list(map(int,input().split()))

div = [0 for _ in range(k)]

for num in nums:
    div[num%k]+=1

answer = 0

answer+= (div[0]//2)

if not k%2:
    answer+=(div[k//2]//2)

i =1
j = k-1

while i < j:
    answer+=min(div[i],div[j])
    i+=1
    j-=1

print(answer*2)