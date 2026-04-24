class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        max_v = 0
        
        while right > left:
            v = min(heights[right], heights[left]) * (right-left)
            max_v = max(max_v, v)

            if heights[right] > heights[left]:
                left += 1
            else:
                right -= 1

        return max_v