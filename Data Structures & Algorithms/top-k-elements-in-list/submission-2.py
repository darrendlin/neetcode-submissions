import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = collections.defaultdict(lambda: 0)
        for num in nums:
            m[num] += 1
        
        freq = collections.defaultdict(list)
        for i in m:
            freq[m[i]].append(i)
        
        sorted_freqs = sorted(freq.keys())
        print(sorted_freqs)
        out = []
        for i in range(len(sorted_freqs) - 1, -1, -1):
            for val in freq[sorted_freqs[i]]:
                out.append(val)
                if len(out) == k:
                    return out
        return out