class Solution:
    def trap(self, height: List[int]) -> int:

        l = 0 
        r = len(height) - 1

        water = 0

        left_max = 0
        right_max = 0

        while l < r:

            if height[l] < height[r]:
                
                if left_max <= height[l]:
                    left_max = height[l]
                else:
                    water += left_max - height[l]

                l += 1

            else:
                if right_max <= height[r]:
                    right_max = height[r]
                else:
                    water += right_max - height[r]
                r -= 1

        return water
          
            

            
        