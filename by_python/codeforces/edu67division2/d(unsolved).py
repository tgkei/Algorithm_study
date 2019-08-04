for _ in range(int(input())):
    n = int(input())
    s1 = list(map(int,input().split()))
    s2 = list(map(int,input().split()))
    res = []
    index =0
    while index < n:
        while index < n and s1[index] == s2[index]:
            res.append(s1[index])
            index+=1
        start = index
        while index < n and s1[index] <= s1[start] and s1[start] > s2[index]:
            index+=1
        if index == n:
            res += sorted(s1[start:])
        else:
            res += sorted(s1[start : index+1])
        index +=1
    if res == s2: print("YES")
    else: print("NO") 