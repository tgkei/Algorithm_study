def solution(maps):
    adj = set()
    most ={}
    answer = []
    row, col = len(maps), len(maps[0])
    for cur_row, mm in enumerate(maps):
        for cur_col, m in enumerate(mm):
            if m == "." : continue

            if cur_col + 1 < col:
                right = mm[cur_col+1]
                if right !="." and right != m:
                    adj.add((m,right))
                    adj.add((right,m))
                    
                    if m not in most:
                        most[m] = set()
                        most[m].add(right)
                    else:
                        most[m].add(right)
                    
                    if right not in most:
                        most[right] = set()
                        most[right].add(m)
                    else:
                        most[right].add(m)

            if cur_row + 1 < row:
                down = maps[cur_row+1][cur_col]
                if down != "." and down != m:
                    adj.add((m,down))
                    adj.add((down,m))
                    
                    if m not in most:
                        most[m] = set()
                        most[m].add(down)
                    else:
                        most[m].add(down)
                    
                    if down not in most:
                        most[down] = set()
                        most[down].add(m)
                    else:
                        most[down].add(m)
    answer.append(len(adj)//2)

    maximum = 0
    for _, v in most.items():
        if maximum < len(v):
            maximum = len(v)

    answer.append(maximum)
    return answer

if __name__ == '__main__':
    maps = ["..........","AAACC.....",".AAA.....Z","..AAAA..C.","...BBBBB..","....BBB...","...ZBBB...","ZZZZAAAC..",".....CCCC.","QQ......C.",".........."]
    print(solution(maps))

    #["A.B.C.D", ".B.C.D."]