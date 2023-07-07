class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # solution 1

        # if needle in haystack:
        #     return haystack.index(needle)
        # else:
        #     return -1


        # solution 2

        if needle == "":
            return 0
        haystack_length = len(haystack)
        needle_length = len(needle)
        for i in range(haystack_length - needle_length + 1):
            substring = haystack[i:i+needle_length]
            if substring == needle:
                return i
        return -1


        
