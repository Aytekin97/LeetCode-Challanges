class Solution(object):
    def strStr(self, haystack, needle):
        for i in range(len(haystack)):
            print(haystack[i:i+len(needle)])
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1


"""
:type haystack: str
:type needle: str
:rtype: int
"""
obj = Solution()
print(obj.strStr("butsad", "sad"))    