possible = ["+", "-", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
INTMAX = 2**31-1
INTMIN = -2**31

class Solution:
    def myAtoi(self, input_str):
        pad_str = input_str.strip()
        if pad_str =="":return 0
        negative = False
        if pad_str[0] not in possible:
            return 0

        if pad_str[0] in ["-","+"]:
            if pad_str[0] == "-": negative = True
            pad_str = pad_str[1:]

        if not pad_str or pad_str[0] in ["-","+"]:
            return 0

        num = 0
        for one_str in pad_str:
            if one_str not in ["1","2","3","4","5","6","7","8","9","0"]:
                break
            num *= 10
            num += int(one_str)

        if negative: num = -num
        if num > INTMAX: num = INTMAX
        if num < INTMIN: num = INTMIN
        return num

if __name__=="__main__":
    sol = Solution()
    test_inputs = ["0-1", "42", "-42", "4193", "words and 987", "-91283472332"]
    for test_input in test_inputs:
        print(sol.myAtoi(test_input))
