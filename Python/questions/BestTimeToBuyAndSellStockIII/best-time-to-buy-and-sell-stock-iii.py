import sys

def maxProfit(prices: list[int]) -> int:
    firstMinPrice = sys.maxsize
    secondMinPrice = sys.maxsize
    firstResult = 0
    secondResult = 0

    for price in prices:

        firstMinPrice = min(firstMinPrice, price)
        firstResult = max(firstResult, price - firstMinPrice)

        secondMinPrice = min(secondMinPrice, price - firstResult)
        secondResult = max(secondResult, price - secondMinPrice)

    return secondResult


if __name__ == "__main__":
    print(maxProfit([3,3,5,0,0,3,1,4]))
    print(maxProfit([1,2,3,4,5]))
    print(maxProfit([7,6,4,3,1]))
    print(maxProfit([1]))