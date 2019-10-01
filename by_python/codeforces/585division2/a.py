first_n = int(input())
second_n = int(input())
first_limit = int(input())
second_limit = int(input())
cards = int(input())

minimum = min(first_limit, second_limit)
maximum = 0
if cards - ((first_limit-1)*first_n + second_n*(second_limit-1))>0:
    print(cards - ((first_limit-1)*first_n + second_n*(second_limit-1)),end = " ")
else:
    print(0,end=" ")
if minimum == first_limit:
    while first_n and cards-first_limit >= 0:
        first_n-=1
        cards-=first_limit
        maximum+=1
    while second_n and cards - second_limit >= 0:
        second_n-=1
        cards-=second_limit
        maximum+=1
else:
    while second_n and cards-second_limit >= 0:
        second_n-=1
        cards-=second_limit
        maximum+=1
    while first_n and cards - first_limit >= 0:
        first_n-=1
        cards-=first_limit
        maximum+=1
print(maximum)