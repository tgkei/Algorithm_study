def solution(n, times):
    answer = 0
    times.sort()
    start = 0
    end = n * times[-1]
    while start <= end:
        mid = (end+start)//2
        total = 0
        for time in times:
            total += mid // time
        if total >= n:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1

    return answer

if __name__ =='__main__':
    print(solution(1,[7,10]))