class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:

            if char in mapping:

                top_element = stack.pop() if stack else '#'

                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack
        
        # sol 2
        
        # while "()" in s or "{}" in s or '[]' in s:
        #     s = s.replace("()", "").replace('{}', "").replace('[]', "")
        # return s == ''