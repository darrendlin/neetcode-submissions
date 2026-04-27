class Solution:
    def reverse(self, x: int) -> int:
        
        rev = 0
        neg = x < 0
        minint = -2**31
        maxint = 2**31-1

        while x:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)
            
            if maxint//10 < rev or (maxint//10 == rev and digit >= maxint%10):
                return 0
            if minint//10 > rev or (minint//10 == rev and digit <= minint%10):
                return 0
            rev = rev * 10 + digit

        return rev