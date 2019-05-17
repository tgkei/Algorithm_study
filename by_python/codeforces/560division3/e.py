n = int(input())

a = list(map(int,input().split()))
b = list(map(int,input().split()))


start = 1
end = n

for i in range(n):
    a[i] *= (start*end)
    start+=1
    end-=1

a.sort()
b.sort(reverse=True)

res = 0

for aa, bb in zip(a,b):
    res += (aa*bb)

print(res%998244353)