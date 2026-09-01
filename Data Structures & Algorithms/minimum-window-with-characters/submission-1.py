class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        dict_s = {}
        dict_t = {}

        ans = ""

        l = 0

        for i in range(len(t)):
            dict_t[t[i]] = 1 + dict_t.get(t[i], 0)

        formed = 0
        for r in range(len(s)):
            if s[r] in dict_t:
                dict_s[s[r]] = 1 + dict_s.get(s[r], 0)
                
                if dict_s[s[r]] == dict_t[s[r]]:
                    formed += 1
                
                while formed == len(dict_t):
                    if ans == "":
                        ans  = s[l:r+1]
                    elif (r - l + 1) < len(ans):
                        ans = s[l:r+1]
                    
                    if s[l] in dict_t:
                        dict_s[s[l]] -= 1

                        if dict_s[s[l]] < dict_t[s[l]]:
                            formed -= 1

                        if dict_s[s[l]] == 0:
                            dict_s.pop(s[l], None)

                    l += 1
        return ans


