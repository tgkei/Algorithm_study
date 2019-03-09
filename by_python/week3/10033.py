#from collections import OrderedDict

N = int(input())

index = []

cow = {}
cnt = 0
for _ in range(N):
    cow_pos, cow_color = input().split()
    cow_pos = int(cow_pos)
    if cow_color == 'W':
        cnt +=1
        cow[cow_pos] = 1
    else:
        cnt -=1
        cow[cow_pos] = -1
    index.append(cow_pos)

#cow = OrderedDict(sorted(cow.items())) ## 정렬 된 소의 정보 (위치가 KEY이기 색에 VALUE)
index.sort()  ## 소의 위치를 index로 지정하기 위해서

maximum = 0
temp = 0

for i in range(len(index)):
    # j의 값 중 가장 큰 값을 구함 여기서부터 i+1 즉 i까지 내려가면 [j, i)로 가능 -2 씩 하강
    
    if i != 0: # 0번째를 제외하고 1번째부터 시작한다고하면 1번째 부터 시작이면 그 전 값을 빼줘야함
        cnt -= cow[index[i-1]]
    
    temp = cnt
    ## j 값 구하는 곳   
    if i %2 ==0: # i 가 짝수이면 j는 N-1 이하 중 가장 큰 홀수
        if N % 2 ==0:
            j = N-1
        else:
            j = N-2
    else: # i 가 홀수이면 j는 N-1 이하 중 가장 큰 짝수
        if N % 2 ==0: #N이 짝수
            j = N-2
        else:
            j = N-1

    if maximum > (index[j]-index[i]):  ## max의 길이보다 배열이 짧을 경우 그냥 끝냄
        break

    for ind in range(j,i,-2):
        if maximum > (index[ind] - index[i]):
            break
        
        if ind+1 < N: ## ind+1이 N이 아니면 ind보다 한칸 오른쪽에 해당하는 값 하나를 빼줘 ind+1이 N이면 즉 ind가 배열의 제일 오른쪽이면 그냥 temp 사용. ind가 배열 제일 오른쪽이 아니면 바로 오른쪽에 하나 값을 뺀다
            temp -= cow[index[ind+1]]

        if temp >= 0 and temp %2 ==0:
            maximum = max(index[ind]-index[i],maximum)
            break
        temp -= cow[index[ind]] # 자신을 사용했고 다음에는 자신을 제외하고 해야 되니깐 자신의 부분을 뺀다.

print(maximum)