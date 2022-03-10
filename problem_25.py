class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket_char in s:
            if bracket_char == ')':
                if len(stack) == 0 or stack.pop() != '(':
                    return False
            elif bracket_char == ']':
                if len(stack) == 0 or stack.pop() != '[':
                    return False
            elif bracket_char == '}':
                if len(stack) == 0 or stack.pop() != '{':
                    return False
            else:
                stack.append(bracket_char)

        if len(stack) == 0:
            return True
        else:
            return False
