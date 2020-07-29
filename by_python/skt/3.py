# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(indices, K):
    # write your code in Python 3.6
    ret = []
    chunk_size = len(indices)//K

    if not len(indices)%K:
        for i in range(K):
            training = []
            test = []
            training += indices[:chunk_size*i]
            training += indices[chunk_size*(i+1):]
            test += indices[chunk_size*i:chunk_size*(i+1)]
            ret.append(training)
            ret.append(test)
    else:
        for i in range(K-1):
            training = []
            test = []
            training += indices[:chunk_size*i]
            training += indices[chunk_size*(i+1):]
            test += indices[chunk_size*i:chunk_size*(i+1)]
            ret.append(training)
            ret.append(test)
        ret.append(indices[:chunk_size*(K-1)])
        ret.append(indices[chunk_size*(K-1):])
    return ret

if __name__=="__main__":
    K = 2
    indices = [1,2,3,4]
    print(solution(indices, K))