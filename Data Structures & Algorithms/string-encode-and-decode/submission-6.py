class Solution:

    def encode(self, strs: List[str]) -> str:
        
        encode_str = ""

        for st in strs:
            encode_str += (str(len(st))+"#"+st)

        return encode_str


    def decode(self, s: str) -> List[str]:
        ans = []

        i = 0
        while i < len(s):
             
             j=i
             while s[j] != "#":
                j += 1

             sub_str = s[i:j]
             leng = int(sub_str)

             ans.append(s[j+1:j+leng+1])

             i = j+leng+1

        
        return ans

