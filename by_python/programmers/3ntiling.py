def solution(n):
    if n%2:
        return 0
    dp = [0,3,0,11]
    while len(dp) <= n:
        val = dp[-2] * 3
        val += dp[-4] * 2
        dp.append(val)
    answer = dp[n-1] % 1000000007
    return answer

if __name__=="__main__":
    n = int(input())
    print(solution(n))

"""N=int(input())
if N%2==1:print(0)
else:
        dp = [0]*16
        dp[0] = 1
        N //= 2
        for i in range(1,N+1):
                dp[i] += dp[i-1] * 3
                for j in range(2, i+1):
                        dp[i] += dp[i-j] * 2
        print(dp[N])"""