"""
https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050ff4/0000000000051183
"""

for T in range(int(input())):
    F, L = map(int,input().split())

    temp = F
    result = 0

    while temp <= L:
        temp3 = str(temp)
        ok = True
        if temp != 0 and temp%9 == 0:
            temp += 1
            continue
        for t in temp3:
            if t =='9':
                ok = False
                break
        if ok:
            result+=1
        temp+=1

    print("Case #{}: {}".format(T+1, result))
                
    