from collections import deque

n, m = map(int, input().split())

numbers = deque()
result = []

check = [False for _ in range(n)]
for i in range(n):
    numbers.append(i+1)

i = 0
while numbers:
    i = i+1
    if i != m:
        numbers.rotate(-1)
    else:
        result.append(str(numbers.popleft()))
        i = 0

print('<'+', '.join(result)+'>')