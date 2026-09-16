class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for i in s:
            if i in ['(','{','[']:
                stack.append(i)
            else:
                if stack == []:
                    return False
                else:
                    top = stack[-1]

                    if (i == ')' and top != '(') or \
                    (i == '}' and top !='{') or \
                    (i == ']' and top != '['):
                        return False
                    else:
                        stack.pop()
                        
        return stack == []