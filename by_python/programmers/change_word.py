from math import inf


def diff(word, each_word):
    n = len(word)
    idx = 0
    diff = 0
    while idx < n:
        if word[idx] != each_word[idx]:
            diff += 1
        if diff >= 2:
            break
        idx += 1
    return diff == 1


def dfs(word, target, words, ans, used):
    if word == target:
        return ans
    if not words:
        return inf

    ret = inf

    for each_word in words:
        if diff(word, each_word) and each_word not in used:
            used.add(each_word)
            ret = min(ret, dfs(each_word, target, words, ans+1, used))
            used.remove(each_word)

    return ret


def solution(begin, target, words):
    answer = 0
    used = set()
    answer = dfs(begin, target, words, 0, used)
    if answer == inf:
        answer = 0

    return answer


if __name__ == "__main__":
    begin = "hit"
    target = "cog"
    words = ["hot", "dot", "dog", "lot", "log"]
    print(solution(begin, target, words))
