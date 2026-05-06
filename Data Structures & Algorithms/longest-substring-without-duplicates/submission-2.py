class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, longest = 0, 0
        substr = {}
        for i in range(len(s)):
            if s[i] not in substr or substr[s[i]] < l:
                substr[s[i]] = i
                longest = max(longest, i-l+1)
            else:
                l = max(l, substr[s[i]]+1)
                substr[s[i]] = i
        return longest