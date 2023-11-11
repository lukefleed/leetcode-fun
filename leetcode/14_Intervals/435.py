class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1]) # sort by end time

        count = 0
        end = intervals[0][1] # end time of the first interval
        for i in range(1, len(intervals)):
            if intervals[i][0] < end: # if the start time of the current interval is less than the end time of the previous interval
                count += 1 # then we need to remove the current interval because it overlaps with the previous interval
            else:
                end = intervals[i][1] # otherwise, we update the end time of the previous interval to the end time of the current interval because we are not removing the current interval
        return count

