command = []
for _ in range(int(input())):
    command.append(input())

result =list(command[0])

i = 0
for com in command[1:]:
    temp = list(com)
    for r, t in zip(result, temp):
        if r != t:
            result[i] = '?'
        i +=1
    i =0
print(''.join(result))        