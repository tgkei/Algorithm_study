def jlis(cur, a_pos, b_pos):
    if cache[a_pos][b_pos] != -1: return cache[a_pos][b_pos]
    if num1[a_pos] == num2[b_pos]: ret =1
    else: ret =2
    for i in range(a_pos+1, a):
        if cur < num1[i]:
            ret = max(ret, jlis(num1[i], i, b_pos)+1)
    for i in range(b_pos+1, b):
        if cur < num2[i]:
            ret = max(ret, jlis(num2[i], a_pos, i)+1)
    cache[a_pos][b_pos] = ret
    return ret

for _ in range(int(input())):
    a, b = map(int,input().split())
    num1 = list(map(int,input().split()))
    num2 = list(map(int,input().split()))

    cache = [[-1 for _ in range(b)] for _ in range(a)]
    ret = -1
    for i in range(a):
        ret = max(ret, jlis(num1[i],i,0))
    for j in range(b):
        ret = max(ret, jlis(num2[j],0,j))
    print(ret)