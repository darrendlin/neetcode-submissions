class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        max_seq = 0

        for num in nums:

            if num-1 not in s:
                # start of sequence
                seq = 0
                while num in s:
                    seq += 1
                    max_seq = max(max_seq, seq)
                    num += 1
        return max_seq 