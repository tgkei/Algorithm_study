def solution(penter, pexit, pescape, data):
    answer = ''
    answer += penter
    n = len(penter)
    for idx in range(0, len(data), n):
        d = data[idx:idx+n]
        print(d)
        if d in [penter, pexit, pescape]:
            answer += pescape
        answer += d

    answer += pexit
    return answer


if __name__ == "__main__":
    penter = "1100"
    pexit = "0010"
    pescape = "1001"
    data = "1101100100101111001111000000"
    print(solution(penter, pexit, pescape, data))
