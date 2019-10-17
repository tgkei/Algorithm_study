class Solution:
    def findPeakElement(self, nums: "List[int]") -> int:
        n = len(nums)
        start = 0
        end = n-1
        while True:
            if start == end: # 시작과 끝이 같다면 즉 값이 마지막 하나라면
                return start
            mid = (end+start)//2 # 가운데 찾기
            if mid == start: return start if nums[start] > nums[start+1] else start+1 # 
            if mid == end: return end if nums[end] > nums[end-1] else end-1
            if nums[mid] >= nums[mid+1] and nums[mid] >= nums[mid-1]:
                return mid
            if nums[mid] < nums[mid+1]:
                start = mid + 1
            else:
                end = mid - 1
"""
class Solution:
    def findPeakElement(self, nums):
        n = len(nums)
        if n < 1: return 0
        compare = n-1
        for i in range(n-1,0,-1):
            if(nums[i-1] > nums[i]):
                compare = nums.index(nums[i-1])
        return compare
"""

"""class Solution:
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
        return self.peakIndex(idx//2,start, idx)"""
"""
class Solution:
    def findPeakElement(self, nums):
        n = len(nums)
        if n < 2 : return 0
        if n==2 :
            if(nums[0] < nums[1]):
                compare = 1
            else:
                compare = 0
        if n > 2:
            compare = 0
            for i in range(n-1):
                if(nums[i] < nums[i+1]):
                    compare = i+1
        return compare
"""
if __name__ == '__main__':
    peak_elements = [1,2,3,1]
    a = Solution()

    print(a.findPeakElement(peak_elements))
