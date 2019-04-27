input()

chest = list(map(int,input().split()))
keys = list(map(int,input().split()))

odd_chest = 0
even_chest = 0
odd_keys = 0
even_keys = 0

for c in chest:
    if c % 2 ==0:
        even_chest+=1
    else:
        odd_chest+=1

for key in keys:
    if key % 2 == 0:
        even_keys +=1
    else:
        odd_keys +=1

result = 0
result += min(odd_chest, even_keys)
result += min(even_chest, odd_keys)

print(result)