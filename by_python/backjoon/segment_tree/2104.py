import sys
from math import ceil, log2
input = sys.stdin.readline
inf = int(1e9)


def construct_tree(low, high, pos):
    global tree
    global nums
    if low == high:
        tree[pos] = nums[low]
        return tree[pos]
    mid = (low+high)//2
    tree[pos] = min(construct_tree(low, mid, pos*2+1),
                    construct_tree(mid+1, high, pos*2+2))
    return tree[pos]


def retrieve(low, high, pos):
    global global_low
    global global_high
    if low >= global_low and high <= global_high:
        return tree[pos]
    if high < global_low or low > global_high:
        return inf
    mid = (low+high)//2

    return min(retrieve(low, mid, pos*2+1), retrieve(mid+1, high, pos*2+2))


n = int(input())
nums = list(map(int, input().split()))
depth = 2 * (2**ceil(log2(n))) - 1

l = []
tree = [0] * depth

construct_tree(0, n-1, 0)
prefix = []

for num in nums:
    if not prefix:
        prefix.append(num)
    else:
        prefix.append(prefix[-1]+num)

l, r = 0, 0

answer = -1
smallest = inf
while l < n:
    if r == n:
        l += 1
        r = l
        smallest = inf
        if l == n:
            break
    period_sum = 0
    if l == 0:
        period_sum = prefix[r]
    else:
        period_sum = prefix[r] - prefix[l-1]

    if smallest > nums[r]:
        global_low = l
        global_high = r
        smallest = retrieve(0, n-1, 0)
    answer = max(answer, smallest * period_sum)

    r += 1

print(answer)
