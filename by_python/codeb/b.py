import copy

n = int(input())
maps = []


def check_board(board):
    for row in board:
        for each in row:
            if each == 0:
                return False
    return True


for _ in range(n):
    maps.append(list(map(int, input().split())))

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for i in range(n):
    for j in range(n):
        if not maps[i][j]:
            for i_dir, j_dir in directions:
                new_i = i + i_dir
                new_j = j + j_dir
                if (0 <= new_i < n and 0 <= new_j < n):
                    if maps[new_i][new_j] == 0:
                        break
            else:
                maps[i][j] = 1

filled_map = [[0 for _ in range(n)] for _ in range(n)]
filled_map[0][0] = 1

move_map = [[0 for _ in range(n)] for _ in range(n)]
move_map[n-1][n-1] = 1

for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            filled_map[i][j] = -1
            move_map[i][j] = -1

while True:
    if check_board(filled_map):
        break

    for i in range(n):
        for j in range(n):
            cur = filled_map[i][j]
            if cur > 0:
                for i_dir, j_dir in directions:
                    new_i = i+i_dir
                    new_j = j+j_dir
                    if 0 <= new_i < n and 0 <= new_j < n and filled_map[new_i][new_j] != -1 and (filled_map[new_i][new_j] > cur+1 or filled_map[new_i][new_j] == 0):
                        filled_map[new_i][new_j] = cur+1


while True:
    if check_board(move_map):
        break

    for i in reversed(range(n)):
        for j in reversed(range(n)):
            cur = move_map[i][j]
            if cur > 0:
                for i_dir, j_dir in directions:
                    new_i = i+i_dir
                    new_j = j+j_dir
                    if 0 <= new_i < n and 0 <= new_j < n and move_map[new_i][new_j] != -1 and (move_map[new_i][new_j] > cur+1 or move_map[new_i][new_j] == 0):
                        move_map[new_i][new_j] = cur+1

print(filled_map)
print(move_map)
answer = -1
for i in range(n):
    for j in range(n):
        update = True
        for i_dir, j_dir in directions:
            new_i = i+i_dir
            new_j = j+j_dir
            if 0 <= new_i < n and 0 <= new_j < n and move_map[i][j] != -1 and filled_map[new_i][new_j] != -1:
                if filled_map[new_i][new_j] + 1 <= move_map[i][j]:
                    break
        else:
            answer = max(answer, move_map[i][j])

print(answer)
