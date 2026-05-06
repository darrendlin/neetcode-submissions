class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        import collections
        freq = collections.defaultdict(lambda: 0)
        max_freq, l, res = 0, 0, 0

        for i in range(len(s)):
            freq[s[i]] += 1
            for key in freq.keys():
                max_freq = max(max_freq, freq[key])

            while i - l - max_freq +1 > k:
                freq[s[l]] -= 1
                l += 1
                for key in freq.keys():
                    max_freq = max(max_freq, freq[key])
            
            res = max(res, i - l + 1)
        return res