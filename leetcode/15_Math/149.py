class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        # function to calculate the slope between two points
        def slope(p1, p2):
            if p1[0] == p2[0]:
                return 'inf'
            return (p1[1] - p2[1]) / (p1[0] - p2[0])

        slopes = collections.defaultdict(int) # key: slope, value: count

        max_count = 0 # max number of points on the same line
        for i in range(len(points)): 
            slopes.clear() # clear the slopes dict for each point
            same_points = 1 # number of points that are the same as the current point
            for j in range(i+1, len(points)): # loop through the rest of the points, use i+1 to avoid duplicate
                if points[i] == points[j]: # if the points are the same, increment same_points
                    same_points += 1
                else: # if the points are not the same, calculate the slope and increment the count
                    s = slope(points[i], points[j])
                    slopes[s] += 1
            max_count = max(max_count, same_points + max(slopes.values(), default=0)) # update max_count as the max of the current max_count and the current point's same_points + the max number of points on the same line. If slopes is empty, use 0 as the default value for max() function

        return max_count

