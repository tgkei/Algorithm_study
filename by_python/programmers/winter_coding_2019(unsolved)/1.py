from math import floor, ceil

def solution(w,h):
    answer = h*w
    div = 0
    gradient = h/w
    
    if h > w:
        while not h%2:
            div += 1
            h/=2
            w/=2
    else:
        while not w%2:
            div += 1
            h/=2
            w/=2
    not_ans = 0
    for x in range(int(w)):
        start = x * gradient
        end = (x+1)*gradient
        not_ans += (ceil(end) - floor(start))
    div = 1 if div is 0 else div
    not_ans **= div
    answer -= not_ans
    return answer

if __name__ == '__main__':
    w = 8
    h = 12
    print(solution(w,h))