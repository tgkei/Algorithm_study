input()

figures = list(map(lambda x: int(x)-1,input().split()))

finite=False
num = 0
prev = -1

for first, second in zip(figures[:-1],figures[1:]):
    if first == 0 and second == 1:
        if prev == 2:
            num+=2
        else:
            num+=3
    elif first == 0 and second == 2:
        num += 4
    elif first == 1 and second == 0:
        num += 3
    elif first == 2 and second == 0:
        num += 4
    else:
        finite = True
        break
    prev = first

if finite:
    print("Infinite")
else:
    print("Finite")
    print(num) 
