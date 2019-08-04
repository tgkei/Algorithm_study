def change(a_idx,b_idx):
    if cache[a_idx][b_idx] != -1: return cache[a_idx][b_idx]
    if a_idx == b_idx: 
        if a[a_idx] == b[b_idx]: return 1
        else: return 0
    if a_idx >b_idx:
        return 0

    res = 0
    if a[a_idx] == b[b_idx]: res+=1
    if a[b_idx] == b[a_idx]: res+=1
    res += change(a_idx+1,b_idx-1)
    cache[a_idx][b_idx] = res
    return res

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    cache = [[-1 for i in range(n)] for i in range(n)]
    cache2 = [-1 for i in range(n)]

    res = 0
    for i in range(n):
        if a[i] == b[i] : 
            res+=1
        cache2[i] = res
    
    for i in range(n):
        for j in range(n-1,i,-1):
            temp = -1
            if a[i] == b[j]:
                if i<j:
                    if i ==0:
                        temp = cache2[-1] - cache2[j] + change(i,j)
                    else:
                        temp = cache2[-1] - cache2[j] + cache2[i-1] + change(i,j)
                else:
                    if j ==0 :
                        temp = cache2[-1] - cache2[i] + change(j,i)
                    else:
                        temp = cache2[-1] - cache2[i] + cache2[j-1] + change(j,i)
                res = max(res,temp)
    print("Case #{}".format(_+1))
    print(res)