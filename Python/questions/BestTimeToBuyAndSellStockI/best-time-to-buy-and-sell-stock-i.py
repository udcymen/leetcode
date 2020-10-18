import sys

def maxProfit(prices: list[int]) -> int:
        result = 0
        minPrice = sys.maxsize
        
        for price in prices:
            if (price < minPrice):
                minPrice = price
            elif (price > minPrice):
                result = max(result, price - minPrice)
        
        return result

if __name__ == "__main__":
    print(maxProfit([7,1,5,3,6,4]))
    print(maxProfit([7,6,4,3,1]))