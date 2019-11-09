def solution(budgets, M):
    """
    알고리즘 설명
    1. 일단 budgets를 정렬한다.
    2. budgets에서 작은 값부터 돌면서 값들이 조건에 만족하는지 확인한다. 이때 룰들은 다음과 같다.
        - 이전까지 사용된 budget들은 계속 더해져서 tracking 된다.
        - 이전 총합 + 현재 budget * (n-지금까지 더해진 budget 갯수 == 남은 지방의 수)를 활용한다. 나올 수 있는 경우는 2-1 부터 2-3과 같다.
        2-1: 이전 총합 + 현재 budget *(남은 지방의 수)이 M보다 작은 경우:
            이전 총합에 현재 budget을 더하고 다음으로 넘어간다.
        2-2: 이전 총합 + 현재 budget *(남은 지방의 수)이 M이면:
            현재 budget이 상한선이다
        2-3: 이전 총합 + 현재 budget *(남은 지방의 수)이 M보다 크면:
            이미 상한선을 넘은거다 이럴 때 간단한 수학을 통해서 구하면 된다. 간단한 수학은 다음과 같다
            내림((M - 이전 총합)/(남은 지방의 수))
    2번을 다 했는데도 반환이 안된 경우 즉 모든 지방에 대한 예산을 더해도 M보다 작을 때는 그냥 제일 큰 값 즉 정렬된 곳에서 마지막 값을 반환

    위 알고리즘이 효율적인 이유:
        sum을 사용하면 n이 작용되지만 실질적으로 저기서는 sum을 하는 과정에서 거를 수 있는건 걸렀다. (하지만 sort 자체가 nlogn이기 때문에 time complexity는 nlogn 사실 n 몇번 덜 했다고 시간적으로 큰 차이는 없다!)
        더한 값을 계속 트래킹 하기 위해 아래 코드를 보면 prefix_sum을 사용하는데 이는 부분합이라는 알고리즘에서 굉장히 중요한 기법 중 하나이다. 꼭 관련 문제는 많이 풀어보길!!
    """
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
    return budgets[-1]

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