import sys

def solve(x, y , A,width):
    for _ in range(1000):
        if x > width:
            x = 2
        print(x,y)
        sys.stdout.flush()
        s = input()
        if s == "0 0":
            return True
        elif s == "-1 -1":
            exit()
        else:
            x += 3
    else:
        return False

T = int(input())
for _ in range(T):
    A = int(input())
    x = 2

    if (A % 9) ==0:
        width = A//9
    else:
        width = ((A//9)+1)

    width = 2 + ((width-1)*3)

    while True:
        if (solve(x,2,A,width)):
            break