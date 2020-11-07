def solution(n, horizontal):
    answer = [[-1 for _ in range(n)] for _ in range(n)]

    row = 0
    col = 0
    cur_time = 0
    turn = 0
    answer[row][col] = cur_time
    while True:
        if row == n - 1 and col == n - 1:
            break
        if turn % 2 == 0:
            if horizontal:
                if col + 1 < n:
                    col += 1
                else:
                    row += 1
            else:
                if row + 1 < n:
                    row += 1
                else:
                    col += 1
            horizontal = not horizontal
            cur_time += 1
            answer[row][col] = cur_time
        else:
            tmp_row = row
            tmp_col = col
            while tmp_row != col and tmp_col != row:
                cur_time += 2
                if horizontal:
                    tmp_row -= 1
                    tmp_col += 1
                else:
                    tmp_row += 1
                    tmp_col -= 1
                answer[tmp_row][tmp_col] = cur_time
            row, col = col, row
        turn += 1

    return answer


if __name__ == "__main__":
    n = 4
    horizontal = True
    print(solution(n, horizontal))
