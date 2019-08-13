n = int(input())
l = input()

rooms = [0] * 10
for ll in l:
    l_idx = 0
    r_idx = 9
    if ll == 'L':
        while rooms[l_idx]: l_idx+=1
        rooms[l_idx] = 1
    elif ll =="R": 
        while rooms[r_idx]:r_idx -=1
        rooms[r_idx] = 1
    else:
        rooms[int(ll)] = 0
for room in rooms:
    print(room,end="")