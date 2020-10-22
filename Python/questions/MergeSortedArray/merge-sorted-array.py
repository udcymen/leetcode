def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    
    index = m + n - 1
    m -= 1
    n -=1
    
    while m > -1 and n > -1:
        a, b = nums1[m], nums2[n]
        
        if a > b:
            nums1[index] = a
            m -= 1
        else:
            nums1[index] = b
            n -= 1
            
        index -= 1
        
    while n > -1:
        nums1[index] = nums2[n]
        n -= 1
        index -= 1
