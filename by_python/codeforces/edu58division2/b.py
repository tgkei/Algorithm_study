"""

l = list(input())

open_bracket= False
start= False
pos_close = False
finished = False

num = 0

res = []
finish = []
first = True

for char in l:
    if first:
        if not open_bracket and char == '[': 
            open_bracket= True
            continue
        if open_bracket and char == ':':
            start = True
            first= False
            continue
    if not start:
        continue
    if char == '|': num+=1
    if char == ':': 
        pos_close = True
        res.append(num)
    if pos_close and char =="]":
        finished = True
        finish.append(res[-1])
if finished:
    print(finish[-1]+4)
else:
    print(-1)"""

s = input()
a = s.find('[')
b = s.find(':',a)
c = s.rfind(']',b)
d = s.rfind(':',b,c)

if a< b< d< c:
    print(4+s[b:d].count("|"))
else:
    print(-1)