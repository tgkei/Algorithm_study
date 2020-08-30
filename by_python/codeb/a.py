def find_cat(a):
    global N
    status = (a/(220-N))*100
    if status < 60: return 0
    elif status < 68: return 1
    elif status < 75: return 2
    elif status < 80: return 3
    elif status < 90: return 4
    return 5

N = int(input())
answers = [0 for _ in range(6)]

while True:
    try:
        x = input()
        answers[find_cat(int(x))]+=1
    except EOFError:
        break
        

for answer in reversed(answers):
    print(answer, end= ' ')