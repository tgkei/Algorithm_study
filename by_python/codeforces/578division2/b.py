for _ in range(int(input())):
    n,m,k = map(int,input().split())
    heights = list(map(int,input().split()))
    pos = True
    for h1,h2 in zip(heights[:-1],heights[1:]):
        if h1 >= (h2-k):
            if h2-k >=0:
                m += (h1 - (h2-k))
            else:
                m += h1
        elif h2-k-h1<=m:
            m -= (h2-k-h1)
        else:
            pos = False
    print("YES" if pos else "NO")