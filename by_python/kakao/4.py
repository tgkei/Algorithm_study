from math import inf

def solution(k, room_number):
    answer = []
    start = dict()
    for room in room_number:
        if room not in start:
            answer.append(room)
            next_room = room + 1
            while next_room in start:
                start[next_room] = room
                next_room += 1
            start[room] = next_room
        else:
            next_room = start[room]
            start_point = room
            while next_room in start:
                start_point = min(start_point, start[next_room])
                temp = start[next_room]
                start[next_room] = start_point
                next_room = temp
            answer.append(next_room)
            start[next_room] = start_point
            start[start_point] = next_room+1
    return answer

if __name__ == '__main__':
    k = 10
    room_number = [1,3,4,1,3,1]
    print(solution(k,room_number))