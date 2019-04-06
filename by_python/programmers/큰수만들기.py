number = input()
k = int(input())
number = list(number)
a = len(number)-k
result = []
s = 0
for i in range(a):
    maximum = max(number[s:k+i+1])
    s=(number[s:k+i+1].index(maximum))+1 + s 
    result.append(maximum)
answer = ''.join(result)
print(answer)