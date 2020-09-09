from collections import deque


def solution(n, computers):
    answer = 0
    # bfs
    q = deque()
    visited = [False for _ in range(n)]
    for i in range(n):
        if visited[i]:
            continue
        answer += 1
        visited[i] = True
        q.append(i)
        while q:
            cur = q.popleft()
            visited[cur] = True
            for idx, connected in enumerate(computers[cur]):
                if connected and not visited[idx]:
                    q.append(idx)

    return answer


if __name__ == "__main__":
    n = 3
    computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    print(solution(n, computers))
