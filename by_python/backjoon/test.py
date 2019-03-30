n = int(input())

a= [0, 1,1,1]

for i in range(3, 100_001):
    if i %3 ==0:
        i //= 3
    elif i %2 == 0:
        i //= 2
    else:
        i -=1

for i in range(1,n+1):
    if i == 1 or i ==n:
        print(' '*(n-i)+'*'*(2*i-1))
    else:
        print(' '*(n-i)+'*'+' '*(2*(i-1)-1)+'*')