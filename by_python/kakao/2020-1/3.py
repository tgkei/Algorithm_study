import numpy as np


def check(M, N, board):
    for i in range(M-1, M-1+N):
        for j in range(M-1, M-1+N):
            if board[i][j] != 1:
                return False
    return True


def key_open(key, x, y, M, board):
    for i in range(M):
        for j in range(M):
            board[x+i][y+j] += key[i][j]


def key_close(key, x, y, M, board):
    for i in range(M):
        for j in range(M):
            board[x+i][y+j] -= key[i][j]


def solution(key, lock):
    keys = []

    N = len(lock)
    M = len(key)

    for _ in range(4):
        keys.append(key)
        key = np.rot90(key).tolist()

    board = [[0 for _ in range(N+(M-1)*2)] for _ in range(N+(M-1)*2)]

    for idx1, i in enumerate(range(M-1, M-1+N)):
        for idx2, j in enumerate(range(M-1, M-1+N)):
            board[i][j] = lock[idx1][idx2]

    for rotated_key in keys:
        for i in range(M-1+N):
            for j in range(M-1+N):
                key_open(rotated_key, i, j, M, board)

                if check(M, N, board):
                    return True

                key_close(rotated_key, i, j, M, board)

    return False


if __name__ == "__main__":
    key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
    lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    print(solution(key, lock))
