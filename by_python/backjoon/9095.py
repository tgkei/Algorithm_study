cache = [-1]*11

def find(n):
    if cache[n] != -1:
        return cache[n]
    cache[n] = find(n-1)+find(n-2)+find(n-3)
    return cache[n]

cache[0] = 1
cache[1] = 2
cache[2] = 4

for _ in range(int(input())):
    n = int(input())
    print(find(n-1))