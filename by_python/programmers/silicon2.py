def solution(office, k):
    maximum = -1
    N = len(office)
    
    for x_start in range(N-(k-1)):
        for y_start in range(N-(k-1)):
            x_cur = x_start
            y_cur = y_start
            res = 0
            for i in range(k):
                for j in range(k):
                    res+=office[x_cur+i][y_cur+j]
            maximum = max(maximum,res)
    return maximum

print(solution([[1,0,0,0],[0,0,0,1],[0,0,1,0],[0,1,1,0]],2))