import math

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        list1Num = 0
        list2Num = 0
        for i in range(len(l1)):
            list1Num += l1[i]*(10**i)
        for j in range(len(l2)):
            list2Num += l2[j]*(10**j)
        print(list1Num)
        print(list2Num)
        resultList = []
        resultNum = list1Num+list2Num
        while resultNum > 9:
            instance = resultNum%10
            resultList.append(instance)
            resultNum = math.floor(resultNum/10)
        resultList.append(resultNum)
        return resultList

obj = Solution()  
l1 = [5,2,3]
l2 = [3,2,8]
print(obj.addTwoNumbers(l1, l2))
"""
:type l1: ListNode
:type l2: ListNode
:rtype: ListNode
"""