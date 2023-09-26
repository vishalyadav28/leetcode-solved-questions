#worst
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        count = 0
        for i in range(len(A)):
            for j in range(i,len(A)):
                xorr=0
                for k in range(i,j+1):
                    xorr = xorr ^ A[k]
                if (xorr == B):
                    count+=1
        return count
#better

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)  # size of the given array.
        cnt = 0
        for i in range(n):
            xorr = 0
            for j in range(i, n):
                xorr = xorr ^ A[j]
                if (xorr == B):
                    cnt += 1

        return cnt
    
# optimal
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        from collections import defaultdict
        mpp = defaultdict(int)
        count = 0
        xr = 0
        mpp[xr] = 1
        for i in range(len(A)):
            xr = xr ^ A[i]
            x = xr ^ B
            count += mpp[x]
            mpp[xr]+=1
        return count
