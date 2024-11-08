class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        xVals = []
        maxDistance = 0
        for i in range(len(points)):
            xVals.append(points[i][0])
        xVals.sort()
        for i in range(len(xVals)):
            if i != len(xVals)-1:
                distance = xVals[i+1]-xVals[i]
            if distance >= maxDistance:
                maxDistance = distance
        return maxDistance
        """
        :type points: List[List[int]]
        :rtype: int
        """
obj = Solution()
points = [[3,2], [9,4], [2,6], [1,8]]
print(obj.maxWidthOfVerticalArea(points))