N = int(input())

cache = {}

def f(target, avoid):
    ret = 0
    for new_avoid in range(1,4):
        if new_avoid == avoid:
            continue
        
        f(target-1,new_avoid)
    return ret


for _ in range(N):
    ret = 0
    target = int(input())
    cur_score = 0

    for avoid in range(1,4):
        ret = f(target, avoid)

    print(res%1000000009)