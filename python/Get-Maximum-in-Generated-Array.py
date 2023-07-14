# 1646. class Solution:

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        tb=[0,1]
        if n==0:
            return 0
        for i in range(2,n+1):
            if i%2==0:
                tb.append(tb[i//2])
            else:
                tb.append(tb[i//2]+tb[(i//2)+1])
        return max(tb)