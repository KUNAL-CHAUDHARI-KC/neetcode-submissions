class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicts = {}

        for strg in strs:
            sorted_strs = "".join(sorted(strg))

            if sorted_strs in dicts:
                dicts[sorted_strs].append(strg)
            else:
                dicts[sorted_strs] = [strg]
            
        return list(dicts.values())