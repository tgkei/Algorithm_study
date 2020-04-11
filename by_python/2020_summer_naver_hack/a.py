def solution(n, delivery):
    answer = ''
    remain_array = [-1 for _ in range(n+1)]
    have_set = set()
    delivery=sorted(delivery,key=lambda x: x[2], reverse= True)

    for deli in delivery:
        if not deli[2]:
            if deli[0] in have_set:
                remain_array[deli[1]] = 0
            elif deli[1] in have_set:
                remain_array[deli[0]] = 0
        else:
            remain_array[deli[0]] = 1 
            remain_array[deli[1]] = 1
            if deli[0] not in have_set: have_set.add(deli[0])
            if deli[1] not in have_set: have_set.add(deli[1])

    for each in remain_array[1:]:
        if each == -1:
            answer+="?"
        elif each == 0:
            answer+="X"
        else:
            answer+="O"

    return answer

if __name__ == "__main__":
    n = 7
    delivery = [[5,6,0],[1,3,1],[1,5,0],[7,6,0],[3,7,1],[2,5,0]]	
    print(solution(n, delivery))