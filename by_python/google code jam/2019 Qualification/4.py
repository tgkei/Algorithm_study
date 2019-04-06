import sys

output= ["01"*512, "0011"*256, "00001111"*128, "0000000011111111" * 64, "00000000000000001111111111111111"*32]

for _ in range(int(input())):
    value = []
    N, B, _ = map(int, input().split())

    for i in range(5):
        print(output[i][:N])
        sys.stdout.flush()
        value.append(input())

    maximum = -1
    test = [True]*N
    th = 0
    for i in range(N-B):
        temp = 0
        temp += int(value[0][i])*1
        temp += int(value[1][i])*2
        temp += int(value[2][i])*4
        temp += int(value[3][i])*8
        temp += int(value[4][i])*16
        if maximum > temp: 
            th += 1
        if th > 0:
            temp = temp+ (32*th)
        maximum = temp - (32*th)
        test[temp] = False

    result = ""

    for i,t in enumerate(test):
        if t:
            result += (str(i))
            result += " "
            if len(result) == (2*B):
                break

    print(result)
    sys.stdout.flush()
    input()