from math import inf

for T in range(int(input())):
    result = 0
    n, r = map(int, input().split())
    skills = list(map(int,input().split()))
    
    skills.sort()

    diff = []

    cache = []
    repeat = len(skills)-1

    
    for i in range(repeat):
        diff.append(skills[i+1] - skills[i])
    
    r = r-1
    repeat = len(diff)-1
    for i in range(repeat, r-1, -1):
        result = 0
        for new_r in range(r,0,-1):
            result += (diff[i]*new_r)
        cache.append(result)
    
    result = min(cache)

    print("Case #{}: {}".format(T+1, result))