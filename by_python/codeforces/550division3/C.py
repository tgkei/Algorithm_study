import sys

input()
numbers = list(map(int,sys.stdin.readline().split()))
ascending =[]
descending =[]
is_no = False
numbers.sort()

prev = -1
cont = 0

for number in numbers:
    if prev == number:
        cont+=1
    else:
        cont = 0
        prev = number

    if cont == 2:
        is_no = True
        print("No")
        break

    elif cont == 1:
        descending.append(number)
    else:
        ascending.append(str(number))

if not is_no:
    print("YES")
    print(len(ascending))
    print(' '.join(ascending))
    print(len(descending))
    descending.sort(reverse=True)
    for i,num in enumerate(descending):
        descending[i] = str(num)
    print(' '.join(descending))
