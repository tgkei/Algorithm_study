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

def solution(budgets, M):
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

        return answer

if __name__ == '__main__':
    budgets = [120, 110, 140, 150]
    M = 485
    print(solution(budgets, M))