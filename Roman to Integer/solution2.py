class Solution(object):
    def romanToInt(self, s):
        charList = list(s)  
        translation = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        index = len(charList) - 1
        total = 0
        print("First Total: " + str(total))
        print("First Index: " + str(index))

        for i in range(len(charList)):
            if translation[charList[len(charList) - i - 1]] < translation[charList[index]]:
                total -= translation[charList[len(charList) - i - 1]]
                print(total)
            if translation[charList[len(charList) - i - 1]] == translation[charList[index]]:
                total += translation[charList[len(charList) - i - 1]]
            if translation[charList[len(charList) - i - 1]] > translation[charList[index]]:
                total += translation[charList[len(charList) - i - 1]]
                index = len(charList) - i - 1
        
        return total

obj = Solution()
print(obj.romanToInt("MCMXCIV"))