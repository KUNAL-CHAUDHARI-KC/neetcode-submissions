class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_str = ""

        for stg in strs:
            encoded_str += str(len(stg)) + "#" + stg
        
        return encoded_str

    def decode(self, s: str) -> List[str]:

        decoded_str = []

        i = 0
        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            leng = int(s[i:j])

            decoded_str.append(s[j+1: j+1+leng])

            i = j+1+leng
        
        return decoded_str




