class Solution:
    def isPalindrome(self, s: str) -> bool:
        l_offset = 0
        r_offset = 0

        while l_offset < len(s) - 1 - r_offset:
            left = s[l_offset].lower()
            while not left.isalnum():
                l_offset += 1
                if l_offset >= len(s):
                    return True
                left = s[l_offset].lower()
            right = s[len(s) - 1 - r_offset].lower()
            while not right.isalnum():
                r_offset += 1
                if len(s) - 1 - r_offset < 0:
                    return True
                right = s[len(s) - 1 - r_offset].lower()
            if left != right:
                return False
            l_offset += 1
            r_offset += 1
        return True