from math import inf


def solve(cur, target, used):
    global repeated_arr
    if used > 8:
        return inf
    if cur == target:
        return used

    ret = inf

    for cur_num, repeat in repeated_arr:
        if repeat + used > 8:
            break
        ret = min(ret, solve(cur + cur_num,  target, used+repeat))
        ret = min(ret, solve(cur - cur_num, target, used+repeat))
        ret = min(ret, solve(cur * cur_num, target, used+repeat))
        ret = min(ret, solve(cur//cur_num, target, used+repeat))

    return ret


def make_repeated_nums(arr, num):
    tmp = num
    for i in range(1, 9):
        arr.append([tmp, i])
        tmp = tmp * 10 + num


def solution(N, number):
    global repeated_arr
    answer = 0
    repeated_arr = []

    make_repeated_nums(repeated_arr, N)
    answer = solve(0, number, 0)

    if answer == inf:
        answer = -1
    return answer


if __name__ == "__main__":
    N = 2
    number = 11
    print(solution(N, number))
