"""for i in range(int(input())):
    N = int(input())
    paths = input()
    S_or_E =[]
    paths[0]
    my_path = ""
    index = 0
    two = False
    if paths[0] == 'S':
        if paths[-1] == 'E':
            for _ in range(N-1):
                my_path += "E"
            for _ in range(N-1):
                my_path += "S"
        else:
            for path in paths[1:]:
                if path == "E":
                    if two:
                        for _ in range(index):
                            my_path += "E"
                        for _ in range(N-1):
                            my_path += "S"
                        for _ in range(N-1-index):
                            my_path += "E"
                        break
                    else:
                        two = True
                        index += 1
                else:
                    two = False
    else:
        if paths[-1] == "S":
            for _ in range(N-1):
                my_path += "S"
            for _ in range(N-1):
                my_path += "E"
        else:
            for path in paths[1:]:
                if path == "S":
                    if two:
                        for _ in range(index):
                            my_path += "S"
                        for _ in range(N-1):
                            my_path += "E"
                        for _ in range(N-1-index):
                            my_path += "S"
                        break
                    else:
                        two = True
                        index += 1
                else:
                    two = False
    print("Case #{}: {}".format(i+1, my_path))"""

"""for T in range(int(input())):
    N = int(input())
    P = input()
    
    answer = []
    
    for p in P:
        if p == "S":
            answer.append("E")
        else:
            answer.append("S")
    answer = "".join(answer)
    print("Case #{}: {}".format(T+1,answer))"""

for T in range(int(input())):
    N = int(input())
    P = input()
    way = []
    for i in range(2*N-2):
        if(P[i] == 'S'):
            way.append('E')
        else:
            way.append('S')
    
    way = str("".join(way))
    print("Case #{}: {}".format(T+1, way))