class Solution(object):
    def distMoney(self, money, children):
        if money < children:
            return -1
        if money < children+7:
            return 0
        dictOfKids = {}
        for i in range(children):
            dictOfKids[i] = 1
        money -= children
        i = 0
        numberOfMax = 0
        while money > 0:
            dictOfKids, numberOfMax, money = self.recur(dictOfKids, i, money, numberOfMax)    
            i += 1           
        
        return numberOfMax

    def recur(self, dictOfKids, index, money, numberOfMax):
        if money >= 7:
            dictOfKids[index] += 7
            numberOfMax += 1
            money -= 7
        if money < 7:
            dictOfKids[index] += money
            money = 0
        
        if dictOfKids[index] == 4:
            if dictOfKids[index] == dictOfKids[len(dictOfKids)-1] and len(dictOfKids) == 2:
                numberOfMax = 0
            elif dictOfKids[index] == dictOfKids[len(dictOfKids)-1]:
                dictOfKids[index-1] = 9
                dictOfKids[index] = 3
                numberOfMax -= 1        
            money = 0                           

        return dictOfKids, numberOfMax, money
        
obj = Solution()
print(obj.distMoney(20, 2))