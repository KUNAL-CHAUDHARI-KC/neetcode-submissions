class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicts = {}

        for s in strs:
            sorted_s = "".join(sorted(s))

            if sorted_s in dicts:
                dicts[sorted_s].append(s)
            else:
                dicts[sorted_s] = [s]
        
        return list(dicts.values())
         