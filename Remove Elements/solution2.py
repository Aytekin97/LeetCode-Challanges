class Solution(object):
    def removeElement(self, nums, val):
        i = 0
        for x in nums:
            if x != val:
                nums[i] = x
                i += 1
            print(nums)
        return i

obj = Solution()
print(obj.removeElement([0,1,2,2,3,0,4,2], 2))