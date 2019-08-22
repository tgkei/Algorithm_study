#https://www.acmicpc.net/problem/2042
from math import ceil, log2

def construct_tree(low,high, pos):
    global tree
    if low == high:
        tree[pos] = nums[low]
        return tree[pos]
    mid = (low+high)//2
    tree[pos] = construct_tree(low,mid,pos*2+1) + construct_tree(mid+1,high,pos*2+2)
    return tree[pos]

def solve(low, high, pos):
    global global_low
    global global_high
    if low >= global_low and high <= global_high:
        return tree[pos]
    if high < global_low or low > global_high: return 0
    mid = (low+high)//2
    return solve(low,mid,pos*2+1) + solve(mid+1,high,pos*2+2)

def change(low,high,target,pos,diff):
    global tree
    if low <= target and target <= high:
        tree[pos] += diff
    else:
        return
    if low== high: return
    mid= (low+high)//2
    change(low,mid,target,2*pos+1,diff)
    change(mid+1,high,target,2*pos+2,diff)

n, m, k = map(int,input().split())

nums = []
for _ in range(n):
    nums.append(int(input()))
depth = 2 * (2**ceil(log2(n))) - 1
tree = [-1 for _ in range(depth)]
construct_tree(0,n-1,0)
for _ in range(m+k):
    command, n1, n2 = map(int,input().split())
    if command == 1:
        diff = n2 - nums[n1-1]
        nums[n1-1] = n2
        change(0,n-1,n1-1, 0, diff)
    else:
        k-=1
        global_low = n1-1
        global_high = n2-1
        print(solve(0,n-1,0))