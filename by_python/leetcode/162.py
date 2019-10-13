class Solution:
    def findPeakElement(self, nums: "List[int]") -> int:
        self.nums = nums
        self.n = len(self.nums)
        if self.n == 1: return 0
        return self.peakIndex(self.n//2, 0, self.n)

    def peakIndex(self, idx,start, end):
        if idx ==0:
            return 0 if self.nums[0]>self.nums[1] else 1
        if idx == end-1:
            return end-1 if self.nums[end-1] > self.nums[end-2] else end-2
        if self.nums[idx] >= self.nums[idx+1] and self.nums[idx] >= self.nums[idx-1]:
            return idx
        if self.nums[idx] < self.nums[idx+1]:
            return self.peakIndex(idx+(end - idx)//2,idx+1, end)
        return self.peakIndex(idx//2,start, idx)

if __name__ =="__main__":
    sol = Solution()
    nums = [2,3,4,3,2,1]
    print(sol.findPeakElement(nums))