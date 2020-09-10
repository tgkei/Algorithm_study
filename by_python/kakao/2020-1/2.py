def rec(w):
    if w == "":
        return ""

    open_cnt = 0
    close_cnt = 0
    for idx, each in enumerate(w):
        if each == '(':
            open_cnt += 1
        else:
            close_cnt += 1
        if open_cnt and open_cnt == close_cnt:
            u = w[:idx+1]
            v = w[idx+1:]
            break
    correct = False
    check_u = []

    for each in u:
        if not check_u and each == ')':
            break
        if each == '(':
            check_u.append(each)
        else:
            check_u.pop()
    else:
        correct = True

    ret = ""
    if correct:
        ret = u + rec(v)
    else:
        ret = '(' + rec(v) + ')'
        for each in u[1:-1]:
            if each == '(':
                ret += ')'
            else:
                ret += '('

    return ret


def solution(p):
    answer = rec(p)
    return answer


if __name__ == "__main__":
    print(solution("(()())()"))
