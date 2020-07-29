# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, F, M):
    # write your code in Python 3.6
    total = M * (len(A) + F)
    start = 1
    needed = total - sum(A)
    if start * F > needed: return [0]
    while (((start+1) * F) < needed) and start < 6:
        start+=1
    
    if start == 6:
        if (6 * F) == needed: return [6 for _ in range(F)]
        else: return [0]

    num_of_big = needed - (start * F)
    num_of_small = F - num_of_big
    ret = []
    for _ in range(num_of_small):
        ret.append(start)
    for _ in range(num_of_big):
        ret.append(start+1)
    return ret
    
if __name__ =="__main__":
    A = [6,1]
    F = 1
    M = 1
    print(solution(A,F,M))