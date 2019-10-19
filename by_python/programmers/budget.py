"""def solution(budgets, M):
    n = len(budgets)
    budgets.sort()
    
    prefix_sum = 0
    
    for idx, budget in enumerate(budgets):
        if prefix_sum + budget * (n-idx) < M:
            prefix_sum += budget
            continue
        elif prefix_sum + budget*(n-idx) == M:
            return budget
        else:
            return (M - prefix_sum)//(n-idx)
    return budgets[-1]"""

"""def solution(budgets, M):
    n = len(budgets)
    budgets.sort()
    total = sum(budgets)
    standard_avg = total//n
    second_avg = 0
    modified_total = M+1
    less_avg = []
    above_avg = []

    if(total < M):
        return max(budgets)
    else:
        for i in range(n):
            if(budgets[i] < standard_avg):
                less_avg.append(budgets[i])
            else:
                above_avg.append(budgets[i])
        second_avg = total - sum(less_avg)
        second_standard = second_avg // len(above_avg)
        for j in range(len(above_avg)):
            above_avg[j] = second_standard

        while M < modified_total:
            w = len(above_avg)
            for l in range (w):
                above_avg[l] -= 1
            modified_total = sum(above_avg) + sum(less_avg)
        answer = sum(above_avg) // len(above_avg)

        return answer"""
def solution(budgets, M):
    # 0부터 M 사이에서 상한선을 찾는 건데 이진 탐색이 총 log M의 시간이 걸리고 한번 할때 마다 값을 계산하기 위해 budgets를 탐색해야 해서 (len(budgets) * log M)
    start = 0
    last = max(budgets)
    limit = last // 2 # 이렇게 되면 0 부터 max budgets 중에 상한선을 찾으면 되는데 그걸 이진 탐색으로
    answer = -1
    while start <= last:
        limit = start + (last - start)//2
        total = 0
        for budget in budgets:
            if budget < limit: total += budget
            else : total += limit
        if total > M: 
            last = limit - 1
        else: 
            answer = limit
            start = limit + 1
    return answer

if __name__ == '__main__':
    budgets = [10, 10, 10, 10]
    M = 40
    print(solution(budgets, M))