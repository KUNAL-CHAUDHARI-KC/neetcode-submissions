class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dicts = {}

        for i in range(len(nums)):
            dicts[nums[i]] = 1 + dicts.get(nums[i], 0)
        
        sorted_dict = sorted(dicts.items(), key=lambda x:x[1], reverse=True)

        res = []
        for i in range(k):
            res.append(sorted_dict[i][0])
        
        return res
