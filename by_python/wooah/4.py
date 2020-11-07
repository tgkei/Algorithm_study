def cal_dir(target, cur, n):
    inner_weight = abs(target - cur)
    if cur < target:
        outer_weight = cur + n - target
    else:
        outer_weight = target + n - cur

    if inner_weight < outer_weight:
        return inner_weight
    else:
        return outer_weight


def solution(n, board):
    cache = dict()
    answer = n ** 2
    target = 0

    row = 0
    col = 0
    for r_i, r in enumerate(board):
        for c_i, each in enumerate(r):
            cache[each] = [r_i, c_i]

    while target < n ** 2:
        target += 1

        t_row, t_col = cache[target]

        row_weight = cal_dir(t_row, row, n)
        col_weight = cal_dir(t_col, col, n)

        if t_row != row:
            answer += row_weight

        if t_col != col:
            answer += col_weight

        row, col = t_row, t_col

    return answer


if __name__ == "__main__":
    n = 3
    board = [[3, 5, 6], [9, 2, 7], [4, 1, 8]]
    print(solution(n, board))
