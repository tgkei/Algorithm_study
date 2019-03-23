input()
buildings = list(map(int,input().split()))
stack =[]
result = []
for res, building in enumerate(buildings):
    if not stack:
        stack.append((res+1,building))
        result.append(0)
        continue
    while stack and stack[-1][1] < building:
        stack.pop()
    if not stack:
        result.append(0)
    else:
        result.append(stack[-1][0])
    stack.append((res+1,building))
        
print(' '.join(str(res) for res in result))