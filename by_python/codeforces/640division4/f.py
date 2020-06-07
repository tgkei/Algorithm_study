T = int(input())

for _ in range(T):
    n0, n1, n2 = map(int, input().split())
    answer = ""
    if n1 == 0:
        if n0:
            answer = "0" * (n0 + 1)
        else:
            answer = "1" * (n2 + 1)
    else:
        answer = "10" * (n1 // 2 + n1 % 2)
        if n1 % 2 == 0:
            answer += "1"
        answer = answer[0] + ("0" * n0) + answer[1:]
        answer = ("1" * (n2)) + answer

    print(answer)
