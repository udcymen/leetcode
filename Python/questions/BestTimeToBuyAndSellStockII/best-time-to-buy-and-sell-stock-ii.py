def maxProfit(prices: list[int]) -> int:
    result = 0
    
    for i in range(1, len(prices)):
        prev, curr = prices[i - 1], prices[i]
        
        if curr > prev:
            result += curr - prev
            
    return result

if __name__ == "__main__":
    print(maxProfit([7,1,5,3,6,4]))
    print(maxProfit([1,2,3,4,5]))
    print(maxProfit([7,6,4,3,1]))