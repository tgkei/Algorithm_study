def solution(n):
    answer = 0
    dp = [-1 for _ in range(n+1)]
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    for i in range(3,n+1):
        dp[i] = (dp[i-1] + dp[i-2])%1000000007
    return dp[n]

if __name__ =='__main__':
    n = int(input())
    print(solution(n))