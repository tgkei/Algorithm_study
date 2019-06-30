"""
529 div3
https://codeforces.com/problemset/problem/1095/C
"""

n, k = map(int,input().split())

binary = []

while n > 0:
    i = 0
    while 2**i <= n:
        i+=1
    i-=1
    binary.append(2**i)
    n-=2**i

k -= len(binary)
i=0
while k >0 and i <len(binary):
    while k>0 and binary[i]>1:
        binary.append(binary[i]//2)
        binary[i]//=2
        k-=1
    i+=1

if k != 0:
    print("NO")
else:
    print("YES")
    print(*binary)