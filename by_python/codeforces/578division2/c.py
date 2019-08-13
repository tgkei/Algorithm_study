import sys

sys.setrecursionlimit(9999999)
def gcd(a,b):
    while (b!=0):
        r = a%b
        a = b
        b = r
    return a

n, m , q = map(int,input().split())

a = gcd(n,m)

for _ in range(q):
    s_x,s_y,e_x,e_y = map(int,input().split())
    if s_x == 1:
        s_pos = (s_y-1)//(n//a)
    else:
        s_pos = (s_y-1)//(m//a)
    if e_x == 1:
        e_pos = (e_y-1)//(n//a)
    else:
        e_pos = (e_y-1)//(m//a)
    print("YES" if e_pos == s_pos else "NO")