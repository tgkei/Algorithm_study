n = int(input())

imp = True

nums= [*map(int,list(input())[:-10])]

if nums.count(8)<=(n-11)//2:
    print("NO")
else:
    print("YES")