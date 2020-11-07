def solution(grades, weights, threshold):
    answer = 0
    table = {
        "A+": 10,
        "A0": 9,
        "B+": 8,
        "B0": 7,
        "C+": 6,
        "C0": 5,
        "D+": 4,
        "D0": 3,
        "F": 0,
    }

    for i, grade in enumerate(grades):
        answer += table[grade] * weights[idx]

    return answer - threshold


if __name__ == "__main__":
    solution(grades, weights, threshold)
