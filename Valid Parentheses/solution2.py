#This doesn't work either. "{[]}" is supposed to be True, but it comes False
class Solution(object):
    def isValid(self, s):
        matches = {"(":")",
                   "[":"]",
                   "{":"}"}
        total = 0
        for i in range(0, len(s), 2):
            print("i is: "+str(i))
            print("string " + str(i) + " is " +s[i])

            for j in range(2):
                if i+j < len(s):
                    print("j is: "+str(i+j))
                    print("jstring " + str(i+j) + " is " +s[i+j])
                    if s[i] == s[i+j]:
                        print("Next")
                        continue
                    if matches[s[i]] == s[i+j]:
                        print("Match")
                        total += 1
                    else:
                        return False

        if total == len(s)/2:
            return True
        return False

obj = Solution()
print(obj.isValid("([)]"))