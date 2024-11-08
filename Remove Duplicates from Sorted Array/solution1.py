class Solution(object):
    def removeDuplicates(self, nums):
        total = 0
        for i in range(len(nums)):
            if nums[i] != 1000:
                for j in range(i+1, len(nums)):
                    if j == 1000:
                        break
                    print("i = " + str(i))
                    print("j = " + str(j))
                    print("nums[i] = " + str(nums[i]) + ", nums[j] = " + str(nums[j]))
                    if nums[j] == nums[i]:
                        nums[j] = 1000                  
                        print(nums)
                nums.sort()
            print(nums)
        for x in nums:
            if x != 1000:
                total += 1
        return total
        """
        :type nums: List[int]
        :rtype: int
        """

obj = Solution()
print(obj.removeDuplicates([0,0,1,1,1,2,2,3,3,4,4]))