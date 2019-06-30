import sys

inf = sys.stdin 

T = inf.readline()

for t in range(0, int(T)):
    
    Answer=0
    n = int(input())
    nums = list(map(int,input().split()))

    i = 0
    j = 1
    prev = nums[i]
    while j < n:
        if prev > nums[j]:
            if j-1 == i:
                prev = (prev+nums[j])/2
            else:
                prev = ((prev*(j-i))+nums[j])/(j+1-i)
    print('Case #%d' %(t+1))    
    print(Answer)
inf.close()