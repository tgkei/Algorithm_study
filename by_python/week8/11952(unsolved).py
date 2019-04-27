"""
좀비
"""

N, M, K, S = map(int,input().split())

p, q = map(int, input().split())

linked = [[] for _ in range(N)]

result = [-1 for _ in range(N)]

infected = []

for _ in K:
    infected.append(int(input()))

for _ in M:
    t1, t2 = map(int,input().split())
    linked[t1-1].append(t2-1)
    linked[t2-1].append(t1-1)

cur_pos = 0

while True:
    if result[N-1] != -1:
        break
    for next_pos in linked[cur_pos]:
        extra = p if ?? else q
        if result[0][next_pos] != -1:
            continue
        else:
            result[0][next_pos]=result[0][cur_pos] + extra
        