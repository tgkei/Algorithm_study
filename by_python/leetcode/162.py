"""class Solution:
    def findPeakElement(self, nums: "List[int]") -> int:
        n = len(nums)
        start = 0
        end = n-1
        while True:
            if start == end:
                return start
            mid = (end+start)//2
            if mid == start: return start if nums[start] > nums[start+1] else start+1
            if mid == end: return end if nums[end] > nums[end-1] else end-1
            if nums[mid] >= nums[mid+1] and nums[mid] >= nums[mid-1]:
                return mid
            if nums[mid] < nums[mid+1]:
                start = mid + 1
            else:
                end = mid - 1"""

"""class Solution:
    def findPeakElement(self, nums):
        n = len(nums)
        if n < 1: return 0
        compare = n-1
        for i in range(n-1,0,-1):
            if(nums[i-1] > nums[i]):
                compare = nums.index(nums[i-1])
        return compare"""

if __name__ == '__main__':
    peak_elements = [1,2]
    a = Solution()

    print(a.findPeakElement(peak_elements))