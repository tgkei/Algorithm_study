import heapq

def solution(jobs):
    n = len(jobs)

    jobs.sort()
    answer = 0

    possible_process = []
    temp = heapq.heappop(jobs)
    possible_process.append([temp[1],temp[0]])
    prev = 0
    now = 0

    while possible_process:
        cur = heapq.heappop(possible_process)
        if prev < cur[1]:
            prev = cur[1]
        now = cur[0] + prev
        while jobs and jobs[0][0] <= now:
            temp = heapq.heappop(jobs)
            heapq.heappush(possible_process, [temp[1],temp[0]])
        if jobs and not possible_process:
            temp = heapq.heappop(jobs)
            heapq.heappush(possible_process, [temp[1],temp[0]])
        answer += cur[0]
        if prev >= cur[1]:
            answer += prev - cur[1]
        prev = now 
    answer //= n
    return answer