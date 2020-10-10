def solution(people, limit):
    answer = 0
    people.sort()
    L = 0
    R = len(people) - 1

    while L <= R:
        while L != R and people[L] + people[R] > limit:
            answer += 1
            R -= 1
        answer += 1
        L += 1
        R -= 1

    return answer


if __name__ == "__main__":
    people = [1, 2, 3]
    limit = 100
    print(solution(people, limit))
