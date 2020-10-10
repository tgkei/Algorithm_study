def solution(number, k):
    n = len(number) - k
    stack = []

    print(n)
    for num in number:
        if stack:
            num = int(num)
            while k > 0 and stack and num > stack[-1]:
                stack.pop()
                k -= 1
            stack.append(num)
        else:
            stack.append(int(num))

    return ''.join(map(str, stack[:n]))


if __name__ == "__main__":
    number = "4177252841"
    k = 4
    print(solution(number, k))
