s = input()

dic = dict()
i = 0
j = 1
dic[s[i]] = 0
res = 1
while j < len(s):
    if not s[j] in dic:
        dic[s[j]] = j
        res = max(res, j-i+1)
        j+=1
    else:
        i = dic[s[j]]+1
        dic[s[j]] = j
        res = max(res, j-i+1)
        j+=1
print(res)