"""
find biggest square
https://programmers.co.kr/learn/courses/30/lessons/12905?language=python3
"""


def solution(board):
    """
    answer = 0
    col = 0
    row = 0
    size = len(board)
    col_size = len(board[0])

    while row < size:
        if not col or not row:
            answer = max(answer,board[row][col]**2)
        else:
            if board[row][col]:
                tmp = min(board[row-1][col-1], board[row-1]
                          [col], board[row][col-1])+1
                board[row][col] = tmp
                answer = max(answer, (tmp)**2)

        col += 1
        row += col//col_size
        col %= col_size
    """
    answer = 1
    for row_idx, row in enumerate(board):
        for col_idx, col in enumerate(row):
            if not row or not col:
                continue
            if col:
                col = min(board[row_idx-1][col_idx], board[row_idx-1]
                          [col_idx-1], board[row_idx][col_idx-1]) + 1
                board[row_idx][col_idx] = col
                answer = max(answer, col ** 2)

    return answer


if __name__ == "__main__":
    print(solution([[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]))
    print(solution([[0, 0, 1, 1], [1, 1, 1, 1]]))
