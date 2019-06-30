n = int(input())
dic = {}

first_res = []
sec_res = []

for _ in range(n):
    t = input()
    key = t.count('e')+ t.count('u')+ t.count('o')+t.count('i')+t.count('a')
    temp = max(t.rfind('e'), t.rfind('u'), t.rfind('o'), t.rfind('i'), t.rfind('a'))
    if key not in dic.keys(): 
        dic[key] = {}
        dic[key][t[temp]] = [t]
    else:
        if t[temp] not in dic[key].keys():
            dic[key][t[temp]] = [t]
        else:
            dic[key][t[temp]].append(t)

for key, key2 in dic.items():
    temp = []
    for vowel, words in key2.items():
        while len(words)>=2:
            a = words.pop()
            b = words.pop()
            sec_res.append((a,b))
        if len(words): temp.append(words.pop())
    while len(temp) >=2:
        a = temp.pop()
        b = temp.pop()
        first_res.append((a,b))

if len(sec_res)<=len(first_res):
    print(len(sec_res))
    for i in range(len(sec_res)):
        print(first_res[i][0], sec_res[i][0])
        print(first_res[i][1], sec_res[i][1])
else:
    print(len(first_res) + (len(sec_res)-len(first_res))//2)
    j = -1
    for i in range(len(first_res)):
        print(first_res[i][0], sec_res[i][0])
        print(first_res[i][1], sec_res[i][1])
        j = i
    while j+2 < len(sec_res):
        print(sec_res[j+1][0], sec_res[j+2][0])
        print(sec_res[j+1][1], sec_res[j+2][1])
        j+=2