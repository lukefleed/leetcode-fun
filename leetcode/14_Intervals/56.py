class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0]) # sort by start time
        res = []
        for i in intervals:
            if res and res[-1][1] >= i[0]: # if there is overlap, merge
                res[-1][1] = max(res[-1][1], i[1]) # update end time
            else:
                res.append(i) # no overlap, add new interval
        return res
