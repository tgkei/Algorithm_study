for _ in range(int(input())):
    inputs = input()
    result = 0
    for par in inputs:
        if par == '(':
            result+=1
        else:
            result -=1
        if result <0:
            break

    if result==0:
        print("YES")
    else:
        print("NO")