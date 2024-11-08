import math

class Solution(object):
    def isPalindrome(self, x):
        numList = []
        indexCheck = 0
        if x >= 0 and x <= 9:
            return True
        elif x >= -9 and x < 0:
            return False
        elif x > 0:
            while x >= 10:
                numList.append(x%10)
                x = math.floor(x/10)
            numList.append(x)
        elif x < 0:
            while x <= -10:
                numList.append(x%10)
                x /= 10
            numList.append(x)
        for i in range(int(math.ceil(len(numList)/2))):
            if numList[i] == numList[len(numList)-i-1]:
                indexCheck+=1
            else:
                return False
        return True 

palinrdome_number = 112211
non_palindrome_number = 112315

obj = Solution()
print(obj.isPalindrome(palinrdome_number))
print(obj.isPalindrome(non_palindrome_number))
print(obj.isPalindrome(-3))
print(obj.isPalindrome(6))
print(obj.isPalindrome(0))