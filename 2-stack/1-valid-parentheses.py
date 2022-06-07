class Solution:
    def isValid(self, s: str) -> bool:
        open_close_brackets = {"(":")", "{":"}", "[":"]"}
        stack = []
        for bracket in s:
            if bracket in open_close_brackets:
                stack.append(bracket)
            else:
                if stack:
                    if stack[-1] in open_close_brackets and open_close_brackets[stack[-1]] == bracket:
                        stack.pop()
                    else:
                        return False
                else:
                    stack.append(bracket)
        return not stack