def search(nums: list[int], target: int) -> int:
    start, end = 0, len(nums) - 1
    
    while start + 1 < end:
        mid = (start + end) // 2
        
        if nums[mid] == target:
            return mid

        # Situaion 1: mid is in the left ascending part
        if nums[mid] > nums[start]:
            if target >= nums[start] and target < nums[mid]:
                end = mid
            else:
                start = mid
        # Situaion 2: mid is in the right ascending part
        else:
            if target <= nums[end] and target > nums[mid]:
                start = mid
            else:
                end = mid
    
    if nums[start] == target:
        return start
    
    if nums[end] == target:
        return end
    
    return -1


if __name__ == "__main__":
    print(search([4,5,6,7,0,1,2], 0))
    print(search([4,5,6,7,0,1,2], 3))
    print(search([1], 0))
    print(search([1,3,5], 1))
    print(search([5,1,3], 5))