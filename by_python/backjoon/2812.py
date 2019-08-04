n, m = map(int,input().split())

target = n - m
l = input()
stack = []
start = -1

for idx, num in enumerate(l):
    while stack and stack[-1] < num and m>0:
        stack.pop()
        m -=1
    if not m: 
        start = idx
        break
    stack.append(num)

if len(stack) >= target:
    stack = stack[:target]
else:  
    stack+=l[start:]
res = ""
for num in stack: res+=num
print(res)