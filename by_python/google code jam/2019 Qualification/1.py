for j in range(int(input())):
    N = list(input())
    a=0
    b=0
    for i, n in enumerate(reversed(N)):
        if n == '4':
            b +=2 * (10**i)
            a +=2 * (10**i)
        else:
            a += int(n) *(10**i)
    print("Case #{}: {} {}".format(j+1, a, b))