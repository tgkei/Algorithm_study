def solution(k, score):
    answer = -1
    cache = dict()
    for prev_score, cur_score in zip(score[0:], score[1:]):
        diff = prev_score - cur_score
        if diff not in cache:
            tmp = set()
            cache[diff] = [1, tmp]
        else:
            cache[diff][0] += 1
        cache[diff][1].add(prev_score)
        cache[diff][1].add(cur_score)
    answer_set = set()
    for _, arr in cache.items():
        diff, ranks = arr[0], arr[1]
        if diff >= k:
            answer_set = answer_set.union(ranks)

    answer = len(score) - len(answer_set)

    return answer


if __name__ == "__main__":
    k = 1
    score = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(solution(k, score))
