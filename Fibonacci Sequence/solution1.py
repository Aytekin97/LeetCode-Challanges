class Solution(object):
    def fibonacci(self, x):
        if x < 2:
            return x
        return self.fibonacci(x-1) + self.fibonacci(x-2)
obj = Solution()
print(obj.fibonacci(11))
