class Solution:

    def encode(self, strs: List[str]) -> str:

        response = ""

        for st in strs:
            response += str(len(st))+"#"+st

        return response 

    def decode(self, s: str) -> List[str]:

        ans = []

        i = 0
        while i < len(s):

            j = i
            while s[j] != "#":
                j += 1
                
            leng = int(s[i:j])

            ans.append(s[j+1:j+1+leng])

            i = j+1+leng
        
        return ans


