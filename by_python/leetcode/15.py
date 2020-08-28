from collections import Counter, defaultdict


class Solution:
    def threeSum(self, nums):
        c = Counter(nums)
        two_sum = defaultdict(list)

        nums_set = list(set(nums))

        for i in range(len(nums_set)):
            for j in range(i, len(nums_set)):
                two_sum[nums_set[i] + nums_set[j]] = [nums_set[i], nums_set[j]]

        answer = []
        for num in nums:
            c[num] -= 1
            target = 0 - num
            if two_sum[target]:
                a, b = two_sum[target]
                if c[a] > 0 and c[b] > 0:
                    answer.append([num, a, b])
            c[num] += 1
