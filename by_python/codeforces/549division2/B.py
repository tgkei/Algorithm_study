n = input()

result = 1
"""
length = len(n)

a_1 = int(n[0])*int(n[1])

max(int(n[0])*int(n[1]), int(n[0])*int(n[1]))
if length ==1:
    result *= int(n)
"""
new_num = []
for i in n:
    new_num.append(int(i))

length = len(new_num)
for i in range(1, length+1):
    i = -i
    if i != -1:
        temp = new_num[i]-1
        if i == -length and temp == 0:
            temp =1
    else:
        temp = new_num[i]
    for j in range(i-1,-length-1,-1):
        temp *= new_num[j]
    temp *= (9**(-(i+1)))
    result = max(temp, result)



print(result)