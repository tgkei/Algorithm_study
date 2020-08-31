T = int(input())

for t in range(T):
    N, A, B, C = map(int, input().split())

    print("Case #{}: ".format(t+1), end=" ")
    if A+B-C > N:
        print("IMPOSSIBLE")
    elif N == 1:
        print("1")
    elif N >= 2 and A+B-C == 1:
        print("IMPOSSIBLE")
    elif N == 2:
        if C == 2:
            print("1 1")
        elif A == 2:
            print("1 2")
        else:
            print("2 1")
    else:
        num_left = A-C
        num_right = B-C
        hidden = N - (A+B-C)
        answer = []

        for _ in range(num_left):
            answer.append(2)
        for _ in range(C):
            answer.append(3)
        for _ in range(num_right):
            answer.append(str(2))

        for _ in range(hidden):
            answer.insert(1, 1)

        for num in answer:
            print(num, end=" ")
        print()
