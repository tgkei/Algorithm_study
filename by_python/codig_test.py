# greatest common divisor Euler

def gcd(m,n):   
    while True:
        if n > m :
            m, n = n, m
        r = m%n
        if (r ==0):
             return n
        else:
            m = n
            n = r



## Binary search

from bisect import bisect_left 
  
def BinarySearch(a, x): 
    i = bisect_left(a, x) 
    if i != len(a) and a[i] == x: 
        return i 
    else: 
        return -1
  
a  = [1, 2, 4, 4, 8] 
x = int(4) 
res = BinarySearch(a, x) 
if res == -1: 
    print(x, "is absent") 
else: 
    print("First occurrence of", x, "is present at", res)


## interactive

import sys

print("anything")
sys.stdout.flush()
s = input()