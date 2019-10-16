from math import inf

def solution(grade):
    answer = 0
    smallest = grade[-1]
    for g in grade[-2::-1]:
        if smallest < g:
            answer += g-smallest
        else:
            smallest = g
    return answer

if __name__ == '__main__':
    grade = [2,1,3]
    print(solution(grade))