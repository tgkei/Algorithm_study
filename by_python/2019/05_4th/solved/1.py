"""
556 division 1 a.py
https://codeforces.com/contest/1149/problem/A
"""

input()

l = list(map(int,input().split()))

num1 = l.count(1)
num2 = l.count(2)

if num1 == 0:
    for _ in range(num2):
        print(2,end=" ")
elif num2 == 0:
    for _ in range(num1):
        print(1, end = " ")
else:
    num1-=1
    num2-=1
    print(2,1,end=" ")
    for _ in range(num2):
        print(2, end=" ")
    for _ in range(num1):
        print(1, end=" ")