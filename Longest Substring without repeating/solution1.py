class Solution(object):

    def lengthOfLongestSubstring(self, s):
        left = 0
        seen = {}
        length = 0

        for right in range(len(s)-1):
            char = s[right]
            if char in seen and seen[char] >= left:
                left = seen[char]+1
            else:
                length = max(length, right - left + 1)
            seen[char] = right

        return length
    
obj = Solution()
print(obj.lengthOfLongestSubstring("abcabcbb"))