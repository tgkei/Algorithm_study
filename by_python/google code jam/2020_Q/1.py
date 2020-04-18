T = int(input())

for Test in range(T):
    N = int(input())
    k, r, c = 0, 0, 0

    matric = []

    for row in range(N):
        tmp = list(map(int, input().split()))
        tmp_set = set(tmp)
        k += tmp[row]
        if len(tmp_set) != N: r +=1
        matric.append(tmp)
    for column in range(N):
        tmp = set()
        for row in range(N):
            if matric[row][column] in tmp:
                c+=1
                break
            tmp.add(matric[row][column])

    print("Case #{}: {} {} {}".format(Test+1, k, r, c))
