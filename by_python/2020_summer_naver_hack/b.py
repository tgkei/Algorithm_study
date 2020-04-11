def solution(id_list, k):
    answer = 0
    board = dict()

    for each_id in id_list:
        tmp = list(each_id.split())
        today = set()
        for each in tmp:
            if each not in board: 
                board[each] = 1
                today.add(each)
                answer+=1
            elif board[each] < k and each not in today:
                board[each] +=1
                today.add(each)
                answer+=1

    return answer

if __name__=="__main__":
    k = 3
    id_list = ["JAY", "JAY ELLE JAY MAY", "MAY ELLE MAY", "ELLE MAY", "ELLE ELLE ELLE", "MAY"]	
    print(solution(id_list, k))