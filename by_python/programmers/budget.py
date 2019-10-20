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

if __name__ == '__main__':
    budgets = [120, 110, 140, 150]
    M = 485
    print(solution(budgets, M))