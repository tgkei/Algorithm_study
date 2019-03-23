cache = [[-1 for _ in range(30)]for _ in range(30)]

def find(n, m):
    if cache[n][m] != -1:
        return cache[n][m]
    cache[n][m] = find(n-1,m-1)+find(n,m-1)
    return cache[n][m]

for i in range(30):
    cache[0][i] =(i+1)
    cache[i][i] = 1


for _ in range(int(input())):
    n, m = map(int, input().split())
    n, m = n-1, m-1
    result = 0 
    
    result = find(n, m)

    print(result)