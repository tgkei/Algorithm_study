from math import inf

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

a, b = map(int,input().split())

result = 0
minimum = inf

if a>b:
    a, b = b, a

for i in range(a):
    temp_a = a+i
    temp_b = b+i
    temp = minimum
    common_div = gcd(temp_a,temp_b)
    minimum= min(minimum,temp_a*(temp_b//common_div))
    if minimum != temp:
        result = i

print(result)