
"""import math

input()
chocos = list(map(int,input().split()))

maximum = math.inf
result = 0
cur = 0

for i, choco in enumerate(chocos):
    d = 0
    if maximum >= choco:
        if maximum != math.inf:
            temp = choco - 1
            while i>0 and chocos[i-1] >=temp:
                d = d + (chocos[i-1] - temp) ## HOW MUCH DECREASED
                chocos[i-1] = temp
                temp = (chocos[i-1]-1) if chocos[i-1]-1 > 0 else 0
                i -= 1
            cur = cur - d

           
        maximum = choco
        cur = maximum + cur
    else:
        cur += choco
        maximum = choco

    result = max(result,cur)
print(result)"""

