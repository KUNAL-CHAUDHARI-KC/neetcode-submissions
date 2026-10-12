class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""

        for st in strs:
            encoded_str += str(len(st)) + "#" + st
        
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_str = []

        i = 0
        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1
                
            leng = int(s[i:j])

            decoded_str.append(s[j+1:j+leng+1])
        
            i = j+leng+1
        
        return decoded_str










