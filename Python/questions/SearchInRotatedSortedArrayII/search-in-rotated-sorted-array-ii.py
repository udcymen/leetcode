def search(self, nums: List[int], target: int) -> bool:
    # In this case, it would be possible that nums[start] = nums[end] = nums[mid]. 
    # So we would not be able to figure out which half to cut off. 
    # Therefore, iterate the nums would be the worst case scenarios for cases like [1, 3, 1, 1, 1] with binary search.
    
    for num in nums:
        if target == num:
            return True
    
    return False


if __name__ == "__main__":
    print(search([2,5,6,0,0,1,2], 0))
    print(search([2,5,6,0,0,1,2], 3))
    print(search([1,3,1,1,1], 3))