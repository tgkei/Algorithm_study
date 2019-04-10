two = [2,4,8,6]
three=[3,9,7,1]
four = [4,6]
seven = [7,9,3,1]
eight=[8,4,2,6]
nine = [9,1]

for _ in range(int(input())):
    a, b = map(int,input().split())
    a = a %10
    if a == 0:
        print(10)
    elif a == 1:
        print("1")
    elif a == 2:
        b -=1
        b = b % 4
        print(two[b])
    elif a == 3:
        b -=1
        b = b % 4
        print(three[b])
    elif a == 4:
        b -=1
        b = b % 2
        print(four[b])
    elif a == 5:
        print(5)
    elif a == 6:
        print(6)
    elif a == 7:
        b-=1
        b = b % 4
        print(seven[b])
    elif a == 8:
        b-=1
        b = b % 4
        print(eight[b])
    elif a == 9:
        b -=1
        b = b%2
        print(nine[b])
    