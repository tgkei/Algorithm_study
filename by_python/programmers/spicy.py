import heapq

def solution(scoville, K):
    answer = 0
    scoville.sort()
    minimum = heapq.heappop(scoville)

    while scoville and minimum < K:
        new_val=minimum + heapq.heappop(scoville)*2
        heapq.heappush(scoville,new_val)
        answer +=1
        minimum = heapq.heappop(scoville)

    answer = answer if mimimum < K else -1
    return -1

if __name__ =='__main__':
    scoville = [1, 2, 3, 9, 10, 12]	
    k = 10000000
    print(solution(scoville,k))