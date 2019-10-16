class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a =dict()
        for idx, num in enumerate(nums):
            comp = target - num
            if num in a:
                a[num].append(idx)
            else:
                a[num] = [idx]
            if comp in a:
                for idx2 in a[comp]:
                    if idx == idx2: continue
                    ret = sorted([idx,idx2])
                    return ret
if __name__ == "__main__":
    a = Solution()
    a.twoSum()