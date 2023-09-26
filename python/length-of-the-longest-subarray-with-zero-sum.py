#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        #Code here
        
        #bruteforce and TLE issue
        
        
        # max_len = 0
        # if len(arr) == 1:
        #     return len(arr)
        # for i in range(len(arr)):
        #     sum=0
        #     for j in range(i,len(arr)):
        #         sum +=arr[j]
        #         if sum == 0:
        #             temp_len = (j-i)+1
        #             max_len = max(temp_len,max_len)
        # return max_len
                    
        #better
        sum=0
        mpp={}
        maxi = 0
        for i in range(n):
            sum+=arr[i]
            if sum == 0:
                maxi = i + 1
            else:
                if sum in mpp:
                    maxi = max(maxi,i-mpp[sum])
                else:
                    mpp[sum] = i
        return maxi
            
                
            


#{ 
 # Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends