n = int(input())

d ={}

l = 0
r = 1

for _ in range(n):
    command, num = input().split()
    
    if command == "L":
        d[num] = l
        l-=1
    elif command == "R":
        d[num] = r
        r += 1
    else:
        print(min(d[num]-l-1, r-1-d[num]))