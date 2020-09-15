def solution(ball, order):
    answer = []
    memory = set()

    l_idx = 0
    r_idx = len(ball) - 1

    for o in order:
        if o == ball[l_idx]:
            l_idx += 1
            answer.append(o)
            while l_idx <= r_idx and ball[l_idx] in memory:
                answer.append(ball[l_idx])
                l_idx += 1
        elif o == ball[r_idx]:
            r_idx -= 1
            answer.append(o)
            while l_idx <= r_idx and ball[r_idx] in memory:
                answer.append(ball[r_idx])
                r_idx -= 1
        else:
            memory.add(o)
        if l_idx > r_idx:
            break

    return answer


if __name__ == "__main__":
    ball = [1, 2, 3, 4, 5, 6]
    order = [6, 2, 5, 1, 4, 3]
    print(solution(ball, order))
