# 66. Plus One 
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits_len=len(digits)
        
        for i in range(digits_len-1,-1,-1):
            #1,2,3 convert 3 -> 4
            digits[i]+=1
            if digits[i]<10:
                return digits
            else:
                #99 case
                digits[i]=0
        digits.insert(0,1)
        return digits