#!/usr/bin/python3
"""
leetcode #7 Reverse Integer
https://leetcode.com/problems/reverse-integer/
"""
MIN_NUM = -2147483648
MAX_NUM = 2147483647
class Solution:
    def reverse(self, x: int) -> int:
        is_neg = x<0
        tmp = []
        ret = 0
        
        if is_neg: x = -x

        while x//10:
            tmp.append(x%10)
            x //= 10
        tmp.append(x)
        tmp_ret = []

        is_skipping_num = tmp[0] == 0
        for num in tmp:
            if is_skipping_num and num == 0:
                continue
            is_skipping_num = False
            tmp_ret.append(str(num))

        if tmp_ret:
            ret = int("".join(tmp_ret))
        if is_neg: ret = -ret
        if ret < MIN_NUM or ret > MAX_NUM: return 0
        return ret

if __name__=="__main__":
    xs = [901000, 123, -123, 120, 2147483648, -2147483648]
    sol = Solution()
    
    for x in xs:
        print(sol.reverse(x))
