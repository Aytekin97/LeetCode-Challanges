class Solution(object):
    def strongPasswordChecker(self, password):
        lowerCase = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
        upperCase = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
        ints = '0123456789'
        lowerCount = 0
        upperCount = 0
        intCount = 0
        repeatCount = 0
        repeatError = 0
        correctionSteps = 0
        if len(password) > 20:
            correctionSteps += len(password)-20
        for i in range(len(password)):
            if i == 0:
                repeatCount = 1
            if lowerCount == 0:
                if password[i] in lowerCase:                   
                    lowerCount = 1
                    print('lower: ' + str(lowerCount))
            if intCount == 0:
                if password[i] in ints:
                    intCount = 1
                    print('int: ' + str(intCount))
            if upperCount == 0:
                if password[i] in upperCase:
                    upperCount = 1
                    print("upper: "+str(upperCount))
            if i != 0:
                if password[i] == password[i-1]:
                    repeatCount += 1
                    print('iteration: ' + str(i) + ' ,correctionSteps: ' + str(correctionSteps) + ', repetationError: ' + str(repeatError) + ', repatationCount: ' + str(repeatCount))
                elif repeatCount != 0 and password[i] != password[i-1]:
                    repeatCount = 1
                    print('iteration: ' + str(i) + ' ,correctionSteps: ' + str(correctionSteps) + ', repetationError: ' + str(repeatError) + ', repatationCount: ' + str(repeatCount))
                if repeatCount == 3:
                    repeatError += 1
                    repeatCount = 1
                    print('iteration: ' + str(i) + ' ,correctionSteps: ' + str(correctionSteps) + ', repetationError: ' + str(repeatError) + ', repatationCount: ' + str(repeatCount))
        if lowerCount == 0:
            correctionSteps += 1
        if upperCount == 0:
            correctionSteps += 1
        if intCount == 0:
            correctionSteps += 1
        if repeatError != 0 and lowerCount == 0:
            repeatError -= 1
        if repeatError != 0 and upperCount == 0:
            repeatError -= 1
        if repeatError != 0 and intCount == 0:
            repeatError -= 1
        correctionSteps += repeatError
        x = len(password)+correctionSteps
        if x < 6:
            correctionSteps += 6-x
        return correctionSteps


"""
:type password: str
:rtype: int
"""       
obj = Solution()
print(obj.strongPasswordChecker("aaaabbbbccccddeeddeeddeedd"))