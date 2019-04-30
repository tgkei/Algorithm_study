"""
input()
s=input()
print(min(sum(min(x,26-x)for x in
map(lambda x,y:abs(ord(x)-ord(y)),t,'ACTG'))for
t in zip(s,s[1:],s[2:],s[3:])))"""



input()

l = [a for a in map(ord,input())]

print(min(sum(min(abs(x-g), abs(26-(x-g))) for x, g in zip(l[i:i+4],[ord("A"),ord("C"),ord("T"),ord("G")])) for i in range(len(l)-3)))
