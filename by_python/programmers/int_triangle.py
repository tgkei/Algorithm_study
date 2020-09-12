def dfs(col, row, n):
    global cache
    global global_triangle

    if col >= n or row >= n:
        return 0

    if cache[row][col] != -1:
        return cache[row][col]

    ret = dfs(col, row+1, n)
    ret = max(ret, dfs(col+1, row+1, n))

    cache[row][col] = global_triangle[row][col] + ret

    return cache[row][col]


def solution(triangle):
    global cache
    global global_triangle
    global_triangle = triangle

    n = len(triangle)
    col = 0
    row = 0
    cache = [[-1 for _ in range(n)] for _ in range(n)]

    answer = dfs(col, row, n)
    return answer


if __name__ == "__main__":
    triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
    print(solution(triangle))
