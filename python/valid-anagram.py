class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # #brute
        # def get_object(s:str)->dict:
        #     dict = {}
        #     for w in (s):
        #         if w in dict:
        #             dict[w] += 1
        #         else:
        #             dict[w] = 1
        #     return dict
        # dic1 = get_object(s)         
        # # dic2 = get_object(t)

        # #instead of this 

        # # if dic1==dic2:
        # #     return True
        # # else:
        # #     False 
        # ls=[]
        # for i in t:
        #     if i not in dic1:
        #         return False
        #     else:
        #         if dic1[i] > 0:
        #             dic1[i]-=1
        #             ls.append(i)
        # if len(ls) != len(s):
        #     return False
        # elif len(s) != len(t):
        #     return False
        # else:
        #     return True

        #or do sorting merge sort and then compare them 
        def merge_sort(s):
            if len(s) <= 1:
                return s
            
            # Split the string into two halves
            mid = len(s) // 2
            left = s[:mid]
            right = s[mid:]
            
            # Recursively apply merge sort on each half
            left = merge_sort(left)
            right = merge_sort(right)
            
            # Merge the sorted halves
            return merge(left, right)

        def merge(left, right):
            result = []
            i = j = 0
            
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            
            result.extend(left[i:])
            result.extend(right[j:])
            return ''.join(result)
        s1 = merge_sort(s)
        t1 = merge_sort(t)
        if s1==t1:
            return True
        else:
            return False


        


        

        