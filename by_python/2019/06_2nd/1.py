# https://codeforces.com/contest/1185/problem/D

input()

nums = list(map(int,input().split()))
dic = {}
for idx, num in enumerate(nums):
    dic[num] = idx

