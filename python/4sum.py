class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        #Bruteforce

        # s = set()
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         for k in range(j+1,len(nums)):
        #             for l in range(k+1,len(nums)):
        #                 if nums[i] + nums[j]+ nums[k]+ nums[l] == target:
        #                     temp = [nums[i], nums[j], nums[k], nums[l]]
        #                     temp.sort()
        #                     s.add(tuple(temp))
        # result = [i for i in s]
        # return result

        #Better

        # sf = set()
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         s = set()
        #         for k in range(j+1,len(nums)):
        #             fourth = target-(nums[i] + nums[j]+ nums[k])
        #             if fourth in s:
        #                 temp = [nums[i], nums[j], nums[k], fourth]
        #                 temp.sort()
        #                 sf.add(tuple(temp))
        #             else:
        #                 s.add(nums[k])

        # result = [i for i in sf]
        # return result

        #Best
        nums.sort()
        temp = []
        n = len(nums)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i + 1, n):
                # avoid the duplicates while moving j:
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                k=j+1
                l=len(nums)-1
                while k<l:
                    sum = nums[i] + nums[j] +nums[k] +nums[l]
                    if sum == target:
                        temp.append([nums[i] , nums[j] ,nums[k] ,nums[l]])
                        k+=1
                        l-=1
                        while k<l and nums[k] == nums[k-1]:
                            k+=1
                        while k<l and nums[l] == nums[l+1]:
                            l-=1
                    elif sum < target:
                        k+=1
                    else:
                        l-=1
                        
                    



        return temp        