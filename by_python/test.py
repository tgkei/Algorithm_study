from itertools import combinations

def pick(so_far,taken):
    global total
    first = -1
    for idx, take in enumerate(taken):
        if take: continue
        first = idx
        break
    if first == -1:
        total+=1
        print("#"+str(total))
        for key, value in so_far.items():
            print("(",key, value,")", end=" ")
        print()
        return
    
    for i in range(26):
        if i != first and not taken[i]:
            so_far[i] = first
            so_far[first] = i
            taken[first] = True
            taken[i] = True
            pick(so_far,taken)
            so_far.pop(i,None)
            so_far.pop(first,None)
            taken[first] = False
            taken[i] = False


a = []
for i in range(26):
        a.append(i)

c = combinations(a,2)
taken = [False] * 26
so_far = {}
total = 0
pick(so_far,taken)