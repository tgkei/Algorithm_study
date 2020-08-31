def solution(n, times):
    answer = 0
    times.sort()
    start = times[-1] * n
    end = times[0] * n

    while start < end:
        mid = start + end // 2
        total = 0
        for time in times:
            total += mid // time
        if total >= n:
            answer = mid
            end = mid
        else:
            start = mid

    return answer


if __name__ == "__main__":
    n = 6
    times = [7, 10]
    print(solution(n, times))
