from collections import Counter

a = input()
target = int(input())
c= Counter(a)
length = len(a) - 2* c["*"] - 2 * c["?"]

if length > target:
    print("Impossible")
else:
    pure = length + c["*"] + c["?"]
    pon = pure - target
    if not pon:
        for aa in a:
            if aa=="*" or aa=="?":
                continue
            else:
                print(aa,end="")
    elif pon < 0:
        if c["*"] == 0:
            print("Impossible")
        else:
            for idx, aa in enumerate(a):
                if aa =="?":
                    continue
                elif aa =="*":
                    while pon != 0:
                        print(a[idx-1],end="")
                        pon+=1
                else:
                    print(aa,end="")
    else:
        b = []
        for aa in a:
            if b and pon > 0 and (aa=="*" or aa=="?"):
                b.pop()
                pon-=1
            elif (aa=="*" or aa=="?"):
                continue
            else:
                b.append(aa)
        print("".join(b))