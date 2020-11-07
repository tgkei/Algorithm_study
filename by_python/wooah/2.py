def solution(s, op):
    answer = []
    left_idx = 1
    while left_idx < len(s):
        if op == "+":
            answer.append(int(s[:left_idx]) + int(s[left_idx:]))
        elif op == "-":
            answer.append(int(s[:left_idx]) - int(s[left_idx:]))
        elif op == "*":
            answer.append(int(s[:left_idx]) * int(s[left_idx:]))
        left_idx += 1
    return answer


if __name__ == "__main__":

    print(solution(s, op))
