n = int(input())

for _ in range(n):
    t = int(input())
    if t < 4:
        print(-1)
    else:
        start = 0
        if t % 2:
            start = -1
        else:
            start = -2
        for i in range(1, t + 1)[start::-2]:
            print(i, end=" ")
        print("4 2", end=" ")
        for i in range(6, t + 1)[::2]:
            print(i, end=" ")
        print()
