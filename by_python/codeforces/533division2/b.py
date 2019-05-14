letter = "abcdefghijklmnopqrstuvwxyz"

n, m = map(int,input().split())

string = input()

level = -1

for l in letter:
    temp = 0
    k = 0
    for s in string:
        if l == s:
            k+=1
            if k % m ==0:
                temp+=1
                k=0
        else:
            k = 0
    level = max(level,temp)

print(level)