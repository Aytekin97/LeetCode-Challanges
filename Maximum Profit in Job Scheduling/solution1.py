class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        left = 0
        right = 0
        maxProfit = 0
        profitList = []
        length = len(startTime)
        for i in range(length):
            left = startTime[i]
            right = endTime[i]
            maxProfit += profit[i]
            for j in range[i+1 : length]:
                if startTime[j] <= right:
                    maxProfit += profit[j]
                    left = right



"""
:type startTime: List[int]
:type endTime: List[int]
:type profit: List[int]
:rtype: int
"""
startTime = [1,2,3,3]
endTime = [3,4,5,6]
profit = [50,10,40,70]
obj = Solution()
print(obj.jobScheduling(startTime, endTime, profit))