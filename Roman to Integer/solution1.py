class Solution(object):
    def romanToInt(self, s):
        roman_list = list(s)
        num_list = []  

        for roman in range(len(roman_list)):
            if roman_list[roman] == 'I':
                num_list.append(1)
            if roman_list[roman] == 'V':
                num_list.append(5)
            if roman_list[roman] == 'X':
                num_list.append(10)
            if roman_list[roman] == 'L':
                num_list.append(50)
            if roman_list[roman] == 'C':
                num_list.append(100)
            if roman_list[roman] == 'D':
                num_list.append(500)
            if roman_list[roman] == 'M':
                num_list.append(1000)

        print(num_list)
        index = len(num_list) - 1
        total = 0
        print("First Total: " + str(total))
        print("First Index: " + str(index))

        for i in range(len(num_list)):
            if num_list[len(num_list) - i - 1] < num_list[index]:
                total -= num_list[len(num_list) - i - 1]
                print(total)
            if num_list[len(num_list) - i - 1] == num_list[index]:
                total += num_list[len(num_list) - i - 1]
            if num_list[len(num_list) - i - 1] > num_list[index]:
                total += num_list[len(num_list) - i - 1]
                index = len(num_list) - i - 1
        
        return total

obj = Solution()
print(obj.romanToInt("MCMXCIV"))