def solution(money, expected, actual):
    answer = -1
    cur_money = 100
    for predict, real in zip(expected, actual):
        if predict == real:
            money += cur_money
            cur_money = 100
        else:
            money -= cur_money
            cur_money = cur_money * 2 if cur_money * 2 <= money else money
    answer = money if money > 0 else 0
    return answer


if __name__ == "__main__":
    money = 1200
    expected = ["T", "T", "H", "H", "H"]
    actual = ["H", "H", "T", "H", "T"]
    print(solution(money, expected, actual))
