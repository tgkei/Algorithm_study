def solution(phrases, second):
    n = len(phrases)
    target = second%(2*n)
    answer = ""
    if target <= n:
        answer+= "_"*(n-target)
        answer+= phrases[:target]
    else:
        answer+=phrases[target-n:]
        answer+="_"*(n-(2*n-target))
    return answer

print(solution("happy-birthday",29))