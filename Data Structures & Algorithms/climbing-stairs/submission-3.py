class Solution:
    def __init__(self):
        self.m = {}
        
    def climbStairs(self, n: int) -> int:
        ret = 0
        if n in self.m:
            return self.m[n]

        if n <= 2:
            ret = n
        else:
            ret = self.climbStairs(n-1) + self.climbStairs(n-2)
        self.m[n] = ret

        return ret