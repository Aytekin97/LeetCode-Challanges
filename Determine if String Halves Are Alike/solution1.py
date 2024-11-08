class Solution(object):
    def halvesAreAlike(self, s):
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        half1 = 0
        half2 = 0
        for i in range(len(s)):
            if i <= (len(s)/2)-1:
                if s[i] in vowels:
                    half1 += 1
            else:
                if s[i] in vowels:
                    half2 += 1
        return half1 == half2
"""
:type s: str
:rtype: bool
"""
obj = Solution()
print(obj.halvesAreAlike('boolas')) 