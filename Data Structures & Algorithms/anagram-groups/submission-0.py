class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = {}

        for st in strs:
            key = "". join(sorted(st))
            if key in dict1:
                dict1[key].append(st)
            else:
                dict1[key] = [st]

        return list(dict1.values())