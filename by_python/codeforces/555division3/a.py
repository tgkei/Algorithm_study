"""
n=input()
print(9+sum(9-int(d)for d in n[1:])+(len(n)>1))
"""

n = int(input())

result = 0
if not n % 10:
    result = 1
    n+=1

while n>10:
    n +=1
    while not n% 10:
        if n < 10:
            break
        n = n//10
    else:
        result +=1

result += 9
print(result)