def twoSum(nums: list[int], target: int) -> list[int]:
    dictionary = {}
    
    for index, num in enumerate(nums):
        target_num = target - num
        
        if target_num in dictionary:
            return [dictionary[target_num], index]
        
        dictionary[num] = index


if __name__ == "__main__":
    print(twoSum([2,7,11,15], 9))
    print(twoSum([3,2,4], 6))
    print(twoSum([3,3], 6))