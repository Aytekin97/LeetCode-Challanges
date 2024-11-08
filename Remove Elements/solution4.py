class Solution(object):
    def removeElement(self, nums, val):
        print(nums)
        nums[:] = [x for x in nums if x != val]
        print(nums)
        return len(nums)

        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """