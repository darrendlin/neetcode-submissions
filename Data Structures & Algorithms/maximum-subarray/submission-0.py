class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_max = nums[0]
        cur_sum = 0

        for num in nums:
            cur_sum += num
            cur_max = max(cur_max, cur_sum)

            if cur_sum < 0:
                cur_sum = 0

        return cur_max