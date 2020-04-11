def recursive(remain_n, remain_m, k, ski, board, is_ski):
    if remain_n <= 0 or remain_m <= 0:
        # 실패한 경우 baseline
        return 0

    if remain_n ==1:
        if remain_m > k :
            return 0
        # 성공하는 경우 base line
        if is_ski:
            ski += remain_m 
        else:
            board += remain_m
        
        if ski == board:
            return 1
        else:
            return 0
    
    if dp[remain_n][remain_m] != -1:
        # 이미 한번 방문한 경우
        return dp[remain_n][remain_m]
    
    #방문 안 한 경우
    #1칸 부터 k칸까지 가져보면서 dp
    ret = 0

    for i in range(1,k+1):
        if is_ski:
            ret += recursive(remain_n-1, remain_m-i, k, ski + i, board, not is_ski)
        else:
            ret += recursive(remain_n-1, remain_m-i, k, ski, board + i, not is_ski)

    dp[remain_n][remain_m] = ret
    return ret


def solution(n, m, k):
    global dp
    dp = [[-1 for _ in range(m + 1)] for _ in range(n+1)]
    answer = 2 * recursive(n,m,k,0,0,True)
    return answer % 1000000007

if __name__=="__main__":
    n = 50
    m = 150
    k = 20
    print(solution(n, m, k))