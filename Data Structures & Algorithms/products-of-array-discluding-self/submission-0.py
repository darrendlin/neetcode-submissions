class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        prefix[0] = nums[0]
        postfix[-1] = nums[-1]
        out = [1] * len(nums)
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i]
            postfix[-i-1] = postfix[-i] * nums[-i-1]
        out[0] = postfix[1]
        out[-1] = prefix[-2]
        for i in range(1, len(nums)-1):
            out[i] = prefix[i-1] * postfix[i+1]
        return out