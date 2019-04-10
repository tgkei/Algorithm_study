input()
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a.sort(reverse= True)
b.sort()
maximum = 0
for A, B in zip(a,b):
    maximum += A*B
print(maximum)