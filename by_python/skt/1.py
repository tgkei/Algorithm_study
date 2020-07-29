# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, q):
    # sensitivity = Recall
    tmp = 0
    if q: # specificity
        for idx,a in enumerate(A):
            if not a and not B[idx]: tmp +=1
        specificity = tmp/(len(A) - sum(A))
        return specificity
    for idx, b in enumerate(B):
        if b and A[idx]: tmp +=1
    sensitivity = tmp/(sum(A))
    return sensitivity

if __name__=="__main__":
    A = [1, 0, 1, 1, 0, 1]
    B = [0, 1, 1, 0, 0, 1]
    q = False
    print(solution(A,B,q))