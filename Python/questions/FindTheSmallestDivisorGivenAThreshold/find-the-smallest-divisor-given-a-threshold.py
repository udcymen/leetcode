import math


def smallestDivisor(nums: list[int], threshold: int) -> int:
    nums = sorted(nums)
    
    start, end = 1, nums[-1]
    
    while start + 1 < end:
        mid = (start + end) // 2
        temp = sum([1 if mid >= num else math.ceil(num / mid) for num in nums])
        
        if temp <= threshold:
            end = mid
        else:
            start = mid
            
    if sum([1 if start >= num else math.ceil(num / start) for num in nums]) <= threshold:
        return start
    
    return end


if __name__ == "__main__":
    print(smallestDivisor([1,2,5,9], 6))
    print(smallestDivisor([2,3,5,7,11], 11))
    print(smallestDivisor([19], 5))