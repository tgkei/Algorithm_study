def solution(n, delivery):
    answer = ''
    cache = [-1 for _ in range(n)]
    for _ in range(2):
        for each in delivery:
            a1, a2, result = each
            a1 -= 1
            a2 -= 1

            if result:
                cache[a1] = 1
                cache[a2] = 1
            else:
                if cache[a1] == 1:
                    cache[a2] = 0
                elif cache[a2] == 1:
                    cache[a1] = 0

    for each in cache:
        if each == -1:
            answer += "?"
        elif each == 1:
            answer += "O"
        else:
            answer += "X"
    return answer


if __name__ == "__main__":
    n = 7
    delivery = [[5, 6, 0], [1, 3, 1], [1, 5, 0],
                [7, 6, 0], [3, 7, 1], [2, 5, 0]]
    print(solution(n, delivery))
