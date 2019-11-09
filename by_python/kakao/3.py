def pick(user, left, banned_id, temp):
    if left == len(banned_id): 
        temp.sort()
        temp = tuple(temp)
        if temp in cache: return 0
        cache[temp] = 1
        return 1
    answer = 0
    cur_ban = banned_id[left]
    users = list(user.keys())

    for user_name in users:
        if len(user_name) == len(cur_ban):
            for i in range(len(user_name)):
                if user_name[i] != cur_ban[i] and cur_ban[i] != "*": break
            else:
                temp.append(user_name)
                user.pop(user_name)
                answer += pick(user, left + 1, banned_id,temp)
                temp.remove(user_name)
                user[user_name] = 1
    return answer

def solution(user_id, banned_id):
    global user_cache
    global cache

    cache = dict()
    answer = 0
    user_cache = dict()
    for user in user_id:
        user_cache[user] = 1
    answer = pick(user_cache, 0, banned_id,[])
    return answer

if __name__ == "__main__":
    user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
    banned_id = ["fr*d*", "*rodo", "******", "******"]	
    print(solution(user_id,banned_id))