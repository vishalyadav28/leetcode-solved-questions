class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        # s_len = len(s)
        # count=0
        # for i in range(1,s_len+1):
        #     for j in words:
        #         if s[:i] == j:
        #             count+=1
        # return count
        count = 0
        for word in words:
            w_len = len(word)
            if s[:w_len] == word:
                count+=1
        return count
        