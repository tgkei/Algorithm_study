for i in range(int(input())):
    result = -1
    n,k = map(int,input().split())
    distance = list(map(int,input().split()))
    color = list(map(int,input().split()))

    j = 1
    ptr = 1
    prev = color[0]
    point =[(ptr,distance[0])]
    while j < n:
        if prev == color[j]:
            ptr+=1
            point.append((ptr,distance[j]))
        else:
            ptr = 1
            point.append((ptr,distance[j]))
            prev = color[j]
        j+=1
    
    print("Case #{}: {}".format(i+1, result))