class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        i = 0
        pre = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i > len(s)-1:
                    return pre
                if s[i] != strs[0][i]:
                    return pre
            pre += strs[0][i]
            i += 1
        return pre