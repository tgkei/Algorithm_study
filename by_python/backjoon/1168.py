from collections import deque

n, k = map(int, input().split())

numbers = deque(list(range(1,n+1)))

print("<",end="")
i = 0
while len(numbers) > 1:
    i = i+1
    temp = numbers.popleft()
    if i%k == 0:
        print(str(temp)+", ",end="")
        i = 0
    else:
        numbers.append(temp)

print(str(numbers.popleft())+">")