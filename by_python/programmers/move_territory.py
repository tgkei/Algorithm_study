from collections import deque

MOVES = [[1, 0], [0, 1], [-1, 0], [0, -1]]
MOVES2 = [[1, 0], [0, 1]]


def find_group(x, y, group, height, land):
    global cache
    q = deque()
    q.append([x, y])
    cache[x][y] = group
    while q:
        x, y = q.popleft()
        for dx, dy in MOVES:
            nx, ny = dx+x, dy+y
            if 0 <= nx < len(land) and 0 <= ny < len(land) and abs(land[x][y] - land[nx][ny]) <= height and cache[nx][ny] == -1:
                cache[nx][ny] = group
                q.append([nx, ny])


def check_parent(ptr):
    global disjoint

    if ptr == disjoint[ptr]:
        return ptr
    else:
        p = check_parent(disjoint[ptr])
        disjoint[ptr] = p
        return p


def is_cycle(group1, group2):
    global disjoint
    parent1 = check_parent(group1)
    parent2 = check_parent(group2)

    if parent1 == parent2:
        return True

    disjoint[parent1] = parent2
    return False


def solution(land, height):
    global disjoint
    global cache
    answer = 0
    N = len(land)
    costs = set()
    cost2loc = dict()
    cache = [[-1 for _ in range(N)] for _ in range(N)]
    group = 0

    for x in range(N):
        for y in range(N):
            if cache[x][y] == -1:
                find_group(x, y, group, height, land)
                group += 1

    for x in range(N):
        for y in range(N):
            for x_mv, y_mv in MOVES2:
                x_nxt = x + x_mv
                y_nxt = y + y_mv

                if x_nxt >= N or y_nxt >= N:
                    continue

                if cache[x][y] == cache[x_nxt][y_nxt]:
                    continue

                diff = abs(land[x][y] - land[x_nxt][y_nxt])
                cost = diff

                if cost != 0:
                    costs.add(cost)

                if cost not in cost2loc:
                    cost2loc[cost] = [[cache[x][y], cache[x_nxt][y_nxt]]]
                else:
                    cost2loc[cost].append([cache[x][y], cache[x_nxt][y_nxt]])

    costs = sorted(costs)

    disjoint = []
    for i in range(group):
        disjoint.append(i)

    for cost in costs:
        while cost2loc[cost]:
            group1, group2 = cost2loc[cost].pop()
            if not is_cycle(group1, group2):
                answer += cost

    return answer


if __name__ == "__main__":
    land = [[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]]
    height = 1
    print(solution(land, height))
