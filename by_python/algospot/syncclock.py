from math import inf

switches = [
    [True, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, True, False, False, False, True, False, True, False, True, False, False, False, False],
    [False, False, False, False, True, False, False, False, False, False, True, False, False, False, True, True],
    [True, False, False, False, True, True, True, True, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, True, True, True, False, True, False, True, False, False, False],
    [True, False, True, False, False, False, False, False, False, False, False, False, False, False, True, True],
    [False, False, False, True, False, False, False, False, False, False, False, False, False, False, True, True],
    [False, False, False, False, True, True, False, True, False, False, False, False, False, False, True, True],
    [False, True, True, True, True, True, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, True, True, True, False, False, False, True, False, False, False, True, False, False]
]

def twelve():
    for i in range(16):
        if clocks[i] != 12:
            return False
    return True

def change(switch):
    global clocks
    for i in range(16):
        if switches[switch][i]:
            clocks[i] +=3
            if clocks[i] == 15:
                clocks[i] = 3

def push(switch):
    if switch == 10:
        if twelve():
            return 0
        else:
            return inf
    
    ret = inf
    for i in range(4):
        ret = min(ret, i+push(switch+1))
        change(switch)
    return ret

for _ in range(int(input())):
    clocks = list(map(int,input().split()))

    res = push(0)

    print(res)
    