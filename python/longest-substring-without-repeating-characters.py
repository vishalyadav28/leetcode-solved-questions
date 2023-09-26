class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # longest = 0

        # def linearSearch(sub, char):
        #     return char in sub

        # for i in range(len(s)):
        #     sub = s[i]
        #     count = 1
        #     for j in range(i+1,len(s)):
        #         if not linearSearch(sub, s[j]):
        #             count += 1
        #             sub += s[j]
        #         else:
        #             break
        #     longest = max(longest, count)

        # return(longest)

        char_indices = {}
        max_length = 0
        start = 0
        for i,char in enumerate(s):
            if char in char_indices and char_indices[char] >= start:
                start = char_indices[char]+1
            char_indices[char] = i
            max_length = max(max_length,i-start+1)
        return max_length

        