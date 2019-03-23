stack = []
result = []
yorn = True
i = 1
for _ in range(int(input())):
    if not yorn:
        break
    target = int(input())
    
    if not stack:
        stack.append(i)
        i+=1
        result.append("+")

    if stack[-1] > target:
        while stack and stack[-1] != target:
            result.append("-")
            if stack.pop() < target or not stack:
                yorn = False
                break

    
    if yorn and stack[-1] < target:
        while stack[-1] != target:
            result.append("+")
            stack.append(i)
            i+=1
            if stack[-1] > target:
                yorn = False
                break

        
    if stack and stack[-1] == target:
        result.append("-")
        stack.pop()


if yorn:
    print('\n'.join(result))
else:
    print("NO")