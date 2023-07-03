#Solution #1
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        if x<0:
            return False
        else:
            return x==int(str(x)[::-1])
        
#Solution #2
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        sum=0
        i=x
        if x<0:
            return False
        while x>0:
            sum=(sum*10)+x%10
            x=x//10
        return sum==i