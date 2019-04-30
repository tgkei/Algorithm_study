l = []
for _ in range(12):
    l.append(float(input()))

result = round(sum(l)/12,2)
result = "$"+str(result)
if result[-2] == '.':
    result+="0"

if result[-2:] == "00":
    result = result[:-3]
print(result)