#from collections import OrderedDict

N = int(input())

cow = []
# cnt should be nonnegative even number.
for i in range(N):
    cow_pos, cow_color = input().split()
    cow_pos = int(cow_pos)
    if cow_color == 'W':
        cow.append((cow_pos, 1))
    else:
        cow.append((cow_pos, -1))

cow.sort()  ## sorting cow

maximum = 0
temp = 0

odd_num =[]  # cow with odd base
even_num =[] # cow with even base

base = 0
even = True
maximum = 0
index = 0

for i in range(N):
    if even:
        if (len(even_num)==0 or even_num[-1][0] > base):
            even_num.append((base, cow[i][0]))
    else:
        if (len(odd_num)==0 or odd_num[-1][0] > base):
            odd_num.append((base, cow[i][0]))
    
    base += cow[i][1]
    even = not even

    if even:
        ## even_num 중에 현재 base보다 작거나 같은 것 중 가장 앞에 것 찾아야 함.
        if( not(len(even_num)==0) and even_num[-1][0]<= base):
            if base >= 0 :
                index = 0
            else:
                index = abs(base//2)
            maximum = max(maximum, cow[i][0]-even_num[index][1])
    else:
        if (not(len(odd_num)==0) and odd_num[-1][0] <= base):
            if odd_num[0][0] == 1:
                if base >= 1:
                    index = 0
                else:
                    index = abs(base//2)
            else: #-1일때 입니다.
                if base >= -1:
                    index = 0
                else:
                    index = (abs(base//2)-1)
            maximum = max(maximum, cow[i][0] - odd_num[index][1])

print(maximum)