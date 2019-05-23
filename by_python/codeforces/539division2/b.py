import math

input()
powers = sorted(map(int,input().split()), reverse = True)

total = sum(powers)
minimum = total

for pwr in powers:
    for i in range(2, int(math.sqrt(pwr))+1):
        if pwr% i == 0:
            minimum = min(total - pwr + (pwr//i) + powers[-1]*i-powers[-1], minimum)

print(minimum)