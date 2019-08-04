n = int(input())

a = [*map(int,input().split())]
b = [*map(int,input().split())]

cache1 = [a[0]]
cache2 = [b[0]]

for i in range(n-1):
    cache1.append(max(cache1[i],cache2[i]+a[i+1]))
    cache2.append(max(cache2[i], cache1[i]+b[i+1]))

print(max(cache1[-1],cache2[-1]))