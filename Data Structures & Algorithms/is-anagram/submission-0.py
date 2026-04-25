class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        m = {}

        for c in s:
            if c in m:
                m[c] += 1
            else:
                m[c] = 1
        
        for d in t:
            if d not in m:
                return False
            else:
                m[d] -= 1
                if m[d] == 0:
                    del m[d]
        return True