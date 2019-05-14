n = int(input())
pile = input()

pos = 0
neg = 0
initial = 0
total = 0

for p in pile:
    if p == "+":
        pos +=1
        total +=1
    else:
        neg +=1
        total -=1
    if total <0:
        initial = max(initial,abs(total))
    
print(initial +pos-neg)