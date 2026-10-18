class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        countS1 = {}
        countS2 = {}
        l = 0

        for s in s1:
            countS1[s] = 1 + countS1.get(s, 0)    

        for i in range(len(s1)):
                countS2[s2[i]] = 1 + countS2.get(s2[i], 0)

        if countS1 == countS2:
                return True

        for r in range(len(s1), len(s2)):
            countS2[s2[l]] -= 1

            if countS2[s2[l]] == 0:
                del countS2[s2[l]]
            l += 1

            countS2[s2[r]] = 1 + countS2.get(s2[r], 0)

            if countS1 == countS2:
                return True
        
        return False
        
        