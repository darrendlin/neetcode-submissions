import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        {num_letters: {sum, [words]}}
        """

        m = collections.defaultdict(lambda: collections.defaultdict(list))

        for s in strs:
            length = len(s)
            hash_sum = tuple(sorted(s))

            m[length][hash_sum].append(s)
        
        out = []
        for i in m:
            for j in m[i]:
                out.append(m[i][j])
        return out
