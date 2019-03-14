import time

N = int(input())

answer = input().split()

town, road = map(int, input().split())

connection = [[] for _ in range(town)]
score = [[-1 for _ in range(town)] for _ in range(N)]

for _ in range(road):
    city_1, city_2, color = input().split()
    city_1, city_2 = int(city_1)-1, int(city_2)-1
    connection[city_1].append((city_2, color))
    connection[city_2].append((city_1, color))

def longest(num_so_far, origin):
    if (num_so_far == N-1):
        return 0
    if score[num_so_far][origin] != -1:
        return score[num_so_far][origin]
    for destination, temp_color in connection[origin]:
        score[num_so_far][origin] = max(score[num_so_far][origin], longest(num_so_far+1, destination)+ (10 if (temp_color==answer[num_so_far+1]) else 0))
    return score[num_so_far][origin]

start_time = time.time() 

maximum = 0

for destination, temp_color in connection[0]:
    maximum = max(maximum, longest(0, destination) + (10 if (temp_color==answer[0]) else 0))

print(maximum)

print("start_time", start_time) #출력해보면, 시간형식이 사람이 읽기 힘든 일련번호형식입니다.
print("--- %s seconds ---" %(time.time() - start_time))