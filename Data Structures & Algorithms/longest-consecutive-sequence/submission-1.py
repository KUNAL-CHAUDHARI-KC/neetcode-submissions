class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num_set = set(nums)

        length = 0

        for num in nums:
            curr_len = 1

            if num-1 not in num_set:
                start = num
                
                while start+1 in num_set:
                    start = start+1
                    curr_len += 1

                length = max(length, curr_len)
        
        return length
        