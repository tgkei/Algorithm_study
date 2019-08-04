"""
https://codeforces.com/contest/1066/problem/C
"""
n = int(input())
dic = {}

left = 0
right = 1

for _ in range(n):
    pos, num = input().split()
    if pos =='L':
        dic[num] =left
        left -=1
    elif pos == 'R':
        dic[num] = right
        right +=1
    else:
        print("{}".format(min(dic[num]- (left+1) ,right-1-dic[num])))