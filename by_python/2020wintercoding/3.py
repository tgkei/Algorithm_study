import sys

sys.setrecursionlimit(999999)

cache = []
counter = {0: 0, 1: 0, 2: 0}


def dfs(row, col, cur_crop, v):
    if not(row < len(v) and row >= 0 and col < len(v[0]) and col >= 0):
        return False
    if cache[row][col]:
        return False

    if row < len(v) and row >= 0 and col < len(v[0]) and col >= 0:
        if v[row][col] == cur_crop:
            cache[row][col] = True
            dfs(row + 1, col, cur_crop, v)
            dfs(row - 1, col, cur_crop, v)
            dfs(row, col + 1, cur_crop, v)
            dfs(row, col - 1, cur_crop, v)
    return True


def solution(v):
    global cache
    cache = [[False for _ in range(len(v[0]))] for _ in range(len(v))]
    row = 0
    col = 0
    answer = []
    for row in range(len(v)):
        for col in range(len(v[0])):
            cur_crop = v[row][col]
            if dfs(row, col, cur_crop, v):
                counter[cur_crop] += 1

    for v in counter.values():
        answer.append(v)
    return answer


if __name__ == "__main__":
    v = [[0, 0, 1, 1], [1, 1, 1, 1], [2, 2, 2, 1], [0, 0, 0, 2]]
    print(solution(v))
