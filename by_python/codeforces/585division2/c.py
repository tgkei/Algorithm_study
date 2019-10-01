n = int(input())
s1= input()
s2= input()
dif = 0 
s1_a = []
s2_a = []
for idx in range(n):
    if s1[idx] != s2[idx]:
        dif +=1
        if s1[idx]=='a': s1_a.append(idx+1)
        else: s2_a.append(idx+1)
if dif%2:
    print(-1)
else:
    print(len(s1_a)//2 + len(s2_a)//2 + 2*(len(s1_a)%2))
    while len(s1_a)>=2:
        print(s1_a.pop(), s1_a.pop())
    while len(s2_a)>=2:
        print(s2_a.pop(), s2_a.pop())
    while s1_a:
        t = s1_a.pop()
        print(t, t)
        print(s2_a.pop(), t)

