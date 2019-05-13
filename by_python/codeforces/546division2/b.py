n, k = map(int,input().split())

short = min(n-k,k-1)
not_short = max(n-k,k-1)
path = short * 2 + not_short
result = 2 * n + 1 + path

print(result)