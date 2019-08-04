for _ in range(int(input())):
    a, b, c = map(int,input().split())
    at_least = min(b,c)
    print(a-at_least+1)