def solution(skill, skill_trees):
    answer = 0

    for tree in skill_trees:
        tmp = list(reversed(list(skill)))
        for each in tree:
            if tmp and each in tmp:
                if tmp.pop() != each:
                    break
        else:
            answer += 1

    return answer
