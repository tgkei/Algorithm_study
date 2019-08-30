def solution(sticker):    
    answer = 1
    n = len(sticker)
    dp = [[0 for _ in range(n)] for _ in range(4)]
    if n == 1: return sticker[0]
    elif n ==2: return max(sticker[0],sticker[1])
    
    dp[0][0] = sticker[0]
    dp[0][1] = dp[0][0]
    for i in range(2,n-1):
        dp[0][i] = max(dp[0][i-2]+sticker[i],dp[0][i-1])
    dp[1][0] = 0
    dp[1][1] = sticker[1]
    for i in range(2,n):
        dp[1][i] = max(dp[1][i-2]+sticker[i],dp[1][i-1])
    answer = max(dp[0][-2], dp[1][-1])
    return answer