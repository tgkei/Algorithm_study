#!/usr/local/bin/python3

def solution(n):
    if n%2:
        return 0
    dp =[1]
    n = n//2
    dp = [-1] * n
    dp[0] = 3
    new = 2
    for i in range(1,n):
        dp[i] = dp[i-1] * 3
        dp[i] += new
        new += 2 * dp[i-1]
    answer = dp[-1] % 1000000007
    return answer

if __name__ =="__main__":
    n = int(input())
    print(solution(n))
