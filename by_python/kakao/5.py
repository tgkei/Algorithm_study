from math import inf
import sys

sys.setrecursionlimit(100000)

def check(mid,k, stones):
    k_comp = 0
    for stone in stones:
        if stone - mid <= 0:
            k_comp += 1
            if k_comp == k: return True
        else: k_comp = 0
    return False

def find_answer(minimum, maximum,k, answer, stones):
    if minimum > maximum: return
    if minimum == maximum:
        if check(minimum,k, stones): answer[0] = min(minimum,answer[0])
        return
    mid = (minimum + maximum) // 2
    if check(mid,k, stones):
        answer[0] = min(mid,answer[0])
        find_answer(minimum, mid, k, answer)
    else:
        find_answer(mid+1,maximum, k, answer)


def solution(stones, k):
    answer = [inf]

    minimum = inf
    maximum = -1

    for stone in stones:
        if minimum > stone: minimum = stone
        if maximum < stone: maximum = stone
    
    find_answer(minimum, maximum, k, answer, stones)

    return answer[0]

if __name__ == "__main__":
    stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
    k = 3
    print(solution(stones,k))