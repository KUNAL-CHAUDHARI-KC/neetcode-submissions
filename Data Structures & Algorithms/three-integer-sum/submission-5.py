class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        nums.sort()
        res = []

        f = 0

        while f < len(nums):

            if f != 0 and nums[f] == nums[f-1]:
                f += 1
                continue

            l = f+1
            r = len(nums)-1

            while l < r:
                threeSum = nums[f] + nums[l] + nums[r]

                if threeSum < 0:
                    l += 1
                
                elif threeSum > 0:
                    r -= 1

                else:
                    res.append([nums[f], nums[l], nums[r]])
                    
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
            f += 1
        
        return res

                   
                    
