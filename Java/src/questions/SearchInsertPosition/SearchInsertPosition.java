package questions.SearchInsertPosition;

import java.util.*;

public class SearchInsertPosition {
    public static int searchInsert(int[] nums, int target) {
        int start = 0;
        int end = nums.length - 1;

        while (start + 1 < end) {
            int mid = start + (end - start) / 2;

            if (nums[mid] >= target) {
                end = mid;
            } else {
                start = mid;
            }
        }

        if (nums[start] >= target) {
            return start;
        } else if (nums[start] < target && nums[end] >= target) {
            return end;
        } else {
            return end + 1;
        }
    }

    public static void main(String[] args) {
        System.out.println(SearchInsertPosition.searchInsert(new int[] { 1, 3, 5, 6 }, 5));
        System.out.println(SearchInsertPosition.searchInsert(new int[] { 1, 3, 5, 6 }, 2));
        System.out.println(SearchInsertPosition.searchInsert(new int[] { 1, 3, 5, 6 }, 7));
        System.out.println(SearchInsertPosition.searchInsert(new int[] { 1, 3, 5, 6 }, 0));
        System.out.println(SearchInsertPosition.searchInsert(new int[] { 1 }, 0));
    }
}