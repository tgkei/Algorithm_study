N = int(input())

targets = []
for _ in range(N):
    targets.append(int(input())-1)

max_target = max(targets)

cache = [[-1 for _ in range(100000)] for _ in range(3)]
cache[0][0] = 0
cache[0][1] = 1
cache[0][2] = 2
cache[1][0] = 1
cache[1][1] = 0
cache[1][2] = 2
cache[2][0] = 1
cache[2][1] = 1
cache[2][2] = 2

yirun = [1,1,3]

ii = 2
while ii < max_target:
        ii += 1
        cache[0][ii] = (cache[1][ii-2] + cache[2][ii-3]) % 1000000009
        cache[1][ii] = (cache[0][ii-1] + cache[2][ii-3]) % 1000000009
        cache[2][ii] = (cache[0][ii-1] + cache[1][ii-2]) % 1000000009

for target in targets:
    if target<=2:
        ret = yirun[target]
        print(ret)
        continue
    ret = 0    
    ret += cache[0][target-1] + cache[1][target-2] + cache[2][target-3]

    print(ret%1000000009)