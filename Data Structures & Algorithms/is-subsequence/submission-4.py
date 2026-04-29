class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0
        for i in range(len(s)):
            #print("checking", i, s[i])
            if len(t)-j < len(s) -i:
                return False
            while t[j] != s[i]:
                j += 1
                if j > len(t)-1:
                    return False
            j += 1
        return True