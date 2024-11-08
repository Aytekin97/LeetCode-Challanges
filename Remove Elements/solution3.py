class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        new=[i for i in nums if i !=val]
        nums[:]=new
        return len(nums)

obj = Solution()
print(obj.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))