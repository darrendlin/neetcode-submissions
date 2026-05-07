class Solution:
    def trap(self, height: List[int]) -> int:
        left = [(0,0)] * len(height)
        right = [(0,0)] * len(height)
        water = 0

        cur_tallest = (height[0], 0)
        for i, h in enumerate(height):
            if h >= cur_tallest[0]:
                cur_tallest = (h,i)
            left[i] = cur_tallest
        cur_tallest = (height[-1], len(height)-1)
        for i in range(len(height)-1, -1, -1):
            h = height[i]
            if h >= cur_tallest[0]:
                cur_tallest = (h, i)
            right[i] = cur_tallest

        for i in range(len(height)):
            h = height[i]
            water += max(0, min(left[i][0], right[i][0]) - h)
            # if h < left[i][0] and h < right[i][0]:
            #     water += min(left[i][0], right[i][0]) * (right[i][1] - left[i][1] -1)
            #     print(water)

            #     for j in range(left[i][1] +1, right[i][1]):
            #         water -= height[j]
            #     i = right[i][1]
        return water
