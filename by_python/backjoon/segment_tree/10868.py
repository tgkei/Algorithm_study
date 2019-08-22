import sys
from math import ceil, log2, inf

def construct_tree(low,high,pos):
    global tree
    if low == high:
        tree[pos] = nums[low]
        return tree[pos]
    mid = (low+high)//2
    tree[pos] = min(construct_tree(low,mid,2*pos+1),construct_tree(mid+1,high,2*pos+2))
    return tree[pos]

def find_min(low,high,pos):
    global global_low
    global global_high
    if low >= global_low and high <= global_high: return tree[pos]
    if low > global_high or high < global_low: return inf
    mid = (low+high)//2
    return min(find_min(low,mid,2*pos+1),find_min(mid+1,high,2*pos+2))

n, m = map(int,sys.stdin.readline().split())
depth = 2* (2**ceil(log2(n))) - 1
nums = []
tree = [-1] * depth
for _ in range(n):
    nums.append(int(sys.stdin.readline()))

construct_tree(0,n-1,0)

for _ in range(m):
    global_low, global_high = map(lambda x: int(x)-1, sys.stdin.readline().split())
    print(find_min(0,n-1,0))