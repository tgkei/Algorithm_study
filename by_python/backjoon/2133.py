n = int(input())

if n%2:
    print(0)
else:
    n = n//2
    dp = [-1] * n
    dp[0] = 3
    new = 2
    for i in range(1,n):
        dp[i] = dp[i-1] * 3
        dp[i] += new
        new += 2 * dp[i-1]
    answer = dp[-1] % 1000000007
    print(answer)