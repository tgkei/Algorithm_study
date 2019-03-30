n = int(input())

doors = list(map(int,input().split()))

a = doors.pop()
i = 0
b = 1
while True:
    if a != doors.pop():
        print(n-b)
        break
    else:
        b+=1