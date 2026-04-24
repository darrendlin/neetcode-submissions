# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:

        if len(pairs) <= 1:
            return pairs

        pivot = pairs[-1]
        j = 0

        for i in range(len(pairs)-1):
            if pairs[i].key < pivot.key:
                tmp = pairs[i]
                pairs[i] = pairs[j]
                pairs[j] = tmp

                j += 1
        pairs[-1] = pairs[j]
        pairs[j] = pivot

        pairs[:j] = self.quickSort(pairs[:j])
        pairs[j+1:] = self.quickSort(pairs[j+1:])

        return pairs

