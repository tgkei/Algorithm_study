def change(num, k):
    answer = ""
    while num:
        num, left = num//k, num % k
        answer += str(left)

    return answer


def calc(num, k):
    ret = 1
    for each in num:
        if int(each) == 0:
            continue
        ret *= int(each)
    return ret


def solution(N):
    answer = []

    maximum = -1
    answer = -1
    for k in range(2, 10):
        num = change(N, k)
        tmp = calc(num, k)
        if tmp >= maximum:
            answer = k
            maximum = tmp

    ret = [answer, maximum]
    return ret


if __name__ == "__main__":
    N = 10
    print(solution(N))
