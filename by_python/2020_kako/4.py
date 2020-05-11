# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
a = int(input())
formations = input()
left = ""

for idx, letter in enumerate(formations):
    if a != idx:
        left += letter
    else:
        left += " "
        left += letter
if a == n-1:
    left += " "

user = " "
answer = 0

while (True):
    if len(left) == 1 : break
    winner = ""
    
    for idx, (p1, p2) in enumerate(zip(left[::2], left[1::2])):
        if idx == a//2:
            if a%2: # p2
                if user == ' ':
                    if p1 == 'R': user = 'P'
                    elif p1 == 'S': user = 'R'
                    else: user = 'S'
                else:
                    if p1 == 'R' and user != 'P':
                        answer+=1
                        user = 'P'
                    elif p1 == 'S' and user != 'R':
                        answer+=1
                        user = 'R'
                    elif user != 'S':
                        answer+=1
                        user = 'S'
            else:
                if user == ' ':
                    if p2 == 'R': user = 'P'
                    elif p2 =='S' : user ='R'
                    else: user = 'S'
                else:
                    if p2 == 'R' and user != 'P':
                        answer+=1
                        user = 'P'
                    elif p2 == 'S' and user != 'R':
                        answer+=1
                        user = 'R'
                    elif user != 'S':
                        answer+=1
                        user = 'S'
            a = len(winner)
            winner += user
            continue
        if p1=='R':
            if p2=='S':
                winner += p1
            elif p2=='P':
                winner += p2
        elif p1 == "S":
            if p2=="P":
                winner += p1            
            elif p2=="R":
                winner += p2
        else:
            if p2=="R":
                winner += p1
            elif p2=="S":
                winner += p2
    
    if a == len(left)-1 and (len(left)%2):
        a = len(winner)
        winner+=user
    left = winner

print(answer)