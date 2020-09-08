from math import ceil


def solution(w, h):
    height = max(w, h)
    width = min(w, h)
    return width * (height - ceil(height/width))


if __name__ == "__main__":
    print(solution(8, 12))
