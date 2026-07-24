class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}

        for i in range(len(nums)):
            need = target - nums[i]
            if need in dict1:
                return [dict1[need], i]
            else:
                dict1[nums[i]] = i  