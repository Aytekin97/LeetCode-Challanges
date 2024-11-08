# Doesn't work if the string is not ordered: {(}) is supposed to return False
class Solution(object):
    def isValid(self, s):
        total = 0
        list1 = 0
        list2 = 0
        list3 = 0
        for i in s:
            if i == "{":
                list1 = 1
            if i == "}":
                if list1 == 1:
                    list1 = 0
                    total += 1
                else:
                    return False
            if i == "[":
                list2 = 1
            if i == "]":
                if list2 == 1:
                    list2 = 0
                    total += 1
                else:
                    return False
            if i == "(":
                list3 = 1
            if i == ")":
                if list3 == 1:
                    list3 = 0
                    total += 1
                else:
                    return False
        if total == len(s)/2:
            return True
        return False

obj = Solution()
print(obj.isValid("{}[](){"))