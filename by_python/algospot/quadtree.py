def solve():
    global pos
    if s[pos] == 'w' or s[pos]=='b':
        return s[pos]
    else:
        pos+=1
        top_left = solve()
        pos+=1
        top_right = solve()
        pos+=1
        bottom_left = solve()
        pos+=1
        bottom_right = solve()
        return 'x'+bottom_left + bottom_right + top_left + top_right

for _ in range(int(input())):
    s = input()
    pos = 0

    print(solve())