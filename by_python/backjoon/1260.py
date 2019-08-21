from collections import deque

def dfs(cur_pos):
    global visited
    print(cur_pos+1, end =" ")
    visited[cur_pos] = 1
    for idx, next_pos in enumerate(linked[cur_pos]):
        if next_pos and not visited[idx]: dfs(idx)


def bfs(cur_pos):
    d= deque()
    print(cur_pos+1,end =" ")
    visited[cur_pos] = 1
    for idx,ne in enumerate(linked[cur_pos]):
        if ne: 
            d.append(idx)
            visited[idx] = 1
    while d:
        next_pos = d.popleft()
        print(next_pos+1, end= " ")
        for idx, ne in enumerate(linked[next_pos]):
            if ne and not visited[idx]:
                d.append(idx)
                visited[idx] = 1


n, m , v = map(int,input().split())

linked = [[0 for _ in range(n)] for _ in range(n)]
visited = [0 for _ in range(n)]
for _ in range(m):
    a, b = map(lambda x: int(x)-1, input().split())

    linked[a][b] = 1
    linked[b][a] = 1
dfs(v-1)
print()
visited = [0 for _ in range(n)]
bfs(v-1)
