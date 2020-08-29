CASE = int(input())

for case in range(CASE):
    answer = 0
    n = int(input())
    nums = list(map(int, input().split()))

    idx = 1

    while idx < n:
        tmp_ans = 0
        diff = nums[idx] - nums[idx-1]
        while idx < n and diff == (nums[idx] - nums[idx-1]):
            tmp_ans += 1
            idx += 1
        answer = max(answer, tmp_ans+1)

    print("Case #{}: {}".format(case+1, answer))
