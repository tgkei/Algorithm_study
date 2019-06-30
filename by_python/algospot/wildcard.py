def compare(a, b):
    global cache
    len_a = a
    len_b = b
    if cache[len_a][len_b] != -1: return cache[len_a][len_b]
    while (len_a < len(s) and len_b < len(com) and (s[len_a] == com[len_b] or s[len_a] == '?')):
        len_a +=1
        len_b +=1
    if len_a == len(s): return len_b == len(com)
    if s[len_a] == "*":
        new = 0
        while len_b + new <= len(com):
            if compare(len_a+1,len_b+new):
                cache[len_a][len_b] = True 
                return cache[len_a][len_b]
            new+=1
    cache[len_a][len_b] = False
    return cache[len_a][len_b]

for _ in range(int(input())):
    s = input()
    comp = []
    res = []
    for _ in range(int(input())):
        comp.append(input())
    for com in comp:
        cache = [[-1 for _ in range(101)] for _ in range(101)]
        if compare(0,0): res.append(com)
    res.sort()
    for r in res:
        print(r)