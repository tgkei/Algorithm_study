def solution(boxes):
    answer = 0

    n = len(boxes)

    present = dict()
    total = 0
    for box1, box2 in boxes:
        if box1 in present:
            if present[box1]:
                total += 1
                present[box1] = 0
            else:
                present[box1] = 1
        else:
            present[box1] = 1

        if box2 in present:
            if present[box2]:
                total += 1
                present[box2] = 0
            else:
                present[box2] = 1
        else:
            present[box2] = 1

    needed = n - total

    for v in present.values():
        if needed > 0 and v:
            needed -= 1
            answer += 1

    return answer


if __name__ == "__main__":
    boxes = [[1, 2], [2, 1], [3, 3], [4, 5], [5, 6], [7, 8]]
    boxes = [[1, 2], [3, 4], [5, 6]]
    boxes = [[1, 2], [2, 3], [3, 1]]
    print(solution(boxes))
