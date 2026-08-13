class Solution:
    def twoSum(self, num: List[int], target: int) -> List[int]:

        l = 0
        r = len(num)-1

        while l < r:

            curr_sum = num[l] + num[r]

            if curr_sum > target: 
                r -= 1
            
            elif curr_sum < target:
                l += 1
            
            else:
                return [l+1, r+1]
        
        # return []
            
        

        