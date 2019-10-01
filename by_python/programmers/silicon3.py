def solution(estimates, k):
    prefix = []
    prefix.append(estimates[0])
    pref_sum = prefix[0]
    for i in range(1,len(estimates)):
        pref_sum += estimates[i]
        prefix.append(pref_sum)
    answer = prefix[k-1]
    for i in range(1, len(estimates)-(k-1)):
        answer = max(answer,prefix[i+k-1]-prefix[i-1])
    return answer

print(solution([1, 1, 9, 3, 7, 6, 5, 10],4))