def combination(str_so_far,num):
    global res
    if num == total: 
        res.append(str_so_far)
        return
    for n in l[int(digits[num])]:
        combination(str_so_far+n,num+1)
    

l=["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]

digits = input()
total = len(digits)
res = []
combination("",0)
return res