from itertools import accumulate

n = int(input())

arr = list(map(int,input().split()))
acc_arr = list(accumulate(arr))

if len(set(acc_arr)) != n-1:
    print("-1")
else:
    total = (sum(range(1,n+1))-sum(acc_arr))
    if total % n:
        print("-1")
    else:
        res = [total//n] + [total//n + x for x in acc_arr]
        if sorted(res) != list(range(1,n+1)):
            print("-1")
        else:
            print(*res)