class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        
        if prices == None or len(prices) < 2:
            return result
        
        minPrice = float("inf")
        
        for price in prices:
            if price < minPrice:
                minPrice = price
            elif result < price - minPrice:
                result = price - minPrice

        return result