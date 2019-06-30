n, b, a = map(int,input().split())
max_a = a

ex = list(map(int,input().split()))

pos = 0
while pos<n:
    if not b and not a:
        break
    if ex[pos]:
        if b:
            if a == max_a:
                a-=1
            else:
                b-=1
                a+=1
        else:
            a-=1
    else:
        if a:
            a-=1
        else:
            b-=1
    pos+=1

print(pos)