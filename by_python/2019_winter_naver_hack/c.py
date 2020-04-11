def solution(command, buttons, scores):
    com_len = len(command)
    answer = com_len
    for idx in range(com_len):
        for score_idx, button in enumerate(buttons):
            but_len = len(button)
            if but_len-1 + idx < com_len and command[idx:idx+but_len] == button:
                answer = max(answer,idx + scores[score_idx] + solution(command[idx+but_len:],buttons,scores))                
    return answer

if __name__=='__main__':
    command = "ABCXYZ"
    buttons = ["CXYZ","AB"]
    scores = [2,3]
    print(solution(command, buttons, scores))