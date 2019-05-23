"""import sys
sys.setrecursionlimit(1000000)"""
from math import inf

def connected(x,y,connection): # find all connected land from (x,y)
    if x<0 or x>=n or y<0 or y>=n:
        return
    if connection[x][y]:
        return
    if board[x][y]:
        return
    connection[x][y] = True
    connected(x+1, y, connection)
    connected(x, y+1, connection)
    connected(x-1,y,connection)
    connected(x,y-1,connection)

n = int(input())
x1, y1 = map(lambda x: int(x)-1, input().split())
x2, y2 = map(lambda x: int(x)-1, input().split())

board = [ list(map(int,input())) for _ in range(n)] # given land information

con1 = [[False for _ in range(n)] for _ in range(n)] # for land connected to starting spot
con2 = [[False for _ in range(n)] for _ in range(n)] # for land connected to destination

connected(x1, y1, con1)
connected(x2, y2, con2)

minimum = inf

## check all possible connection between starting land and arrival island
for i in range(n):
    for j in range(n):
        if con1[i][j]:
            for i2 in range(n):
                for j2 in range(n):
                    if con2[i2][j2]:
                        minimum = min(minimum, (i-i2)**2 + (j-j2)**2)

print(minimum)