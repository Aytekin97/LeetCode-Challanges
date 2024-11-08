def buyChoco(prices, money):
        minPrice = float('inf')
        secondMinPrice = float('inf')
        for i in prices: 
            if i <= minPrice:
                secondMinPrice = minPrice
                minPrice = i
            elif i <= secondMinPrice:
                secondMinPrice = i
        if minPrice + secondMinPrice <= money:
            return money - (minPrice + secondMinPrice)
        return money

prices = [1, 2, 3, 4, 5]
money = 5
print(buyChoco(prices, money))
"""
:type prices: List[int]
:type money: int
:rtype: int
"""
