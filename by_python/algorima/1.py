f = open("input.txt","r")
T = int(f.readline())

result=[] 
for testcase in range(1,T+1):
    c_p = 2
    C, F, X = map(float,f.readline().split())
    target = 0
    for_new = 0
    so_far = 0
    while True:
        for_new = C/c_p
        target = X/c_p
        if target <= for_new + (X/(c_p+F)): break
        so_far += for_new
        c_p += F
    result.append("Case #{}: {:.7f}".format(testcase,so_far + target)+"\n")
f.close()
f = open("output.txt","w")
for res in result:
    f.write(res)
f.close()