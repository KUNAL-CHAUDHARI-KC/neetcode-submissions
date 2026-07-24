class Solution:
    def encode(self, strs: List[str]) -> str:
        result = ""
        for str1 in strs:
            length = str(len(str1))
            result += length
            result += "#" 
            result += str1

        return result

    def decode(self, s: str) -> List[str]:
        answer = []
        i = 0

        while i < len(s):
            length = ""
            while s[i] != "#":
                length += s[i]
                i += 1
            
            length = int(length)
            i+=1
            answer.append(s[i:i+length])
            i+=length
        
        return answer
