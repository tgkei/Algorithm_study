#https://codeforces.com/problemset/problem/1194/D

for _ in range(int(input())):
    start, k = map(int,input().split())
    if k %3 != 0:
        print("Alice" if start%3 else "Bob")
    else:
        start %= (k+1)
        if start == k: print("Alice")
        else: print("Alice" if start%3 else "Bob")