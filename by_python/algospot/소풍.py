"""def solve():
    global taken

     # 아직 뽑히지 않은 학생 중 인덱스가 가장 작은 학생을 뽑음
    first = -1
    for idx,i in enumerate(taken):
        if not i:
            first = idx
            break
    if first == -1:
        return 1
    
    # 미리 선택한 first와 짝을 이룰 수 있고 아직 뽑히지 않은 학생을 찾고 solve 재귀 호출 후 총 몇개가 가능한지 반환
    ret = 0
    i = first+1
    while i < n:
        if not taken[i] and friends[first][i]:
            taken[first] = taken[i] = True
            ret += solve()
            taken[first] = taken[i] = False
        i+=1
    return ret

for _ in range(int(input())):
    n, _ = map(int,input().split())
    taken = [False for _ in range(n)] # 뽑힌 학생의 정보를 저장하기 위한 배열
    friends = [[False for _ in range(n)] for _ in range(n)] # 짝이 되는 학생들의 정보를 저장하기 위해

    nums = list(map(int,input().split())) # 주어진 학생 짝들을 저장

    for i, j in zip(nums[::2],nums[1::2]):
        friends[i][j]=friends[j][i]= True

    print(solve())"""

def pick():
    global taken

    first = -1
    for idx, take in enumerate(taken):
        if take:
            continue
        first = idx
        break
    if first == -1:
        return 1
    
    ret = 0
    for i in range(n):
        if i != first and is_friend[i][first] and (not taken[i]):
            taken[first] = taken[i] = True
            ret += pick()
            taken[first] = taken[i] = False
    return ret

for _ in range(int(input())):
    n, m = map(int,input().split())
    taken = [False for _ in range(n)]
    is_friend = [[False for _ in range(n)] for _ in range(n)]
    friend = list(map(int,input().split()))

    for i1,i2 in zip(friend[::2],friend[1::2]):
        is_friend[i1][i2] = is_friend[i2][i1] = True
    print(pick())