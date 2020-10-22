import sys


def findKth(nums1: list[int], start1: int, nums2: list[int], start2: int, k: int):
    if start1 >= len(nums1):
        return nums2[start2 + k - 1]
    
    if start2 >= len(nums2):
        return nums1[start1 + k - 1]
    
    if k == 1:
        return min(nums1[start1], nums2[start2])
    
    mid1 = nums1[start1 + k // 2 - 1] if start1 + k // 2 - 1 < len(nums1) else sys.maxsize
    mid2 = nums2[start2 + k // 2 - 1] if start2 + k // 2 - 1< len(nums2) else sys.maxsize

    if mid1 > mid2:
        return findKth(nums1, start1, nums2, start2 + k // 2, k - k // 2)
    else:
        return findKth(nums1, start1 + k // 2, nums2, start2, k - k // 2)
    
def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    l = len(nums1) + len(nums2)
    mid = l // 2

    if l % 2 == 0:
        return (findKth(nums1, 0, nums2, 0, mid) + findKth(nums1, 0, nums2, 0, mid + 1)) / 2.0
    else:
        return findKth(nums1, 0, nums2, 0, mid + 1)


if __name__ == "__main__":
    print(findMedianSortedArrays([1,3], [2]))
    print(findMedianSortedArrays([1,2], [3,4]))
    print(findMedianSortedArrays([0,0], [0,0]))
    print(findMedianSortedArrays([], [1]))
    print(findMedianSortedArrays([2], []))