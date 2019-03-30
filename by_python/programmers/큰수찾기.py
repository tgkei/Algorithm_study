number = input()
k = int(input())
number = list(map(int,list(number)))
total_len = len(number)
length = total_len-k
answer = []
j = 0
for i in range(length+1):
    new_j = max(number[j:k+i])
    answer.append(new_j)
    j=number.index(new_j)+1

print(answer)