x = int(input())

x = format(x,"b")

pos =[]

i = len(x)
current = x[0]

total = 0
result = ""

for bit in x:
    if i == 1:
        break
    if bit != current:
        current = bit
        pos.append(str(i))
    i -= 1

if len(pos) == 0 and x[-1] == "0":
    print(1)
    print(1)
else:
    total = total + (2* len(pos))
    if x[-1] == "0":
        total -=1
    print(total)
    print(" ".join(pos))