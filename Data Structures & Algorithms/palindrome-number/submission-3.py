class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        num = 0
        i = x
        while i > 0:
            remainder = i % 10
            i = i // 10
            num = num * 10 + remainder
        return num == x
