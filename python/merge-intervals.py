class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # result = []
        # for i in range(len(intervals)):
        #     start = intervals[i][0]
        #     end = intervals[i][1]
            # if result and end <= result[-1][1]:
            #     continue
        #     for j in range(i+1,len(intervals)):
        #         if intervals[j][0] <= end:
        #             end = max(intervals[j][1],end)
        #         else:
        #             break
        #     result.append([start,end])
        # return result
        result = []
        intervals.sort()
        for i in range(len(intervals)):
            if not result or result[-1][1] < intervals[i][0]:
                result.append(intervals[i])
            else:
                result[-1][1] = max(intervals[i][1],result[-1][1])
        return result
            

                
        