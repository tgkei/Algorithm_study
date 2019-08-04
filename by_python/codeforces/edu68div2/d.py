"""for _ in range(int(input())):
    n, k = map(int, input().split())
    if n == k:
        print("Alice")
    elif k>n:
        print("Alice" if n%3 else "Bob")
    elif k%3:
        print("Alice" if n%3 else "Bob")
    else:
        n %= (4 + 3*((n//3)-1))
        if n == (4 + 3*((n//3)-1)-1):
            print("Bob")
        elif n %3 == 0:
            print("Bob")
        else:
            print("Alice")"""

"""for _ in range(int(input())):
    n, k = map(int, input().split())
    if n == k:
        print("Alice")
    elif k%3:
        print("Alice" if n%3 else "Bob")
    else:
        if n < 3: n = 3
        n %= (4 + 3*((n//3)-1))
        if n == (4 + 3*((n//3)-1)-1):
            print("Bob")
        elif n %3 == 0:
            print("Bob")
        else:
            print("Alice")"""

for _ in range(int(input())):
    n,k=map(int,input().split())
    if(k%3==0):
        n%=(k+1)
    if(n%3==0 and n!=k):
        print("Bob")
    else:
        print("Alice")