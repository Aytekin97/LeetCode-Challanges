class Solution(object):
    def removeElement(self, nums, val):
        total = 0
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = 1000            
            print(nums)
        nums.sort()
        print(nums)
        for num in nums:
            if num != 1000:
                total += 1
        print("Total is = " + str(total))
        return total
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
obj = Solution()
print(obj.removeElement([0,1,2,2,3,0,4,2], 2))