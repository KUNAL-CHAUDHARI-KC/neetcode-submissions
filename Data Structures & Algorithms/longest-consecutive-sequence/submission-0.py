class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set1 = set(nums)

        longest = 0

        for x in nums:
            length = 1
            if x-1 not in set1:
                start = x
                while start + 1 in set1:
                    length += 1
                    start += 1
                
                longest = max(longest, length)
        
        return longest

          
