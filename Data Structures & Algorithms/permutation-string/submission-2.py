class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        dicts1 = {}
        dicts2 = {}

        l = 0 

        for d in range(len(s1)):
            dicts1[s1[d]] = 1 + dicts1.get(s1[d], 0)

        for r in range(len(s2)):
            dicts2[s2[r]] = 1 + dicts2.get(s2[r], 0)

            if len(s1) == (r - l + 1): 
                if dicts1 == dicts2:
                    return True
                
                else:
                    dicts2[s2[l]] -= 1

                    if dicts2[s2[l]] == 0:
                         dicts2.pop(s2[l], None)
                    l += 1
        
        return False

