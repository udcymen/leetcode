def findPeakElement(nums: list[int]) -> int:
    start, end = 0, len(nums) - 1
    
    while start + 1 < end:
        mid = (start + end) // 2
        
        if nums[mid] > nums[mid + 1]:
            end = mid
        else:
            start = mid
            
    if nums[start] > nums[end]:
        return start
    
    return end


if __name__ == "__main__":
    print(findPeakElement([1,2,3,1]))
    print(findPeakElement([1,2,1,3,5,6,4]))
    print(findPeakElement([1,2]))
    print(findPeakElement([1]))
    print(findPeakElement([2,1]))