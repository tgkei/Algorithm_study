import sys

def solve(x, y , width):
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

for _ in range(int(input())):
    A = int(input())

    if (A % 9) ==0:
        width = A//9
    else:
        width = ((A//9)+1)

    width = 2 + ((width-1)*3)

    while True:
        if (solve(2,2,width)):
            break
        else:
            exit()