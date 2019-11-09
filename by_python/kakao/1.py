def check_stack(stack):
    result = 0
    while len(stack) >= 2 and stack[-1] == stack[-2]:
        stack.pop()
        stack.pop()
        result += 2
    return result

def solution(board, moves):
    answer = 0
    stack = []
    pos = dict()
    for row,r_value in enumerate(board):
        for column,value in enumerate(r_value):
            if column+1 in pos: continue
            if value != 0 :
                pos[column+1] = row

    for move in moves:
        if pos[move] == len(board): continue
        stack.append(board[pos[move]][move-1])
        pos[move] += 1
        answer += check_stack(stack)
    return answer

if __name__ == '__main__':
    board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
    moves = [1,5,3,5,1,2,1,4]
    print(solution(board,moves))