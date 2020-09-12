def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    n = len(new_id)

    for i in range(n):
        if new_id[i].isalnum():
            answer += new_id[i]
        elif new_id[i] in ['-', '_', '.']:
            answer += new_id[i]

    tmp = ""
    idx = 0

    while idx < len(answer):
        if answer[idx] == '.':
            tmp += answer[idx]
            idx += 1
            while idx < len(answer) and answer[idx] == '.':
                idx += 1
        else:
            tmp += answer[idx]
            idx += 1

    if tmp and tmp[0] == '.':
        if len(tmp) == 1:
            tmp = ""
        else:
            tmp = tmp[1:]
    if tmp and tmp[-1] == '.':
        if len(tmp) == 1:
            tmp = ""
        else:
            tmp = tmp[:-1]

    if not tmp:
        tmp = "a"

    if len(tmp) >= 16:
        tmp = tmp[:15]
    if tmp[-1] == '.':
        tmp = tmp[:-1]

    answer = list(tmp)
    while len(answer) <= 2:
        answer.append(tmp[-1])

    return ''.join(answer)


if __name__ == "__main__":
    new_id = "=.="
    print(solution(new_id))
