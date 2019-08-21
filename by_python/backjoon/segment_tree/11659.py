# prefix_sum

"""import sys

n, m = map(int,sys.stdin.readline().strip().split())

pre_sum = []
temp = 0
for num in list(map(int,sys.stdin.readline().strip().split())):
    temp += num
    pre_sum.append(temp)

for _ in range(m):
    l,h = map(int,sys.stdin.readline().strip().split())
    l-=1
    h-=1
    print(pre_sum[h]-pre_sum[l-1] if l >0 else pre_sum[h])"""
# segment Tree
import sys
from math import log2,ceil

sys.setrecursionlimit(9999999)

def init(l, h,pos):
    global tree
    if l ==h: 
        tree[pos] = nums[l]
        return tree[pos]
    mid = (l+h) //2
    tree[pos] = init(l,mid,pos*2+1) + init(mid+1,h,pos*2+2)
    return tree[pos]

def s_t(l,h,pos):
    if l>=low and h<=high: return tree[pos]
    if h < low or l > high: return 0
    mid = (l+h)//2
    return s_t(l,mid,pos*2+1)+s_t(mid+1,h,pos*2+2)


n, m = map(int,sys.stdin.readline().strip().split())
nums = list(map(int,sys.stdin.readline().strip().split()))
depth = 2* (2**ceil(log2(n))) - 1
tree = [-1 for _ in range(depth)]
init(0,n-1,0)
for _ in range(m):
    low, high = map(lambda x: int(x)-1,sys.stdin.readline().strip().split())
    print(s_t(0,n-1,0))