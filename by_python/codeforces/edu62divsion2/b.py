for _ in range(int(input())):
    n = int(input())

    l = input()

    i = 0
    while True:
        if l[i] == ">" or l[-(i+1)] == "<":
            break
        i+=1
    print(i)