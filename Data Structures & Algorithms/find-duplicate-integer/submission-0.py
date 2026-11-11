class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]

            if slow == fast:
                slow = 0
                # slow = nums[slow]

                while fast != slow:
                    fast = nums[fast]
                    slow = nums[slow]
            
                return slow
            
            
            