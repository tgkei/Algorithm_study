s1 = input()
s2 = input()
l1 = len(s1)
l2 = len(s2)

dp = [[0 for _ in range(l2)] for _ in range(l1)]
is_one= False
for i in range(l1):
    if is_one or s1[i] == s2[0]:
        is_one = True
        dp[i][0] = 1
is_one = False
for i in range(l2):
    if is_one or s1[0] == s2[i]:
        is_one = True
        dp[0][i] = 1

for i in range(1,l1):
    for j in range(1,l2):
        if s1[i] == s2[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])

res = []
x = l1-1
y = l2-1
while dp[x][y] and x>=0 and y >= 0:
    while x>0 and dp[x-1][y] == dp[x][y]:
        x-=1
    while y>0 and dp[x][y-1] == dp[x][y]:
        y-=1
    res.append(s1[x])
    x-=1
    y-=1
print(len(res))
for r in reversed(res):
    print(r,end="")