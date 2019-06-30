for i in range(int(input())):
    _, r,_, row,col = map(int,input().split())
    inst= list(input())
    row = row - 1
    col = col - 1

    visited = [[] for _ in range(r)]
    visited[row].append(col)
    
    for ins in inst:
        if ins == 'E':
            col+=1
            while col in visited[row]:
                col+=1
            visited[row].append(col)
        elif ins == 'W':
            while col in visited[row]:
                col-=1
            visited[row].append(col)
        elif ins == 'S':
            while col in visited[row]:
                row +=1
            visited[row].append(col)
        else:
            while col in visited[row]:
                row-=1
            visited[row].append(col)

    print("Case #{}: {} {}".format(i+1, row+1, col+1))