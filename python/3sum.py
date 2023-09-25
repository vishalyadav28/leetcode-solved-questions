class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # n = len(nums)
        # temp = []
        # for i in range(n - 1):
 
        #     # Find all pairs with sum
        #     # equals to "-nums[i]"
        #     s = set()
        #     for j in range(i + 1, n):
        #         x = -(nums[i] + nums[j])
        #         if x in s:
        #             if sorted([x, nums[i], nums[j]]) in temp:
        #                 continue
        #             else:
        #                 temp.append(sorted([x, nums[i], nums[j]]))
        #         else:
        #             s.add(nums[j])
        # return temp

        nums.sort()
        ans = []
        n = len(nums)
        for i in range(n):
            if i>0 and nums[i] == nums[i-1]:
                continue
            j=i+1
            k=n-1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum < 0:
                    j+=1
                elif sum > 0:
                    k-=1
                else:
                    ans.append([nums[i],nums[j],nums[k]])
                    k-=1
                    j+=1
                    while j<k and nums[j] == nums[j-1]:
                        j+=1
                    while j<k and nums[k] == nums[k+1]:
                        k-=1
        return ans

                


        