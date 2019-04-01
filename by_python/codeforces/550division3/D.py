from collections import Counter

n = int(input())


numbers = list(map(int,input().split()))
cnt = Counter()
for number in numbers: #n
    cnt[number] +=1

for key, _ in cnt.most_common(1):
    mv = key
result = []
j = 1
mv_j = 0
for i, number in enumerate(numbers):
    if number != mv:
        continue
    mv_j = i+1
    temp = mv_j
    while temp > j:
        result.append("1 "+str(temp-1)+" "+str(temp))
        #print("1 {} {}".format(mv_j, j))
        temp -= 1
    else:
        j = i+2
j = n
while j > mv_j:
    result.append("2 "+str(j)+" "+str(j-1))
    #print("2 {} {}".format(j, j-1))
    j-=1
print(len(result))
print("\n".join(result))