class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left = [1]
        right = [1]*len(nums)
        ans = [1]*len(nums)

        for i in range(1, len(nums)):
            left.append(left[i-1] * nums[i-1])
        
        for j in range(len(nums)-2, -1, -1):
            right[j] = right[j+1] * nums[j+1]

        for k in range(len(nums)):
            ans[k] *= left[k] * right[k]

        return ans
        