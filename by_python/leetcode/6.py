#!/usr/bin/python3
"""
6. zigzag conversion
https://leetcode.com/problems/zigzag-conversion/
"""

class Solution:
    def convert(self, s: str, numRow: int) -> str:
        if numRow == 1: return s

        bottom = 2 * (numRow - 1)
        up = 0
        start = 0
        ret_str = ""

        while bottom >= 0:
            pos = start

            is_bottom = True

            while pos < len(s):
                if is_bottom and bottom == 0:
                    is_bottom = not is_bottom
                    continue
                elif not is_bottom and up == 0:
                    is_bottom = not is_bottom
                    continue
            
                ret_str += s[pos]
                if is_bottom:
                    pos+=bottom
                else:
                    pos+=up
                is_bottom = not is_bottom
            bottom -= 2
            up += 2
            start+=1 
        return ret_str

if __name__=="__main__":
    inputs = ["PAYPALISHIRING"]
    numRows = [1, 3, 4]

    case = 1
    sol = Solution()
    for tmp_input in inputs:
        for numRow in numRows:
            print("case {}: {}".format(case, sol.convert(tmp_input, numRow)))
            case+=1
