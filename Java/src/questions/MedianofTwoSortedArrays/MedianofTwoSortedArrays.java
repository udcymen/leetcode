package questions.MedianofTwoSortedArrays;

public class MedianofTwoSortedArrays {
    public static int findKth(int[] nums1, int start1, int[] nums2, int start2, int k) {
        if (start1 >= nums1.length) {
            return nums2[start2 + k - 1];
        }

        if (start2 >= nums2.length) {
            return nums1[start1 + k - 1];
        }

        if (k == 1) {
            return Math.min(nums1[start1], nums2[start2]);
        }

        int mid1 = (start1 + k / 2 - 1) < nums1.length ? nums1[start1 + k / 2 - 1] : Integer.MAX_VALUE;
        int mid2 = (start2 + k / 2 - 1) < nums2.length ? nums2[start2 + k / 2 - 1] : Integer.MAX_VALUE;

        if (mid1 > mid2) {
            return findKth(nums1, start1, nums2, start2 + k / 2, k - k / 2);
        } else {
            return findKth(nums1, start1 + k / 2, nums2, start2, k - k / 2);
        }
    }

    public static double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int len = nums1.length + nums2.length;

        if (len % 2 == 0) {
            return (findKth(nums1, 0, nums2, 0, len / 2) + findKth(nums1, 0, nums2, 0, len / 2 + 1)) / 2.0;
        } else {
            return findKth(nums1, 0, nums2, 0, len / 2 + 1);
        }
    }

    public static void main(String[] args) {
        System.out.println(MedianofTwoSortedArrays.findMedianSortedArrays(new int[] { 1, 3 }, new int[] { 2 }));
        System.out.println(MedianofTwoSortedArrays.findMedianSortedArrays(new int[] { 1, 2 }, new int[] { 3, 4 }));
        System.out.println(MedianofTwoSortedArrays.findMedianSortedArrays(new int[] { 0, 0 }, new int[] { 0, 0 }));
        System.out.println(MedianofTwoSortedArrays.findMedianSortedArrays(new int[] {}, new int[] { 1 }));
        System.out.println(MedianofTwoSortedArrays.findMedianSortedArrays(new int[] { 2 }, new int[] {}));
    }
}
