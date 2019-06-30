n, m = map(int,input().split())

l = []

for _ in range(m):
    t = sorted(map(int,input().split()))
    for ll in l:
        for num in ll:
            