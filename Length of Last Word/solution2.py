class Solution(object):
    def lengthOfLastWord(self, s):
        here = s.split()
        return len(here[-1])
    
"""
:type s: str
:rtype: int
"""
obj = Solution()
print(obj.lengthOfLastWord('   fly me   to   the moon  '))