for T in range(int(input())):
    R, C = map(int,input().split())

    result = [[False for _ in range(C)] for _ in range(R)]
    i = 1
    answer =[]

    while i < R:
        j = 1
        if i == 1 or R % i != 0:
            while j< C:
                answer = []
                col_pos = 0
                row_pos = 0
                for _ in range(R*C):
                    if j == 1 or (C % j != 0):
                        if i == j:
                            break

                        if result[row_pos][col_pos]:
                            result = [[False for _ in range(C)] for _ in range(R)]
                            j+=1
                            continue
                        else:
                            result[row_pos][col_pos] = True
                            answer.append("{} {}".format(row_pos, col_pos))
                            row_pos = (row_pos + i) % R
                            col_pos = (col_pos + j) % C
                j+=1
        i+=1

    if answer:
        print("Case #{}: POSSIBLE".format(T+1))
        for ans in answer:
            a = []
            a.append(str(int(ans[0])+1))
            a.append(str(int(ans[2])+1))
            
            print(" ".join(a))
    else:
        print("Case #{}: IMPOSSIBLE".format(T+1))