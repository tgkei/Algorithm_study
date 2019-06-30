for _ in range(int(input())):
    n = int(input())
    num = input()
    have = False
    n = n - 10
    for i in range(n):
        if num[i] =="8":
            have= True
            break
    if have:
        print("YES")
    else:
        print("NO")