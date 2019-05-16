n = int(input())

l = list(input())

res = ""
delete = 0

is_odd = n%2
i = 0
j = 1
while j< n:
    while j<n and l[j]==l[i]:
        j+=1
    if j == n:
        break
    
    res+=l[i]
    res+=l[j]
    i = j+1
    j = i+1

if n ==1:
    print("1")
else:       
    print(n-len(res))        
    print(res)