def compress(s, txt_len):
    words = []
    for i in range(0, len(s), txt_len):
        words.append(s[i: i+txt_len])

    words += [""]
    ret = ""

    cmp = words[0]

    cnt = 1
    for word in words[1:]:
        if cmp == word:
            cnt += 1
        else:
            ret += str(cnt) if cnt > 1 else ""
            ret += cmp
            cmp = word
            cnt = 1

    return len(ret)


def solution(s):
    answer = len(s)
    for txt_len in range(1, len(s)//2+1):
        answer = min(answer, compress(s, txt_len))
    return answer


if __name__ == "__main__":
    s = "aabbaccc"
    print(solution(s))
