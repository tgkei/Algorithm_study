n, m = map(int,input().split())

first =[list(map(int,input().split())) for _ in range(n)]
second = [list(map(int,input().split())) for _ in range(n)]

row = 0
column = 0
done = False

for i in range(n):
    for j in range(m):
        first[i][j],second[i][j] = min(first[i][j],second[i][j]), max(first[i][j],second[i][j])

for i in range(n-1):
    for j in range(m):
        if first[i][j] >= first[i+1][j] or second[i][j] >= second[i+1][j]:
            done= True
    if done:
        break

for i in range(n):
    for j in range(m-1):
        if first[i][j] >= first[i][j+1] or second[i][j] >= second[i][j+1]:
            done = True
    if done:
        break
if done:
    print("Impossible")
else:
    print("Possible")