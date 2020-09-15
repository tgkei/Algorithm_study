L, U, R, D = 0, 1, 2, 3
dir2left = {R: (-1, 0),
            U: (0, -1),
            L: (1, 0),
            D: (0, 1)}

next_move = {L: (0, -1),
             U: (-1, 0),
             R: (0, 1),
             D: (1, 0)}

to_left = {R: U,
           U: L,
           L: D,
           D: R}

to_right = {R: D,
            D: L,
            L: U,
            U: R}


def is_out(x, y, n):
    if x < 0 or x >= n or y < 0 or y >= n:
        return True
    return False


def solution(maze):
    answer = 0
    x, y = 0, 0
    N = len(maze)
    #ans_set = set()

    # ans_set.add((0, 0))

    if maze[0][1]:
        direction = D
    else:
        direction = R

    while x != N-1 or y != N-1:
        dx, dy = next_move[direction]
        nx, ny = x+dx, y+dy

        if is_out(nx, ny, len(maze)) or maze[nx][ny]:
            # if current direction is blocked
            direction = to_right[direction]
        else:
            answer += 1
            x, y = nx, ny
            # print(x, y)
            # ans_set.add((x, y))
            xl, yl = dir2left[direction]
            bx, by = x + xl, yl + y
            if is_out(bx, by, len(maze)) or not maze[bx][by]:
                direction = to_left[direction]

    return answer


if __name__ == "__main__":
    maze = [[0, 1, 0, 0, 0, 0], [0, 1, 0, 1, 1, 0], [0, 1, 0, 0, 1, 0],
            [0, 1, 1, 1, 1, 0], [0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0]]
    print(solution(maze))
