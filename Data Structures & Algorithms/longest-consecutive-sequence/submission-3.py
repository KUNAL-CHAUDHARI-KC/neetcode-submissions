class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        sett = set(nums)

        for i in range(len(nums)):
            if nums[i]-1 not in sett:
                start = nums[i]

                curr_len = 1

                while start+1 in sett:
                    start = start+1
                    curr_len += 1
                
                res = max(res, curr_len)
        
        return res


        