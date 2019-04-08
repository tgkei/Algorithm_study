"""
방법 1
  * 미리 배열을 모두 만들어 놓고 거기서 값을 구하기

from math import inf
n = int(input())

a= [0, 0,1,1]

for i in range(4, 1000001):
    minimum = inf
    if i %3 ==0:
        minimum = a[i // 3]
    if i %2 == 0:
        minimum = min(minimum,a[i // 2])
    minimum = min(minimum,a[i -1])
    a.append(1+minimum)

print(a[n])
"""
"""
방법 2
재귀를 만들어 봤지만 너무 깊어진다 (예를 들어 1000000) 그래서 안되는데 더 효율적이거나 방법이 있을까?

from math import inf

a = [0]*1000000
a[0] = 1
a[1] = 1
a[2] = 1
n = int(input())

def make_one(number):
    minimum = inf
    if a[number-1] != 0:
        return a[number-1]
    if (number)%3 ==0:
        minimum = min(minimum, make_one(number//3))
    if number%2 == 0:
        minimum = min(minimum, make_one(number//2))
    minimum = min(minimum, make_one(number-1))
    a[number-1] = minimum+1
    return a[number-1]

print(make_one(n))
"""