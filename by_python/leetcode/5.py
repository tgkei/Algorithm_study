# 5.longest palidrome
# https://leetcode.com/problems/longest-palindromic-substring/

"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.s = s
        self.dp = [[-1 for _ in range(len(s))] for _ in range(len(s))]
        self.longest = -1
        self.answer = ""
        if not len(s):
            return ""
        for start in range(len(s)):
            for end in range(len(s)-1,start-1,-1):
                self.isPalindrome(start,end)
        return self.answer

    def isPalindrome(self, start, end):
        if start == end:
            if self.longest < 1: 
                self.longest =1
                self.answer = self.s[start]
            return True
        if start == end-1:
            if self.s[start] == self.s[end]:
                self.dp[start][end] = 1
                if self.longest < 2:
                    self.longest = 2
                    self.answer = self.s[start:end+1]
            else:
                self.dp[start][end] = 0
                if self.longest < 1:
                    self.longest = 1
                    self.answer = self.s[start]
            return self.dp[start][end]
        
        if self.dp[start][end] != -1: 
            return self.dp[start][end]
        if self.isPalindrome(start+1,end-1):
            if self.s[start] == self.s[end]:
                self.dp[start][end] = 1
                if self.longest < end-start+1:
                    self.longest = end-start+1
                    self.answer = self.s[start:end+1]
                return 1
            else:
                self.dp[start][end] = 0
                return 0
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        answer_i = 0
        answer_j = 1

        def is_palindrome(a):
            for w1, w2 in zip(a, a[::-1]):
                if w1 != w2:
                    return False
            return True

        low = 1
        high = n
        while low <= high:
            mid = (high+low)//2
            is_palin = False
            for i in range(n-mid+1):
                print(s[i:i+mid])
                if is_palindrome(s[i:i+mid]):
                    is_palin = True
                    if answer_j - answer_i < mid:
                        answer_j = i+mid
                        answer_i = i
                if is_palin:
                    low = mid+1
                else:
                    high = mid-1

        return s[answer_i: answer_j]


if __name__ == "__main__":
    sol = Solution()
    string = "aba"
    print(sol.longestPalindrome(string))

