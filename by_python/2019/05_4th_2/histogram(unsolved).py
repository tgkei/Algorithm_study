"""
codeground
"""

import sys

inf = sys.stdin 

T = inf.readline()

for t in range(0, int(T)):
    
    Answer=0
    n = int(input())
    nums = list(map(int,input().split()))

    i = 0
    j = 1
    prev = -1
    while j < n:
        if nums[j]<nums[j-1]:
            Answer+=(sum(nums[i:j+1])/(j-i+1))
            i = j+1
            j = i+1
        else:
            j+=1
    if i != n:
        Answer+=(sum(nums[i:j])/(j-i+1))
    print('Case #%d' %(t+1))    
    print(Answer)
inf.close()