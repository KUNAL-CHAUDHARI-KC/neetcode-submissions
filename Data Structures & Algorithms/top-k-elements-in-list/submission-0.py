class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frq = {}

        for num in nums:
            if num in frq:
                frq[num] += 1
            else:
                frq[num] = 1
        
        sorted_item = sorted(frq.items(), key=lambda x:x[1], reverse=True)

        result = []
        for i in range(k):
            result.append(sorted_item[i][0])
        
        return result 