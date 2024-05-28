class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:

        #Cause TLE

        # def check_even_odd(i):
        #     return "even" if nums[i]%2==0 else "odd"
        # self.last = ""
        # def check_range(start,end):
        #     self.last = ""
        #     for i in range(start,end+1):
        #         new_output = check_even_odd(i)
        #         if self.last != new_output:
        #             self.last = new_output
        #         else:
        #             return False
        #     return True
        # result = [check_range(i[0],i[1]) for i in queries]
        # return result

        # Optimized
        n=len(nums)
        parity = [0] * (n-1)

        for i in range(n-1):
            parity[i] = (nums[i]%2 != nums[i+1]%2)
        prefix_sum = [0] * n
        for i in range(n-1):
            prefix_sum[i+1] = prefix_sum[i] + (1 if not parity[i] else 0)
        
        result = []
        for fromi, toi in queries:
            if fromi == toi:
                result.append(True)
            else:
                is_special = (prefix_sum[toi] - prefix_sum[fromi]  ==0)
                result.append(is_special)
        return result

        


        
