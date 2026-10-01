class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        n = len(heights)

        max_area = 0

        for i in range(len(heights)):
            if not stack:
                stack.append(i)
            
            elif heights[i] >= heights[stack[-1]]:
                stack.append(i)
            
            else:
                while stack and heights[i] < heights[stack[-1]]:
                    mid = stack.pop()

                    if stack:
                        left = stack[-1]
                    else:
                        left = -1

                    width = i - left - 1
                    area = heights[mid] * width

                    max_area = max(max_area, area)
                stack.append(i)
                    
        while stack:
            mid = stack.pop()
            if stack:
                left = stack[-1]
            else:
                left = -1

            width = n - left - 1
            area = heights[mid] * width

            max_area = max(max_area, area)

        return max_area

