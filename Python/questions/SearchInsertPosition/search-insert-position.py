def searchInsert(nums: list[int], target: int) -> int:
    start, end = 0, len(nums) - 1

    while start + 1 < end:
        mid = (start + end) // 2
        if nums[mid] >= target:
            end = mid
        else:
            start = mid

    if nums[start] >= target:
        return start
    elif nums[start] < target and nums[end] >= target:
        return end
    else:
        return end + 1


if __name__ == "__main__":
    print(searchInsert([1, 3, 5, 6], 5))
    print(searchInsert([1, 3, 5, 6], 2))
    print(searchInsert([1, 3, 5, 6], 7))
    print(searchInsert([1, 3, 5, 6], 0))
    print(searchInsert([1], 0))
