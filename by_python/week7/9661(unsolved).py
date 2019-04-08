N = int(input())
four_th = []
i = 1
j = 4
while j <= N:
    four_th.append(j)
    i += 1
    j = 4**i
i = 0
while four_th:
    if N < four_th[-1]:
        four_th.pop()
    else:
        N -= four_th[-1]
        i += 1

i += N
if i % 2 ==0:
    print("CY")
else:
    print("SK")