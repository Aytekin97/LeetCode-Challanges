class Solution(object):
    def lengthOfLastWord(self, s):
        lengthOfWord = 0
        last = 0
        for i in s:
            if i != ' ':
                if last == 1:
                    lengthOfWord = 1
                    last -= 1
                else:
                    lengthOfWord += 1
            elif i == ' ':
                last = 1

        return lengthOfWord

"""
:type s: str
:rtype: int
"""
obj = Solution()
print(obj.lengthOfLastWord('   fly me   to   the moonss  s'))
        