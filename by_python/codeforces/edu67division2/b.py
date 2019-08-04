input()
s = input()
dic ={}
for idx,ss in enumerate(s):
    if ss in dic.keys():
        dic[ss].append(idx)
    else:
        dic[ss] = [idx]
n = int(input())
for _ in range(n):
    s = input()
    temp_dic ={}
    for ss in s:
        if ss in temp_dic.keys():
            temp_dic[ss] +=1
        else:
            temp_dic[ss] = 1
    res = -1
    for key, value in temp_dic.items():
        res= max(res,dic[key][value-1]+1)
    print(res)