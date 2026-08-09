class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l = 0
        r = len(heights)-1

        max_water = 0

        while l < r:
            # height = 0
            # widht = 0
            # curr_area = 0

            height = min(heights[l], heights[r]) 

            width = r - l

            curr_area = height * width

            max_water = max(max_water, curr_area) 

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            
        return max_water


        