def solution(number, k):
    answer = ''
    stack = []

    for num in number:
        while k and stack and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)

    answer = "".join(stack[:-k]) if k else "".join(stack)

    return answer


if __name__ == "__main__":
    number = "1231234"
    k = 3
    print(solution(number, k))
