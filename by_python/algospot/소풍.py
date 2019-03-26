is_friend = [[False for _ in range(10)] for _ in range(10)]

def find_friend(friends,student):
    small = -1
    for i in range(student):
        if friends[i]:
            small = i
            break
    else:
        return 1
    res = 0
    small2 = small +1
    while small2 < student:
        if friends[small2] and is_friend[small][small2]:
            friends[small] = False
            friends[small2] = False
            res += find_friend(friends, student)
            friends[small] = friends[small2] = True
        small2 += 1 
    return res

for _ in range(int(input())):
    student, _ = map(int, input().split())
    friends = list(map(int, input().split()))
    index = 0
    while index < len(friends):
        a = friends[index]
        b = friends[index+1]
        index += 2
        is_friend[a][b] = is_friend[b][a] = True
    friends = [True for _ in range(student)]
    res = 0
    a ,b = None, None
    res = 0
    res = find_friend(friends, student)

    print(res)

    is_friend = [[False for _ in range(10)] for _ in range(10)]