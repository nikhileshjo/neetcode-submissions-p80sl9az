class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_dict = { '(':')', '{':'}', '[':']'}

        for b in s:
            if b in bracket_dict:
                stack.append(b)
            else:
                if stack:
                    if bracket_dict[stack.pop()] != b:
                        return False
                else:
                    return False
        if stack:
            return False
        return True