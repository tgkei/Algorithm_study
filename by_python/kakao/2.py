def solution(s):
    highest = 0
    dic = dict()
    answer = []
    idx = 1
    while idx < len(s)-1:
        if s[idx] == '{':
            idx +=1
            temp = []
            while s[idx] != '}':
                if s[idx] != ',':
                    num = ""
                    while s[idx] != "," and s[idx] != '}':
                        num += s[idx]
                        idx+=1
                    else:
                        temp.append(int(num))
                    if s[idx] == '}': 
                        idx += 1
                        break
                idx+=1
            if len(temp) > highest: highest = len(temp)
            dic[len(temp)] = temp
        else:
            idx +=1
    for i in range(1,highest+1):
        for x in dic[i]:
            if x not in answer: answer.append(x)
    return answer

if __name__ == '__main__':
    s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"	
    print(solution(s))