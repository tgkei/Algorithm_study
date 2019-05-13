n = int(input())
l = []
r = []
for _ in range(n):
    a, b = map(int, input().split())
    l.append(a)
    r.append(b)

k = int(input())
chapter = 0
        
for i in range(len(l)):
    if l[i] <= k and r[i] >= k:
        chapter = i
        
print(n-chapter)