"""
방법 1
"""

for j in range(int(input())):
    result = 0
    d, inst = input().split()
    d = int(d)
    inst = list(inst)
    num_s = inst.count('S')
    
    # Impossible case
    if num_s > d:
        print("Case #{}: IMPOSSIBLE".format(j+1))
        continue
    
    # Possible case
    dic = [0]
    i = 0
    total = 0

    for char in inst:
        if char == 'S':
            total += (2**i)
            dic[i]+=1
        else:
            i+=1
            dic.append(0)
    
    score = total
    while d < score:
        if dic[-1] ==0:
            dic.pop()
        result +=1
        score -= (2**(len(dic)-2))
        dic[-1] -= 1
        dic[-2] += 1

    print("Case #{}: {}".format(j+1,result))

"""
방법2
"""
"""
def damage(S):
    charge = 1
    ans = 0
    for c in S:
        if c == "S":
            ans+=charge
        else:
            charge *=2
    return ans

for case in range(int(input())):
    d, S = input().split()
    d = int(d)
    S = list(S)
    ans = 0
    while damage(S)>d:
        for i in reversed(range(len(S)-1)):
            if S[i] == 'C' and S[i+1] =='S':
                S[i] = 'S'
                S[i+1] = 'C'
                ans +=1
                break
        else:
            break
    
    if damage(S)>d:
        print("Case #{}: IMPOSSIBLE".format(case+1))
    else:
        print("Case #{}: {}".format(case+1, ans))
        """