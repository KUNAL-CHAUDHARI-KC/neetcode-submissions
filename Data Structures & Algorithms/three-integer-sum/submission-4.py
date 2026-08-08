class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        f = 0

        ans = []


        while f < len(nums)-2:

            if f != 0:
                if nums[f] == nums[f-1]:
                    f += 1
                    continue
           
            l = f+1
            r = len(nums)-1


            while l < r:
            
                three_sum = nums[f] + nums[l] + nums[r]

                if three_sum == 0:
                    ans.append([nums[f], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l-1]:
                        l += 1

                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                    continue
                
                elif three_sum <  0:
                    l += 1
                    
                else:
                    r -= 1

            f += 1

        return ans
            