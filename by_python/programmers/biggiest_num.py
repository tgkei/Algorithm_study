def solution(numbers):
    answer = ''

    str_arr = list(map(str, numbers))

    str_arr.sort(key=lambda x: x*3, reverse=True)

    for each in str_arr:
        answer += each

    return str(int(answer))


if __name__ == "__main__":
    print(solution([3, 30, 34, 5, 9]))
