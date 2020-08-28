class Solution:
    def isOneBitCharacter(self, bits) -> bool:
        idx = 0
        while idx <= len(bits) - 1:
            if idx == len(bits) - 1:
                if not bits[idx]:
                    return True

            if bits[idx]:
                idx += 2
            else:
                idx += 1

        return False


if __name__ == "__main__":
    s = Solution()
    print(s.isOneBitCharacter([1, 1, 0]))
