class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""

        base = strs[0]
        for i in range(len(base)):
            for word in strs[1:]:
                if i == len(word) or word[i] != base[i]:
                    return base[0:i]

        return base
  

obj = Solution()
strs = ["flower","flower","flight"]
print(obj.longestCommonPrefix(strs))