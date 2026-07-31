class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(t) != len(s):
            return False

        dict1 = {}

        for str1 in s:
            if str1 in dict1:
                dict1[str1] += 1
            else:
                dict1[str1] = 1

        for str1 in t:
            if str1 in dict1:
                dict1[str1] -= 1
            else:
                return False
        
        for val in dict1.values():
            if val != 0:
                return False
        
        return True
        


        # if len(s) != len(t):
        #    return False 

        # visited = [False]* len(t)


        # for i in range(len(s)):
        #     found = False
        #     for j in range(len(t)):
        #         if s[i] == t[j] and not visited[j]:
        #             visited[j] = True
        #             found = True
        #             break
                
        #     if found is False:
        #         return False

        # return True      